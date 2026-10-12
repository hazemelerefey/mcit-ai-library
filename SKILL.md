# MCIT AI Library Skill

Use this skill whenever generating a visual deliverable: presentations,
infographics, reports, whiteboards, forms/surveys, charts, documents,
or any other templated content.

## Step 1 — Pick a template

Read `~/workspace/mcit-ai-library/templates.json`. Match the request to:
- `category` — the deliverable type (presentations, infographics, ...).
- `name` — keywords describing the topic or layout.

Each entry has `name`, `url` (Visme template page), and `thumbnail`
(preview image URL). Open the thumbnail to see the layout.

## Step 2 — Pick the generator

Read `~/workspace/mcit-ai-library/free-tools-research.md`, find the
template's category, and use the listed free/open-source tool:

- presentations → PptxGenJS / python-pptx
- infographics → antvis/Infographic (.ifgc) / Satori
- reports → Typst / WeasyPrint / ReportLab
- charts & graphs → Apache ECharts / Vega-Lite / Matplotlib
- whiteboards → tldraw SDK / Excalidraw
- forms & surveys → SurveyJS
- documents → Typst / docx
- social media graphics → Satori / Pillow

## Step 3 — Customize professionally

Follow the template's **structure**: layout, section order, visual
hierarchy, and information density. Do NOT copy its artwork, stock
photos, or text content.

Apply in order:
1. The user's real data and copy (never lorem ipsum in final output).
2. MCIT Platinum theme (`#0A1A2F` navy, `#5E6B7A` steel, `#B9C2CE`
   silver, `#F4F6F8` light) unless the user specifies otherwise.
3. The user's standing design rules: no em/en dashes in prose, no
   gradient text, no glowing pills, no glassmorphism, no decorative
   gradient soup, sharp professional layouts.
4. Arabic deliverables are genuinely RTL: mirrored layout, right
   alignment, Arabic reshaping where the renderer needs it.

## Step 4 — Deliver

- Open and judge the output yourself before handing it over.
- Include the source template name and URL in your working notes so
  the choice is auditable.
- If the user wants to edit further in Visme, give them the template URL.
