# Catálogo de skills

Índice de todo lo incluido. La ruta es relativa a `skills/`.

## 🎬 Animación

| Skill | Qué hace | Origen |
|---|---|---|
| `animacion/roblox-animation` | Crea animaciones R15/R6 "headless" en Blender a partir de una especificación de poses JSON; las verifica con contact sheets y GIFs y las compara con una pose de referencia. | SyphoDev-yt/roblox-ai-skills |
| `animacion/roblox-animations` | Referencia de sistemas de animación: AnimationTrack, reproducción, parada y blending, eventos, reemplazo de animaciones por defecto y depuración. | sentinelcore/roblox-skills |
| `animacion/animate-roblox-characters` | Crea, pule, inspecciona y exporta animaciones completas R6/R15 (caminar, correr, idle, ataques, emotes) con rigs auténticos de Studio vía Blender MCP. | dillydog580/animate-roblox-characters |
| `animacion/vfxskill` | VFX y animación por Roblox Studio MCP: partículas, haces, estelas, slashes, impactos, explosiones, hechizos, auras, flipbooks y animaciones R15/R6. | adnvli/vfxskill |
| `animacion/openrig-studio` | Herramienta open source (no es un skill suelto): describes un movimiento, la IA genera la animación R15/R6, se previsualiza en un rig 3D y se envía a Roblox Studio. | hildlabs/openrig-studio |

## 🧊 Modelado 3D y creación de assets

| Skill | Qué hace | Origen |
|---|---|---|
| `modelado-3d/roblox-3d-model` | Texto → MeshPart listo para el juego, de extremo a extremo: concepto 2D verificado, malla high-poly (Hi3DGen), retopo y export. Individual o por lotes. | SyphoDev-yt/roblox-ai-skills |
| `modelado-3d/roblox-texture-gen` | Genera texturas/skins con IA (camo, dorado, fibra de carbono, óxido…) para armas, herramientas y cualquier mesh, y las aplica automáticamente en Studio. | SyphoDev-yt/roblox-ai-skills |
| `modelado-3d/blender-game-artist` | Artista senior de Blender para Roblox: investiga la referencia real, modela props y entornos, hace UVs, bake, materiales, texturizado y exportación. | kapscripts/claude-skills |
| `packs/claude-roblox-game-studio/.claude/skills/generate-asset` | Crea modelos 3D desde texto o los descarga de PolyHaven/Sketchfab. | CodePhobiia/claude-roblox-game-studio |
| `packs/claude-roblox-game-studio/.claude/skills/asset-from-image` | Convierte imágenes de referencia en assets 3D. | CodePhobiia/claude-roblox-game-studio |

## 🖥️ Interfaces (UI)

| Skill | Qué hace | Origen |
|---|---|---|
| `ui/roblox-ui` | Construye GUIs headless desde una spec JSON (HUD, tienda, inventario, ajustes) y genera el set de iconos: mockup PNG + `.model.json` de Rojo + builder Luau desde un único árbol resuelto. | SyphoDev-yt/roblox-ai-skills |
| `ui/roblox-ui-designer` | Diseñador UI/UX senior para Roblox: HUDs, menús, inventarios, tiendas, recompensas, pantallas de carga, animación de UI y paso de Figma a Studio. | kapscripts/claude-skills |
| `ui/figma-to-roblox-ui` | Importa marcos de Figma a Studio con precisión: solo escala, AnchorPoint centrado, UIStroke escalable, UICorner en escala y formas complejas como imágenes. | xtrair/figma-to-roblox-ui |
| `ui/roblox-gui` | Referencia para construir HUDs, barras de progreso y menús: ScreenGui, SurfaceGui, BillboardGui, UDim2, tweens y lógica de LocalScript. | sentinelcore/roblox-skills |

## ✨ VFX

| Skill | Qué hace | Origen |
|---|---|---|
| `vfx/roblox-vfx` | VFX de nivel profesional headless: movimientos estilo anime, slashes, haces, impactos, auras y ultimates, con simulador en navegador para juzgar fotograma a fotograma. | SyphoDev-yt/roblox-ai-skills |

## 🔊 Audio

| Skill | Qué hace | Origen |
|---|---|---|
| `audio/roblox-sfx` | Busca, verifica y conecta el sonido del juego desde el Creator Store por asset id (pasos, disparos, UI, ambiente, música), sin subir archivos ni usar API key. | SyphoDev-yt/roblox-ai-skills |

## 🗺️ Mapas

| Skill | Qué hace | Origen |
|---|---|---|
| `mapas/roblox-map` | Construye y verifica mapas, niveles y arenas headless desde una spec JSON: greybox, cobertura, repisas, rampas, escaleras, spawns, kill planes y terreno voxel orgánico. | SyphoDev-yt/roblox-ai-skills |

## 🧑‍💻 Programación

| Skill | Qué hace | Origen |
|---|---|---|
| `programacion/roblox-code` | Luau que sobrevive a un playtest real: servidor autoritativo, servicios y controladores Knit, RemoteEvents, todo configurable en `Config` y reglas puras en módulos Core. | SyphoDev-yt/roblox-ai-skills |
| `programacion/roblox-security` | Anti-exploit: validación de acciones de jugador, monedas, stats y daño, revisión de patrones explotables y endurecimiento de Remotes. | sentinelcore/roblox-skills |
| `programacion/roblox-datastores` | Persistencia de datos: guardado/carga de stats e inventario, leaderboards, migraciones de versión, autosave y diagnóstico de pérdida de datos. | sentinelcore/roblox-skills |
| `programacion/roblox-remote-events` | Comunicación cliente-servidor: RemoteEvents/RemoteFunctions, sincronización de estado y defensa frente a su abuso. | sentinelcore/roblox-skills |
| `programacion/roblox-performance` | Rendimiento: FPS, streaming, draw calls, object pooling, LOD, MicroProfiler y mundos grandes. | sentinelcore/roblox-skills |
| `programacion/roblox-monetization` | Monetización: Game Passes, Developer Products, UGC y Premium Payouts, tanto en scripting como en el dashboard de Creator Hub. | sentinelcore/roblox-skills |
| `programacion/claude-api` | Referencia completa de la API de Claude / SDK de Anthropic: ids de modelo, precios, parámetros, streaming, tool use, MCP, agentes, caching, conteo de tokens y migración de modelos. | anthropics/skills |

## 🎨 Frontend

| Skill | Qué hace | Origen |
|---|---|---|
| `frontend/frontend-design` | Skill oficial de Anthropic para generar interfaces con una dirección estética y tipográfica definida, evitando el aspecto genérico y repetitivo de la IA. | anthropics/skills |

## 🗂️ Planificación

| Skill | Qué hace | Origen |
|---|---|---|
| `planificacion/planning-with-files` | Bucle de planificación persistente en disco (`task_plan.md`, `findings.md`, `progress.md`) con hooks de ciclo de vida y recuperación automática; pensado para tareas largas y refactorizaciones multiarchivo. | OthmanAdi/planning-with-files |

## 🤖 Agentes y orquestación

| Skill | Qué hace | Origen |
|---|---|---|
| `agentes/orchestrating-chat-agents` | Reparte trabajo de Claude en paralelo por la API de Anthropic: contexto compartido en caché, streaming, hilos de conversación largos y pools de agentes con nombre. Útil para análisis paralelos y revisiones con múltiples perspectivas. | oaustegard/claude-skills |
| `agentes/swarm-orchestration` | Orquesta "enjambres" de agentes con agentic-flow: ejecución paralela, topologías dinámicas y coordinación inteligente, con scripts de arranque y monitorización. | ruvnet/ruflo (`@claude-flow/cli`) |

> El skill `orchestrating-agents` que pediste fue renombrado aguas arriba a `orchestrating-chat-agents`;
> se incluye la versión mantenida.

## 📺 YouTube

| Skill | Qué hace | Origen |
|---|---|---|
| `youtube/youtube-agent-skills` | Pack de 11 skills (`yt-*`) para operar un canal: guiones con ganchos puntuados, SEO, retención, planificación semanal, Shorts, auditoría, capítulos, comentarios, edición, empaquetado y análisis de lo viral. | BEHA-AF/youtube-agent-skills |
| `youtube/youtube-marketing-skills` | Toolkit de crecimiento con 21 comandos, agentes especializados y un servidor MCP conectado a la API de YouTube: analíticas, títulos/descripciones/etiquetas, actualizaciones masivas y campañas de email. | adityaarsharma/youtube-marketing-skills |

## 🎬 Vídeo con código

| Skill | Qué hace | Origen |
|---|---|---|
| `video/xilo-opus-video` | Crea vídeos escribiendo código (Canvas/HTML/CSS/SVG, WebGL, Three.js, Remotion, Manim): propone tres ideas con keyframes, y tras confirmar renderiza frame a frame con Playwright y FFmpeg. | Kianzzz/xilo-opus-video |
| `video/claude-awesome-video-creation` | Vídeos tutoriales y explicativos "follow-along": guion, voz, música, subtítulos y una mascota con lip-sync, sincronizados en una línea de tiempo basada en la voz. | HaochenSHI66/claude-awesome-video-creation |
| `video/code-video` | Investiga un tema y renderiza un vídeo promocional en MP4 con estilos visuales concretos (dibujado a mano, 8-bit y otros). | Changroro/code-video |

## 📦 Packs

| Pack | Qué incluye | Origen |
|---|---|---|
| `packs/claude-roblox-game-studio` | Suite completa: 51 skills en `.claude/skills/` (`start`, `prototype`, `generate-asset`, `team-ui`, `team-combat`, `wiki-*`, `perf-profile`…), más `CLAUDE.md`, reglas, wiki de Luau/Roblox, plantillas de proyecto y herramientas de Studio. | CodePhobiia/claude-roblox-game-studio |
| `packs/roblox-game-skill` | Skill de ciclo de vida completo: workflows, referencias profundas de animación/VFX y sistemas GUI, plantillas y documentación de juego. | brockmartin/roblox-game-skill |
| `packs/create-roblox-game` | Lleva un juego de "género" a construido, jugable y publicado, una sección por sesión, con `HANDOFF.md` entre sesiones para no perder contexto. | SyphoDev-yt/roblox-ai-skills |
| `packs/roblox-build-orchestrator` | Ejecuta el pipeline como una run temporizada y logueada (investigación, diseño, código, arte, ensamblaje, playtest, publicación) repartiendo el bloque de assets a subagentes. Incluye `agents/`. | SyphoDev-yt/roblox-ai-skills |
| `packs/superpowers` | Suite de 15 skills de desarrollo: brainstorming antes de crear, planes escritos, TDD, depuración sistemática, revisiones de código, worktrees de git, agentes en paralelo y verificación antes de dar algo por terminado. | obra/superpowers |

## 🛠️ Utilidades

| Skill | Qué hace | Origen |
|---|---|---|
| `utilidades/roblox-skills-setup` | Comprueba qué herramientas hay en la máquina (Python, Rojo, Wally, Lune, Selene, StyLua, Blender, MCP de Studio), guía lo que falte y escribe el `LOCAL.md` de cada skill. | SyphoDev-yt/roblox-ai-skills |

---

**Cobertura del pack SyphoDev-yt/roblox-ai-skills:** sus 11 skills están repartidos por categoría —
`roblox-animation` → animación, `roblox-3d-model` y `roblox-texture-gen` → modelado 3D,
`roblox-ui` → UI, `roblox-vfx` → VFX, `roblox-sfx` → audio, `roblox-map` → mapas,
`roblox-code` → programación, `create-roblox-game` y `roblox-build-orchestrator` → packs y
`roblox-skills-setup` → utilidades.
