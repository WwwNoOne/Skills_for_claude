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
| [obra/superpowers](https://github.com/obra/superpowers) | obra (Jesse Vincent) | MIT | Suite completa (15 skills) |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic | Apache 2.0 | `frontend-design` y `claude-api` |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | OthmanAdi | MIT | Skill `planning-with-files` (scripts y plantillas incluidos) |
| [oaustegard/claude-skills](https://github.com/oaustegard/claude-skills) | oaustegard | MIT | `orchestrating-chat-agents` |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | ruvnet | MIT | `swarm-orchestration` (skill y scripts) |
| [BEHA-AF/youtube-agent-skills](https://github.com/BEHA-AF/youtube-agent-skills) | BEHA-AF | MIT | 11 skills `yt-*` |
| [adityaarsharma/youtube-marketing-skills](https://github.com/adityaarsharma/youtube-marketing-skills) | adityaarsharma | MIT | Pack completo (21 comandos + servidor MCP) |
| [Kianzzz/xilo-opus-video](https://github.com/Kianzzz/xilo-opus-video) | Kianzzz | MIT | Skill completo |
| [HaochenSHI66/claude-awesome-video-creation](https://github.com/HaochenSHI66/claude-awesome-video-creation) | HaochenSHI66 | MIT | Skill completo |
| [Changroro/code-video](https://github.com/Changroro/code-video) | Changroro | MIT | Skill completo (sin `docs/`, la galería de 28 MB) |

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
- **Changroro/code-video** se incluye sin su carpeta `docs/` (galería de 28 MB de GIFs y un MP4 de
  muestra); el skill funciona igual. Si la quieres, clónala del repositorio original.
- **orchestrating-agents** fue renombrado por su autor a `orchestrating-chat-agents`; aquí está la
  versión mantenida, con el mismo propósito.
- **youtube-marketing-skills** incluye un servidor MCP que necesita credenciales de la API de YouTube;
  revisa su `INSTALL.md`.

## Cómo actualizar un skill

```bash
git clone --depth 1 https://github.com/<autor>/<repo>.git /tmp/repo
cp -a /tmp/repo/<ruta-del-skill>/. skills/<categoria>/<skill>/
```

Y actualiza las tablas de este archivo y de [CATALOGO.md](CATALOGO.md) si cambia la procedencia.
