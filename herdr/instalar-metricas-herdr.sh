#!/usr/bin/env bash
# Instala el visor de métricas de Herdr: contexto, tokens y cuota restante
# (5h / 7d) de Claude, Codex y demás agentes soportados.
#
# Usa el plugin herdr-agent-usage (levi-qiao/herdr-agent-usage) como recolector
# y añade un panel propio, más los atajos para abrirlo:
#   - Herdr de escritorio:  Ctrl+Shift+M
#   - Herdr headless (TUI): prefix+shift+m
#
# Uso:
#   ./herdr/instalar-metricas-herdr.sh
#   ./herdr/instalar-metricas-herdr.sh --agent claude,codex

set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENTES="${AGENTES:-claude,codex}"
PLUGINS_JSON="${HERDR_PLUGINS_JSON:-$HOME/.config/herdr/plugins.json}"
STATE_DIR="${HERDR_PLUGIN_STATE_DIR:-$HOME/.local/state/herdr/plugins/herdr-agent-usage}"
CONFIG="${HERDR_CONFIG:-$HOME/.config/herdr/config.toml}"
APP_HOME="${HERDR_APP_HOME:-$HOME/.config/herdr-app}"
BIN_DIR="$HOME/.local/bin"

for arg in "$@"; do
  case "$arg" in
    --agent=*) AGENTES="${arg#*=}" ;;
    --agent) shift; AGENTES="${1:-$AGENTES}" ;;
    -h|--help) sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Opción desconocida: $arg" >&2; exit 2 ;;
  esac
done

command -v herdr >/dev/null || echo "aviso: 'herdr' no está en PATH (el plugin se configura igual)" >&2
command -v python3 >/dev/null || { echo "Falta python3." >&2; exit 1; }

if [ ! -f "$PLUGINS_JSON" ] || ! grep -q '"herdr-agent-usage"' "$PLUGINS_JSON"; then
  cat >&2 <<'EOF'
El plugin herdr-agent-usage no está instalado. Instálalo desde Herdr:

  herdr plugin install levi-qiao/herdr-agent-usage

y vuelve a ejecutar este script.
EOF
  exit 1
fi

BIN="$(python3 - "$PLUGINS_JSON" <<'PY'
import json, sys
for plugin in json.load(open(sys.argv[1])):
    if plugin.get("plugin_id") == "herdr-agent-usage" and plugin.get("plugin_root"):
        print(plugin["plugin_root"] + "/target/release/herdr-agent-usage")
        break
PY
)"

if [ -z "$BIN" ] || [ ! -x "$BIN" ]; then
  echo "El plugin está registrado pero su binario no existe: $BIN" >&2
  echo "Abre Herdr para que termine de construirse o reinstala el plugin." >&2
  exit 1
fi

mkdir -p "$STATE_DIR"

echo "== Configurando el recolector para: $AGENTES"
# Herdr pasa esta variable a las acciones del plugin; usarla mantiene el mismo
# caché que los colectores que ya están corriendo.
HERDR_PLUGIN_STATE_DIR="$STATE_DIR" "$BIN" configure --apply --agent "$AGENTES"

echo "== Instalando el visor"
mkdir -p "$BIN_DIR"
install -m 0755 "$RAIZ/herdr/herdr-metrics.py" "$BIN_DIR/herdr-metrics"

cat > "$BIN_DIR/herdr-agent-usage-dashboard" <<'EOF'
#!/bin/sh
# Generado por Skills_for_claude/herdr/instalar-metricas-herdr.sh
set -eu
if [ -x "$HOME/.local/bin/herdr-metrics" ]; then
  exec "$HOME/.local/bin/herdr-metrics"
fi
exec "$HOME/.local/bin/herdr-agent-usage-panel"
EOF
chmod +x "$BIN_DIR/herdr-agent-usage-dashboard"

# Panel oficial del plugin, como respaldo si falta el visor propio.
cat > "$BIN_DIR/herdr-agent-usage-panel" <<EOF
#!/bin/sh
set -eu
BIN="\$(python3 - "$PLUGINS_JSON" <<'PY'
import json, sys
for plugin in json.load(open(sys.argv[1])):
    if plugin.get("plugin_id") == "herdr-agent-usage" and plugin.get("plugin_root"):
        print(plugin["plugin_root"] + "/target/release/herdr-agent-usage")
        break
PY
)"
[ -n "\$BIN" ] && [ -x "\$BIN" ] || { echo "herdr-agent-usage no encontrado" >&2; exit 1; }
mkdir -p "$STATE_DIR"
HERDR_PLUGIN_STATE_DIR="$STATE_DIR" exec "\$BIN" dashboard
EOF
chmod +x "$BIN_DIR/herdr-agent-usage-panel"

echo "== Añadiendo atajos"
# Herdr de escritorio: keys.json (no lee el config.toml del TUI).
if [ -d "$APP_HOME" ]; then
  python3 - "$APP_HOME/keys.json" "$BIN_DIR/herdr-agent-usage-dashboard" <<'PY'
import json, os, sys, time
path, viewer = sys.argv[1], sys.argv[2]
data = {}
if os.path.exists(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if "ctrl-shift-m" in data.get("global", {}):
        print("   Ctrl+Shift+M ya estaba configurado")
        raise SystemExit
    with open(path + ".bak-" + str(int(time.time())), "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
data.setdefault("global", {})["ctrl-shift-m"] = {
    "command": "terminal.open",
    "args": {"argv": [viewer], "place": "down", "name": "Metrics"},
}
with open(path, "w", encoding="utf-8") as fh:
    json.dump(data, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print("   Ctrl+Shift+M -> panel de métricas (Herdr de escritorio)")
PY
else
  echo "   (sin ~/.config/herdr-app: se omite el atajo del escritorio)"
fi

# Herdr headless (TUI): config.toml.
if [ -f "$CONFIG" ] && ! grep -q 'herdr-agent-usage-dashboard' "$CONFIG" 2>/dev/null; then
  cp "$CONFIG" "$CONFIG.bak-$(date +%s)"
  cat >> "$CONFIG" <<EOF

# Visor de métricas (contexto, tokens, cuota 5h/7d).
[[keys.command]]
key = "prefix+shift+m"
type = "popup"
command = "'$BIN_DIR/herdr-agent-usage-dashboard'"
width = "80%"
height = "70%"
description = "agent metrics: context, tokens, quota"
EOF
  echo "   prefix+shift+m -> panel de métricas (TUI)"
elif [ -f "$CONFIG" ]; then
  echo "   prefix+shift+m ya estaba configurado (TUI)"
fi

echo
echo "Listo."
echo "  Ctrl+Shift+M   abre el panel en Herdr de escritorio"
echo "  prefix+shift+q ajustes del plugin (TUI)"
echo "  prefix+shift+r refrescar cuotas (TUI)"
echo "En el panel: r refresca, q sale. Los datos se actualizan cada 5 s."
