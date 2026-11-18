# Créditos y licencias

Todo el contenido de `skills/` proviene de repositorios públicos de terceros. Este almacén solo
reúne y reorganiza esos skills; **la autoría es de sus autores originales**. Los textos completos de
las licencias están en [`LICENCIAS/`](LICENCIAS/).

| Repositorio | Autor | Licencia | Qué se incluyó |
|---|---|---|---|
| [SyphoDev-yt/roblox-ai-skills](https://github.com/SyphoDev-yt/roblox-ai-skills) | SyphoDev | Free licence (uso libre, incluido comercial; no reventa; atribución) | 11 skills + `agents/` del orquestador |
| [hildlabs/openrig-studio](https://github.com/hildlabs/openrig-studio) | hildlabs | MIT | Herramienta completa (app + prompts) |
| [adnvli/vfxskill](https://github.com/adnvli/vfxskill) | adnvli | MIT | Skill completo (`roblox-vfx-animation`) |
| [dillydog580/animate-roblox-characters](https://github.com/dillydog580/animate-roblox-characters) | dillydog580 | MIT | Skill completo |
| [kapscripts/claude-skills](https://github.com/kapscripts/claude-skills) | kapscripts | ⚠️ Sin licencia declarada | `blender-game-artist` y `roblox-ui-designer` |
| [CodePhobiia/claude-roblox-game-studio](https://github.com/CodePhobiia/claude-roblox-game-studio) | FoG Studios | MIT | Suite completa |
| [xtrair/figma-to-roblox-ui](https://github.com/xtrair/figma-to-roblox-ui) | xtrair | MIT | Skill completo |
| [sentinelcore/roblox-skills](https://github.com/sentinelcore/roblox-skills) | sentinelcore | ⚠️ Sin licencia declarada | 7 skills |
| [brockmartin/roblox-game-skill](https://github.com/brockmartin/roblox-game-skill) | brockmartin | ⚠️ Sin licencia declarada | Skill completo |

## Notas

- **SyphoDev** permite usar y modificar los skills, incluso en juegos comerciales, pero prohíbe
  venderlos o incluirlos en un bundle de pago; si se comparten, hay que enlazar al canal de YouTube
  del autor como fuente.
- **Sin licencia declarada** significa que, por defecto, rigen todos los derechos reservados del
  autor. Se incluyen aquí para uso personal; si planeas publicar o redistribuir este repositorio,
  conviene pedir permiso o quitar esas carpetas.
- Las fuentes incluidas en `ui/roblox-ui/references/fonts` son Fredoka, bajo SIL Open Font
  License 1.1.
- `animacion/vfxskill/third_party/` puede contener código de terceros con sus propias licencias.

## Cómo actualizar un skill

```bash
git clone --depth 1 https://github.com/<autor>/<repo>.git /tmp/repo
cp -a /tmp/repo/<ruta-del-skill>/. skills/<categoria>/<skill>/
```

Y actualiza las tablas de este archivo y de [CATALOGO.md](CATALOGO.md) si cambia la procedencia.
