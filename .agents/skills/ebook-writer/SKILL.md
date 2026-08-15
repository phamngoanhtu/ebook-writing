---
name: ebook-writer
description: >-
  Comprehensive end-to-end framework for authoring, planning, outlining, drafting,
  editing, continuity tracking, quality gating, and publishing high-quality fiction
  and non-fiction eBooks and print manuscripts. Synthesizes fractal scene architecture,
  anti-AI prose suppression, two-tier persistent memory, 22-pass editorial analysis,
  mathematical word budgeting, and multi-format publication (EPUB/PDF/DOCX).
---

# E-Book Writer Skill (Master Workflow Framework)

This skill equips the agent with a production-grade, end-to-end system for writing and publishing commercial and literary eBooks. It synthesizes proven design patterns from 18 specialized repositories into an actionable, multi-stage authoring engine.

---

## Core Principles & Non-Negotiables

1. **Architecture Before Prose**: Never write chapter prose without a validated 12-section `BOOK_BLUEPRINT.md` and chapter-level beat sheets.
2. **Two-Tier State Management**: Maintain absolute continuity via `MEMORY.md` (durable canon & world rules) and `CHANGELOG_AI.md` (session handoff & entry/exit states).
3. **Strict Canon Mutation Control**: Never alter established facts, character traits, or past timeline events without an explicit authorized canon update.
4. **Fractal Scene Architecture**: Every scene must complete a circuit of change: Goal → Conflict → Disaster (Action) followed by Reaction → Dilemma → Decision (Sequel).
5. **Zero AI Cliché Policy**: Actively suppress recognizable AI writing patterns ("delve", "tapestry", "beacon", "testament", emotional moralizing, syntactic symmetry).
6. **Tiered Editorial Quality Gates**: Always separate Developmental Editing (structure, pacing, arcs) from Line Editing (cadence, subtext) and Copy Editing (grammar, terms).

---

## End-to-End BookOps Lifecycle

```text
Phase 1: Project Conception & Market Validation
  ↓
Phase 2: Master Book Blueprint Generation (BOOK_BLUEPRINT.md)
  ↓
Phase 3: Story Bible & Character System Setup (MEMORY.md)
  ↓
Phase 4: Hierarchical Outlining & Mathematical Word Budgeting
  ↓
Phase 5: Chapter-by-Chapter Drafting (with Triple Anchor Context)
  ↓
Phase 6: Multi-Stage Quality Gates & Anti-AI Prose Suppression
  ↓
Phase 7: Developmental, Line, and Dialogue Surgery Passes
  ↓
Phase 8: Manuscript Assembly & Export (Markdown / EPUB / PDF / DOCX)
  ↓
Phase 9: Amazon KDP Metadata & Launch Preparation
```

---

## Phase 1: Project Conception & Briefing

### Required Inputs
Collect or prompt the user for the foundational brief:
- **Title / Working Concept**: Core topic or high-concept hook.
- **Genre & Target Audience**: Reader avatar, knowledge level, and desired transformation.
- **Category (Fiction vs Non-Fiction)**:
  - *Fiction*: Protagonist want vs need, antagonist force, core theme, narrative POV.
  - *Non-Fiction*: Core thesis, reader pain points, target skill acquisition, comparable books.
- **Target Scale**: Total target word count (e.g. 25,000 / 50,000 / 80,000 words), number of parts/chapters.

---

## Phase 2: Master Book Blueprint

Generate `BOOK_BLUEPRINT.md` adhering to the standard 12-section structure:
1. **§1. Executive Concept**: One-sentence premise, one-paragraph hook, back-cover positioning, core reader promise.
2. **§2. Target Length & Format**: Total word count, chapter-count philosophy, format recommendation (eBook-first, print).
3. **§3. Reader Experience Design**: Emotional/cognitive milestones at 10 pages, 25%, midpoint, and climax.
4. **§4. Macro Structure**: Act breaks / Thesis progression, major turning points, escalation path.
5. **§5. Character System / Domain Model**: Principal characters (want, need, flaw, arc, voice) or Non-fiction framework modules.
6. **§6. Chapter-by-Chapter Plan**: Entry state → Core dramatic/pedagogical beat → Exit state for every chapter.
7. **§7. Style Guide**: Narrative POV, tense, tone register, sentence rhythm rules, banned patterns.
8. **§8. Dual-Clue / Subplot Ledger**: Tracking surface events vs hidden depths/open threads.
9. **§9. Production Assumptions**: Manuscript layout convention (`manuscript/chapters/chNN.md`), front/back matter.
10. **§10. Quality Gates**: 6 mandatory gates per chapter before marking complete.
11. **§11. Risk Review**: Top story, pacing, and clarity risks with one-sentence mitigations.
12. **§12. Drafting Instructions**: Order of execution and session handoff rules.

*(See full template in [references/book_blueprint_template.md](./references/book_blueprint_template.md))*

---

## Phase 3: Context & Two-Tier Memory Setup

Initialize the project filesystem:
```text
project-root/
├── BOOK_BLUEPRINT.md
├── MEMORY.md
├── CHANGELOG_AI.md
├── STYLE_GUIDE.md
├── manuscript/
│   ├── manifest.md
│   └── chapters/
│       ├── ch01.md
│       └── ...
├── characters/
├── world/
└── build/
```

- **`MEMORY.md`**: Store canonical facts (world rules, magic/tech limits, established timeline events, character traits).
- **`CHANGELOG_AI.md`**: Log session transitions:
  ```markdown
  ## Chapter NN Handoff
  - **Entry State**: Where characters were / what reader knew.
  - **Key Shifts**: Permanent changes that occurred.
  - **Exit State**: Ending location, active emotional tone, new knowledge.
  - **Open Threads / Clues**: Pending setups requiring future payoffs.
  - **Next Step**: Explicit prompt instruction for Chapter NN+1.
  ```

---

## Phase 4: Hierarchical Outlining & Word Budgeting

1. **Calculate Word Budgets**:
   $$	ext{Budget per Chapter} = rac{	ext{Total Target Words}}{	ext{Number of Chapters}}$$
   $$	ext{Budget per Scene/Item} = rac{	ext{Chapter Budget}}{	ext{Number of Scenes/Items}}$$
2. **Breakdown Chapters into Discrete Beats**:
   - *Fiction*: Scene 1 (Setup → Conflict → Disaster) → Scene 2 (Reaction → Dilemma → Decision).
   - *Non-Fiction*: Hook/Problem → Core Principle → Case Study/Example → Action Steps → Recap.

---

## Phase 5: Chapter Drafting Protocol (Triple Anchor)

When prompting or executing drafting for Chapter $N$, assemble the **Triple Anchor Context**:
1. **Macro Anchor**: Book premise + overall chapter roadmap.
2. **Rolling Bridge**: Summary of Chapter $N-1$ from `CHANGELOG_AI.md` (entry state & emotional momentum).
3. **Micro Anchor**: Chapter $N$ beat sheet from `BOOK_BLUEPRINT.md §6`.

### Drafting Prompt Template
```markdown
You are drafting Chapter [NN]: "[Title]" for the book "[Book Title]".

CONTEXT:
1. Worldview / Core Thesis: [Summary from MEMORY.md]
2. Previous Chapter Exit State: [Summary from CHANGELOG_AI.md]
3. Current Chapter Goal & Beats: [Beat plan from BOOK_BLUEPRINT.md §6]
4. Word Budget: [Min Words] - [Max Words] words.

STRICT CONSTRAINTS:
- Follow Style Guide: POV [POV], Tense [Tense], Tone [Tone].
- Complete Fractal Scene Circuits: Every scene must permanently shift the entry state.
- Suppress AI Writing Clichés: Do NOT use "delve", "tapestry", "beacon", "testament", or neat moralizing summaries.
- Focus on sensory texture (sound, smell, touch) and dialogue subtext.

Draft the full chapter in clean Markdown.
```

---

## Phase 6: Quality Gates & Anti-AI Prose Suppression

Every drafted chapter must pass 6 Quality Gates:

1. **Gate 1 — Scene Circuit Check**: Does every scene complete a circuit of change? (Entry state $
eq$ Exit state).
2. **Gate 2 — Character Hierarchy & Voice**: Are principal characters driving the action? Does dialogue contain distinct acoustic rhythm?
3. **Gate 3 — Anti-AI Prose Suppression**: Audit text against [references/anti_ai_prose_rules.md](./references/anti_ai_prose_rules.md). Strip out symmetry, artificial eloquence, and banned vocabulary.
4. **Gate 4 — Multi-Persona Editorial Pass**: Run narratological, psychological, and pacing checks.
5. **Gate 5 — Blueprint & Canon Continuity**: Verify alignment with `BOOK_BLUEPRINT.md` and `MEMORY.md`.
6. **Gate 6 — Session Handoff Logged**: Record entry/exit states and open threads in `CHANGELOG_AI.md`.

---

## Phase 7: Multi-Pass Editorial Refinement

Use the specialized review rubrics from [references/editorial_rubric_22_pass.md](./references/editorial_rubric_22_pass.md):
- **Developmental Pass**: Plot structure integrity (Inciting incident, Midpoint reversal, Climax tension), Pacing heatmap.
- **Dialogue Surgery Pass**: Strip on-the-nose exposition, inject conversational subtext and non-verbal beats.
- **Line Editing Pass**: Sentence length variety, active verb cadence, tightening word count by 10–15%.
- **Copy Editing & Proofreading**: Terminology consistency, punctuation, formatting lock.

---

## Phase 8: Manuscript Assembly & Multi-Format Export

1. **Compile Manifest**: Order all chapters in `manuscript/manifest.md`.
2. **Export Targets**:
   - **EPUB / PDF (via Pandoc)**:
     ```bash
     pandoc -s -o build/book.epub --toc --metadata-file=metadata.yaml manuscript/chapters/*.md
     ```
   - **PDF (via LaTeX)**: For technical books with math/tables using `template.tex`.
   - **DOCX**: For traditional publishing workflows and agent submissions.

---

## Phase 9: KDP Publishing & Launch

1. **Amazon Metadata Formulation**:
   - 7 Backend Search Keyword strings (under 50 characters, high buyer intent).
   - 3 Target Amazon BISAC categories.
2. **High-Converting Book Description**:
   - Headline Hook $ightarrow$ Emotional Agitation $ightarrow$ Core Solution $ightarrow$ Bulleted Feature/Benefits $ightarrow$ Risk-Reversal CTA.
3. **Launch Execution**:
   - Pre-publication proofing checklist ([references/kdp_publishing_checklist.md](./references/kdp_publishing_checklist.md)).
   - Back-matter lead magnets and reader review request.

---

## Quick Command Reference

| Action | Recommended Tool / File |
| :--- | :--- |
| **Start Project** | Initialize `BOOK_BLUEPRINT.md` from `references/book_blueprint_template.md` |
| **Check Canon** | Verify against `MEMORY.md` and `references/canon_mutation_protocol.md` |
| **Draft Chapter** | Run Triple-Anchor prompt with word budget |
| **Sanitize Prose** | Apply `references/anti_ai_prose_rules.md` |
| **Audit Manuscript**| Execute 22-pass review from `references/editorial_rubric_22_pass.md` |
| **Build Book** | Compile `manuscript/manifest.md` via Pandoc/DOCX build script |
