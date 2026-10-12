# MCIT AI Library

A curated template reference library for the MCIT document-generation agent.
Technology-topic templates indexed from Visme's template gallery, organized
by category, paired with free/open-source generator tools the agent can drive
programmatically.

## Contents

- `templates.json` — master index: every template with name, category,
  Visme URL, and thumbnail URL.
- `categories/<slug>.json` — per-category index (same schema, filtered).
- `gallery.html` — visual browser: browse all templates by category,
  click through to the Visme template page.
- `free-tools-research.md` — free/open-source generator per category,
  with GitHub URL, license, and what it generates.
- `SKILL.md` — the agent skill: how to pick a template and customize it.
- `raw/` — raw scrape outputs (one JSON per category).

## Categories

Presentations, Infographics, Reports, Charts & Graphs, Whiteboards,
Forms & Surveys, Documents, Social Media Graphics, Videos, Ebooks,
Proposals, Newsletters, Brochures, Posters, Flyers, Timelines,
Flowcharts, Banners, and more. See `templates.json` for the full list.

## How the agent uses it

1. Read `templates.json` (or the category file) and match the user's
   request to a template by category + name keywords.
2. Open the template's Visme URL as the visual reference.
3. Generate the deliverable with the free tool listed for that category
   in `free-tools-research.md`, following the template's structure:
   layout, section order, and visual hierarchy — not its copyrighted
   artwork, photos, or text.
4. Apply the MCIT Platinum theme unless the user asks otherwise.

## License note

Template metadata (names, categories, URLs, thumbnail links) is factual
reference data. Template designs themselves belong to MCIT AI
