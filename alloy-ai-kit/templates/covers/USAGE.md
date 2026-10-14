# Constant Cover Images — Agent Usage Guide

These covers are APPROVED and CONSTANT. Every presentation and every
report the agent generates opens and closes with them. Do not redesign
them, do not substitute stock art, do not recolor them.

## Files

- `cover-hero.png` — opening cover art (2048x1152). Midnight Noir
  hero with gold ornament. Use for: first slide of every deck,
  cover page of every PDF report.
- `cover-end.png` — closing cover art (2048x1152). Use for: last
  slide of every deck, back cover of every PDF report.
- `cover-clean.png` — the Noir background WITHOUT ornament. Use only
  when a cover needs a clean variant (rare; default to the ornament
  versions).
- `PALETTE.md` — the sampled Midnight Noir palette. The single source
  of truth for hex values.

## How the agent uses them (exactly as the reference builds did)

### PowerPoint (PptxGenJS + DeckCraft)

1. First slide: full-bleed image `cover-hero.png` (cover the whole
   13.33x7.5in slide), then native text boxes on top: eyebrow
   (top-left), title (Nohemi Bold), subtitle (Libre Franklin).
   The MCIT logo goes on a white rounded card, top-left.
2. Last slide: full-bleed `cover-end.png`, centered "Thank You"
   (Nohemi), MCIT line + URL in Pale Gold.
3. Content slides: solid Midnight `#010612` (dark) or white (light)
   backgrounds — never the cover art. One accent per slide.
4. Reference builder: `~/workspace/wsis-deck/build_deck.py` (dark),
   `build_deck_light.py` (light). Reference output:
   `../powerpoint/MCIT-WSIS-Egypt-30-DARK.pptx` /
   `MCIT-WSIS-Egypt-30-LIGHT.pptx`.
5. QA every deck with DeckCraft render before delivery.

### PDF report (ReportLab + PdfCraft)

1. Cover page: `cover-hero.png` across the top (full page width,
   ~335pt tall), title block below on Midnight `#010612`.
2. Back cover: `cover-end.png` across the top, "Thank You" block below.
3. Reference builder: `~/workspace/wsis-deck/build_report_noir.py`
   (4-page sample), `build_report_noir_full.py` (7-page full report).
4. Dark and light versions share structure; only the palette flips.
   The cover art itself never changes between themes.

### Word report (WordCraft)

1. Cover: `insert.picture` with base64 `cover-hero.png` (NOT `path=`,
   which is broken in headless mode), then `caret.docEnd` before any
   paragraph command (a bare `newParagraph` after insert deletes the
   picture).
2. Back cover: same pattern with `cover-end.png`.
3. Reference driver: `~/workspace/wsis-deck/build_docx_wordcraft.py`.

## Rules

- Gold ornament lives ONLY on these covers. Never add gold
  decoration to content slides or pages.
- Never stretch the art non-uniformly; always preserve aspect ratio.
- The logo sits on a constant white card, never directly on the art.
- If the user asks for a different cover, ask — do not freelance.
