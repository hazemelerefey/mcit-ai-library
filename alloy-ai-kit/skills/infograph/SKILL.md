---
name: alloy-infograph
description: Build infographics in the approved sketchnote style — real CC0 hand-drawn doodles plus VectorCraft headless layout. Zero image-generation APIs. Red/dark on white.
---

# Infograph skill

Use for one-page visual explainers. The default style is the
**sketchnote**: hand-drawn doodles, speech-bubble title, columns,
verdict box. It is built with zero image-generation APIs.

## When to use

Any request for an infographic, visual explainer, "how it works"
diagram, or sketchnote.

## Tools (default pipeline)

- **Open Doodles** — CC0 hand-drawn doodle SVGs at
  `~/workspace/tools/sketchnote-doodles/` (17 as of 2026-10-13).
  Free for any use, no attribution. Source: https://www.opendoodles.com
- **VectorCraft** — `~/workspace/tools/vectorcraft/vectorcraft-0.10.0-linux-x86_64/bin/vectorcraft-cli`
  headless layout: `file.new`, `shape.*`, `text.create`,
  `file.place` (doodles), `path.create` (arrows), `--export PNG`.
- Full method: `~/workspace/skills/infographic/SKETCHNOTE.md`

## Design tokens (sketchnote — approved)

- Red `#D92626` · Dark `#1A1A1A` · White background
- Big speech-bubble title (rounded rect + open-V tail)
- Column layout with central dashed divider; red rounded column headers
- Numbered red badges, bold headings, red underline accents
- Curved arrows with triangle heads between ideas
- One doodle per block, placed near the text it illustrates
- Verdict box bottom-center

## Workflow

1. **Write the content first.** Title, 2 columns (or sections) of
   3–4 blocks each, each block: number, bold heading, 2–3 short
   lines. Verdict: one line.
2. **Pick doodles.** Map each block to a doodle by vibe from
   `~/workspace/tools/sketchnote-doodles/`. Verify each SVG contains
   `<svg` and `<path` with sane byte size.
3. **Lay out in VectorCraft** (single chained `run`: artboard →
   shapes/text/places/paths → save → export PNG). Style each object
   right after creating it (selection-based styling).
4. **Read the PNG.** Fix overlaps, clipping, orphaned arrows,
   unbalanced whitespace. Dense but never cluttered.
5. **Deliver** after visual review.

## Worked example

Approved piece: `../templates/infograph/sketchnote-toolchain.png`
("AI TOOLCHAIN SKETCHNOTES") with `../templates/infograph/DESIGN.md`.
Built with zero image APIs — compare any new piece against it for
density, balance, and doodle placement.

## Gotchas

- `path.create` in/out handles are ABSOLUTE positions, not relative
  offsets — relative-looking values balloon curves across the canvas.
- `text.create` y is baseline-ish, not top — add manual offsets;
  measure with PIL for centering (no built-in centering).
- Fill color needs a second pass: create the shape, then
  `appearance.setItem` to recolor.
- Do NOT style after `file.place` — it would recolor the doodle.
- Open Doodles carry their own pink fills; close enough to the
  red/black scheme to leave untouched.

## Alternative methods (not default)

- **Hand-drawn "HOW X WORKS"** via `~/workspace/skills/infographic/`
  (amigoscode skill, MIT) — richer bespoke illustration but needs an
  image pipeline (Gemini key or equivalent).
- **Clean vector diagrams** via AntV Infographic —
  `../figures/SKILL.md` — for geometric, data-driven styles.

## References

- Template + design notes: `../templates/infograph/`
- No-API pipeline: `~/workspace/skills/infographic/SKETCHNOTE.md`
- Tool inventory: `../../tools/TOOLS.md`
