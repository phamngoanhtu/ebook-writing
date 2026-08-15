import os
import json

BASE_DIR = "/Users/tupham/Personal/.personal/Ernest/research/ebook-writing/book-writing-research"
SUMMARIES_DIR = os.path.join(BASE_DIR, "summaries")
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")
MATRICES_DIR = os.path.join(BASE_DIR, "matrices")
EVIDENCE_DIR = os.path.join(BASE_DIR, "evidence")

os.makedirs(SUMMARIES_DIR, exist_ok=True)
os.makedirs(KNOWLEDGE_DIR, exist_ok=True)
os.makedirs(MATRICES_DIR, exist_ok=True)

# 1. writing-template-for-ai
with open(os.path.join(SUMMARIES_DIR, "writing-template-for-ai.md"), "w", encoding="utf-8") as f:
    f.write("""# Repository Report: writing-template-for-ai

## Repository
- **Name**: writing-template-for-ai
- **URL**: https://github.com/hottweelz/writing-template-for-ai
- **Commit**: `b28fd1890175d65076efc4794bfe17a4d6a6b830`
- **Status**: SUCCESS
- **Primary purpose**: End-to-end AI-assisted book architecture, drafting, quality-gated editing, and Pandoc compilation system.
- **Primary target**: Both (Fiction & Non-fiction with explicit genre-routing protocols).

---

## Important Paths
- `book_generator_prompt.md`: Lead developmental editor system prompt creating the complete `BOOK_BLUEPRINT.md`.
- `BOOK_BLUEPRINT.md`: Comprehensive 12-section master blueprint defining premise, length, character hierarchy, chapter plans, style guide, dual-clue ledger, and quality gates.
- `AGENTS.md`: Core system configuration and operational handbook for multi-agent execution.
- `MEMORY.md`: Persistent memory file tracking durable facts, canon, world state, and decisions.
- `CHANGELOG_AI.md`: Rolling AI session handoff log recording entry state, exit state, and quality gate audit results per chapter.
- `.ai/agents/`: 9 specialized agent prompts including `writing-fractal-scene-architect.md`, `writing-prose-suppression.md`, `academic-narratologist.md`, `academic-psychologist.md`, `writing-character-hierarchy.md`, `writing-semantic-gradient.md`, `writing-yorke-dramaturg.md`, `marketing-book-co-author.md`, and `marketing-narrative-consistency-auditor.md`.
- `.ai/rules/`: 9 strict operational rules covering canon mutation control, prose quality protocols, editorial passes, publication boundary, and manuscript file structure.
- `scripts/build.sh`: Pandoc-based build script compiling Markdown files from `manuscript/manifest.md` into clean EPUB and PDF outputs.

---

## Workflow
Author Brief (`START_HERE.md` / `book_project_data.md`) 
→ Book Generator Prompt (`book_generator_prompt.md`) 
→ Master Blueprint (`BOOK_BLUEPRINT.md`) 
→ Chapter Planning 
→ Scene Circuit Drafting (`writing-fractal-scene-architect.md`) 
→ AI Prose Suppression (`writing-prose-suppression.md`) 
→ Multi-Persona Editorial Pass (`editorial-pass.md`) 
→ Canon & Memory Update (`MEMORY.md` & `CHANGELOG_AI.md`) 
→ Manuscript Manifest Assembly (`manuscript/manifest.md`) 
→ Pandoc EPUB/PDF Build (`scripts/build.sh`).

---

## Inputs and Outputs

```text
Stage 1: Ideation & Architecture
Input: START_HERE.md, book_project_data.md, MEMORY.md, docs/genre-routing.md
Process: Execution of book_generator_prompt.md by Lead Developmental Editor AI
Output: BOOK_BLUEPRINT.md (12 detailed sections)
Used by next stage: Stage 2 Chapter Drafting

Stage 2: Chapter Drafting
Input: BOOK_BLUEPRINT.md (§6 Chapter Plan, §7 Style Guide), MEMORY.md, previous chapter context
Process: Scene circuit generation via writing-fractal-scene-architect.md
Output: Manuscript chapter draft (manuscript/chapters/chNN.md)
Used by next stage: Stage 3 Quality Gates & Editing

Stage 3: Editing & Quality Gates
Input: Raw chapter draft, Quality Gate rules (.ai/rules/prose-quality-protocols.md)
Process: 6-part Quality Gate scan (Scene circuit check, character hierarchy check, prose suppression check, editorial pass, blueprint continuity, handoff logging)
Output: Polished chapter draft + CHANGELOG_AI.md entry + MEMORY.md updates
Used by next stage: Next chapter drafting & final assembly

Stage 4: Manuscript Assembly & Export
Input: Manuscript chapters listed in manuscript/manifest.md
Process: Execution of scripts/build.sh using Pandoc
Output: Clean EPUB, PDF, and HTML book files
Used by next stage: Publishing / Distribution
```

---

## Prompt Inventory

### Prompt 1: Book Generator Prompt
- **File**: `book_generator_prompt.md`
- **Purpose**: Creates the complete master blueprint (`BOOK_BLUEPRINT.md`) before any drafting begins.
- **Required inputs**: `START_HERE.md` (author brief), `book_project_data.md` (optional data), `MEMORY.md` (existing facts), `docs/genre-routing.md`.
- **Expected output**: Clean `BOOK_BLUEPRINT.md` containing 12 structured sections.
- **Important constraints**: Must NOT draft manuscript prose yet; must resolve brief contradictions commercially.
- **Downstream consumer**: Stage 2 Drafting Agents & Session Handoff.

### Prompt 2: Fractal Scene Architect Prompt
- **File**: `.ai/agents/writing-fractal-scene-architect.md`
- **Purpose**: Enforces fractal scene structure (Goal → Conflict → Disaster → Reaction → Dilemma → Decision) per scene.
- **Required inputs**: Chapter beat from blueprint, character motivations, current world state.
- **Expected output**: Scene draft where every scene completes a formal circuit of change.
- **Important constraints**: Avoid linear plot dumping; every scene must alter entry state to exit state.
- **Downstream consumer**: Prose Suppression & Editorial Pass.

### Prompt 3: AI Prose Suppression Prompt
- **File**: `.ai/agents/writing-prose-suppression.md`
- **Purpose**: Audits and eliminates common AI writing clichés, hyper-articulate dialogue, structural symmetry, and over-explanation.
- **Required inputs**: Draft chapter text.
- **Expected output**: Cleaned prose text with banned AI patterns replaced with organic human phrasing.
- **Important constraints**: Strict pattern matching against AI telltale words (e.g., "delve", "tapestry", "testament", "beacon").
- **Downstream consumer**: Editorial Pass & Final Chapter Acceptance.

---

## Context / Memory Strategy
Uses a two-tier state management system:
1. **Durable Memory (`MEMORY.md`)**: Stores immutable canonical facts, world rules, character traits, timeline events, and resolved plot points. Updated whenever new canon is established.
2. **Rolling Session Log (`CHANGELOG_AI.md`)**: Tracks incremental progress across chat sessions. Records entry state, chapter changes, quality gate results, open continuity threads, and explicit next-session instructions.

---

## Editing Strategy
- **Developmental editing**: Executed via `BOOK_BLUEPRINT.md` macro-structure evaluation and `academic-narratologist.md`.
- **Continuity**: Enforced by `canon-mutation-control.md` and `marketing-narrative-consistency-auditor.md`.
- **Fact checking**: Verified against `MEMORY.md`.
- **Line editing**: Applied via `writing-semantic-gradient.md` and `writing-yorke-dramaturg.md`.
- **Copy editing**: Applied via `prose-quality-protocols.md`.
- **Proofreading**: Final manuscript sanity check before Pandoc export.
- **Style review**: Enforced via `writing-prose-suppression.md` and `editorial-pass.md`.

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown (`manuscript/chapters/chNN.md`).
- **Chapter organization**: Managed explicitly via `manuscript/manifest.md`.
- **Assembly method**: Shell script (`scripts/build.sh`) leveraging `pandoc`.
- **Output formats**: EPUB, PDF (via LaTeX engine), HTML.
- **Scripts/tools required**: Pandoc, LaTeX (xelatex/pdflatex), Bash.

---

## Strongest Ideas
1. **Fractal Scene Architecture**: Ensuring every scene completes a circuit of change (entry state ≠ exit state).
2. **AI Prose Suppression Engine**: Explicit detection and eradication of AI writing tropes, syntactical symmetry, and artificial dialogue.
3. **Canon Mutation Control**: Strict rules preventing LLMs from changing established character rules or plot facts mid-manuscript.
4. **Dual-Clue Ledger**: Structured tracking for mystery and multi-surface narrative elements (surface reading vs deeper reading).

---

## Weaknesses
- Heavy reliance on local CLI tools (Pandoc, LaTeX) for PDF output.
- Requires strict discipline in updating `CHANGELOG_AI.md` manually or via script.

---

## Reusable Knowledge
- Master blueprint prompt structure (`book_generator_prompt.md`).
- Anti-AI prose tropes rulebook (`writing-prose-suppression.md`).
- Canon mutation prevention protocol (`canon-mutation-control.md`).
- Two-tier context tracking (`MEMORY.md` + `CHANGELOG_AI.md`).
""")

print("Wrote summary for writing-template-for-ai.")
