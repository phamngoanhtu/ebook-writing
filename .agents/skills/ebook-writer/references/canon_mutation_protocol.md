# Canon Mutation Control & State Management Protocol

Rules governing how the agent interacts with, preserves, and modifies story canon and persistent memory.

---

## 1. The Canon Hierarchy

1. **Level 1 — Immutable World Laws (`MEMORY.md`)**: Physical constants, magic rules, historical dates, and foundational lore. Cannot be changed without explicit human approval.
2. **Level 2 — Character & Entity State (`characters/*.md`)**: Dynamic attributes (injuries, knowledge, inventory, emotional state). Updated after every scene/chapter.
3. **Level 3 — Session State (`CHANGELOG_AI.md`)**: Rolling handoffs, recent chapter exit states, and open thread ledgers.

---

## 2. Canon Mutation Rules

- **No Hallucinated Retcons**: An agent drafting Chapter 10 cannot alter facts established in Chapter 2. If a plot contradiction arises, the agent must pause and flag it.
- **Explicit Canon Patches**: If an author decides to change a character's backstory or world rule mid-manuscript:
  1. Update `MEMORY.md` with a dated entry.
  2. Create a refactor task in `CHANGELOG_AI.md` listing all prior chapters that require revision.
- **Knowledge Boundary Enforcement**: Characters may only speak of or act on events they witnessed or were informed of on-page.

---

## 3. Session Handoff Procedure

After every drafted chapter, append the following block to `CHANGELOG_AI.md`:

```markdown
## [Date] — Chapter [NN] Completed
- **File**: `manuscript/chapters/chNN.md`
- **Word Count**: [Actual words] vs [Budgeted words]
- **Entry State**: [Brief recap of character position/mindset]
- **Key Actions / Shifts**: [Permanent plot/argument developments]
- **Exit State**: [Final character status, physical setting, active emotion]
- **Established Canon**: [New characters, places, or rules introduced]
- **Open Threads / Clues**: [Active unresolved setups]
- **Quality Gates Status**: [All 6 Gates Passed ✓]
- **Next Action**: [Draft Chapter NN+1: "[Title]"]
```
