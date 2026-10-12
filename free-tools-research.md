# Free & Open-Source Generator Tools — Research Report

**Date:** 2026-10-13
**Purpose:** For each Visme template category, the best free/open-source tools an AI agent can drive programmatically (API, CLI, or code library). GUI-only editors are excluded.

**Selection criteria:** permissive license preferred (MIT/Apache-2.0), actively maintained, headless-capable, agent-drivable. Licenses were checked against the repos on 2026-10-13; re-verify at the linked repo before shipping a product on it.

---

## 1. Presentations

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| PptxGenJS | https://github.com/gitbrent/PptxGenJS | MIT | Native `.pptx` decks from JS/TS code; zero dependencies, runs in Node or browser. |
| python-pptx | https://github.com/scanny/python-pptx | MIT | Reads + writes `.pptx` from Python; can load and fill branded template files, native OOXML charts. |
| Apache POI | https://github.com/apache/poi | Apache-2.0 | Enterprise-grade OOXML manipulation for Java/Kotlin stacks. |

## 2. Infographics

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| antvis/Infographic | https://github.com/antvis/Infographic | MIT | Code-driven infographic rendering framework (`.ifgc` syntax → SVG/PNG/PDF); AI-oriented, headless pipeline proven. |
| antvis/GPT-Vis | https://github.com/antvis/GPT-Vis | Apache-2.0 | LLM-friendly chart/infographic components with SSR bindings for server-side rendering. |
| Satori | https://github.com/vercel/satori | MIT | HTML/CSS → SVG/PNG; ideal for stat cards, KPI blocks, and social-style infographic tiles. |

## 3. Reports

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Typst | https://github.com/typst/typst | Apache-2.0 | Programmable markup → PDF; ~30MB static binary, millisecond renders, no browser needed. Best agent-driven report engine. |
| WeasyPrint | https://github.com/Kozea/WeasyPrint | BSD-3-Clause | HTML/CSS → PDF; design reports like web pages (Jinja2 templating pairs well). |
| ReportLab | https://github.com/reportlab/reportlab | BSD (open-source core) | Low-level Python PDF canvas + Platypus layout engine; precise control for formal documents. |

## 4. Whiteboards

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| tldraw SDK | https://github.com/tldraw/tldraw | MIT | Embeddable infinite-canvas whiteboard; agent can create shapes/docs via its TypeScript API. |
| Excalidraw | https://github.com/excalidraw/excalidraw | MIT | Hand-drawn-style whiteboard component; export to PNG/SVG/JSON programmatically. |

## 5. Forms & Surveys

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| SurveyJS | https://github.com/surveyjs/survey-library | MIT | JSON-defined surveys/forms rendered headlessly; full API for building and collecting responses. |
| Formbricks | https://github.com/formbricks/formbricks | AGPL-3.0 | Self-hosted survey platform with API; use when a managed survey backend is needed (copyleft — check before commercial embedding). |

## 6. Charts & Graphs

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Apache ECharts | https://github.com/apache/echarts | Apache-2.0 | Declarative browser charts (bar/line/pie/scatter/radar/treemap/...); render headless via puppeteer or its SSR. |
| Vega-Lite | https://github.com/vega/vega-lite | BSD-3-Clause | JSON grammar of graphics → SVG/Canvas; perfect for agents (charts as pure data). |
| Matplotlib | https://github.com/matplotlib/matplotlib | PSF/BSD-style | Python plotting to PNG/PDF/SVG; the standard for analytical, publication-grade figures. |

## 7. Documents

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Typst | https://github.com/typst/typst | Apache-2.0 | Same engine as reports; excellent for contracts, manuals, structured docs. |
| docx (dolanmiu) | https://github.com/dolanmiu/docx | MIT | Generates `.docx` from JS/TS with a declarative API. |
| Pandoc | https://github.com/jgm/pandoc | GPL-2.0 | Universal document converter (Markdown ↔ DOCX/EPUB/PDF/...); copyleft, best used as an external binary. |

## 8. Social Media Graphics

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Satori | https://github.com/vercel/satori | MIT | HTML/CSS → PNG/SVG; the standard way agents generate OG images, quote cards, promo tiles. |
| Pillow | https://github.com/python-pillow/Pillow | HPND (permissive) | Python image compositing; full pixel control for banners, thumbnails, overlays. |
| fabric.js | https://github.com/fabricjs/fabric.js | MIT | Canvas object model in JS; scripted layout of text/shapes/images → export PNG/SVG. |

## 9. Videos

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| MoviePy | https://github.com/Zulko/moviepy | MIT | Python scripted video editing: cuts, compositing, text overlays, effects; renders via FFmpeg. |
| Motion Canvas | https://github.com/motion-canvas/motion-canvas | MIT | TypeScript code-driven vector animations with headless rendering; great for explainer videos. |
| FFmpeg | https://ffmpeg.org | LGPL/GPL (build-dependent) | The universal CLI behind everything: encode, mux, subtitles, thumbnails, format conversion. |

## 10. Ebooks

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Pandoc | https://github.com/jgm/pandoc | GPL-2.0 | Markdown → EPUB (also MOBI via KindleGen); the standard agent ebook pipeline. |
| WeasyPrint | https://github.com/Kozea/WeasyPrint | BSD-3-Clause | HTML/CSS → print-ready PDF ebooks with TOC, page numbers, and cover pages. |

## 11. Proposals

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Typst | https://github.com/typst/typst | Apache-2.0 | Templated proposals with variables (client name, pricing tables) rendered in milliseconds. |
| docx (dolanmiu) | https://github.com/dolanmiu/docx | MIT | Editable `.docx` proposals clients can redline; pairs with a JSON brief. |

## 12. Newsletters

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| MJML | https://github.com/mjmlio/mjml | MIT | Markup → responsive, client-proof HTML email; the industry standard for newsletters. |
| Maizzle | https://github.com/maizzle/maizzle | MIT | Tailwind-style HTML email framework with a CLI build; agent-friendly component workflow. |

## 13. Brochures

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| WeasyPrint | https://github.com/Kozea/WeasyPrint | BSD-3-Clause | HTML/CSS print layouts → PDF brochures (multi-column, bleeds, CMYK-ish control). |
| Satori + Pillow | https://github.com/vercel/satori / https://github.com/python-pillow/Pillow | MIT / HPND | Component-based brochure panels composited into print sheets. |

## 14. Posters

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Satori | https://github.com/vercel/satori | MIT | Large-format HTML/CSS → PNG/SVG posters; typography-driven designs. |
| Pillow | https://github.com/python-pillow/Pillow | HPND (permissive) | Photo + text poster compositing with full layout control in Python. |

## 15. Flyers

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Satori | https://github.com/vercel/satori | MIT | Same pipeline as posters, sized for flyer formats; fast iteration from templates. |
| WeasyPrint | https://github.com/Kozea/WeasyPrint | BSD-3-Clause | HTML → single-page PDF flyers with print CSS. |

## 16. Timelines

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Mermaid | https://github.com/mermaid-js/mermaid | MIT | Text → timeline/gantt/journey diagrams; renders to SVG headlessly via mermaid-cli. |
| vis-timeline | https://github.com/visjs/vis-timeline | Apache-2.0 + MIT (dual) | Interactive timeline component; agent feeds it JSON items. |

## 17. Flowcharts

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Mermaid | https://github.com/mermaid-js/mermaid | MIT | Text → flowcharts, sequence, state, ER diagrams; the default agent diagram tool. |
| diagrams (mingrammer) | https://github.com/mingrammer/diagrams | Apache-2.0 | Python → cloud/infra architecture diagrams as code (AWS/GCP/Azure icons). |
| Graphviz | https://graphviz.org | CPL-1.0 | DOT language → directed graphs; the classic, scriptable graph renderer. |

## 18. Mind Maps

| Tool | GitHub | License | What it generates |
|---|---|---|---|
| Mermaid (mindmap) | https://github.com/mermaid-js/mermaid | MIT | Indented text → mindmap diagrams; zero new tooling if Mermaid is already in the stack. |
| mind-elixir | https://github.com/ssshooter/mind-elixir | MIT | Interactive mind-map core; agent supplies the JSON node tree. |

---

## Agent-integration notes

- **One stack covers most categories:** Typst (reports/documents/proposals/ebooks-PDF), Satori (infographic tiles/social/posters/flyers/brochures), Mermaid (flowcharts/timelines/mind maps), ECharts or Vega-Lite (charts), PptxGenJS/python-pptx (presentations), MJML/Maizzle (newsletters), MoviePy + FFmpeg (videos), SurveyJS (forms), tldraw (whiteboards), Pandoc (ebook EPUB + format conversion).
- **Already proven in this workspace:** antvis/Infographic (`.ifgc` → SVG/PNG/PDF pipeline), PptxGenJS deck generators, Matplotlib report figures, MJML-style HTML email.
- **Caution on licenses:** Remotion is source-available under its own commercial license (not OSI open source) — prefer MoviePy/Motion Canvas for video. Formbricks and EbookLib are AGPL — fine for internal/self-hosted use, review before embedding in a commercial product. Pandoc/FFmpeg are GPL-family — safest used as external binaries, not linked libraries.
