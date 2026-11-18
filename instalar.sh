#!/usr/bin/env bash
# Instala los skills de este repositorio en Claude Code.
#
#   ./instalar.sh            enlaza cada skill en ~/.claude/skills (recomendado)
#   ./instalar.sh --copiar   copia las carpetas en vez de enlazarlas
#   ./instalar.sh --forzar   reemplaza las instalaciones que ya existan
#
# Por defecto usa ~/.claude/skills; cambia el destino con DESTINO=/ruta ./instalar.sh

set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DESTINO="${DESTINO:-$HOME/.claude/skills}"
MODO="enlazar"
FORZAR=0

for arg in "$@"; do
  case "$arg" in
    --copiar) MODO="copiar" ;;
    --forzar) FORZAR=1 ;;
    -h|--help) sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Opción desconocida: $arg" >&2; exit 2 ;;
  esac
done

mkdir -p "$DESTINO"
instalados=0
omitidos=0

while IFS= read -r skill_md; do
  origen="$(dirname "$skill_md")"
  nombre="$(grep -m1 '^name:' "$skill_md" | sed 's/^name:[[:space:]]*//' | tr -d '"'"'"'')"
  [ -n "$nombre" ] || nombre="$(basename "$origen")"
  nombre="$(echo "$nombre" | tr ' ' '-' | tr -cd '[:alnum:]._-')"
  destino="$DESTINO/$nombre"

  if [ -e "$destino" ] || [ -L "$destino" ]; then
    if [ "$FORZAR" -eq 1 ]; then
      rm -rf "$destino"
    else
      echo "· ya existe: $nombre (usa --forzar para reemplazarlo)"
      omitidos=$((omitidos + 1))
      continue
    fi
  fi

  if [ "$MODO" = "copiar" ]; then
    cp -a "$origen" "$destino"
  else
    ln -s "$origen" "$destino"
  fi
  echo "✓ $nombre  <-  ${origen#"$RAIZ"/}"
  instalados=$((instalados + 1))
done < <(find "$RAIZ/skills" -name SKILL.md -not -path '*/node_modules/*' | sort)

echo
echo "Instalados: $instalados · Omitidos: $omitidos · Destino: $DESTINO"
echo "Los packs sin SKILL.md en la raíz (claude-roblox-game-studio, openrig-studio) se instalan a mano; ver README.md."
