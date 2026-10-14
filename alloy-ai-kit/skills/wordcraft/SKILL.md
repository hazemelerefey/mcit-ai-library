---
name: alloy-wordcraft
description: Build editable Word reports (.docx) with WordCraft — the craft toolchain for Word. Headless command sequences, constant Noir covers, visual QA per page.
---

# WordCraft skill

Use for editable Word documents: reports the user will revise in Word.
For fixed print PDFs use `../pdf-report/SKILL.md` instead.

## When to use

Any request for a .docx report, an editable version of a PDF report,
or Word-native delivery of a templated document.

## Tools

- **WordCraft** — `~/workspace/tools/wordcraft/wordcraft-0.6.1-linux-x86_64/bin/wordcraft-cli`
  Headless: `run [--file F] --cmd 'id={json}' ... --save OUT`.
  QA: `render <file> <out.png> --page N`. Info: `info`, `inspect`.
- Reference driver: `~/workspace/wsis-deck/build_docx_wordcraft.py`
  (7-page Noir report, dark + light — the pattern to copy).
- Template outputs: `~/workspace/your_files/MCIT-WSIS-Report-Noir-DARK.docx`
  / `-LIGHT.docx`.
- Covers: `../../templates/covers/` — see `USAGE.md`. Constant art.

## Workflow

1. **Pick the template.** Noir report = 7 pages: cover, contents,
   at-a-glance table, 2 figure pages, findings, back cover.
2. **Drive it with a command script.** A Python driver that assembles
   the `--cmd` list is the sane way (hundreds of commands). Set
   typing attributes (`format.font/size/color/bold`) BEFORE
   `text.insert`; paragraph props (`para.align/spacing`) before too.
3. **Covers.** `insert.picture` with base64 `data=` (see gotchas),
   then `caret.docEnd`, then continue. Hero art on page 1, end art
   on the last page.
4. **Tables.** `insert.table`, fill with Tab navigation, `caret.down`
   to exit. Header row bold + accent color.
5. **Render every page** (`render --page N`) and fix before delivery.

## Gotchas (all verified — do not rediscover them)

- `insert.picture` with `path=` is BROKEN in headless `run`. Use
  base64 `data=` (keep each arg under ~120KB; MAX_ARG_STRLEN).
- `text.newParagraph` immediately after `insert.picture` DELETES the
  picture. Always `caret.docEnd` (or `caret.right`) first.
- `para.borders` is STICKY: set it AFTER `text.insert` so it lands on
  the right paragraph, then clear with `{"kind":"none"}` or it leaks
  onto every following paragraph.
- Tab in the LAST table cell creates a new row — skip the trailing Tab.
- `design.pageColor` sets the page background (dark theme).
- Fonts are referenced by name; the reader needs them installed.

## References

- Master template index: `../../templates/TEMPLATES.md`
- Cover usage: `../../templates/covers/USAGE.md`
- Tool inventory: `../../tools/TOOLS.md`
