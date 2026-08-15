# Repository Report: novel-template

## Repository
- **Name**: novel-template
- **URL**: https://github.com/10Legs/novel-template
- **Commit**: `714f4673`
- **Status**: SUCCESS
- **Primary purpose**: Claude-optimized workspace and agentic authoring environment for long-form fiction.
- **Primary target**: Fiction (Novels, series).

---

## Important Paths
- `CLAUDE.md`: System instructions, workspace structure, and command conventions for Claude Code.
- `.claude/agents/`: 10 specialized agent personas:
  - `story-architect.md`: Master plotting, structural integrity, and theme development.
  - `scene-crafter.md`: Detailed scene beat construction and dramatic tension.
  - `character-weaver.md`: Psychological depth, character arcs, and motivation tracking.
  - `dialogue-surgeon.md`: Subtext, rhythm, voice differentiation, and dialogue trimming.
  - `world-tender.md`: Setting immersion, lore continuity, and sensory world-building.
  - `continuity-keeper.md`: Timeline audit, object tracking, and canon enforcement.
  - `developmental-editor.md`: Macro narrative flow, pacing curves, and structural critique.
  - `line-editor.md`: Prose cadence, sentence variety, concision, and style polishing.
  - `idea-excavator.md`: Premise brainstorming, concept pressure-testing, and theme mining.
  - `story-director.md`: Workflow orchestrator and session management.
- `characters/`: Character dossiers and dynamic arc sheets.
- `world/`: World-building files, maps, factions, and rules.
- `manuscript/`: Structured chapter folders and scene drafts.
- `patterns/`: Reusable storytelling frameworks (Save the Cat, Hero's Journey, 7-Point Story Structure).

---

## Workflow
Idea Excavation (`idea-excavator.md`)
→ World & Character Design (`world-tender.md`, `character-weaver.md`)
→ Narrative Architecture (`story-architect.md` using `patterns/`)
→ Scene Planning & Crafting (`scene-crafter.md`)
→ Drafting (`manuscript/`)
→ Dialogue Refinement (`dialogue-surgeon.md`)
→ Continuity Audit (`continuity-keeper.md`)
→ Developmental Editing (`developmental-editor.md`)
→ Line Editing (`line-editor.md`)
→ Export Preparation (`exports/`).

---

## Inputs and Outputs

```text
Stage 1: Ideation & World Architecture
Input: Raw concept, genre inspiration
Process: idea-excavator.md + world-tender.md + character-weaver.md
Output: ideation/premise.md, world/*.md, characters/*.md
Used by next stage: Story Architecture

Stage 2: Story Architecture & Plotting
Input: Premise, Character goals, Narrative pattern template (patterns/)
Process: story-architect.md generates 3-Act / 7-Point plot breakdown
Output: outline.md, chapter_plans/*.md
Used by next stage: Scene Crafting & Drafting

Stage 3: Drafting & Dialogue Surgery
Input: Chapter plan, Character voice notes
Process: scene-crafter.md drafts scene → dialogue-surgeon.md polishes dialogue
Output: manuscript/chapter_XX.md
Used by next stage: Continuity & Editorial Passes

Stage 4: Quality Control & Polishing
Input: Drafted chapter, world/timeline.md, characters/
Process: continuity-keeper.md audits facts → developmental-editor.md reviews pacing → line-editor.md polishes prose
Output: Final manuscript files ready for export
Used by next stage: Publication
```

---

## Prompt Inventory

### Prompt: `dialogue-surgeon.md`
- **Purpose**: Refines character dialogue to eliminate on-the-nose exposition, inject subtext, and establish unique acoustic voices.
- **Required inputs**: Scene draft, character personality sheets, relationship dynamics.
- **Expected output**: Revised dialogue with sharpened subtext, distinct vocal rhythms, and non-verbal character beats.
- **Important constraints**: Preserve core plot information while removing artificial exposition dumps.
- **Downstream consumer**: `line-editor.md`.

### Prompt: `continuity-keeper.md`
- **Purpose**: Audits chapter drafts against the timeline, character state files, and world bible.
- **Required inputs**: Draft chapter text, `world/rules.md`, `world/timeline.md`, character dossiers.
- **Expected output**: Continuity report highlighting discrepancies in timelines, character locations, knowledge leaks, and inventory.
- **Important constraints**: Distinguish deliberate character deception from authorial mistakes.
- **Downstream consumer**: Author / Scene revision.

---

## Context / Memory Strategy
File-based directory architecture where knowledge is cleanly partitioned:
- `characters/`: One markdown file per character detailing arc, voice, knowledge boundaries.
- `world/`: Topic-specific markdown files (e.g. `locations.md`, `rules.md`, `history.md`, `timeline.md`).
- `notes/`: Session logs, author scratchpads, and unresolved creative questions.

---

## Editing Strategy
- **Developmental editing**: `developmental-editor.md`.
- **Continuity**: `continuity-keeper.md` (deep timeline and state auditing).
- **Fact checking**: `world-tender.md`.
- **Line editing**: `line-editor.md`.
- **Copy editing**: `line-editor.md`.
- **Proofreading**: Final line-editor pass.
- **Style review**: `dialogue-surgeon.md` + `scene-crafter.md`.

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown in `manuscript/`.
- **Chapter organization**: Sequentially numbered chapter files.
- **Assembly method**: Manual / Scripted joining into `exports/`.
- **Output formats**: Markdown, Text.
- **Scripts/tools required**: Markdown tooling.

---

## Strongest Ideas
1. **Dialogue Surgeon Role**: Highly specialized agent focusing exclusively on subtext, conversational rhythm, and acoustic voice differentiation.
2. **Storytelling Patterns Library**: Explicit integration of established narrative frameworks (`patterns/` e.g., Save the Cat, Dan Harmon Story Circle, Hero's Journey).
3. **Modular Character and World Dossiers**: Clean filesystem layout that makes context easily retrievable by LLM sessions.

---

## Weaknesses
- No automated CLI or Pandoc compilation scripts included out-of-the-box.

---

## Reusable Knowledge
- Specialized agent prompt instructions (`dialogue-surgeon.md`, `character-weaver.md`, `continuity-keeper.md`).
- Filesystem organization pattern for creative writing workspaces.
