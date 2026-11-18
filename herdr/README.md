# Visor de métricas para Herdr

Panel para ver **contexto, tokens y cuota restante** (5h / 7d) de los agentes que
corren dentro de Herdr: Claude Code, Codex, Grok, OpenCode, Pi, OMP, Devin, Muse,
Cursor, Kilo y MiMo.

Se apoya en el plugin [`levi-qiao/herdr-agent-usage`](https://github.com/levi-qiao/herdr-agent-usage),
que añade filas de cuota a la barra lateral y recoge los datos de cada proveedor.

## Instalación

```bash
./herdr/instalar-metricas-herdr.sh                  # Claude + Codex
./herdr/instalar-metricas-herdr.sh --agent claude   # solo Claude
```

El script:

1. Comprueba que el plugin `herdr-agent-usage` está instalado (si no, te dice el
   comando exacto para instalarlo desde Herdr).
2. Ejecuta `configure --apply` con el mismo directorio de estado que usa Herdr,
   de modo que la barra lateral, el `statusLine` de Claude y los colectores
   compartan caché.
3. Instala el atajo `prefix+shift+m`, que abre el panel en un popup.

Después **reinicia Herdr** para que cargue la barra lateral y los atajos.

## Uso

| Atajo | Acción |
|---|---|
| `prefix+shift+m` | Panel de métricas (popup): cuota 5h/7d y reset |
| `prefix+shift+q` | Ajustes del plugin (campos, %, orden, intervalo) |
| `prefix+shift+r` | Refrescar cuotas ahora |
| `prefix+shift+o` | Alternar orden por cuota / por pestañas |

En la barra lateral, cada agente muestra icono, proveedor, modelo, contexto
usado, caché, TTL y las cuotas. El panel del popup resume lo mismo por proveedor.

También puedes lanzarlo fuera de Herdr:

```bash
herdr-agent-usage-dashboard
```

## Qué mide

- **Contexto**: porcentaje de ventana usado y tokens de la sesión.
- **Tokens**: entrada fresca, lectura de caché, tokens escritos, acierto de caché.
- **Cuota restante**: ventana de 5 horas y semanal, con hora de reset.
- **Estado**: inactivo / trabajando / terminado / bloqueado por agente.

Los datos de Claude llegan por el `statusLine` que instala el plugin; los de
Codex y el resto, leyendo sus credenciales locales y consultando el endpoint de
uso del proveedor. Nada se sube a terceros: el plugin es local y de código
abierto (MIT).

## Si algo no aparece

- **La barra lateral no cambia**: falta reiniciar Herdr o recargar la config.
- **Todo sale `unavailable`**: ejecuta `prefix+shift+r`; si sigue igual, el
  agente no tiene credenciales activas (inicia sesión en ese CLI).
- **Iconos como cajas**: el terminal no tiene mapeada la fuente de iconos. En
  Linux se instala en `~/.local/share/fonts`; añade los rangos `U+E1A0–U+E1B6`
  y `U+E1C0–U+E1C5` a la fuente del terminal y reinícialo.
- **El CLI de Herdr da `WireResponse`**: hay una actualización de Herdr
  pendiente de reinicio; el cliente nuevo no habla con el servidor viejo.
  Reinicia Herdr.

## Desinstalar

```bash
herdr plugin action invoke uninstall --plugin herdr-agent-usage
rm -f ~/.local/bin/herdr-agent-usage-dashboard
```

Y borra el bloque `herdr-agent-usage-dashboard` de `~/.config/herdr/config.toml`.
