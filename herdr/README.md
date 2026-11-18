# Visor de métricas para Herdr

Panel para ver **contexto, tokens y cuota restante** (5h / 7d) de los agentes que
corren dentro de Herdr: Claude Code, Codex, Grok, OpenCode, Pi, OMP, Devin, Muse,
Cursor, Kilo y MiMo.

Consta de dos piezas:

- **Recolector**: el plugin [`levi-qiao/herdr-agent-usage`](https://github.com/levi-qiao/herdr-agent-usage),
  que lee las credenciales locales de cada CLI, consulta la cuota de cada
  proveedor y la deja en `~/.local/state/herdr/plugins/herdr-agent-usage/`.
- **Visor**: `herdr/herdr-metrics.py`, un panel que lee esas instantáneas y pinta
  contexto, tokens, caché y cuota, refrescándose cada 5 segundos.

## Instalación

```bash
./herdr/instalar-metricas-herdr.sh                  # Claude + Codex
./herdr/instalar-metricas-herdr.sh --agent claude   # solo Claude
```

El script:

1. Comprueba que el plugin está instalado (si no, te dice el comando exacto).
2. Ejecuta su `configure --apply` con el mismo directorio de estado que usa
   Herdr, de modo que recolector y visor compartan caché.
3. Instala `~/.local/bin/herdr-metrics` y su lanzador
   `~/.local/bin/herdr-agent-usage-dashboard`.
4. Añade los atajos:
   - **Herdr de escritorio** (`~/.config/herdr-app/keys.json`): `Ctrl+Shift+M`
     abre el panel en un split.
   - **Herdr headless / TUI** (`~/.config/herdr/config.toml`): `prefix+shift+m`
     abre el panel en un popup.

## Uso

| Dónde | Atajo | Acción |
|---|---|---|
| Escritorio | `Ctrl+Shift+M` | Abre el panel en un split inferior |
| TUI | `prefix+shift+m` | Abre el panel en un popup |
| TUI | `prefix+shift+q` | Ajustes del plugin (campos, %, orden) |
| TUI | `prefix+shift+r` | Refrescar cuotas |
| TUI | `prefix+shift+o` | Alternar orden por cuota / pestañas |

Dentro del panel: `r` fuerza una recolección y `q` sale.

También se puede lanzar a mano:

```bash
herdr-metrics            # panel interactivo
herdr-metrics --once     # imprime una vez (útil para scripts)
herdr-agent-usage-dashboard   # alias que usa el atajo
```

## Qué mide

- **Contexto**: porcentaje de ventana usado y tokens de la sesión más reciente.
- **Tokens**: entrada nueva, tokens escritos, lectura de caché y acierto de caché.
- **Cuota restante**: ventana de 5 horas y semanal, con tiempo hasta el reset.
- **Frescura**: cuándo se recolectó cada dato.

Los datos de Claude llegan por el `statusLine` que instala el plugin; los de
Codex y el resto, leyendo sus credenciales locales y consultando el endpoint de
uso del proveedor. Todo es local y de código abierto (MIT).

## Notas

- La **barra lateral de cuota** que añade el plugin solo se dibuja en el Herdr
  headless/TUI. La app de escritorio usa su propio sidebar (`~/.config/herdr-app`),
  por eso el visor se abre como panel.
- El panel lee las instantáneas; si un agente no tiene credenciales activas,
  aparece sin datos. Inicia sesión en ese CLI y pulsa `r`.
- Si los iconos del plugin salen como cajas, falta mapear la fuente de iconos en
  el terminal (`U+E1A0–U+E1B6`, `U+E1C0–U+E1C5`).

## Desinstalar

```bash
herdr plugin action invoke uninstall --plugin herdr-agent-usage
rm -f ~/.local/bin/herdr-metrics ~/.local/bin/herdr-agent-usage-dashboard \
      ~/.local/bin/herdr-agent-usage-panel
```

Y borra la entrada `ctrl-shift-m` de `~/.config/herdr-app/keys.json` y el bloque
`herdr-agent-usage-dashboard` de `~/.config/herdr/config.toml`.
