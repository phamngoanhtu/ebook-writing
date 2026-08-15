# Repository Report: speckit-preset-fiction-book-writing

## Repository
- **Name**: speckit-preset-fiction-book-writing
- **URL**: https://github.com/adaumann/speckit-preset-fiction-book-writing
- **Commit**: `4764c888`
- **Status**: SUCCESS
- **Primary purpose**: Specification-driven command framework for authoring fiction books using modular prompt commands.
- **Primary target**: Fiction (Novels, series, short stories).

---

## Important Paths
- `fiction-book-writing/preset.yml`: Master configuration defining 34 discrete CLI-invocable writing and editing commands.
- `fiction-book-writing/commands/speckit.constitution.md`: Core narrative constitution setting world rules, tone, and authorial principles.
- `fiction-book-writing/commands/speckit.continuity.md`: Specialized command for deep continuity verification across characters, objects, and timeline.
- `fiction-book-writing/commands/speckit.outline.md`: Multi-level outline generator (High-level, Acts, Chapters, Scenes).
- `fiction-book-writing/commands/speckit.plan.md`: Chapter-by-chapter scene planning command.
- `fiction-book-writing/commands/speckit.implement.md`: Scene and chapter drafting command.
- `fiction-book-writing/commands/speckit.polish.md`: Line-level polish, prose tightening, and sensory enhancement command.
- `fiction-book-writing/commands/speckit.series.md`: Long-term series arc and continuity manager.
- `fiction-book-writing/commands/speckit.subplot.md`: Subplot weaving and tracking command.
- `fiction-book-writing/commands/speckit.pacing.md`: Scene pacing and tension curve auditor.

---

## Workflow
Constitution Setup (`speckit.constitution.md`)
→ Brainstorming & Ideation (`speckit.brainstorm.md`)
→ Worldbuilding & Character Spec (`speckit.specify.md`)
→ Subplot Design (`speckit.subplot.md`)
→ Multi-Level Outlining (`speckit.outline.md`)
→ Chapter Planning (`speckit.plan.md`)
→ Drafting (`speckit.implement.md`)
→ Continuity Audit (`speckit.continuity.md`)
→ Pacing Analysis (`speckit.pacing.md`)
→ Revision & Polish (`speckit.polish.md` & `speckit.revise.md`)
→ Export & Publishing (`speckit.export.md`).

---

## Inputs and Outputs

```text
Stage: Specification & Constitution
Input: Author premise, genre constraints, core vision
Process: speckit.constitution.md + speckit.specify.md
Output: Constitution file, Character sheets, World glossary
Used by next stage: Outlining & Scene Planning

Stage: Outlining & Subplot Tracking
Input: Constitution, Character sheets, Theme
Process: speckit.outline.md + speckit.subplot.md
Output: Outline spec (Act breakdown, scene beats, subplot thread map)
Used by next stage: Chapter Planning & Implementation

Stage: Implementation & Drafting
Input: Chapter plan, scene objectives, active subplot threads
Process: speckit.implement.md
Output: Chapter prose markdown
Used by next stage: Continuity & Polish passes

Stage: Quality Assurance & Audit
Input: Drafted chapters, Constitution, Character knowledge states
Process: speckit.continuity.md + speckit.pacing.md + speckit.polish.md
Output: Continuity fix report, polished manuscript chapters
Used by next stage: Export & Assembly
```

---

## Prompt Inventory

### Prompt: speckit.continuity.md
- **File**: `fiction-book-writing/commands/speckit.continuity.md`
- **Purpose**: Scans chapters against the project constitution and character states to catch contradictions.
- **Required inputs**: Chapter text, character knowledge tracker, timeline ledger, world rules.
- **Expected output**: Continuity report categorizing issues by severity (Blocking, Major, Minor).
- **Important constraints**: Must verify character knowledge state (i.e. characters cannot know secrets before they are revealed).
- **Downstream consumer**: `speckit.revise.md`.

### Prompt: speckit.pacing.md
- **File**: `fiction-book-writing/commands/speckit.pacing.md`
- **Purpose**: Evaluates tension beats, action-to-exposition ratios, and narrative momentum across scenes.
- **Required inputs**: Chapter draft text.
- **Expected output**: Pacing graph analysis, identification of sagging middle/exposition dumps, actionable tightening advice.
- **Important constraints**: Evaluates sentence length variation and scene transition speed.
- **Downstream consumer**: `speckit.polish.md`.

---

## Context / Memory Strategy
Maintains a formal **Narrative Constitution** and modular state files:
- `constitution.md`: Immutable rules of the universe and narrative tone.
- `glossary.md`: Canonical names, terms, places, factions.
- `character_state.md`: Tracks dynamic character status, location, possessions, emotional wounds, and active knowledge.
- `timeline.md`: Chronological log of story events.

---

## Editing Strategy
- **Developmental editing**: `speckit.outline.md` and `speckit.analyze.md`.
- **Continuity**: `speckit.continuity.md` (explicit multi-factor verification).
- **Fact checking**: `speckit.research.md`.
- **Line editing**: `speckit.polish.md`.
- **Copy editing**: `speckit.revise.md`.
- **Proofreading**: `speckit.polish.md` final pass.
- **Style review**: `speckit.pov.md` and `speckit.pacing.md`.

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown.
- **Chapter organization**: Managed via SpecKit preset configuration.
- **Assembly method**: `speckit.export.md` command.
- **Output formats**: Markdown, EPUB, PDF.
- **Scripts/tools required**: SpecKit CLI / LLM command executor.

---

## Strongest Ideas
1. **Command-Driven Modular Architecture**: Over 30 specialized commands targeting specific micro-tasks (POV consistency, pacing, subplots, sensitivity).
2. **Narrative Constitution Concept**: A formal foundational document governing all downstream LLM generations.
3. **Multi-Book Series Continuity**: Dedicated tools (`speckit.series.md`) for tracking arcs across multi-book franchises.

---

## Weaknesses
- Command structure is tailored to the SpecKit framework/CLI; requires adaptation for standalone use.

---

## Reusable Knowledge
- Granular prompt structures for specific craft challenges (pacing, POV drift, subplot weaving).
- Narrative constitution schema.
- Character knowledge state tracking methodology.
