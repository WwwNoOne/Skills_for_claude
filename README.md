# Skills for Claude

Almacén personal de **skills** (Claude Code / Agent Skills) para desarrollo de videojuegos en **Roblox**
y para trabajo general: programación, orquestación de agentes, canales de YouTube y creación de vídeo
con código.

Cada carpeta de primer nivel es una categoría y cada subcarpeta es un skill listo para copiar a
`~/.claude/skills/` (o a `.claude/skills/` dentro de un proyecto).

## Paquetes

| Paquete | Contenido | Estado |
|---|---|---|
| **1. Roblox** | Animación, modelado 3D, UI, VFX, audio, mapas, programación y packs de juego | ✅ incluido |
| **2. Desarrollo, agentes, YouTube y vídeo** | Programación, orquestación, canales de YouTube y vídeo generado con código | ✅ incluido |

## Estructura

```text
skills/
├── animacion/          R6/R15, VFX y Blender
├── modelado-3d/        MeshParts, texturas y arte de Blender
├── ui/                 GUIs de Roblox, HUDs y Figma → Studio
├── frontend/           Diseño visual para interfaces web
├── vfx/                Partículas, haces y estelas
├── audio/              SFX y música
├── mapas/              Niveles, greybox y terreno
├── programacion/       Luau, seguridad, DataStores, rendimiento y API de Claude
├── planificacion/      Planificación persistente basada en archivos
├── agentes/            Orquestación de agentes y enjambres
├── youtube/            Guiones, SEO, retención, Shorts y marketing
├── video/              Vídeo generado con código (Canvas, Three.js, Remotion…)
├── packs/              Suites completas (juegos, superpowers)
└── utilidades/         Setup y comprobación de herramientas
```

Índice detallado de cada skill: **[CATALOGO.md](CATALOGO.md)**
Origen y licencias de cada aportación: **[CREDITOS.md](CREDITOS.md)**

## Instalación

Un skill = una carpeta con `SKILL.md`. Para instalarlos todos en Claude Code:

```bash
./instalar.sh            # enlaza cada skill en ~/.claude/skills
./instalar.sh --copiar   # copia en vez de enlazar
```

O a mano, skill por skill:

```bash
cp -r skills/animacion/roblox-animation ~/.claude/skills/
```

Para un proyecto concreto, usa `.claude/skills/` en la raíz del proyecto en lugar de `~/.claude/skills/`.

### Packs

Los packs traen su propio flujo de trabajo, no son un skill suelto:

- `packs/claude-roblox-game-studio/`: copia su `CLAUDE.md` al proyecto y los skills de
  `.claude/skills/` a `~/.claude/skills/` (51 skills: `start`, `prototype`, `team-ui`, `generate-asset`…).
- `packs/roblox-build-orchestrator/`: incluye `agents/`; sigue su sección *Setup* para instalar los
  subagentes en `~/.claude/agents/`.
- `packs/create-roblox-game/` y `packs/roblox-game-skill/`: orquestadores de ciclo completo; funcionan
  mejor con el resto de skills instalados.
- `packs/superpowers/`: plugin de 15 skills (brainstorming, planes, TDD, revisiones, worktrees…).
  Instálalo como plugin con `/plugin marketplace add obra/superpowers` o copia
  `packs/superpowers/skills/*` a `~/.claude/skills/`.
- `youtube/*/skills/` y `video/*/skills/`: skills anidados; `instalar.sh` los detecta e instala con su
  nombre propio (`yt-script`, `xilo-opus-video`, `youtube`…).

## Requisitos habituales

Python 3, [Rojo](https://rojo.space), [Wally](https://wally.run), [Lune](https://lune-org.github.io/docs),
[Selene](https://github.com/Kampfkarren/selene), [StyLua](https://github.com/JohnnyMorganz/StyLua),
Blender y el MCP oficial de Roblox Studio. El skill `utilidades/roblox-skills-setup` comprueba todo y
guía la instalación de lo que falte.

## Aviso

Contenido de terceros recopilado con fines personales. Cada skill conserva la licencia de su
repositorio original; revisa [CREDITOS.md](CREDITOS.md) antes de redistribuirlo o usarlo
comercialmente.
