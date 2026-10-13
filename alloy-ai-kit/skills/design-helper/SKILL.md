---
name: alloy-design-helper
description: VectorCraft headless vector design for stunning custom graphics — covers, diagrams, one-off artwork that the type tools cannot express. Sharp, flat, no AI-slop.
---

# Design helper skill (VectorCraft)

Use for custom vector designs that don't fit a document type:
covers, hero graphics, diagrams, decorative elements, one-off
artwork. VectorCraft is the helper, not a substitute — when a job
belongs to a type tool (deck, report, sheet), the type tool stays
in charge.

## When to use

- A design no type template can express.
- Custom diagrams, covers, or graphics for use inside documents.
- Sketchnote layout assembly (see `../infograph/SKILL.md`).

When NOT to use: building a deck (use the powerpoint skill),
a report (pdf-report skill), or a dashboard (spreadsheet skill).

## Tool

**VectorCraft** — `~/workspace/tools/vectorcraft/vectorcraft-0.10.0-linux-x86_64/bin/vectorcraft-cli`

Chain everything in one `run` invocation; each `--cmd ID --params JSON`
prints one JSON result. Styling is selection-based: style each object
immediately after creating it.

## Command basics

- `file.new {"width":1200,"height":800,"units":"Pixels","backgroundContents":"white"}`
- `shape.rectangle {"x":..,"y":..,"width":..,"height":..,"radius":..}` —
  then `appearance.setItem {"index":0,"color":"#0A1A2F"}` (fill),
  `appearance.setItem {"index":1,"color":"#5E6B7A"}` (stroke) or
  `{"index":1,"none":true}` (no stroke), `stroke.set {"weight":2}`.
- `shape.ellipse` — same styling pattern.
- `text.create {"x":..,"y":..,"text":..,"size":..,"font":"DejaVu Sans","style":"Bold","color":"#0A1A2F"}` —
  one text object per line.
- `file.place {"path":"<absolute path>","rect":[x,y,w,h]}` — places
  SVG/PNG artwork, fitted to rect, aspect kept.
- `path.create {"anchors":[...]}` — bezier paths; then `stroke.set`
  for weight, caps, dashes, arrowheads.
- `document.save {"path":"/tmp/work.vectorcraft"}` then `--export out.png`
  (1 unit = 1 px with Pixels units).

## Design rules

- One accent color, used sparingly. Flat surfaces, hairline borders.
- Platinum Silver default: navy `#0A1A2F`, steel `#5E6B7A`,
  silver `#B9C2CE`, light `#F4F6F8`.
- Banned: gradients, gradient text, glassmorphism, ambient glows,
  glowing pills, purple-blue soup, emojis as icons.

## Workflow

1. **Sketch the composition** (mentally or on paper): artboard size,
   zones, hierarchy, one focal point.
2. **Drive it with a script** (Python emitting the `--cmd/--params`
   chain is the proven pattern) — deterministic re-runs for layout
   iteration. Use PIL to measure text for centering.
3. **Export PNG, read it.** Fix overlaps, alignment, whitespace.
4. Iterate until it looks intentional.

## Worked example

The sketchnote toolchain infographic
(`../infograph/` template) was laid out entirely in VectorCraft:
122 chained commands, placed CC0 doodles, curved arrows, verdict
box — the reference for headless VectorCraft work.

## Gotchas

- Fill needs a recolor pass: `shape.*` creates, then
  `appearance.setItem` sets the color. No single-call fill.
- `text.create` y is baseline-ish, not top — add manual offsets.
- `path.create` in/out handles are ABSOLUTE positions, not
  relative offsets.
- Do not style after `file.place` — it recolors placed artwork.
- `select.set` + align-to-key is fiddly; manual measurement is
  more reliable.

## References

- Sketchnote pipeline: `~/workspace/skills/infographic/SKETCHNOTE.md`
- Infograph skill: `../infograph/SKILL.md`
- Tool inventory: `../../tools/TOOLS.md`
