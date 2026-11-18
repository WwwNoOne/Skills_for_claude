#!/usr/bin/env bash
# Instala el visor de métricas de Herdr: contexto, tokens y cuota restante
# (5h / 7d) de Claude, Codex y demás agentes soportados.
#
# Usa el plugin herdr-agent-usage (levi-qiao/herdr-agent-usage) y añade:
#   - las filas de cuota en la barra lateral de Herdr
#   - el statusLine de Claude Code (fuente de la cuota)
#   - el atajo prefix+shift+m para abrir el panel completo
#
# Uso:
#   ./herdr/instalar-metricas-herdr.sh
#   ./herdr/instalar-metricas-herdr.sh --agent claude,codex

set -euo pipefail

AGENTES="${AGENTES:-claude,codex}"
PLUGINS_JSON="${HERDR_PLUGINS_JSON:-$HOME/.config/herdr/plugins.json}"
STATE_DIR="${HERDR_PLUGIN_STATE_DIR:-$HOME/.local/state/herdr/plugins/herdr-agent-usage}"
CONFIG="${HERDR_CONFIG:-$HOME/.config/herdr/config.toml}"
WRAPPER="$HOME/.local/bin/herdr-agent-usage-dashboard"

for arg in "$@"; do
  case "$arg" in
    --agent=*) AGENTES="${arg#*=}" ;;
    --agent) shift; AGENTES="${1:-$AGENTES}" ;;
    -h|--help) sed -n '2,14p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Opción desconocida: $arg" >&2; exit 2 ;;
  esac
done

command -v herdr >/dev/null || { echo "Falta herdr en PATH." >&2; exit 1; }
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

echo "== Configurando plugin para: $AGENTES"
# Herdr pasa esta variable a las acciones del plugin; usarla mantiene el mismo
# caché que los colectores que ya están corriendo.
HERDR_PLUGIN_STATE_DIR="$STATE_DIR" "$BIN" configure --apply --agent "$AGENTES"

echo "== Instalando el atajo prefix+shift+m"
mkdir -p "$(dirname "$WRAPPER")"
cat > "$WRAPPER" <<EOF
#!/bin/sh
# Generado por Skills_for_claude/herdr/instalar-metricas-herdr.sh
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
chmod +x "$WRAPPER"

if ! grep -q 'herdr-agent-usage-dashboard' "$CONFIG" 2>/dev/null; then
  cp "$CONFIG" "$CONFIG.bak-$(date +%s)"
  cat >> "$CONFIG" <<EOF

# Visor de métricas (contexto, tokens, cuota 5h/7d).
[[keys.command]]
key = "prefix+shift+m"
type = "popup"
command = "'$WRAPPER'"
width = "80%"
height = "70%"
description = "agent metrics: context, tokens, quota"
EOF
  echo "   añadido a $CONFIG"
else
  echo "   ya estaba configurado en $CONFIG"
fi

echo
echo "Listo. Reinicia Herdr para que cargue la barra lateral y los atajos."
echo "  prefix+shift+m  panel de métricas (popup)"
echo "  prefix+shift+q  ajustes del plugin"
echo "  prefix+shift+r  refrescar cuotas"
echo "  prefix+shift+o  alternar orden cuota/pestañas"
