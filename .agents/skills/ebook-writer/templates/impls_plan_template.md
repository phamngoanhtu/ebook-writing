# BookOps Implementation Plan Template

Use this template to create structured implementation plans in `impls/` before executing any major BookOps stage.

---

```markdown
# [IMPL PLAN] Stage [N]: [Stage Name] — [Book Title]

## 1. Stage Objective & Scope
- **Current BookOps State**: [e.g. STAGE_3_OUTLINED → Transitioning to STAGE_4_DRAFTING]
- **Target Artifacts**: [List exact files to create or modify, e.g. `manuscript/chapters/ch01.md`, `CHANGELOG_AI.md`]
- **Assigned Word Budget / Constraints**: [e.g. 3,200 words, Third-Person Limited, Past Tense]

---

## 2. Pre-Execution Context & Provenance
- **Prerequisite Artifacts Verified**:
  - [ ] `BOOK_BLUEPRINT.md` (§[Section Number])
  - [ ] `MEMORY.md` (Active Canon & World Rules)
  - [ ] `CHANGELOG_AI.md` (Exit State of Previous Chapter / Session)
- **Active Character & World Constraints**:
  - *Active Characters*: [Names, current locations, emotional wounds]
  - *Character Knowledge Boundaries*: [What characters know vs do NOT know at this point]
  - *Setting / Physical Constraints*: [Room layout, weather, time elapsed]

---

## 3. Step-by-Step Execution Breakdown

### Step 1: Context Assembly & Triple-Anchor Verification
- Ingest `MEMORY.md` + last entry of `CHANGELOG_AI.md` + Chapter beat sheet.
- Confirm negative constraints and anti-AI suppressed words.

### Step 2: Generation / Execution Pass
- [Detail exact prompt parameters, scene beats, or editorial criteria]
- Scene 1: [Goal $\rightarrow$ Conflict $\rightarrow$ Disaster]
- Scene 2: [Reaction $\rightarrow$ Dilemma $\rightarrow$ Decision]

### Step 3: Immediate In-Memory Sanitization Pass
- Apply `anti_ai_prose_rules.md` (grep and replace overused tropes).
- Check sentence cadence and dialogue subtext.

---

## 4. Quality Gate Verification Checklist
Before declaring this implementation step complete, verify all quality gates:

- [ ] **Gate 1 (Circuit of Change)**: Entry state $\neq$ Exit state.
- [ ] **Gate 2 (Character Oxygen)**: Principal character owns the dramatic turning point.
- [ ] **Gate 3 (Prose Sanitized)**: Zero banned AI tropes ("delve", "tapestry", "beacon").
- [ ] **Gate 4 (Canon Check)**: No retcons or contradictions against `MEMORY.md`.
- [ ] **Gate 5 (Word Budget)**: Actual word count within $\pm 10\%$ of budgeted range.

---

## 5. Post-Execution State Capture & Handoff
- [ ] Record runtime notes in `diary/session_YYYYMMDD_chNN.md`.
- [ ] Append chapter entry/exit state handoff to `CHANGELOG_AI.md`.
- [ ] If new canonical facts were established, append patch to `MEMORY.md`.
- [ ] Log voice/model calibration insights to `learning/`.
```
