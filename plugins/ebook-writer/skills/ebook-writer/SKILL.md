---
name: ebook-writer
description: >-
  Comprehensive end-to-end framework for authoring, planning, outlining, drafting,
  editing, continuity tracking, quality gating, and publishing high-quality fiction
  and non-fiction eBooks and print manuscripts. Synthesizes BookOps state machine,
  local-workflow implementation planning, fractal scene architecture, anti-AI prose
  suppression, two-tier persistent memory, 22-pass editorial analysis, mathematical
  word budgeting, and multi-format publication (EPUB/PDF/DOCX).
---

# E-Book Writer Skill (Master Workflow Framework)

This skill equips the agent with a production-grade, end-to-end system for writing and publishing commercial and literary eBooks. It integrates a deterministic **BookOps State Machine** and strict **Local-Workflow Implementation Planning** (`impls/`, `reqs/`, `diary/`, `learning/`, `SPEC.md`, `LEARNING.md`) to guarantee that every stage captures runtime state accurately and prevents continuity drift.

---

## Core Principles & Non-Negotiables

1. **Mandatory Pre-Execution Plan (`impls/`)**: An agent must NEVER generate or edit manuscript prose without first creating a structured implementation plan file in `impls/`.
2. **Two-Tier State Management**: Maintain absolute continuity via `MEMORY.md` (durable canon & world rules) and `CHANGELOG_AI.md` (session handoff & entry/exit states).
3. **Session Diary & Learning Capture**: Record raw generation notes into `diary/` and post-pass craft calibrations into `learning/` and `LEARNING.md`.
4. **Strict Canon Mutation Control**: Never alter established facts, character traits, or past timeline events without an explicit authorized canon patch in `MEMORY.md`.
5. **Fractal Scene Architecture**: Every scene must complete a circuit of change: Goal → Conflict → Disaster (Action) followed by Reaction → Dilemma → Decision (Sequel).
6. **Zero AI Cliché Policy**: Actively suppress recognizable AI writing patterns ("delve", "tapestry", "beacon", "testament", emotional moralizing, syntactic symmetry).
7. **Tiered Editorial Quality Gates**: Always separate Developmental Editing (structure, pacing, arcs) from Line Editing (cadence, subtext) and Copy Editing (grammar, terms).

---

## BookOps Lifecycle & State Machine

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        STAGE 0: INCEPTION                              │
│  State: STAGE_0_INCEPTION                                              │
│  Artifacts: reqs/project_brief.md, reqs/audience_avatar.md              │
│  Plan Required: impls/stage0_inception_plan.md                         │
│  Exit Gate: Approved Premise & Format Scope                            │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        STAGE 1: ARCHITECTURE                           │
│  State: STAGE_1_BLUEPRINTING                                           │
│  Artifacts: SPEC.md, BOOK_BLUEPRINT.md                                 │
│  Plan Required: impls/stage1_blueprint_plan.md                         │
│  Exit Gate: Complete 12-Section Blueprint Validated                    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        STAGE 2: FOUNDATION                             │
│  State: STAGE_2_FOUNDATION                                             │
│  Artifacts: MEMORY.md, characters/*.md, world/*.md, STYLE_GUIDE.md     │
│  Plan Required: impls/stage2_foundation_plan.md                        │
│  Exit Gate: Immutable Canon & Character Hierarchy Locked              │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        STAGE 3: OUTLINING                              │
│  State: STAGE_3_OUTLINING                                              │
│  Artifacts: OUTLINE.md, manuscript/manifest.md                         │
│  Plan Required: impls/stage3_outline_budget_plan.md                    │
│  Exit Gate: Mathematical Word Budget Allocated per Chapter & Scene     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        STAGE 4: DRAFTING (Loop per Chapter)            │
│  State: STAGE_4_DRAFTING                                               │
│  Artifacts: manuscript/chapters/chNN.md, CHANGELOG_AI.md, diary/*.md   │
│  Plan Required: impls/stage4_chNN_drafting_plan.md                     │
│  Exit Gate: 6 Quality Gates Passed + Exit State Logged in CHANGELOG    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        STAGE 5: EDITORIAL GATES                        │
│  State: STAGE_5_EDITING                                                │
│  Artifacts: impls/stage5_editorial_report.md, polished chapters        │
│  Plan Required: impls/stage5_editorial_plan.md                         │
│  Exit Gate: 22-Pass Audit Complete (Pacing Heatmap + Dialogue Surgery) │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        STAGE 6: ASSEMBLY & BUILD                       │
│  State: STAGE_6_ASSEMBLY                                               │
│  Artifacts: build/book.epub, build/book.pdf, build/book.docx           │
│  Plan Required: impls/stage6_compilation_plan.md                       │
│  Exit Gate: Clean Pandoc/LaTeX/DOCX Build & Formatting Validation      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        STAGE 7: PUBLISHING & LAUNCH                    │
│  State: STAGE_7_PUBLISHING                                             │
│  Artifacts: kdp-ready/*, marketing/*, LEARNING.md, learning/*.md       │
│  Plan Required: impls/stage7_publishing_plan.md                        │
│  Exit Gate: KDP Metadata Verified + Project Retrospective Captured     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Workspace Directory & State Capture Standard

Every book project managed by this skill maintains the following directory layout:

```text
project-root/
├── SPEC.md                              # Authoritative project technical specification
├── BOOK_BLUEPRINT.md                    # Master 12-section architectural blueprint
├── MEMORY.md                            # Level-1 immutable canon, world rules & facts
├── CHANGELOG_AI.md                      # Level-3 rolling session handoffs & exit states
├── STYLE_GUIDE.md                       # Project voice, formatting, and vocabulary rules
├── LEARNING.md                          # Project-level retrospective & craft takeaways
├── reqs/                                # Requirements, briefs, reader avatar dossiers
├── impls/                               # Stage-specific implementation plans (MANDATORY)
├── diary/                               # Runtime session execution notes & raw prompts
├── learning/                            # Granular chapter-level craft calibration logs
├── manuscript/
│   ├── manifest.md                      # Ordered chapter build manifest
│   └── chapters/
│       ├── ch01.md
│       ├── ch02.md
│       └── ...
├── characters/                          # Character dossiers (want, need, flaw, voice)
├── world/                               # World-building files (locations, rules, timeline)
├── build/                               # Compiled EPUB, PDF, and DOCX output files
└── kdp-ready/                           # Amazon KDP metadata, formatted interiors, covers
```

---

## Detailed Stage Execution Protocols

### Stage 0: Inception & Project Briefing (`STAGE_0_INCEPTION`)
1. **Create Plan**: Write `impls/stage0_inception_plan.md`.
2. **Collect Brief**: Prompt author for Title/Topic, Genre, Target Reader Avatar, Category (Fiction vs Non-Fiction), and Target Word Count.
3. **Capture State**: Write `reqs/project_brief.md` and `reqs/audience_avatar.md`.
4. **Exit Gate**: Human confirms scope and reader transformation goals.

---

### Stage 1: Architecture & Master Blueprint (`STAGE_1_BLUEPRINTING`)
1. **Create Plan**: Write `impls/stage1_blueprint_plan.md`.
2. **Generate `SPEC.md`**: Define the technical boundaries, file conventions, and delivery timelines.
3. **Generate `BOOK_BLUEPRINT.md`**: Execute the 12-section blueprinting process using [references/book_blueprint_template.md](./references/book_blueprint_template.md).
4. **Exit Gate**: All 12 sections validated with complete chapter-by-chapter entry/exit definitions.

---

### Stage 2: Foundation & Canon Locking (`STAGE_2_FOUNDATION`)
1. **Create Plan**: Write `impls/stage2_foundation_plan.md`.
2. **Initialize Canon**: Populate `MEMORY.md` with immutable world laws, technology/magic boundaries, historical chronology, and core character facts.
3. **Establish Style Guide**: Write `STYLE_GUIDE.md` defining POV, tense, tone register, and banned AI tropes.
4. **Create Character & World Files**: Write `characters/*.md` and `world/*.md`.
5. **Exit Gate**: Canon locked under [references/canon_mutation_protocol.md](./references/canon_mutation_protocol.md).

---

### Stage 3: Hierarchical Outlining & Word Budgeting (`STAGE_3_OUTLINING`)
1. **Create Plan**: Write `impls/stage3_outline_budget_plan.md`.
2. **Calculate Word Budgets**:
   $$\text{Budget per Chapter} = \frac{\text{Total Target Words}}{\text{Number of Chapters}}$$
   $$\text{Budget per Scene/Beat} = \frac{\text{Chapter Budget}}{\text{Number of Beats (e.g. 3-4)}}$$
3. **Generate `OUTLINE.md`**: Build 3-tier outline (Acts $\rightarrow$ Chapters $\rightarrow$ Scene Circuits).
4. **Initialize Build Manifest**: Create `manuscript/manifest.md`.
5. **Exit Gate**: Every chapter has assigned word budget and verified dramatic/pedagogical objective.

---

### Stage 4: Chapter Drafting Protocol (`STAGE_4_DRAFTING`)
*(Executed iteratively for Chapter 01 through Chapter NN)*

1. **Create Chapter Implementation Plan**:
   - Write `impls/stage4_chNN_drafting_plan.md` using [templates/impls_plan_template.md](./templates/impls_plan_template.md).
   - Ingest **Triple-Anchor Context**:
     - *Macro Anchor*: Core premise from `BOOK_BLUEPRINT.md`.
     - *Rolling Bridge*: Exit state of Chapter $N-1$ from `CHANGELOG_AI.md`.
     - *Micro Anchor*: Chapter $N$ beat sheet from `BOOK_BLUEPRINT.md §6`.
2. **Draft Prose**: Generate scene-by-scene prose adhering to fractal circuits (*Goal $\rightarrow$ Conflict $\rightarrow$ Disaster* and *Reaction $\rightarrow$ Dilemma $\rightarrow$ Decision*).
3. **Apply Anti-AI Prose Sanitization**: Strip out banned tropes using [references/anti_ai_prose_rules.md](./references/anti_ai_prose_rules.md).
4. **Capture Session State**:
   - Write runtime diary log to `diary/session_YYYYMMDD_chNN.md`.
   - Append chapter handoff entry to `CHANGELOG_AI.md` (Entry State, Permanent Shifts, Exit State, Open Clues/Threads).
   - Log any voice calibrations or prompt tweaks to `learning/chNN_learnings.md`.
5. **Exit Gate**: All 6 Chapter Quality Gates verified:
   - [ ] Gate 1: Circuit of change completed (Entry $\neq$ Exit).
   - [ ] Gate 2: Character hierarchy & voice differentiation respected.
   - [ ] Gate 3: Anti-AI prose suppression verified (zero banned words).
   - [ ] Gate 4: Zero canon contradictions against `MEMORY.md`.
   - [ ] Gate 5: Actual word count within $\pm 10\%$ of budget.
   - [ ] Gate 6: Handoff logged in `CHANGELOG_AI.md`.

---

### Stage 5: Multi-Pass Editorial Refinement (`STAGE_5_EDITING`)
1. **Create Plan**: Write `impls/stage5_editorial_plan.md`.
2. **Run 22-Pass Editorial Audit**: Execute review passes from [references/editorial_rubric_22_pass.md](./references/editorial_rubric_22_pass.md).
   - *Pass 1–6 (Developmental)*: Plot structure, Pacing heatmap, Character arcs, Thematic coherence.
   - *Pass 7–10 (Continuity)*: World lore, Timeline audit, Character knowledge leaks, Inventory tracking.
   - *Pass 15–17 (Dialogue)*: Dialogue surgery, subtext stripping, acoustic rhythm differentiation.
   - *Pass 18–20 (Line Editing)*: Sentence length variety, active cadence, concision trimming.
   - *Pass 21–22 (Copy/Proofreading)*: Terminology lock, punctuation, layout consistency.
3. **Capture Editorial Findings**: Generate `impls/stage5_editorial_report.md`.
4. **Execute Revisions**: Patch chapter markdown files directly.
5. **Exit Gate**: All critical and major severity flags resolved; pacing heatmap clean.

---

### Stage 6: Assembly & Compilation (`STAGE_6_ASSEMBLY`)
1. **Create Plan**: Write `impls/stage6_compilation_plan.md`.
2. **Validate Manifest**: Check `manuscript/manifest.md` for complete front matter, body chapters, and back matter.
3. **Compile Output Formats**:
   - **EPUB**: `pandoc -s -o build/book.epub --toc manuscript/manifest.md`
   - **PDF**: LaTeX compilation (`template.tex`) or Pandoc PDF.
   - **DOCX**: Word compilation via `python-docx` for traditional submissions.
4. **Exit Gate**: Build passes with clean typography, working TOC hyperlinks, and verified page breaks.

---

### Stage 7: Publishing & Launch (`STAGE_7_PUBLISHING`)
1. **Create Plan**: Write `impls/stage7_publishing_plan.md`.
2. **Generate Amazon KDP Package**:
   - Formulate 7 backend search keyword phrases and 3 BISAC categories using [references/kdp_publishing_checklist.md](./references/kdp_publishing_checklist.md).
   - Write HTML sales description (Headline $\rightarrow$ Hook $\rightarrow$ Bullets $\rightarrow$ CTA).
3. **Consolidate Learnings**: Synthesize `learning/*.md` into root `LEARNING.md`.
4. **Exit Gate**: Complete KDP upload package ready in `kdp-ready/` + final project retrospective locked.

---

## Reference Guides Index

| Reference Document | Location | Core Purpose |
| :--- | :--- | :--- |
| **BookOps State Machine** | [references/bookops_state_machine.md](./references/bookops_state_machine.md) | Lifecycle states, deterministic transitions, and directory standards |
| **Implementation Plan Template** | [templates/impls_plan_template.md](./templates/impls_plan_template.md) | Mandatory pre-execution planning template |
| **Book Blueprint Specification** | [references/book_blueprint_template.md](./references/book_blueprint_template.md) | 12-Section architectural blueprint template |
| **Anti-AI Prose Suppression Rules**| [references/anti_ai_prose_rules.md](./references/anti_ai_prose_rules.md) | Banned vocabulary, syntactic symmetry breaks, and prose sanitization |
| **22-Pass Editorial Rubric** | [references/editorial_rubric_22_pass.md](./references/editorial_rubric_22_pass.md) | Full manuscript developmental, line, and dialogue audit rubric |
| **Canon Mutation Protocol** | [references/canon_mutation_protocol.md](./references/canon_mutation_protocol.md) | Two-tier state management, canon governance, and handoff logging |
| **KDP Publishing Checklist** | [references/kdp_publishing_checklist.md](./references/kdp_publishing_checklist.md) | Amazon KDP metadata, category selection, and sales copywriting |
"""

with open(os.path.join(SKILL_DIR, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write(skill_md)

print("Updated SKILL.md with BookOps State Machine and Local-Workflow Planning.")
