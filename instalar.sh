#!/usr/bin/env bash
# Instala los skills de este repositorio para Claude Code y/o Codex.
#
#   ./instalar.sh              instala en Claude Code (~/.claude/skills)
#   ./instalar.sh --codex      instala en Codex (~/.codex/skills)
#   ./instalar.sh --todos      instala en ambos
#   ./instalar.sh --copiar     copia las carpetas en vez de enlazarlas
#   ./instalar.sh --forzar     reemplaza las instalaciones que ya existan
#
# Destinos alternativos:
#   DESTINO=/ruta ./instalar.sh
#   DESTINO_CODEX=/ruta ./instalar.sh --codex

set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DESTINO_CLAUDE="${DESTINO:-$HOME/.claude/skills}"
DESTINO_CODEX="${DESTINO_CODEX:-${CODEX_HOME:-$HOME/.codex}/skills}"
MODO="enlazar"
FORZAR=0
DESTINOS=("$DESTINO_CLAUDE")

for arg in "$@"; do
  case "$arg" in
    --codex) DESTINOS=("$DESTINO_CODEX") ;;
    --todos|--todo) DESTINOS=("$DESTINO_CLAUDE" "$DESTINO_CODEX") ;;
    --copiar) MODO="copiar" ;;
    --forzar) FORZAR=1 ;;
    -h|--help) sed -n '2,13p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Opción desconocida: $arg" >&2; exit 2 ;;
  esac
done

for d in "${DESTINOS[@]}"; do mkdir -p "$d"; done

instalados=0
omitidos=0

while IFS= read -r skill_md; do
  origen="$(dirname "$skill_md")"
  nombre="$(grep -m1 '^name:' "$skill_md" | sed 's/^name:[[:space:]]*//' | tr -d '"'"'"'')"
  [ -n "$nombre" ] || nombre="$(basename "$origen")"
  nombre="$(echo "$nombre" | tr ' ' '-' | tr -cd '[:alnum:]._-')"

  for destino_base in "${DESTINOS[@]}"; do
    destino="$destino_base/$nombre"

    if [ -e "$destino" ] || [ -L "$destino" ]; then
      if [ "$FORZAR" -eq 1 ]; then
        rm -rf "$destino"
      else
        echo "· ya existe: $nombre en ${destino_base/#$HOME/~} (usa --forzar para reemplazarlo)"
        omitidos=$((omitidos + 1))
        continue
      fi
    fi

    if [ "$MODO" = "copiar" ]; then
      cp -a "$origen" "$destino"
    else
      ln -s "$origen" "$destino"
    fi
    echo "✓ $nombre  ->  ${destino_base/#$HOME/~}"
    instalados=$((instalados + 1))
  done
done < <(find "$RAIZ/skills" -name SKILL.md -not -path '*/node_modules/*' | sort)

echo
echo "Instalados: $instalados · Omitidos: $omitidos"
for d in "${DESTINOS[@]}"; do echo "  destino: ${d/#$HOME/~}"; done
echo "Los packs sin SKILL.md en la raíz (claude-roblox-game-studio, superpowers, openrig-studio) se instalan a mano; ver README.md."
