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

## 📦 Packs "todo en uno"

| Pack | Qué incluye | Origen |
|---|---|---|
| `packs/claude-roblox-game-studio` | Suite completa: 51 skills en `.claude/skills/` (`start`, `prototype`, `generate-asset`, `team-ui`, `team-combat`, `wiki-*`, `perf-profile`…), más `CLAUDE.md`, reglas, wiki de Luau/Roblox, plantillas de proyecto y herramientas de Studio. | CodePhobiia/claude-roblox-game-studio |
| `packs/roblox-game-skill` | Skill de ciclo de vida completo: workflows, referencias profundas de animación/VFX y sistemas GUI, plantillas y documentación de juego. | brockmartin/roblox-game-skill |
| `packs/create-roblox-game` | Lleva un juego de "género" a construido, jugable y publicado, una sección por sesión, con `HANDOFF.md` entre sesiones para no perder contexto. | SyphoDev-yt/roblox-ai-skills |
| `packs/roblox-build-orchestrator` | Ejecuta el pipeline como una run temporizada y logueada (investigación, diseño, código, arte, ensamblaje, playtest, publicación) repartiendo el bloque de assets a subagentes. Incluye `agents/`. | SyphoDev-yt/roblox-ai-skills |

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
