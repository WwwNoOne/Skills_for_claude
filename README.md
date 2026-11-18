# Skills for Claude

Almacén personal de **skills** (Claude Code / Agent Skills) para desarrollo de videojuegos en **Roblox**:
animación, modelado 3D, UI, VFX, audio, mapas, programación y packs "todo en uno".

Cada carpeta de primer nivel es una categoría y cada subcarpeta es un skill listo para copiar a
`~/.claude/skills/` (o a `.claude/skills/` dentro de un proyecto).

## Paquetes

| Paquete | Estado |
|---|---|
| **1. Roblox** (animación, modelado, UI, VFX, audio, mapas, programación, packs) | ✅ incluido |
| **2. Por definir** | ⏳ pendiente |

## Estructura

```text
skills/
├── animacion/          R6/R15, VFX y Blender
├── modelado-3d/        MeshParts, texturas y arte de Blender
├── ui/                 GUIs, HUDs y Figma → Studio
├── vfx/                Partículas, haces y estelas
├── audio/              SFX y música
├── mapas/              Niveles, greybox y terreno
├── programacion/       Luau, seguridad, DataStores, rendimiento
├── packs/              Suites completas de creación de juegos
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

## Requisitos habituales

Python 3, [Rojo](https://rojo.space), [Wally](https://wally.run), [Lune](https://lune-org.github.io/docs),
[Selene](https://github.com/Kampfkarren/selene), [StyLua](https://github.com/JohnnyMorganz/StyLua),
Blender y el MCP oficial de Roblox Studio. El skill `utilidades/roblox-skills-setup` comprueba todo y
guía la instalación de lo que falte.

## Aviso

Contenido de terceros recopilado con fines personales. Cada skill conserva la licencia de su
repositorio original; revisa [CREDITOS.md](CREDITOS.md) antes de redistribuirlo o usarlo
comercialmente.
