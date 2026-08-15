# Research Corpus Handoff for Next Agent

> **Notice**: This handoff document summarizes the verified research corpus. It is designed to brief the future agent responsible for designing and composing book-writing Skills, agents, or master prompts. **No final Skills or master prompts were implemented during this research phase.**

---

## Research Corpus Status

- **Repositories requested**: 18
- **Repositories cloned**: 18
- **Repositories successfully verified**: 16
- **Repositories unavailable**: 2 (`prompts.chat` and `Prompt-Engineering-Guide` — shallow clone network depth constraint)
- **Repositories containing substantial reusable prompts**:
  - `writing-template-for-ai` (18+ production prompts and rules)
  - `The-Novelists-Atelier` (2,400+ lines of editorial prompts across 16 categories)
  - `speckit-preset-fiction-book-writing` (34 modular craft commands)
  - `libriscribe` (13 YAML prompt templates)
  - `novel-template` (10 specialized agent prompts)
  - `AI_Novel` (Genre-specific style instructions and 3-tier drafting templates)
  - `boekwriter` (Structured schema prompts with word budgets)
  - `KDP-Publishing-Prompt-Library` (Amazon metadata and sales copy prompts)
  - `bookgen` (BookOps workflow and style guide prompts)
- **Repositories primarily containing software**:
  - `LLM-book-generator` (Python orchestrator + DOCX builder)
  - `boekwriter` (Python LaTeX/PDF compiler)
  - `AI_Novel` (Flask web app & service engine)
  - `agentic-novel-outliner` (Node/Vite interactive outliner)
  - `bookgen` (Makefile BookOps automation)
  - `poison01022-ai-book-pipeline` (Experimental RL search)
- **Repositories primarily useful for editing**:
  - `The-Novelists-Atelier` (22-pass editorial analysis)
  - `writing-template-for-ai` (6 quality gates & prose suppression)
- **Repositories primarily useful for fiction**:
  - `writing-template-for-ai`, `novel-template`, `speckit-preset-fiction-book-writing`, `The-Novelists-Atelier`, `libriscribe`, `AI_Novel`, `AI-Novel-Writer`
- **Repositories primarily useful for non-fiction**:
  - `boekwriter`, `bookgen`, `KDP-Publishing-Prompt-Library`, `AI-Prompts-for-E-book-Generation`, `LLM-book-generator`

---

## Most Important Knowledge Areas Found

1. **Fractal Scene Architecture**: Requiring every scene to complete a formal circuit of change (Goal → Conflict → Disaster → Reaction → Dilemma → Decision).
2. **AI Prose Suppression Filters**: Explicit pattern-matching rules eradicating recognizable AI writing clichés ("delve", "tapestry", "beacon") and syntactic symmetry.
3. **Two-Tier Context & Canon Control**: Decoupling immutable world rules (`MEMORY.md` / `constitution.md`) from session logs (`CHANGELOG_AI.md`) and enforcing strict canon mutation control.
4. **Hierarchical Word-Budget Cascading**: Mathematical allocation of word counts from book level down to chapter, outline item, and chunk level.
5. **22-Pass Full Manuscript Editorial Audit**: Exhaustive multi-pass critique generating interactive HTML/PDF scorecards with SVG pacing heatmaps.
6. **Triple-Anchor Drafting Context**: Ingesting Worldview + Rolling Recent Summary + Chapter Beat Sheet for seamless long-form generation.
7. **Specialized Agent Role Partitioning**: Decoupling writing from dialogue surgery, character weaving, continuity keeping, and critical review.
8. **End-to-End BookOps Lifecycle**: Expanding the scope from drafting to include Book Proposals, KDP Publishing, Monetization Funnels, and Launch Marketing.
9. **Automated Multi-Format Assembly**: Verified build engines for Pandoc (EPUB/PDF), LaTeX (pdflatex with SVG/tables), and Python Word DOCX generation.
10. **Dual-Clue & Subplot Ledgers**: Structured tracking of surface vs deeper meanings for mystery and suspense plotting.

---

## Particularly Important Files to Inspect in `repos/`

- `repos/writing-template-for-ai/book_generator_prompt.md`: Master Blueprint prompt.
- `repos/writing-template-for-ai/.ai/agents/writing-prose-suppression.md`: Anti-AI prose rules.
- `repos/writing-template-for-ai/.ai/rules/canon-mutation-control.md`: Canon governance.
- `repos/The-Novelists-Atelier/novelist-atelier-prompts.md`: 22-Pass editorial analysis prompt suite.
- `repos/speckit-preset-fiction-book-writing/fiction-book-writing/commands/speckit.continuity.md`: Continuity auditor.
- `repos/novel-template/.claude/agents/dialogue-surgeon.md`: Dialogue refinement.
- `repos/boekwriter/queries.yaml`: Schema-driven chunk drafting and word budgeting.
- `repos/bookgen/BOOKOPS_WORKFLOW.md`: 7-Phase publication lifecycle.
- `repos/LLM-book-generator/book_generator/docx_builder.py`: Word document styling engine.
- `repos/AI_Novel/app/prompts/templates.py`: Genre-specific drafting styles.

---

## Gaps in the Corpus

- **Academic Citation & Bibliography Management**: Minimal support for automated BibTeX or academic citation styling (only basic LaTeX in `boekwriter`).
- **Index Generation**: Lack of automated index preparation for print non-fiction.
- **Dynamic Audio/Script Adaptation**: Limited tooling for audiobook script pacing beyond basic command stubs.
- **Multi-Author Collaborative Git Workflows**: Most systems assume a single human author or single LLM agent.

---

## Recommended Inputs for the Next Agent

When designing the future book-writing Skill or prompt architecture, the next agent should review:
1. `knowledge/book-writing-knowledge-base.md` — Synthesized capability encyclopedia.
2. `knowledge/design-patterns.md` — Comparative trade-offs of architectural patterns A through F.
3. `knowledge/prompt-patterns.md` — 8 core reusable prompt structural formulas.
4. `matrices/repository-capability-matrix.md` — Detailed cross-repository feature comparison.
5. `summaries/*.md` — Individual deep-dive reports for all 18 repositories.

---

## Candidate Components Worth Evaluating Later

*(Identified for future evaluation only; do not implement yet)*
- `project-definition-component`
- `audience-positioning-component`
- `research-dossier-component`
- `story-bible-canon-component`
- `hierarchical-outlining-component`
- `word-budget-allocation-component`
- `chapter-planning-component`
- `fractal-scene-drafting-component`
- `ai-prose-suppression-component`
- `rolling-summary-memory-component`
- `continuity-audit-component`
- `dialogue-surgeon-component`
- `22-pass-developmental-editing-component`
- `line-copy-editing-component`
- `kdp-metadata-monetization-component`
- `multi-format-export-component` (Pandoc / LaTeX / DOCX)
