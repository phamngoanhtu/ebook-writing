# BookOps State Machine & State Capture Architecture

A formal specification of the BookOps lifecycle state machine, deterministic stage transitions, and local artifact capture protocols.

---

## 1. The BookOps State Machine

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

## 2. Directory Standard for State Capture

Every book project managed by the `ebook-writer` skill must organize runtime state into these standardized directories:

| Directory / File | Lifecycle Purpose | In Git? (Rule 3) |
| :--- | :--- | :---: |
| `reqs/` | Project briefs, market research, competitor matrices, reader avatars. | Ignored via `.gitignore` |
| `impls/` | Step-by-step technical implementation plans created *before* executing each stage. | Ignored via `.gitignore` |
| `diary/` | Runtime execution logs, intermediate prompts, and raw generation notes. | Ignored via `.gitignore` |
| `learning/` | Post-chapter and post-book retrospectives, voice calibrations, prompt tweaks. | Ignored via `.gitignore` |
| `SPEC.md` | Authoritative technical specification of project constraints and deliverables. | Ignored via `.gitignore` |
| `LEARNING.md` | Consolidated project-level takeaways and craft calibrations. | Ignored via `.gitignore` |
| `BOOK_BLUEPRINT.md` | The master 12-section architectural blueprint. | Tracked |
| `MEMORY.md` | Level-1 immutable canon, world rules, and durable facts. | Tracked |
| `CHANGELOG_AI.md` | Level-3 rolling session handoff and chapter entry/exit state tracker. | Tracked |
| `manuscript/` | Clean chapter markdown files (`manuscript/chapters/chNN.md`) and `manifest.md`. | Tracked |

---

## 3. Strict Pre-Execution Planning Rule (Local-Workflow)

**NON-NEGOTIABLE RULE**: An agent must NEVER begin generating or editing chapter prose without first creating an implementation plan file in `impls/`.

For example, before drafting Chapter 3:
1. Agent creates `impls/stage4_ch03_drafting_plan.md` using the template.
2. The plan explicitly notes:
   - Target word count budget.
   - Entry state from `CHANGELOG_AI.md`.
   - Character knowledge constraints from `MEMORY.md`.
   - Scene-by-scene circuit of change.
   - Specific anti-AI words to watch for.
3. Agent executes the draft strictly according to the plan.
4. Agent logs runtime observations into `diary/session_YYYYMMDD_ch03.md`.
5. Agent updates `CHANGELOG_AI.md` with the chapter exit state and verifies all 6 Quality Gates.
6. Agent updates `learning/` with any voice calibration insights.
"""

with open(os.path.join(SKILL_DIR, "references", "bookops_state_machine.md"), "w", encoding="utf-8") as f:
    f.write(bookops_state_machine)

print("Created references/bookops_state_machine.md")
