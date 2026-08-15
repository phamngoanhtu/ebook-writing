# Repository Report: bookgen

## Repository
- **Name**: bookgen
- **URL**: https://github.com/laqaer/bookgen
- **Commit**: `a4578467`
- **Status**: SUCCESS
- **Primary purpose**: Complete BookOps automated publication lifecycle system: ideation, proposal, writing, editing, KDP publishing, monetization, marketing, and web launch.
- **Primary target**: Both (Commercial Non-fiction & Fiction publishing).

---

## Important Paths
- `BOOKOPS_WORKFLOW.md`: Complete lifecycle specification defining the 7 phases of BookOps (Ideation, Proposal, Writing, Editing, Publishing, Monetization, Launch).
- `bookops.py`: Python automation engine executing stage transitions, quality gates, and file operations.
- `bookgen.py`: Automated generation script for chapter drafting and assembly.
- `STYLE_GUIDE.md`: Comprehensive style rules, voice guidelines, formatting constraints, and vocabulary standards.
- `RUNBOOK.md`: Step-by-step operational guide for running BookOps pipelines.
- `ideation/`: Market research, reader pain point identification, and competitor analysis tools.
- `proposal/`: Book proposal templates, table of contents, and sample chapters for stakeholders.
- `kdp-ready/`: Pre-formatted files and metadata ready for direct Amazon KDP upload.
- `marketing/`: Launch email sequences, social media copy, and press releases.
- `monetization/`: Backend product funnel templates (workbooks, courses, consulting upsells).
- `Makefile`: Make commands automating the entire build, test, lint, and publish process.

---

## Workflow
Phase 1: Ideation (`ideation/` — market validation, reader pain points)
→ Phase 2: Proposal (`proposal/` — book proposal, positioning, TOC)
→ Phase 3: Writing (`bookgen.py` — chapter drafting against `STYLE_GUIDE.md`)
→ Phase 4: Editing (`bookops.py` — multi-pass editorial review and linting)
→ Phase 5: Publishing (`kdp-ready/` — metadata, covers, interior formatting)
→ Phase 6: Monetization (`monetization/` — upsell funnels, companion workbooks)
→ Phase 7: Launch (`marketing/` & `launch/` — email sequences, press kits, site deployment).

---

## Inputs and Outputs

```text
Stage 1: Ideation & Market Validation
Input: Niche topic, target audience
Process: ideation/ analysis tools
Output: Validated market brief, reader avatar, competitor differentiation matrix
Used by next stage: Phase 2 Proposal

Stage 2: Proposal & Architecture
Input: Market brief, core thesis
Process: proposal/ generator
Output: Formal Book Proposal, Detailed Table of Contents, Chapter outlines
Used by next stage: Phase 3 Writing

Stage 3: Automated Drafting
Input: Chapter outline, STYLE_GUIDE.md
Process: bookgen.py generates chapter prose
Output: Raw manuscript markdown (manuscript/)
Used by next stage: Phase 4 Editing

Stage 4: Editing & Quality Gates
Input: Raw manuscript, style guide
Process: bookops.py editorial checks
Output: Polished manuscript (book.md)
Used by next stage: Phase 5 Publishing

Stage 5: Packaging & KDP Preparation
Input: Polished manuscript, metadata
Process: Makefile build targets (Pandoc / formatting scripts)
Output: KDP-ready EPUB, PDF, print interior, and metadata package (kdp-ready/)
Used by next stage: Phase 6 & 7 Monetization & Launch
```

---

## Prompt Inventory

### Prompt: BookOps Chapter Generator Prompt
- **File**: `bookgen.py`
- **Purpose**: Generates high-impact non-fiction chapters adhering strictly to `STYLE_GUIDE.md`.
- **Required inputs**: Chapter outline, Target word count, Tone specification, Reader takeaway goal.
- **Expected output**: Structured chapter markdown with intro hook, core frameworks, case studies, action steps, and recap.
- **Important constraints**: Must follow typography and header conventions in `STYLE_GUIDE.md`.
- **Downstream consumer**: `bookops.py` editing engine.

---

## Context / Memory Strategy
File-based project directories with central `OUTLINE.md`, `STYLE_GUIDE.md`, and master compilation manuscript `book.md`.

---

## Editing Strategy
- **Developmental editing**: Executed in Phase 4 via structural review against `OUTLINE.md`.
- **Continuity**: Validated against `STYLE_GUIDE.md`.
- **Fact checking**: Supported via proposal phase grounding.
- **Line editing**: Governed by `STYLE_GUIDE.md` rules.
- **Copy editing**: Automated linting in `bookops.py`.
- **Proofreading**: Final KDP inspection.
- **Style review**: Automated style adherence checks.

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown (`manuscript/` and master `book.md`).
- **Chapter organization**: Modular chapter files merged into master release files.
- **Assembly method**: `Makefile` + `bookops.py` + `pandoc`.
- **Output formats**: Markdown, EPUB, PDF, Print-ready PDF, KDP packages.
- **Scripts/tools required**: Python, Make, Pandoc.

---

## Strongest Ideas
1. **Complete BookOps Lifecycle Model**: Expanding beyond writing to include Proposals, KDP Publishing, Backend Monetization, and Marketing.
2. **Makefile-Driven Automation**: Reproducible CLI commands (`make build`, `make lint`, `make kdp`) for book generation and compilation.
3. **Formal `STYLE_GUIDE.md`**: Strict document governing tone, voice, formatting, and prohibited terminology.

---

## Weaknesses
- Chapter generation is relatively straightforward compared to the sophisticated scene-circuit architectures of specialized fiction templates.

---

## Reusable Knowledge
- The 7-Phase BookOps lifecycle framework (`BOOKOPS_WORKFLOW.md`).
- Style guide template for AI generation (`STYLE_GUIDE.md`).
- Makefile automation patterns for multi-format publishing.
