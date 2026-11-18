#!/usr/bin/env python3
"""Visor de métricas para Herdr: contexto, tokens y cuota restante.

Lee las instantáneas que deja el plugin herdr-agent-usage y las pinta en un
panel que se refresca solo. Pensado para abrirse en una terminal/popup de Herdr.

    herdr-metrics            # panel interactivo (q salir, r refrescar)
    herdr-metrics --once     # imprime una vez y sale
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import select
import subprocess
import sys
import time
from datetime import datetime

STATE_DIR = os.environ.get(
    "HERDR_PLUGIN_STATE_DIR",
    os.path.expanduser("~/.local/state/herdr/plugins/herdr-agent-usage"),
)
REFRESH_SECONDS = float(os.environ.get("HERDR_METRICS_REFRESH", "5"))

RESET = "\x1b[0m"
BOLD = "\x1b[1m"
DIM = "\x1b[2m"
GREEN = "\x1b[38;5;114m"
YELLOW = "\x1b[38;5;179m"
RED = "\x1b[38;5;204m"
BLUE = "\x1b[38;5;110m"
GREY = "\x1b[38;5;245m"
WHITE = "\x1b[38;5;253m"

PROVIDERS = {
    "claude": "Claude",
    "codex": "Codex",
    "grok": "Grok",
    "agy": "Antigravity",
    "opencode": "OpenCode",
    "opencode_go": "OpenCode",
    "pi": "Pi",
    "omp": "OMP",
    "devin": "Devin",
    "muse": "Muse",
    "cursor": "Cursor",
    "kilo": "Kilo",
    "mimo": "MiMo",
}
WINDOWS = {"five_hour": "5h", "weekly": "7d", "monthly": "30d"}


def color_for(remaining: float) -> str:
    if remaining <= 10:
        return RED
    if remaining <= 30:
        return YELLOW
    return GREEN


def bar(percent: float, width: int = 10) -> str:
    percent = max(0.0, min(100.0, percent))
    filled = round(percent / 100 * width)
    return "▓" * filled + "░" * (width - filled)


def fmt_tokens(value) -> str:
    try:
        n = float(value)
    except (TypeError, ValueError):
        return "?"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return f"{n:.0f}"


def fmt_when(resets_at) -> str:
    try:
        ts = float(resets_at)
    except (TypeError, ValueError):
        return ""
    delta = ts - time.time()
    if delta <= 0:
        return "ya resetea"
    if delta >= 86400:
        return f"en {int(delta // 86400)}d{int(delta % 86400 // 3600)}h"
    if delta >= 3600:
        return f"en {int(delta // 3600)}h{int(delta % 3600 // 60):02d}m"
    return f"en {int(delta // 60)}m"


def fmt_ago(fetched_at) -> str:
    try:
        delta = time.time() - float(fetched_at)
    except (TypeError, ValueError):
        return ""
    if delta < 60:
        return "ahora"
    if delta < 3600:
        return f"hace {int(delta // 60)}m"
    return f"hace {int(delta // 3600)}h"


def load_snapshots():
    snapshots = []
    for path in sorted(glob.glob(os.path.join(STATE_DIR, "*.json"))):
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, ValueError):
            continue
        if not isinstance(data, dict) or "provider" not in data or "windows" not in data:
            continue
        if os.path.basename(path).endswith(".observation.json"):
            continue
        data["_path"] = path
        snapshots.append(data)
    snapshots.sort(key=lambda s: PROVIDERS.get(s.get("provider"), s.get("provider", "")))
    return snapshots


def render(snapshots, width: int) -> list[str]:
    now = datetime.now().strftime("%H:%M:%S")
    title = " Herdr · métricas de agentes "
    line = "─" * max(0, width - 2)
    out = [
        f"{BLUE}{BOLD}{title}{RESET}{GREY}{'─' * max(0, width - len(title) - 1)}{RESET} {DIM}{now}{RESET}",
        f"{GREY}{line}{RESET}",
    ]

    if not snapshots:
        out.append(f"  {YELLOW}Sin datos todavía.{RESET} {DIM}Pulsa r para recolectar.{RESET}")
        return out

    for snap in snapshots:
        provider = PROVIDERS.get(snap.get("provider"), snap.get("provider", "?"))
        model = snap.get("model") or ""
        ago = fmt_ago(snap.get("fetched_at_unix"))
        head = f"{BOLD}{WHITE}{provider.upper()}{RESET}"
        if model:
            head += f" {GREY}·{RESET} {BLUE}{model}{RESET}"
        if ago:
            head += f" {DIM}{ago}{RESET}"
        out.append("")
        out.append(" " + head)

        ctx = snap.get("context") or {}
        ctx_label = "contexto"
        if not ctx:
            # Claude publica la cuota sin contexto global: usa la sesión más
            # reciente de las que tenga registradas.
            sessions = snap.get("session_contexts") or {}
            if sessions:
                latest = max(
                    sessions.values(),
                    key=lambda s: ((s.get("cache") or {}).get("last_activity_unix") or 0),
                )
                ctx = latest
                ctx_label = "contexto"
        used = ctx.get("used_percent")
        cache = ctx.get("cache") or {}
        if used is not None:
            c = color_for(100 - float(used))
            detail = []
            if cache.get("hit_percent") is not None:
                detail.append(f"caché {float(cache['hit_percent']):.0f}% acierto")
            if cache.get("read_tokens") is not None:
                detail.append(f"{fmt_tokens(cache['read_tokens'])} leídos")
            suffix = f" {GREY}· {RESET} ".join(detail)
            out.append(
                f"   {GREY}{ctx_label:<8}{RESET} {c}{bar(float(used))}{RESET} {c}{float(used):4.1f}%{RESET}"
                + (f"  {GREY}{suffix}{RESET}" if suffix else "")
            )
            totals = cache.get("session_totals") or {}
            if totals:
                out.append(
                    f"   {GREY}tokens{RESET}    {DIM}in {fmt_tokens(totals.get('fresh_input_tokens'))}"
                    f" · out {fmt_tokens(totals.get('creation_tokens'))}"
                    f" · caché {fmt_tokens(totals.get('read_tokens'))}{RESET}"
                )

        for window in snap.get("windows") or []:
            remaining = window.get("remaining_percent")
            if remaining is None:
                used_pct = window.get("used_percent")
                remaining = 100 - float(used_pct) if used_pct is not None else 0
            remaining = float(remaining)
            c = color_for(remaining)
            label = WINDOWS.get(window.get("kind"), window.get("kind", "?"))
            reset = fmt_when(window.get("resets_at"))
            out.append(
                f"   {GREY}{label:<8}{RESET}  {c}{bar(remaining)}{RESET} {c}{remaining:4.1f}% queda{RESET}"
                + (f"  {DIM}reset {reset}{RESET}" if reset else "")
            )

        error = snap.get("error") or snap.get("unattributed_session_reason")
        if error:
            out.append(f"   {YELLOW}{error}{RESET}")

    return out


def draw(lines, width, height):
    # Recorta a la altura disponible para no romper el layout del panel.
    visible = lines[: max(1, height - 1)]
    sys.stdout.write("\x1b[H" + "".join(line[:width] + "\x1b[K\n" for line in visible) + "\x1b[J")
    sys.stdout.flush()


def refresh_plugin():
    try:
        from_refresh_plugin()
    except Exception:
        pass


def from_refresh_plugin():
    plugins = json.load(open(os.path.expanduser("~/.config/herdr/plugins.json"), encoding="utf-8"))
    for plugin in plugins:
        if plugin.get("plugin_id") != "herdr-agent-usage":
            continue
        binary = os.path.join(plugin.get("plugin_root", ""), "target/release/herdr-agent-usage")
        if os.path.exists(binary):
            subprocess.Popen(
                [binary, "refresh", "--provider", "all", "--force"],
                env={**os.environ, "HERDR_PLUGIN_STATE_DIR": STATE_DIR},
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        return


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--once", action="store_true", help="imprime una vez y sale")
    args = parser.parse_args()

    if args.once or not sys.stdout.isatty():
        width = 78
        print("\n".join(render(load_snapshots(), width)))
        return 0

    import shutil
    import termios
    import tty

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    sys.stdout.write("\x1b[?1049h\x1b[?25l")
    sys.stdout.flush()
    try:
        tty.setcbreak(fd)
        while True:
            size = shutil.get_terminal_size((90, 30))
            draw(render(load_snapshots(), size.columns), size.columns, size.lines)
            deadline = time.time() + REFRESH_SECONDS
            while time.time() < deadline:
                ready, _, _ = select.select([sys.stdin], [], [], 0.5)
                if not ready:
                    continue
                key = sys.stdin.read(1)
                if key in ("q", "\x03"):
                    return 0
                if key == "r":
                    refresh_plugin()
                    deadline = time.time()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        sys.stdout.write("\x1b[?25h\x1b[?1049l")
        sys.stdout.flush()


if __name__ == "__main__":
    raise SystemExit(main())
