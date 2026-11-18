#!/usr/bin/env python3
"""Build README SVG assets from the checked-in layout and original sprite assets.

Run from any directory: python3 docs/render_assets.py
The workflow JSON follows FigureSpec; the local presentation layer adds icon,
band and orthogonal-edge fields without changing its nodes or dependencies.
Only Python's standard library is required. Never edit the generated SVGs.
"""
import base64
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
SKILL = ROOT.parent / 'skills/claude-awesome-video-creation'
INK, MUTED = '#17243D', '#56657D'
FONT = 'Arial, Helvetica, sans-serif'
MONO = 'Menlo, Consolas, monospace'
ICONS = {
    'script': '<path d="M8 3h10l6 6v20H8z M18 3v7h6 M12 15h8 M12 20h8 M12 25h5"/>',
    'voice': '<rect x="12" y="3" width="8" height="16" rx="4"/><path d="M7 14v2a9 9 0 0 0 18 0v-2 M16 25v5 M11 30h10"/>',
    'timing': '<circle cx="16" cy="17" r="11"/><path d="M16 10v7l5 3 M12 2h8 M16 2v4 M26 7l2-2"/>',
    'terminal': '<rect x="2" y="5" width="28" height="23" rx="4"/><path d="M2 11h28 M8 16l4 4-4 4 M16 24h7"/>',
    'mascot': '<rect x="5" y="10" width="22" height="18" rx="7"/><path d="M16 5v5 M13 4h6 M1 16v7 M31 16v7 M11 22q5 5 10 0"/><circle cx="11" cy="17" r="1"/><circle cx="21" cy="17" r="1"/>',
    'music': '<path d="M12 23V8l16-4v15 M12 12l16-4"/><ellipse cx="7" cy="25" rx="5" ry="4"/><ellipse cx="23" cy="21" rx="5" ry="4"/>',
    'check': '<path d="M16 2l12 5v9c0 7-12 14-12 14S4 23 4 16V7z M10 16l4 4 8-9"/>',
    'render': '<rect x="3" y="3" width="26" height="26" rx="4"/><path d="M3 10h26 M10 3v7 M21 3v7 M13 15l8 5-8 5z"/>',
}


def text(x, y, value, size=22, color=INK, weight=400, anchor='start', font=FONT):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'


def rect(x, y, w, h, fill, stroke='none', radius=18, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" {extra}/>'


def icon(name, x, y, color, size=32):
    return f'<g transform="translate({x} {y}) scale({size / 32})" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>'


def svg(w, h, title, desc, content):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>{content}</svg>\n'


def sprite(name):
    path = SKILL / f'assets/examples/teach-it-once/mascot/{name}.png'
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode()


def workflow():
    spec = json.loads((ROOT / 'figures/specs/workflow.json').read_text())
    parts = [rect(0, 0, 1560, 1480, '#F7F9FD', radius=24)]
    colors = sorted({e['color'] for e in spec['edges']})
    parts.append('<defs>')
    for i, color in enumerate(colors):
        parts.append(f'<marker id="arrow{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M1 1L9 5L1 9" fill="none" stroke="{color}" stroke-width="1.6"/></marker>')
    parts.append('</defs>')
    parts += [text(60, 66, 'From brief to verified video.', 40, weight=700),
              text(60, 108, 'The tutorial workflow: explicit artifacts, shared timing and measured review.', 23, MUTED)]
    for x, color, label, dashed in [(60, '#8895AD', 'Production flow', False), (375, '#24B8D0', 'Shared timing', False), (670, '#D1749C', 'Revise and re-render', True)]:
        dash = 'stroke-dasharray="7 5"' if dashed else ''
        parts.append(f'<path d="M{x} 146h42" stroke="{color}" stroke-width="3" {dash}/>')
        parts.append(text(x + 54, 153, label, 20, MUTED))
    for b in spec['bands']:
        y = b['y']
        parts += [rect(40, y, 1430, b['height'], '#FFFFFF', '#E1E7F0', 20),
                  rect(60, y + 22, 54, 34, b['color'], radius=10),
                  text(87, y + 46, b['number'], 21, '#FFFFFF', 700, 'middle'),
                  text(65, y + 105, b['title'][0], 31, weight=700)]
        for i, line in enumerate(b['subtitle']):
            parts.append(text(65, y + 144 + 27 * i, line, 20, MUTED))
    for e in spec['edges']:
        color = e['color']
        dash = ' stroke-dasharray="8 7"' if e['style'] == 'dashed' else ''
        parts.append(f'<path d="{e["path"]}" fill="none" stroke="{color}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow{colors.index(color)})"{dash}/>')
        if 'label' in e:
            x, y = e['label_x'], e['label_y']
            parts += [rect(x - 124, y - 17, 248, 32, '#F7F9FD', radius=8),
                      text(x, y + 7, e['label'], 20, MUTED, anchor='middle')]
    for n in spec['nodes']:
        x, y = n['x'] - n['width'] / 2, n['y'] - n['height'] / 2
        color = n['stroke']
        parts += [rect(x, y, n['width'], n['height'], '#FFFFFF', '#DCE3EF', 16),
                  rect(x, y, 5, n['height'], color, radius=2),
                  rect(x + 16, y + 17, 38, 38, color, radius=11, extra='fill-opacity="0.12"'),
                  icon(n['icon'], x + 22, y + 23, color, 26),
                  text(x + 65, y + 43, n['label'], 22, weight=700)]
        for i, line in enumerate(n['lines']):
            parts.append(text(x + 20, y + 80 + i * 27, line, 19, MUTED))
        parts.append(text(x + 20, y + n['height'] - 18, n['file'], 15.5, '#52627F', font=MONO))
    parts += [text(60, 1445, 'Review failures return to timing and composition; update the source, preview the change, then render again.', 20, MUTED),
              text(60, 1470, 'Optional presenter assets are shown in the composition stage. Each check is run and inspected before delivery.', 18, MUTED)]
    out = svg(1560, 1480, spec['title'], 'Four stages: plan and approve the script; derive shared timing from voice; compose picture, captions, presenter and sound; render, inspect and deliver. A dashed feedback path returns failed reviews to the shared timeline.', ''.join(parts))
    (ASSETS / 'workflow.svg').write_text(out)


def hero():
    p = ['''<defs>
<radialGradient id="aurora"><stop stop-color="#234B82" stop-opacity=".75"/><stop offset="1" stop-color="#081024" stop-opacity="0"/></radialGradient>
<radialGradient id="violet"><stop stop-color="#7751AF" stop-opacity=".45"/><stop offset="1" stop-color="#081024" stop-opacity="0"/></radialGradient>
<linearGradient id="window" x2="1" y2="1"><stop stop-color="#254963"/><stop offset="1" stop-color="#10263D"/></linearGradient>
<linearGradient id="spectrum"><stop stop-color="#5EE7FF"/><stop offset=".35" stop-color="#B48CFF"/><stop offset=".7" stop-color="#FF9D78"/><stop offset="1" stop-color="#9BE564"/></linearGradient>
</defs>''', rect(0, 0, 1600, 790, '#081024', radius=28),
         '<ellipse cx="1120" cy="330" rx="620" ry="490" fill="url(#aurora)"/><ellipse cx="470" cy="760" rx="710" ry="430" fill="url(#violet)"/>']
    for x in range(40, 1600, 48):
        for y in range(32, 790, 48):
            p.append(f'<circle cx="{x}" cy="{y}" r="1" fill="#6F91BD" opacity=".15"/>')
    p += [icon('render', 65, 55, '#FFB38A', 36),
          text(114, 81, 'CLAUDE AWESOME VIDEO CREATION', 22, '#B7C7E3', 700),
          text(65, 228, 'Tutorial videos.', 83, '#F1F5FF', 700),
          text(65, 325, 'Built from code.', 83, '#F1F5FF', 700),
          rect(67, 354, 112, 5, 'url(#spectrum)', radius=2),
          text(68, 410, 'Script, voice, picture and sound.', 30, '#B7C7E3'),
          text(68, 455, 'One shared timeline. Measured QA.', 30, '#B7C7E3')]
    for x, title, col in [(68, 'Claude Code skill', '#E9A080'), (330, 'React / Remotion', '#5EE7FF')]:
        p += [rect(x, 512, 240, 49, col, radius=24, extra='fill-opacity=".1"'),
              text(x + 120, 544, title, 22, col, 600, 'middle')]
    # This is an architectural illustration, not a claim of a rendered film frame.
    p += [rect(850, 150, 660, 405, '#07111F', '#305275', 20),
          rect(836, 136, 660, 405, 'url(#window)', '#3B6080', 20),
          rect(836, 136, 660, 49, '#142A3D', radius=20),
          rect(836, 164, 660, 21, '#142A3D', radius=0)]
    for x, col in [(861, '#FF5F57'), (884, '#FEBC2E'), (907, '#28C840')]:
        p.append(f'<circle cx="{x}" cy="161" r="7" fill="{col}"/>')
    p += [text(1165, 167, 'tutorial — shared timeline', 18, '#ADC6DD', anchor='middle', font=MONO),
          text(865, 228, '01', 20, '#809DB8', font=MONO), text(913, 228, 'Narration → word timings', 23, '#5EE7FF', font=MONO),
          text(865, 273, '02', 20, '#809DB8', font=MONO), text(913, 273, 'timeline.ts', 23, '#B48CFF', font=MONO),
          text(865, 318, '03', 20, '#809DB8', font=MONO), text(913, 318, 'Picture + captions + sound', 23, '#FFC857', font=MONO),
          text(865, 363, '04', 20, '#809DB8', font=MONO), text(913, 363, 'Render → inspect → deliver', 23, '#9BE564', font=MONO)]
    # An original sprite from the checked-in worked example.
    p += [f'<image href="{sprite("wave")}" x="1192" y="335" width="350" height="350"/>',
          text(867, 408, 'VOICE', 14, '#8EAAC5', 700), text(867, 455, 'PICTURE', 14, '#8EAAC5', 700)]
    for i, h in enumerate([13, 24, 18, 36, 28, 16, 30, 22, 38, 18, 26, 14, 29, 20, 33, 22, 15, 28]):
        p.append(rect(958 + i * 12, 400 - h / 2, 5, h, '#5EE7FF', radius=2))
    for i, (w, col) in enumerate([(59, '#B48CFF'), (84, '#FFC857'), (65, '#9BE564')]):
        p.append(rect(958 + i * 77, 437, w, 25, col, radius=5, extra='fill-opacity=".75"'))
    p += [text(866, 510, 'Workflow illustration · original example mascot', 16, '#89A2C3')]
    p += [rect(40, 650, 1520, 103, '#0C1B34', '#233857', 18)]
    for x, name, label, col in [(69, 'script', 'Script & structure', '#B48CFF'), (440, 'voice', 'Voice & timing', '#5EE7FF'), (810, 'terminal', 'Motion & presenter', '#FFC857'), (1180, 'check', 'Render & review', '#9BE564')]:
        p += [rect(x, 677, 48, 48, col, radius=14, extra='fill-opacity=".12"'), icon(name, x + 9, 686, col, 30), text(x + 65, 710, label, 24, '#DFE8FA', 600)]
    (ASSETS / 'hero.svg').write_text(svg(1600, 790, 'Claude Awesome Video Creation', 'An Agent Skill for producing tutorial videos from code. Script, voice, motion, captions, an optional original mascot, sound and measured review share one timeline. The terminal is a workflow illustration.', ''.join(p)))


def sprite_sheet():
    p = [rect(0, 0, 1560, 410, '#0D1931', radius=22),
         text(44, 55, 'The original presenter, in the repository.', 30, '#EDF2FF', 700),
         text(44, 90, 'Selected source sprites from Teach It Once · optional presenter pipeline', 21, '#A8B8D4')]
    for i, (name, label) in enumerate([('closed', 'Closed'), ('ee', 'EE viseme'), ('oo', 'OO viseme'), ('wave', 'Wave'), ('point', 'Point'), ('cheer', 'Cheer')]):
        x = 28 + i * 252
        p += [rect(x, 115, 242, 260, '#132543', '#233D62', 14),
              f'<image href="{sprite(name)}" x="{x + 15}" y="110" width="212" height="240"/>',
              text(x + 121, 359, label, 20, '#C8D6EE', 600, 'middle')]
    (ASSETS / 'presenter.svg').write_text(svg(1560, 410, 'Original presenter source sprites', 'Six actual checked-in mascot sprites: closed mouth, EE and OO visemes, wave, point and cheer. The full example contains 19 sprites.', ''.join(p)))


def main():
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / 'icons').mkdir(exist_ok=True)
    for name, color in [('script', '#8B5CF6'), ('voice', '#089CB5'), ('timing', '#089CB5'), ('terminal', '#D38A22'), ('mascot', '#D7608A'), ('music', '#6079D6'), ('check', '#159C76'), ('render', '#159C76')]:
        body = rect(0, 0, 56, 56, color, radius=16, extra='fill-opacity="0.11"') + icon(name, 12, 12, color)
        (ASSETS / f'icons/{name}.svg').write_text(svg(56, 56, name, f'{name} icon', body))
    workflow()
    hero()
    sprite_sheet()
    print('Built hero, workflow, presenter and eight icons.')


if __name__ == '__main__':
    main()
