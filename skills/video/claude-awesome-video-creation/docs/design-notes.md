# README design notes

The README moves from a visual cover and installation into the production model, then explains the mechanisms, example source and verification criteria. Detailed reference links follow that introduction so a new reader can understand the skill before exploring the full library.

## References

Reviewed on 2026-11-16:

| Reference | Design principle used here |
| :--- | :--- |
| [Remotion](https://github.com/remotion-dev/remotion) | Large product illustration, concise explanation, and a direct path into installation and documentation |
| [Browser Use](https://github.com/browser-use/browser-use) | Strong visual identity, a compact explanation of the execution model, and concrete examples |
| [Dify](https://github.com/langgenius/dify) | Coherent cover and navigation that separates getting started from deeper documentation |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Explain the system’s role before expanding into capabilities and reference material |
| [AutoFigure — ICLR 2026](https://openreview.net/forum?id=5N3z9JQJKq), [paper HTML](https://arxiv.org/html/2602.03828v1) | Extract entities and relationships, plan a symbolic layout, inspect structural fidelity, then refine visual presentation |

AutoFigure separates conceptual grounding and layout generation from aesthetic synthesis and text correction. This README borrows that design logic; it does not run AutoFigure or reproduce a figure from the paper. It uses deterministic SVG drawing so the terminology, geometry and relationships remain editable. The paper’s example palette is a presentation choice rather than a requirement of its method.

## Visual system

The cover extends the skill’s existing navy, Cobalt2, cyan, violet, gold and lime palette. The workflow uses a light canvas to keep dense text readable in either GitHub theme. Color is tied to a stage: violet for planning, cyan for voice and timing, amber for composition, and green for verification and delivery. A pink dashed return path denotes revision. Numbers, headings and line styles preserve those distinctions when color is less visible.

The original line icons share a consistent stroke weight. Presenter artwork comes from the repository’s existing *Teach It Once* sprites, which the skill credits as original AI-generated artwork. The terminal on the cover is labeled as a workflow illustration; the presenter strip shows actual source assets. Neither is represented as a rendered video frame.

## Workflow semantics

The diagram describes tutorial production. The approved script feeds voice preparation. Voice takes produce word timing data, and that data feeds the shared timeline. The timeline drives three composition channels: picture, captions and optional presenter, and sound. Their outputs are assembled through segmented rendering and audio muxing. QA precedes delivery, with a return path for timing or composition changes.

Recorded-word timing is estimated by syllable weight in the bundled voice workflow. It is not described as phoneme recognition or forced alignment. The QA numbers in the README are acceptance targets rather than new benchmark results. The example timeline defines a 116-second cut, correcting the older README’s 1:54 description.

## Editing and rebuilding

Edit `figures/specs/workflow.json` for wording, node geometry and connections. It follows the FigureSpec node and edge schema, with additional presentation fields for icons, bands, body lines, file labels and orthogonal routes. The standard FigureSpec validator checks the base graph; `render_assets.py` renders the README presentation from the same source.

Run from the repository root:

```bash
python3 docs/render_assets.py
```

This rebuilds the SVG cover, workflow, presenter strip and icons using only the Python standard library. Change the renderer source or JSON, then regenerate; do not hand-edit generated SVGs. The text remains selectable and the embedded presenter images remain raster assets.

The README uses PNG copies of the cover and presenter strip to keep their embedded sprites portable. Rasterize them at their native dimensions with an SVG renderer that supports embedded PNGs and system fonts. The checked-in PNGs were rendered with `@resvg/resvg-js`:

```bash
npm install --prefix /tmp/video-readme-render @resvg/resvg-js
NODE_PATH=/tmp/video-readme-render/node_modules node - <<'JS'
const fs = require('node:fs');
const { Resvg } = require('@resvg/resvg-js');
for (const name of ['hero', 'presenter', 'workflow']) {
  const path = `docs/assets/${name}`;
  const image = new Resvg(fs.readFileSync(`${path}.svg`), {
    font: { loadSystemFonts: true },
  }).render();
  fs.writeFileSync(`${path}.png`, image.asPng());
}
JS
```

The workflow and icons are displayed directly as SVG. All README artwork is local; only the live Shields.io badges are external. Review at GitHub content width and on a narrow screen, with the full-size workflow link available for dense labels.
