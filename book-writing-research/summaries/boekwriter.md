# Repository Report: boekwriter

## Repository
- **Name**: boekwriter
- **URL**: https://github.com/andrei-dubovik/boekwriter
- **Commit**: `4c4abd45`
- **Status**: SUCCESS
- **Primary purpose**: Automated non-fiction book generator compiling directly into professional LaTeX and PDF formats with SVG diagrams, tables, and illustrations.
- **Primary target**: Non-fiction (Technical, Academic, Textbooks, Informational).

---

## Important Paths
- `queries.yaml`: Master specification of structured LLM queries, prompts, and output JSON schemas.
- `write_book.py`: Python orchestrator executing book generation, word budget allocation, chunk drafting, and LaTeX assembly.
- `template.tex`: Professional LaTeX book template configured with `booktabs`, figure environments, and typography packages.
- `llmwrapper/`: Python wrapper handling LLM API calls, structured JSON schema parsing, and token caching.

---

## Workflow
Book Title & Target Word Count 
→ Chapter Breakdown with Word Budget Allocation (`queries.yaml: chapters`) 
→ Detailed Chapter Item Planning with Item-Level Word Budgets (`queries.yaml: chapter-outline`) 
→ Visual Aid Selection & Planning (`queries.yaml: visuals`) 
→ Sequential Chunk-by-Chunk Prose Drafting with Prior-Chunk Context (`queries.yaml: chunk`) 
→ SVG Figure Generation (`queries.yaml: figure`) 
→ LaTeX Table Generation (`queries.yaml: table`) 
→ Chapter Headpiece Illustration Description & Image Generation (`queries.yaml: headpiece` & `image`) 
→ LaTeX Manuscript Compilation into PDF (`template.tex` via pdflatex/xelatex).

---

## Inputs and Outputs

```text
Stage 1: Book Architecture & Budgeting
Input: Book title (${book}), Total word count budget (${word_count}), Min words per chapter (${min_words})
Process: queries.yaml: chapters
Output: JSON array: [{number, title, description, word_count}]
Used by next stage: Chapter Outlining

Stage 2: Chapter Planning & Sub-Budgets
Input: Chapter title, chapter description, chapter word budget
Process: queries.yaml: chapter-outline
Output: JSON array: [{item, word_count}] (Sentence-long plan items with individual word counts)
Used by next stage: Visuals planning & Chunk drafting

Stage 3: Visual Aid Architecture
Input: Chapter plan, word budget
Process: queries.yaml: visuals
Output: JSON array: [{number, aid: "Table"|"SVG"|"Photo", description}]
Used by next stage: Chunk drafting & Figure generators

Stage 4: Chunk Drafting
Input: Book outline, Chapter plan, Current plan point, Parent chunk text, Visual description
Process: queries.yaml: chunk
Output: Technical prose chunk (Markdown text + LaTeX math formulas)
Used by next stage: LaTeX book assembly

Stage 5: Visuals & Headpiece Generation
Input: Text chunk referencing figure/table
Process: queries.yaml: figure / table / headpiece / image
Output: Valid SVG code, LaTeX tabular code, PNG chapter headpiece image
Used by next stage: Final LaTeX build
```

---

## Prompt Inventory

### Prompt: Chapter Breakdown with Word Budgeting
- **File**: `queries.yaml` (query: `chapters`)
- **Purpose**: Decomposes a book into chapters and allocates a strict mathematical word budget per chapter.
- **Required inputs**: `${book}`, `${word_count}`, `${min_words}`.
- **Expected output**: JSON schema: `[{number: int, title: str, description: str, word_count: int}]`.
- **Important constraints**: Sum of chapter word counts must fit overall book budget.
- **Downstream consumer**: `chapter-outline` query.

### Prompt: Sequential Chunk Drafting with Prior-Chunk Anchor
- **File**: `queries.yaml` (query: `chunk`)
- **Purpose**: Drafts a single section point while maintaining immediate continuity with the preceding text.
- **Required inputs**: `${book}`, `${chapters}`, `${cid}`, `${outline}`, `${oid}`, `${parent_chunk}`, `${min_words}`, `${max_words}`, `${visual}`.
- **Expected output**: Prose chunk adhering to exact word boundaries, integrating LaTeX math and figure references.
- **Important constraints**: Concise writing, no headers, use Markdown and LaTeX syntax.
- **Downstream consumer**: `write_book.py` LaTeX assembler.

---

## Context / Memory Strategy
- **Macro Memory**: Entire chapter outline passed in context.
- **Local Continuity**: Exact preceding chunk text (`${parent_chunk}`) injected into the prompt when generating point `${oid + 1}`.
- **Word Budget Tracking**: Exact min/max word targets dynamically calculated and enforced per chunk.

---

## Editing Strategy
- **Developmental editing**: Handled structurally via mathematical budget allocation and outline validation.
- **Continuity**: Enforced via prior-chunk injection (`parent_chunk`).
- **Fact checking**: Absent.
- **Line editing**: Handled via prompt constraints ("Be concise in your writing, avoid overly verbose prose").
- **Copy editing**: Absent.
- **Proofreading**: Absent.
- **Style review**: Enforced via prompt rules.

---

## Export / Assembly Strategy
- **Manuscript source format**: Structured JSON cache + LaTeX (`.tex`).
- **Chapter organization**: Scripted assembly in `write_book.py`.
- **Assembly method**: Python script populating `template.tex` and running `pdflatex`.
- **Output formats**: Professional PDF.
- **Scripts/tools required**: Python, LaTeX (pdflatex), SVG/Image tools.

---

## Strongest Ideas
1. **Mathematical Word Budget Allocation**: Downward cascading word budgets (Book → Chapters → Outline Items → Chunks).
2. **Integrated Visual Generation**: Automated creation of SVG diagrams, LaTeX tables, and chapter headpiece illustrations linked to text.
3. **Structured JSON Schema Enforcement**: Every generation stage uses strict schema validation.

---

## Weaknesses
- Exclusively designed for non-fiction/technical books; lacks fiction narrative devices (character arcs, dialogue).
- No post-drafting editorial or revision passes.

---

## Reusable Knowledge
- Hierarchical word-budget allocation prompt logic.
- Structured schema-driven chunk generation with prior-chunk context (`parent_chunk`).
- Integrated SVG and LaTeX table prompt patterns.
