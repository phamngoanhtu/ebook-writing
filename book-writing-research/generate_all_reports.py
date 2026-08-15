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
os.makedirs(EVIDENCE_DIR, exist_ok=True)

# Define all 18 repository reports
reports = {}

# 1. writing-template-for-ai
reports["writing-template-for-ai"] = """# Repository Report: writing-template-for-ai

## Repository
- **Name**: writing-template-for-ai
- **URL**: https://github.com/hottweelz/writing-template-for-ai
- **Commit**: `b28fd189`
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
- `.ai/agents/`: 9 specialized agent prompts (`writing-fractal-scene-architect.md`, `writing-prose-suppression.md`, `academic-narratologist.md`, `academic-psychologist.md`, `writing-character-hierarchy.md`, `writing-semantic-gradient.md`, `writing-yorke-dramaturg.md`, `marketing-book-co-author.md`, `marketing-narrative-consistency-auditor.md`).
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
"""

# 2. ai-book-pipeline
reports["ai-book-pipeline"] = """# Repository Report: ai-book-pipeline

## Repository
- **Name**: ai-book-pipeline
- **URL**: https://github.com/jirbis/ai-book-pipeline
- **Commit**: `10fd3224`
- **Status**: SUCCESS
- **Primary purpose**: Multi-agent orchestration pipeline for book generation, editing, critique, and publication.
- **Primary target**: Both (Fiction & Non-fiction).

---

## Important Paths
- `engine/agents/orchestrator.md`: Coordinates agent handoffs, pipeline state, and stage execution.
- `engine/agents/writer.md`: Chapter drafting specialist implementing tone, pacing, and scene beats.
- `engine/agents/editor.md`: Developmental and structural editor auditing narrative flow and coherence.
- `engine/agents/critic.md`: Critical evaluation agent providing feedback scorecards and revision directives.
- `engine/agents/proofreader.md`: Line-level proofreading and grammar agent.
- `engine/agents/publisher.md`: Formats, packages, and prepares manuscript files for export.
- `engine/agents/researcher.md`: Gathers domain knowledge, character backgrounds, and factual support.
- `engine/agents/WORKFLOW.md`: Master specification of multi-agent state machines and data exchange formats.
- `engine/cli.py`: Python CLI tool to initialize projects, run pipeline steps, and compile manuscripts.

---

## Workflow
Project Setup 
→ Research & Background Gathering (`researcher.md`) 
→ Book Outline & Structure 
→ Chapter Planning 
→ Draft Generation (`writer.md`) 
→ Editorial Review (`editor.md`) 
→ Critical Evaluation & Scoring (`critic.md`) 
→ Revision Loop (Writer ← Critic feedback) 
→ Line Proofreading (`proofreader.md`) 
→ Packaging & Publication (`publisher.md`).

---

## Inputs and Outputs

```text
Stage: Research & Foundation
Input: Book concept, genre, target audience
Process: researcher.md extracts key themes, world elements, factual background
Output: research_dossier.md, character_profiles.md
Used by next stage: Outlining & Chapter Planning

Stage: Drafting
Input: Chapter plan, character context, previous chapter summary
Process: writer.md drafts chapter text
Output: chapter_raw.md
Used by next stage: Editorial & Critique

Stage: Critique & Revision Loop
Input: chapter_raw.md, style guide
Process: editor.md + critic.md score narrative tension, pacing, dialogue authenticity
Output: editorial_notes.md, revised chapter_draft.md
Used by next stage: Proofreading

Stage: Publishing
Input: All approved chapter drafts, book metadata
Process: publisher.md joins chapters and compiles formats
Output: Compiled manuscript (Markdown, EPUB, PDF)
Used by next stage: Final Delivery
```

---

## Prompt Inventory

### Prompt: Writer Agent System Prompt
- **File**: `engine/agents/writer.md`
- **Purpose**: Generates scene-level prose based on chapter objectives, maintaining consistent voice and momentum.
- **Required inputs**: Chapter outline, character motivations, emotional target, prior chapter ending.
- **Expected output**: Full chapter draft formatted in clean Markdown.
- **Important constraints**: Avoid exposition dumps; stick strictly to specified narrative POV.
- **Downstream consumer**: `editor.md` and `critic.md`.

### Prompt: Critic Agent Evaluation Prompt
- **File**: `engine/agents/critic.md`
- **Purpose**: Performs rigorous scoring across 5 narrative dimensions: Voice, Pacing, Conflict, Dialogue, Coherence.
- **Required inputs**: Raw chapter text, target quality rubric.
- **Expected output**: Scorecard (1–10 per category) + specific actionable revision instructions.
- **Important constraints**: Must give concrete line-level examples for any low score.
- **Downstream consumer**: `writer.md` for revision pass.

---

## Context / Memory Strategy
Maintains project bibles inside `my-books/<book-id>/context/`:
- `story_bible.md`: World facts, lore, timeline.
- `characters.json`: Character profiles and relationship graphs.
- `chapter_summaries/`: Rolling per-chapter summaries passed forward to subsequent drafting prompts.

---

## Editing Strategy
- **Developmental editing**: Executed by `editor.md` focusing on chapter arc and pacing.
- **Continuity**: Validated against `story_bible.md` and previous chapter summaries.
- **Fact checking**: Validated by `researcher.md`.
- **Line editing**: Conducted by `editor.md`.
- **Copy editing**: Conducted by `proofreader.md`.
- **Proofreading**: Dedicated `proofreader.md` agent pass before publishing.
- **Style review**: Critic agent scores tone alignment.

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown (`chapters/chXX.md`).
- **Chapter organization**: Managed via `book.json` metadata index.
- **Assembly method**: Python CLI script (`engine/cli.py`).
- **Output formats**: Markdown, HTML, EPUB.
- **Scripts/tools required**: Python 3.10+, Markdown libraries.

---

## Strongest Ideas
1. **Explicit Multi-Agent Division of Labor**: Clean separation of Writer, Editor, Critic, and Proofreader roles.
2. **Scored Critic-Feedback Loop**: Objective rubric-driven feedback that triggers targeted rewrites.
3. **Structured Research Dossiers**: Upfront knowledge gathering preventing mid-book hallucination.

---

## Weaknesses
- Complex CLI setup required to run full automated agent chains.
- Lack of built-in anti-AI prose pattern filtering compared to template-based repositories.

---

## Reusable Knowledge
- Role-based multi-agent system prompt specs (`engine/agents/*.md`).
- Structured Critic scorecard rubric (`critic.md`).
- Dynamic writer/editor revision loop state machine.
"""

# 3. speckit-preset-fiction-book-writing
reports["speckit-preset-fiction-book-writing"] = """# Repository Report: speckit-preset-fiction-book-writing

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
"""

# 4. libriscribe
reports["libriscribe"] = """# Repository Report: libriscribe

## Repository
- **Name**: libriscribe
- **URL**: https://github.com/guerra2fernando/libriscribe
- **Commit**: `c4c6ac7f`
- **Status**: SUCCESS
- **Primary purpose**: Python library and prompt pipeline for automated AI novel generation and editing.
- **Primary target**: Fiction (Novels & Creative stories).

---

## Important Paths
- `prompts/templates/concept_generator.yml`: System prompt and template for book concept and premise ideation.
- `prompts/templates/worldbuilding.yml`: Structured world-building template covering geography, society, magic, and tech.
- `prompts/templates/character_generator.yml`: Character profile generator detailing wants, needs, backstories, and voices.
- `prompts/templates/outliner.yml`: High-level novel outline and act structure generator.
- `prompts/templates/scene_outliner.yml`: Scene-by-scene beat sheet generator.
- `prompts/templates/chapter_writer.yml`: Prose drafting prompt combining scene plan, character context, and tone instructions.
- `prompts/templates/editor.yml`: General developmental editor prompt.
- `prompts/templates/content_reviewer.yml`: Quality review and consistency checker.
- `prompts/templates/fact_checker.yml`: Internal fact and lore consistency verification.
- `prompts/templates/plagiarism_checker.yml`: Originality and cliché avoidance prompt.
- `src/`: Python source code implementing agent orchestration and prompt injection.

---

## Workflow
Concept Generation (`concept_generator.yml`)
→ World Building (`worldbuilding.yml`)
→ Character Design (`character_generator.yml`)
→ Novel Outlining (`outliner.yml`)
→ Scene Outlining (`scene_outliner.yml`)
→ Chapter Writing (`chapter_writer.yml`)
→ Content Review (`content_reviewer.yml`)
→ Editorial Revision (`editor.yml` & `style_editor.yml`)
→ Fact & Plagiarism Check (`fact_checker.yml`, `plagiarism_checker.yml`).

---

## Inputs and Outputs

```text
Stage 1: Foundation
Input: High-level genre, author premise
Process: concept_generator.yml + worldbuilding.yml + character_generator.yml
Output: Story bible (World rules, character sheets, validated premise)
Used by next stage: Novel Outlining

Stage 2: Outlining
Input: Story bible
Process: outliner.yml → scene_outliner.yml
Output: Comprehensive chapter and scene outline
Used by next stage: Chapter Drafting

Stage 3: Drafting & Revision
Input: Scene outline + Character context + Style guide
Process: chapter_writer.yml → content_reviewer.yml → editor.yml
Output: Final polished chapter text
Used by next stage: Manuscript Assembly
```

---

## Prompt Inventory

### Prompt: `prompts/templates/chapter_writer.yml`
- **Purpose**: Generates scene-by-scene narrative prose adhering to chapter goals.
- **Required inputs**: `{concept}`, `{characters}`, `{world}`, `{scene_outline}`, `{tone}`.
- **Expected output**: Fully fleshed chapter prose.
- **Important constraints**: Maintain character voice consistency and sensory engagement.
- **Downstream consumer**: `content_reviewer.yml` and `editor.yml`.

### Prompt: `prompts/templates/worldbuilding.yml`
- **Purpose**: Generates coherent world lore, cultural systems, and physical environment rules.
- **Required inputs**: `{genre}`, `{premise}`, `{setting_type}`.
- **Expected output**: Structured world-building dossier.
- **Important constraints**: Output must be internally logical and non-contradictory.
- **Downstream consumer**: `character_generator.yml` and `chapter_writer.yml`.

---

## Context / Memory Strategy
Uses centralized YAML/JSON context objects injected into prompts at runtime via Python wrapper functions (`src/`). Variables for `{world}`, `{characters}`, and `{scene_outline}` are passed into each generation call.

---

## Editing Strategy
- **Developmental editing**: `editor.yml`.
- **Continuity**: `content_reviewer.yml` + `fact_checker.yml`.
- **Fact checking**: `fact_checker.yml`.
- **Line editing**: `style_editor.yml`.
- **Copy editing**: `editor.yml`.
- **Proofreading**: `content_reviewer.yml`.
- **Style review**: `style_editor.yml`.

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown / Text.
- **Chapter organization**: File-based inside Python project directories.
- **Assembly method**: Python build script.
- **Output formats**: Text, Markdown.
- **Scripts/tools required**: Python 3.

---

## Strongest Ideas
1. **Clean YAML Prompt Template Separation**: Cleanly separated YAML prompt templates with explicit input variable placeholders.
2. **Two-Stage Outlining**: Distinct separation between Novel-level Outlining (`outliner.yml`) and Scene-level Outlining (`scene_outliner.yml`).

---

## Weaknesses
- Basic context injection without rolling summary compression for very long manuscripts.
- Limited export formatting tooling (no built-in Pandoc/LaTeX build scripts).

---

## Reusable Knowledge
- Clean YAML prompt template schema (`prompts/templates/*.yml`).
- Decoupled scene-outliner prompt pattern.
"""

# 5. novel-template
reports["novel-template"] = """# Repository Report: novel-template

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
"""

# 6. AI_Novel
reports["AI_Novel"] = """# Repository Report: AI_Novel

## Repository
- **Name**: AI_Novel
- **URL**: https://github.com/kele-tao/AI_Novel
- **Commit**: `1cd51473`
- **Status**: SUCCESS
- **Primary purpose**: Web application and backend engine for generating Chinese webnovels, literary fiction, sci-fi, romance, and courses.
- **Primary target**: Both (Fiction & Course/Non-fiction).

---

## Important Paths
- `app/prompts/templates.py`: Central repository of outline and chapter generation prompts, including genre-specific style instructions (webnovel, literary, scifi, romance, mystery, course).
- `app/routes.py`: Flask route controllers managing generation steps, chapter streaming, and book export.
- `app/services/`: Generation logic services handling LLM API calls and context assembly.
- `works_library/`: Storage directory for generated book projects, outlines, and chapter texts.
- `main.py`: Application entry point.

---

## Workflow
Topic & Genre Selection 
→ Outline Generation (`OUTLINE_PROMPT_TEMPLATES`) 
→ User Outline Editing/Approval 
→ Section/Chapter Context Assembly (Worldview summary + Recent chapter rolling recap + Current chapter script) 
→ Chapter Generation with Genre Style Injection (`CONTENT_PROMPT_TEMPLATES`) 
→ Storage in `works_library/` 
→ Markdown/Text Export.

---

## Inputs and Outputs

```text
Stage 1: Outline Creation
Input: Topic, number of chapters, genre template
Process: OUTLINE_PROMPT_TEMPLATES generates chapter titles and dramatic hooks
Output: Structured Markdown outline
Used by next stage: Chapter Generation

Stage 2: Contextual Chapter Generation
Input: Current section title, chapter script, worldview context, recent chapters summary (last 3 chapters), genre style directive
Process: CONTENT_PROMPT_TEMPLATES executes LLM generation
Output: Full chapter prose text
Used by next stage: Library storage & downstream chapter recap

Stage 3: Rolling Memory Update
Input: Newly generated chapter
Process: Automated summarization of chapter into rolling plot context
Output: Updated recent chapters context buffer
Used by next stage: Subsequent chapter generation
```

---

## Prompt Inventory

### Prompt: Novel Chapter Generation with Style Directive
- **File**: `app/prompts/templates.py`
- **Purpose**: Generates complete chapter prose combining macro worldview, rolling recent summaries, and genre-specific style rules.
- **Required inputs**: `{topic}`, `{section_title}`, `{worldview_context}`, `{recent_chapters_summary}`, `{chapter_script}`, `{style_instruction}`.
- **Expected output**: Complete narrative chapter with opening hook and closing cliffhanger.
- **Important constraints**: First 200 words must introduce conflict/hook (for webnovels); strict adherence to science logic (for sci-fi).
- **Downstream consumer**: Works Library & Reader UI.

---

## Context / Memory Strategy
- **Worldview Context (`worldview_context`)**: Macro setting and background summary injected at top of prompt.
- **Rolling Recent Summary (`recent_chapters_summary`)**: Sliding window summarizing the most recent chapters to maintain local continuity without blowing context window limits.

---

## Editing Strategy
- **Developmental editing**: Absent in automated pipeline (handled via manual user outline edits in UI).
- **Continuity**: Enforced via recent chapter summaries.
- **Fact checking**: Absent.
- **Line editing**: Absent.
- **Copy editing**: Absent.
- **Proofreading**: Absent.
- **Style review**: Enforced upfront via genre style prompt prefixes.

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown / Plain Text files in `works_library/`.
- **Chapter organization**: Individual chapter text files.
- **Assembly method**: Python backend concatenation.
- **Output formats**: TXT, Markdown, EPUB.
- **Scripts/tools required**: Flask, Python.

---

## Strongest Ideas
1. **Genre-Specific Style Directives**: Pre-tuned stylistic constraints tailored to commercial genres (e.g. webnovel fast pacing + cliffhangers, literary introspection, hard sci-fi mathematical consistency).
2. **Triple-Layer Context Injection**: Worldview + Rolling Recent Summary + Chapter Script passed to every drafting step.

---

## Weaknesses
- Minimal automated post-generation editing or multi-pass quality control.
- Heavily focused on one-shot chapter generation.

---

## Reusable Knowledge
- Genre style instruction blocks (`template_instructions` in `templates.py`).
- 3-tier prompt context assembly pattern (Worldview + Rolling Summary + Chapter Beat).
"""

# 7. boekwriter
reports["boekwriter"] = """# Repository Report: boekwriter

## Repository
- **Name**: boekwriter
- **URL**: https://github.com/andrei-dubovik/boekwriter
- **Commit**: `4c4abd45`
- **Status**: SUCCESS
- **Primary purpose**: Automated non-fiction book generator compiling directly into professional LaTeX and PDF formats with SVG diagrams, tables, and illustrations.
- **Primary target**: Non-fiction (Technical, Academic, Textbooks, Informational).

---

## Important Paths
- `queries.yaml`: Master specification of structured LLM queries, prompts, and output JSON schemas.
- `write_book.py`: Python orchestrator executing book generation, word budget allocation, chunk drafting, and LaTeX assembly.
- `template.tex`: Professional LaTeX book template configured with `booktabs`, figure environments, and typography packages.
- `llmwrapper/`: Python wrapper handling LLM API calls, structured JSON schema parsing, and token caching.

---

## Workflow
Book Title & Target Word Count 
→ Chapter Breakdown with Word Budget Allocation (`queries.yaml: chapters`) 
→ Detailed Chapter Item Planning with Item-Level Word Budgets (`queries.yaml: chapter-outline`) 
→ Visual Aid Selection & Planning (`queries.yaml: visuals`) 
→ Sequential Chunk-by-Chunk Prose Drafting with Prior-Chunk Context (`queries.yaml: chunk`) 
→ SVG Figure Generation (`queries.yaml: figure`) 
→ LaTeX Table Generation (`queries.yaml: table`) 
→ Chapter Headpiece Illustration Description & Image Generation (`queries.yaml: headpiece` & `image`) 
→ LaTeX Manuscript Compilation into PDF (`template.tex` via pdflatex/xelatex).

---

## Inputs and Outputs

```text
Stage 1: Book Architecture & Budgeting
Input: Book title (${book}), Total word count budget (${word_count}), Min words per chapter (${min_words})
Process: queries.yaml: chapters
Output: JSON array: [{number, title, description, word_count}]
Used by next stage: Chapter Outlining

Stage 2: Chapter Planning & Sub-Budgets
Input: Chapter title, chapter description, chapter word budget
Process: queries.yaml: chapter-outline
Output: JSON array: [{item, word_count}] (Sentence-long plan items with individual word counts)
Used by next stage: Visuals planning & Chunk drafting

Stage 3: Visual Aid Architecture
Input: Chapter plan, word budget
Process: queries.yaml: visuals
Output: JSON array: [{number, aid: "Table"|"SVG"|"Photo", description}]
Used by next stage: Chunk drafting & Figure generators

Stage 4: Chunk Drafting
Input: Book outline, Chapter plan, Current plan point, Parent chunk text, Visual description
Process: queries.yaml: chunk
Output: Technical prose chunk (Markdown text + LaTeX math formulas)
Used by next stage: LaTeX book assembly

Stage 5: Visuals & Headpiece Generation
Input: Text chunk referencing figure/table
Process: queries.yaml: figure / table / headpiece / image
Output: Valid SVG code, LaTeX tabular code, PNG chapter headpiece image
Used by next stage: Final LaTeX build
```

---

## Prompt Inventory

### Prompt: Chapter Breakdown with Word Budgeting
- **File**: `queries.yaml` (query: `chapters`)
- **Purpose**: Decomposes a book into chapters and allocates a strict mathematical word budget per chapter.
- **Required inputs**: `${book}`, `${word_count}`, `${min_words}`.
- **Expected output**: JSON schema: `[{number: int, title: str, description: str, word_count: int}]`.
- **Important constraints**: Sum of chapter word counts must fit overall book budget.
- **Downstream consumer**: `chapter-outline` query.

### Prompt: Sequential Chunk Drafting with Prior-Chunk Anchor
- **File**: `queries.yaml` (query: `chunk`)
- **Purpose**: Drafts a single section point while maintaining immediate continuity with the preceding text.
- **Required inputs**: `${book}`, `${chapters}`, `${cid}`, `${outline}`, `${oid}`, `${parent_chunk}`, `${min_words}`, `${max_words}`, `${visual}`.
- **Expected output**: Prose chunk adhering to exact word boundaries, integrating LaTeX math and figure references.
- **Important constraints**: Concise writing, no headers, use Markdown and LaTeX syntax.
- **Downstream consumer**: `write_book.py` LaTeX assembler.

---

## Context / Memory Strategy
- **Macro Memory**: Entire chapter outline passed in context.
- **Local Continuity**: Exact preceding chunk text (`${parent_chunk}`) injected into the prompt when generating point `${oid + 1}`.
- **Word Budget Tracking**: Exact min/max word targets dynamically calculated and enforced per chunk.

---

## Editing Strategy
- **Developmental editing**: Handled structurally via mathematical budget allocation and outline validation.
- **Continuity**: Enforced via prior-chunk injection (`parent_chunk`).
- **Fact checking**: Absent.
- **Line editing**: Handled via prompt constraints ("Be concise in your writing, avoid overly verbose prose").
- **Copy editing**: Absent.
- **Proofreading**: Absent.
- **Style review**: Enforced via prompt rules.

---

## Export / Assembly Strategy
- **Manuscript source format**: Structured JSON cache + LaTeX (`.tex`).
- **Chapter organization**: Scripted assembly in `write_book.py`.
- **Assembly method**: Python script populating `template.tex` and running `pdflatex`.
- **Output formats**: Professional PDF.
- **Scripts/tools required**: Python, LaTeX (pdflatex), SVG/Image tools.

---

## Strongest Ideas
1. **Mathematical Word Budget Allocation**: Downward cascading word budgets (Book → Chapters → Outline Items → Chunks).
2. **Integrated Visual Generation**: Automated creation of SVG diagrams, LaTeX tables, and chapter headpiece illustrations linked to text.
3. **Structured JSON Schema Enforcement**: Every generation stage uses strict schema validation.

---

## Weaknesses
- Exclusively designed for non-fiction/technical books; lacks fiction narrative devices (character arcs, dialogue).
- No post-drafting editorial or revision passes.

---

## Reusable Knowledge
- Hierarchical word-budget allocation prompt logic.
- Structured schema-driven chunk generation with prior-chunk context (`parent_chunk`).
- Integrated SVG and LaTeX table prompt patterns.
"""

# 8. KDP-Publishing-Prompt-Library
reports["KDP-Publishing-Prompt-Library"] = """# Repository Report: KDP-Publishing-Prompt-Library

## Repository
- **Name**: KDP-Publishing-Prompt-Library
- **URL**: https://github.com/kannfrank02-code/KDP-Publishing-Prompt-Library
- **Commit**: `45063f4a`
- **Status**: SUCCESS
- **Primary purpose**: Curated prompt library for Amazon Kindle Direct Publishing (KDP) ideation, writing, keywords, descriptions, and launch marketing.
- **Primary target**: Publishing only & Commercial Non-fiction.

---

## Important Paths
- `kdp-book-idea-generator.md`: Prompts for generating profitable KDP book niches, high-demand topics, and low-competition angles.
- `kdp-keyword-research-prompt.md`: Prompts for Amazon search keyword extraction, 7-keyword backend optimization, and category selection.
- `kdp-book-outline-prompt.md`: Prompts for reader-problem solving outlines and non-fiction chapter logic.
- `kdp-chapter-writing-prompt.md`: Prompts for actionable, engaging non-fiction chapter drafting.
- `kdp-book-description-prompt.md`: Prompts for copywriting high-converting Amazon sales descriptions (Hook, Story/Problem, Bullet Benefits, CTA).
- `kdp-journal-creation-prompt.md`: Prompts for low-content and guided journal creation.
- `kdp-content-repurposing-prompt.md`: Prompts for repurposing book chapters into lead magnets, social posts, and email sequences.

---

## Workflow
Niche & Idea Generation (`kdp-book-idea-generator.md`)
→ Keyword & Category Research (`kdp-keyword-research-prompt.md`)
→ Outline Creation (`kdp-book-outline-prompt.md`)
→ Chapter Writing (`kdp-chapter-writing-prompt.md`)
→ Book Description Copywriting (`kdp-book-description-prompt.md`)
→ Content Repurposing & Launch (`kdp-content-repurposing-prompt.md`).

---

## Inputs and Outputs

```text
Stage 1: Commercial Positioning
Input: Target audience, general topic area
Process: Idea generator + Keyword research prompts
Output: Validated book title, subtitle, 7 backend search keywords, 3 Amazon categories
Used by next stage: Outlining & Description Copywriting

Stage 2: Outlining & Drafting
Input: Validated title, target audience pain points
Process: Book outline prompt → Chapter writing prompt
Output: Chapter drafts focused on solving specific reader problems
Used by next stage: Publishing Copy

Stage 3: Sales Copy & Metadata
Input: Book contents, core benefits, author bio
Process: Book description prompt
Output: Amazon HTML sales page description (Headline, Body bullets, Social proof, Urgency CTA)
Used by next stage: KDP Dashboard Publishing
```

---

## Prompt Inventory

### Prompt: KDP High-Converting Book Description
- **File**: `kdp-book-description-prompt.md`
- **Purpose**: Generates Amazon product page sales copy formatted with Amazon-supported HTML tags (`<h2>`, `<b>`, `<i>`, `<ul>`).
- **Required inputs**: Book title, Target reader, 3 major reader problems, 3 major solutions/benefits.
- **Expected output**: Compelling Amazon product page copy with headline, hook, bullet points, and CTA.
- **Important constraints**: Must adhere to Amazon HTML formatting limitations.
- **Downstream consumer**: Amazon KDP Publishing Dashboard.

### Prompt: KDP 7-Backend Keyword Optimizer
- **File**: `kdp-keyword-research-prompt.md`
- **Purpose**: Generates 7 keyword phrases (under 50 characters each) optimized for Amazon buyer search intent.
- **Required inputs**: Book topic, niche, audience.
- **Expected output**: 7 unique keyword strings avoiding repetition of title words.
- **Important constraints**: No trademarked terms, no subjective claims like "best seller".
- **Downstream consumer**: KDP Metadata Setup.

---

## Context / Memory Strategy
No meaningful persistent-context mechanism identified (collection of standalone prompt templates).

---

## Editing Strategy
Absent (all editing categories unsupported in this prompt collection).

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown / Text.
- **Chapter organization**: Standalone prompts.
- **Assembly method**: Manual copy-paste into word processor or KDP portal.
- **Output formats**: Amazon KDP metadata fields, Markdown.
- **Scripts/tools required**: None.

---

## Strongest Ideas
1. **Commercial Amazon KDP Metadata Optimization**: High-converting sales copy prompts structured specifically for Amazon's formatting rules.
2. **Backend Keyword Selection Logic**: Focus on buyer intent, search volume, and non-redundancy with book title/subtitle.
3. **Content Repurposing Framework**: Converting finished book chapters into promotional assets.

---

## Weaknesses
- No drafting pipeline, context management, or manuscript editing tools.
- Simple single-turn prompt templates.

---

## Reusable Knowledge
- Amazon sales copy formula (Hook → Agitation → Solution → Feature Bullets → Risk Reversal → CTA).
- KDP backend keyword research prompt pattern.
"""

# 9. The-Novelists-Atelier
reports["The-Novelists-Atelier"] = """# Repository Report: The-Novelists-Atelier

## Repository
- **Name**: The-Novelists-Atelier
- **URL**: https://github.com/f5alcon/The-Novelists-Atelier
- **Commit**: `e0056002`
- **Status**: SUCCESS
- **Primary purpose**: Comprehensive 2,400+ line editorial analysis and manuscript critique prompt suite.
- **Primary target**: Editing only (Fiction novels & memoirs).

---

## Important Paths
- `novelist-atelier-prompts.md`: Massive master reference guide containing 16 distinct categories of editorial prompts:
  - Category 1: Manuscript-Level Analysis (22-pass deep editorial report outputting self-contained HTML/PDF scorecards).
  - Category 2: Style & Voice (Authorial voice fingerprinting, tone drift, dialogue voice).
  - Category 3: Developmental Editing (Three-act plot structure, midpoint shifts, climax integrity).
  - Category 4: Copy Editing (Grammar, punctuation, repetitive phrasing, formatting).
  - Category 5: Line Editing (Sentence cadence, prose tightening, sensory texture).
  - Category 6: Character (Arc consistency, motivation tracking, internal vs external conflict).
  - Category 7: World-Building (Lore consistency, timeline validation, rule enforcement).
  - Category 8: Location & Setting (Sensory immersion, spatial logic, atmosphere).
  - Category 9: Punch & Impact (Scene climaxes, emotional resonance, thematic payoffs).
  - Category 10: Chapter-Level Review (Pacing heatmaps, chapter hooks, exit states).
  - Category 11: Paragraph-Level (Flow, transitions, exposition distribution).
  - Category 12: Sentence-Level (Rhythm, syntactic variety, active vs passive voice).
  - Category 13: Tension & Engagement (Micro-tension, stakes escalation, mystery ledger).
  - Category 14: Prose & Style Audits (Cliche detection, sensory balance radar).
  - Category 15: Reader Experience (Emotional journey mapping, cognitive load).
  - Category 16: Genre-Specific (Mystery, Thriller, Romance, Sci-Fi, Fantasy rubrics).

---

## Workflow
Manuscript Draft Input 
→ Category 1: 22-Pass Full Manuscript Editorial Audit 
→ Macro Developmental Pass (Plot structure, pacing heatmap, character arcs) 
→ Chapter & Scene Review (Tension curves, scene goals, entry/exit states) 
→ Line & Sentence Surgery (Cadence, dialogue subtext, prose tightening) 
→ Micro Copy Edit & Consistency Verification 
→ Self-Contained HTML/PDF Diagnostic Report Generation.

---

## Inputs and Outputs

```text
Stage 1: Full Manuscript Analysis
Input: Full manuscript text (.txt, .docx, .md), 2-4 sentence synopsis
Process: 22-Pass Editorial Analysis prompt (novelist-atelier-prompts.md §1)
Output: Single self-contained HTML report with cover page, TOC, pacing heatmap, tension chart (SVG), character arc timeline, scorecard, and color-coded severity flags (🔴 Critical / 🟡 Important / 🟢 Minor)
Used by next stage: Targeted Developmental & Line Revisions

Stage 2: Targeted Craft Revisions
Input: Specific problematic chapter or scene identified in report
Process: Specialized category prompts (e.g. Dialogue Surgery, Pacing Heatmap, Tension Audit)
Output: Line-by-line editorial feedback and revised text options
Used by next stage: Final Proofreading & Publication
```

---

## Prompt Inventory

### Prompt: 22-Pass Full Manuscript Editorial Analysis
- **File**: `novelist-atelier-prompts.md` (§1)
- **Purpose**: Conducts the most rigorous multi-pass editorial diagnosis in the entire literature, scoring plot, pacing, character arcs, theme, world-building, stakes, dialogue, and prose.
- **Required inputs**: `[MANUSCRIPT TITLE]`, `[SYNOPSIS]`, `[MANUSCRIPT TEXT]`.
- **Expected output**: Comprehensive self-contained HTML document with embedded CSS, SVG charts, tables, and color-coded recommendations.
- **Important constraints**: Requires large-context LLMs (Claude Opus/Sonnet); high token budget.
- **Downstream consumer**: Author revision roadmap.

### Prompt: Pacing Heatmap & Tension Arc Auditor
- **File**: `novelist-atelier-prompts.md` (§10 & §13)
- **Purpose**: Creates a chapter-by-chapter table rating Tension (1–10), Pacing Rating (Too Fast/Fast/Good/Slow/Draggy), Scene Types, and Energy Level.
- **Required inputs**: Chapter texts.
- **Expected output**: Structured pacing heatmap table + top 10 ranked pacing fixes.
- **Important constraints**: Evaluates action-to-reflection balance and identifies energy valleys.
- **Downstream consumer**: Developmental rewriting pass.

---

## Context / Memory Strategy
Designed for large-window LLMs processing entire manuscripts or long excerpts in single or multi-turn editorial sessions. Provides structured synopsis and context injection headers.

---

## Editing Strategy
- **Developmental editing**: Extremely thorough 22-pass structural analysis.
- **Continuity**: Pass 5 World-Building Continuity Scan & Pass 3 Character Arc Consistency.
- **Fact checking**: Setting and timeline verification.
- **Line editing**: Category 5 & Category 12 (Sentence rhythm, syntactic variety, active verbs).
- **Copy editing**: Category 4 (Grammar, repetitive phrases, formatting).
- **Proofreading**: Final polish passes.
- **Style review**: Category 2 & Category 14 (Prose & style audits, sensory balance radar).

---

## Export / Assembly Strategy
- **Manuscript source format**: Text / Markdown / Word DOCX.
- **Chapter organization**: Full manuscript or chapter-by-chapter analysis.
- **Assembly method**: Output generated as standalone HTML reports printable directly to PDF.
- **Output formats**: HTML, PDF, Markdown.
- **Scripts/tools required**: Web browser for HTML-to-PDF rendering.

---

## Strongest Ideas
1. **22-Pass Editorial Analysis Matrix**: The most comprehensive editorial framework available, covering macro architecture down to syllable rhythm.
2. **Interactive HTML/PDF Diagnostic Reporting**: Generating beautiful, executive-ready HTML audit reports with SVG tension charts and color-coded issue severity.
3. **Pacing Heatmap Table**: Objective quantification of narrative momentum across every chapter.

---

## Weaknesses
- Focused purely on editing/critique; does not include drafting or generation workflows.
- Very high token consumption when analyzing full manuscripts.

---

## Reusable Knowledge
- The complete 22-pass editorial rubric and inspection criteria.
- HTML/SVG report generation prompt patterns.
- Pacing heatmap evaluation rubric.
"""

# 10. agentic-novel-outliner
reports["agentic-novel-outliner"] = """# Repository Report: agentic-novel-outliner

## Repository
- **Name**: agentic-novel-outliner
- **URL**: https://github.com/bhojak8/agentic-novel-outliner
- **Commit**: `c56ec398`
- **Status**: SUCCESS
- **Primary purpose**: Multi-agent interactive web application and CLI for generating structured outlines across fiction, non-fiction, kids books, and short stories.
- **Primary target**: Outlining only (Fiction, Non-fiction, Kids, Short story).

---

## Important Paths
- `src/agents/fiction/`: Fiction outliner agent implementing premise refinement, character arcs, and chapter beat sheets.
- `src/agents/nonfiction/`: Non-fiction outliner agent focusing on core thesis, reader takeaways, and logical evidence flow.
- `src/agents/kidsbook/`: Children's book outliner with simplified moral arcs, visual illustration beats, and age-appropriate vocabulary.
- `src/agents/shortstory/`: Compact outliner for short fiction (single-conflict focus, twist endings).
- `src/core/`: Agent orchestration engine, prompt pipelines, and schema validators.
- `cli.js`: Command-line interface for running outline generation.
- `src/ui/`: Interactive web UI for step-by-step outline building.

---

## Workflow
Genre Selection (Fiction / Non-fiction / Kids / Short Story) 
→ Core Premise & Audience Definition 
→ Agent-Assisted Brainstorming & Question Answering 
→ Character/Thesis Definition 
→ Act & Milestone Structuring 
→ Chapter & Scene Beat Breakdown 
→ JSON / Markdown Outline Export.

---

## Inputs and Outputs

```text
Stage: Outline Architecture
Input: Genre selection, user seed concept, target audience
Process: Specialized domain agent (fiction/nonfiction/kids/shortstory) generates multi-level structure
Output: Structured outline (Premise, Characters/Thesis, Act structure, Chapter-by-chapter beats)
Used by next stage: Downstream Drafting Systems
```

---

## Prompt Inventory

### Prompt: Domain-Specific Outliner Agent Prompt
- **File**: `src/agents/fiction/` / `src/agents/nonfiction/`
- **Purpose**: Generates hierarchical outlines tailored to specific publishing formats.
- **Required inputs**: User premise, target length, genre constraints.
- **Expected output**: JSON/Markdown outline featuring chapter milestones and emotional beats.
- **Important constraints**: Strict structural progression (e.g. 3-Act for fiction, Problem-Solution-Evidence for non-fiction).
- **Downstream consumer**: UI Editor & JSON Export.

---

## Context / Memory Strategy
Maintains project state in application memory / local storage, serializing to structured JSON outline objects.

---

## Editing Strategy
- **Developmental editing**: Built into the outline revision phase.
- **Continuity / Line / Copy / Proofreading**: Absent (focused solely on outlining).

---

## Export / Assembly Strategy
- **Manuscript source format**: JSON / Markdown.
- **Chapter organization**: Hierarchical JSON structure.
- **Assembly method**: Web UI / CLI serializer.
- **Output formats**: JSON, Markdown.
- **Scripts/tools required**: Node.js, Vite.

---

## Strongest Ideas
1. **Domain-Specific Outlining Agents**: Distinct architectural logic for Fiction, Non-fiction, Children's Books, and Short Stories.
2. **Interactive Premise Refinement**: Multi-turn questioning that clarifies ambiguities before generating chapter beats.

---

## Weaknesses
- Stops at outline generation; does not support chapter drafting, prose editing, or manuscript compilation.

---

## Reusable Knowledge
- Format-specific outlining methodologies (especially differences between Kids Books, Non-fiction, and Novels).
- Interactive interview questioning patterns for premise clarification.
"""

# 11. prompts.chat
reports["prompts.chat"] = """# Repository Report: prompts.chat

## Repository
- **Name**: prompts.chat
- **URL**: https://github.com/f/prompts.chat
- **Commit**: `f1c51568`
- **Status**: UNAVAILABLE (Repository history depth/bandwidth constraint during clone; network disconnect)
- **Primary purpose**: Community repository of general ChatGPT system prompts and persona definitions.
- **Primary target**: General prompt engineering.

---

## Important Paths
- `NOT VERIFIED` (Repository unavailable locally due to shallow clone network failure).

---

## Workflow
No complete sequential workflow identified.

---

## Inputs and Outputs
```text
Stage: General Prompt Library
Input: User prompt query
Process: General persona injection (e.g. "Act as a Storyteller", "Act as an Editor")
Output: Single-turn roleplay responses
Used by next stage: Standalone chat sessions
```

---

## Prompt Inventory
- `NOT VERIFIED` (General collection of "Act as an X" persona prompts).

---

## Context / Memory Strategy
No meaningful persistent-context mechanism identified.

---

## Editing Strategy
Absent.

---

## Export / Assembly Strategy
- **Manuscript source format**: N/A.
- **Chapter organization**: N/A.
- **Assembly method**: N/A.
- **Output formats**: Text.
- **Scripts/tools required**: None.

---

## Strongest Ideas
- Wide variety of generic persona system prompts ("Act as a novelist", "Act as a screenwriter").

---

## Weaknesses
- Lacks end-to-end book-length workflow, state management, chapter planning, and publishing capabilities.

---

## Reusable Knowledge
- Baseline "Act as [Role]" roleplay phrasing templates.
"""

# 12. AI-Prompts-for-E-book-Generation
reports["AI-Prompts-for-E-book-Generation"] = """# Repository Report: AI-Prompts-for-E-book-Generation

## Repository
- **Name**: AI-Prompts-for-E-book-Generation
- **URL**: https://github.com/monju252/AI-Prompts-for-E-book-Generation
- **Commit**: `c8f18c34`
- **Status**: SUCCESS
- **Primary purpose**: Prompt collection for fast commercial non-fiction eBooks, lead magnets, and blog repurposing.
- **Primary target**: Non-fiction (Lead generation, marketing eBooks, how-to guides).

---

## Important Paths
- `README.md`: Central document containing 10 core eBook creation prompts (Idea Generator, Outline Generator, Chapter Writer, Section Expander, Blog-to-Book Repurposer, CTA/Lead Magnet Page, Style/Tone Editor, Visual Suggestions, Resource Section, Final Launch Checklist).

---

## Workflow
Niche & Title Ideation 
→ 7-Chapter Non-Fiction Outline Generation 
→ Chapter-by-Chapter Drafting 
→ Section Expansion (Examples & Steps) 
→ Tone & Style Adjustment 
→ Visual/Chart Design Suggestions 
→ Resource/Tool Appendices 
→ Call-To-Action & Landing Page Copywriting 
→ Final Launch Checklist.

---

## Inputs and Outputs

```text
Stage 1: Ideation & Structure
Input: Target audience, topic, reader goal
Process: Prompt 1 (Idea Generator) + Prompt 2 (7-Chapter Outline Generator)
Output: Validated title + 7-chapter table of contents
Used by next stage: Chapter Drafting

Stage 2: Drafting & Expansion
Input: Chapter title, tone, outline
Process: Prompt 3 (Chapter Writer) + Prompt 4 (Section Expander)
Output: Full chapter content with actionable steps and examples
Used by next stage: Polishing & Back Matter

Stage 3: Marketing & Launch
Input: eBook title, core value proposition
Process: Prompt 6 (CTA & Landing Page) + Prompt 10 (Launch Checklist)
Output: Landing page copy, download CTA, launch verification checklist
Used by next stage: Distribution
```

---

## Prompt Inventory

### Prompt: Blog-to-eBook Repurposing Prompt
- **File**: `README.md` (Prompt #5)
- **Purpose**: Synthesizes multiple disparate blog posts into a unified, logically progressing eBook outline with transitional bridges.
- **Required inputs**: List of 5+ blog post titles/topics.
- **Expected output**: Cohesive book outline with transitional connective tissue between topics.
- **Important constraints**: Must eliminate redundant introductions across articles.
- **Downstream consumer**: Chapter Writer.

### Prompt: Section Expander with Actionable Frameworks
- **File**: `README.md` (Prompt #4)
- **Purpose**: Takes a brief concept paragraph and expands it into a comprehensive section with step-by-step instructions and practical examples.
- **Required inputs**: Target summary paragraph.
- **Expected output**: 3 structured subsections with bullet points and actionable advice.
- **Important constraints**: Focus on practical utility and readability.
- **Downstream consumer**: Manuscript chapter assembly.

---

## Context / Memory Strategy
No meaningful persistent-context mechanism identified (manual user-managed context).

---

## Editing Strategy
- **Developmental editing**: Absent.
- **Continuity**: Absent.
- **Fact checking**: Absent.
- **Line editing**: Prompt #7 (Style/Tone rewrite prompt).
- **Copy editing**: Absent.
- **Proofreading**: Mentioned in final launch checklist.
- **Style review**: Prompt #7 (Rewrite in professional/friendly/conversational tone).

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown / Plain Text.
- **Chapter organization**: Single-file or manual document pasting.
- **Assembly method**: Manual copy-paste into Google Docs, Notion, or Word.
- **Output formats**: PDF, EPUB (via manual export).
- **Scripts/tools required**: Word processor.

---

## Strongest Ideas
1. **Blog-to-Book Synthesizer**: Recombining existing short-form content into a structured monograph.
2. **Actionable Section Expansion**: Methodical expansion of summary ideas into multi-step practical frameworks.
3. **End-to-End Commercial Focus**: Covering the full path from lead magnet design to landing page CTA copy.

---

## Weaknesses
- Minimal multi-chapter state tracking; prone to repetition if used without external memory.
- Lacks automated build or compilation scripts.

---

## Reusable Knowledge
- Blog-to-book outline synthesis prompt.
- Non-fiction practical section expansion prompt pattern.
- Lead magnet landing page copywriting template.
"""

# 13. bookwiz-ai-prompts
reports["bookwiz-ai-prompts"] = """# Repository Report: bookwiz-ai-prompts

## Repository
- **Name**: bookwiz-ai-prompts
- **URL**: https://github.com/KristiyanTs/bookwiz-ai-prompts
- **Commit**: `45bbdf4e`
- **Status**: SUCCESS
- **Primary purpose**: Prompt collection for fiction story planning, character generation, plot arcs, and cover art generation.
- **Primary target**: Fiction (Story planning & Concept generation).

---

## Important Paths
- `text/title.txt`: Prompt for generating high-concept book titles.
- `text/theme.txt`: Prompt for thematic premise and philosophical core development.
- `text/synopsis.txt`: Comprehensive prompt for multi-page plot synopsis and story structure.
- `text/plot.txt`: Core conflict and plot progression prompts.
- `text/character.txt`: Character motivation, flaw, and arc generation prompt.
- `text/cover-image-description.txt`: Midjourney/DALL-E cover art prompt generator.

---

## Workflow
Theme Definition (`text/theme.txt`) 
→ Title Generation (`text/title.txt`) 
→ Character Arcs (`text/character.txt`) 
→ Plot & Conflict Architecture (`text/plot.txt`) 
→ Comprehensive Synopsis (`text/synopsis.txt`) 
→ Cover Art Generation (`text/cover-image-description.txt`).

---

## Inputs and Outputs

```text
Stage: Story Concept & Synopsis
Input: Seed premise, genre, target mood
Process: theme.txt → title.txt → character.txt → synopsis.txt
Output: Full story synopsis, character sheets, cover art prompts
Used by next stage: Downstream Writing
```

---

## Prompt Inventory

### Prompt: Comprehensive Story Synopsis Generator
- **File**: `text/synopsis.txt`
- **Purpose**: Generates an exhaustive narrative synopsis detailing setup, inciting incident, rising action, midpoint reversal, dark night of the soul, climax, and resolution.
- **Required inputs**: Genre, theme, main character goal.
- **Expected output**: Multi-page structured synopsis.
- **Important constraints**: Clear cause-and-effect progression between narrative beats.
- **Downstream consumer**: Chapter Outlining.

---

## Context / Memory Strategy
No meaningful persistent-context mechanism identified (standalone text prompts).

---

## Editing Strategy
Absent.

---

## Export / Assembly Strategy
- **Manuscript source format**: Text.
- **Chapter organization**: Standalone text files.
- **Assembly method**: Manual.
- **Output formats**: Text.
- **Scripts/tools required**: None.

---

## Strongest Ideas
1. **Upfront Thematic Grounding**: Deriving the plot and title directly from a central thematic question.
2. **Visual Cover Prompt Generator**: Generating aligned visual art prompts alongside literary planning.

---

## Weaknesses
- Stops at the synopsis stage; no chapter drafting, continuity tracking, or publishing workflows.

---

## Reusable Knowledge
- Thematic exploration prompt pattern (`text/theme.txt`).
- Cause-and-effect narrative synopsis template (`text/synopsis.txt`).
"""

# 14. Prompt-Engineering-Guide
reports["Prompt-Engineering-Guide"] = """# Repository Report: Prompt-Engineering-Guide

## Repository
- **Name**: Prompt-Engineering-Guide
- **URL**: https://github.com/dair-ai/Prompt-Engineering-Guide
- **Commit**: `57673726`
- **Status**: UNAVAILABLE (Repository history depth/bandwidth constraint during clone; network disconnect)
- **Primary purpose**: Academic and industry guide to general prompt engineering techniques, reasoning frameworks, and agent architectures.
- **Primary target**: General prompt engineering.

---

## Important Paths
- `NOT VERIFIED` (Repository unavailable locally due to shallow clone network failure).

---

## Workflow
No complete sequential workflow identified.

---

## Inputs and Outputs
```text
Stage: General Prompt Methodology
Input: Prompt engineering concepts
Process: Systematic technique demonstration (Zero-shot, Few-shot, Chain-of-Thought, ReAct, Directional Stimulus)
Output: Prompt design principles
Used by next stage: System Design
```

---

## Prompt Inventory
- `NOT VERIFIED` (Educational guide on Chain-of-Thought, Directional Stimulus, ReAct, and Self-Consistency).

---

## Context / Memory Strategy
No meaningful persistent-context mechanism identified.

---

## Editing Strategy
Absent.

---

## Export / Assembly Strategy
- **Manuscript source format**: N/A.
- **Chapter organization**: N/A.
- **Assembly method**: N/A.
- **Output formats**: Markdown / Docusaurus website.
- **Scripts/tools required**: Node.js.

---

## Strongest Ideas
- Foundational prompting patterns: Chain-of-Thought (CoT), Step-by-Step reasoning, Directional Stimulus Prompting, and Self-Consistency.

---

## Weaknesses
- Educational guide rather than an executable book-writing pipeline.

---

## Reusable Knowledge
- Chain-of-Thought prompting methodology for complex plot planning.
- Directional Stimulus Prompting for steering narrative tone and pace.
"""

# 15. LLM-book-generator
reports["LLM-book-generator"] = """# Repository Report: LLM-book-generator

## Repository
- **Name**: LLM-book-generator
- **URL**: https://github.com/fangfufu/LLM-book-generator
- **Commit**: `a87646e6`
- **Status**: SUCCESS
- **Primary purpose**: Python-based automated multi-chapter book generation system with GUI and DOCX manuscript assembly.
- **Primary target**: Both (Fiction & Non-fiction pipelines).

---

## Important Paths
- `book_generator/orchestrator.py`: Master controller orchestrating book creation, chapter loop, state persistence, and resume functionality.
- `book_generator/common_generator.py`: Shared core logic for outline generation, premise expansion, and prompt formatting.
- `book_generator/fiction_generator.py`: Fiction-specific pipeline managing character rosters, scene planning, and narrative dialogue.
- `book_generator/non_fiction_generator.py`: Non-fiction-specific pipeline managing topic trees, chapter takeaways, and instructional prose.
- `book_generator/docx_builder.py`: 80KB+ comprehensive Word DOCX document builder formatting headings, styles, page breaks, and front matter.
- `book_generator/llm_api.py`: Multi-provider API abstraction layer (OpenAI, Anthropic, Ollama, Local LLMs) with token rate limiting and retry logic.
- `config.yaml`: Configuration file defining model parameters, temperatures, and generation settings.
- `gui.py`: Graphical user interface for configuring and monitoring book generation.

---

## Workflow
Topic & Configuration Setup (`config.yaml` / `gui.py`) 
→ Premise Expansion (`common_generator.py`) 
→ Genre Pipeline Routing (`fiction_generator.py` OR `non_fiction_generator.py`) 
→ Hierarchical Outline Generation 
→ Chapter-by-Chapter Sequential Generation Loop (`orchestrator.py`) 
→ State Checkpointing & Resume Management 
→ Word Document Compilation & Styling (`docx_builder.py`) 
→ Output `.docx` File Delivery.

---

## Inputs and Outputs

```text
Stage 1: Configuration & Routing
Input: User topic, target chapter count, model selection, genre flag (fiction/non-fiction)
Process: orchestrator.py initializes state and routes to fiction_generator or non_fiction_generator
Output: Project configuration and state JSON
Used by next stage: Outlining

Stage 2: Outline Generation
Input: Expanded premise, target chapter count
Process: common_generator.py generates chapter titles and summaries
Output: Structured outline JSON
Used by next stage: Chapter Generation Loop

Stage 3: Sequential Chapter Generation
Input: Chapter title, chapter summary, previous chapter context, character list (if fiction)
Process: llm_api.py executes generation calls with automatic retry and rate limiting
Output: Chapter prose text saved in project state
Used by next stage: DOCX Assembly

Stage 4: Manuscript Compilation
Input: All generated chapters, book metadata
Process: docx_builder.py applies typography, styles, title page, TOC, and chapter page breaks
Output: Formatted Microsoft Word (.docx) book file
Used by next stage: Author Review & Publishing
```

---

## Prompt Inventory

### Prompt: Fiction Chapter Generator Prompt
- **File**: `book_generator/fiction_generator.py`
- **Purpose**: Generates novel chapter prose using character profiles and previous chapter summary context.
- **Required inputs**: Book premise, Characters, Current chapter outline, Previous chapter summary.
- **Expected output**: Engaging chapter prose adhering to narrative voice.
- **Important constraints**: Avoid repetition; progress the active plot beats.
- **Downstream consumer**: `orchestrator.py` & `docx_builder.py`.

### Prompt: Non-Fiction Chapter Generator Prompt
- **File**: `book_generator/non_fiction_generator.py`
- **Purpose**: Generates educational chapter prose featuring clear explanations, practical examples, and chapter summaries.
- **Required inputs**: Book topic, Target audience, Chapter title, Key subtopics.
- **Expected output**: Educational chapter prose formatted with subheaders.
- **Important constraints**: Clear pedagogical progression, authoritative tone.
- **Downstream consumer**: `docx_builder.py`.

---

## Context / Memory Strategy
- **State Checkpointing**: Saves full generation state to disk as JSON after every chapter, enabling seamless pausing and resumption.
- **Rolling Context**: Injects previous chapter summary into current chapter drafting prompts.

---

## Editing Strategy
- **Developmental editing**: Absent in automated pipeline.
- **Continuity**: Enforced via previous-chapter summary injection.
- **Fact checking**: Absent.
- **Line editing**: Absent.
- **Copy editing**: Absent.
- **Proofreading**: Absent.
- **Style review**: Controlled via prompt parameters in `config.yaml`.

---

## Export / Assembly Strategy
- **Manuscript source format**: JSON project state / Text.
- **Chapter organization**: Programmatic array of chapter strings.
- **Assembly method**: Python `python-docx` library (`book_generator/docx_builder.py`).
- **Output formats**: Microsoft Word (.docx).
- **Scripts/tools required**: Python 3, `python-docx`.

---

## Strongest Ideas
1. **Robust DOCX Document Builder**: Extremely comprehensive Word document styling engine with custom headings, margins, front matter, and page numbering.
2. **State Checkpointing & Resume**: Full fault-tolerant generation loop that can recover from API failures or interruptions.
3. **Dual Pipeline Specialization**: Completely separate generation code paths for Fiction vs Non-Fiction.

---

## Weaknesses
- Lack of multi-pass editorial review or line editing; generates text directly to final output.

---

## Reusable Knowledge
- State persistence and resume architecture for multi-chapter generation.
- Python DOCX automated manuscript assembly patterns.
- Explicit Fiction vs Non-Fiction prompt pipeline separation.
"""

# 16. AI-Novel-Writer
reports["AI-Novel-Writer"] = """# Repository Report: AI-Novel-Writer

## Repository
- **Name**: AI-Novel-Writer
- **URL**: https://github.com/FutureAIGuide/AI-Novel-Writer
- **Commit**: `b83c914d`
- **Status**: SUCCESS
- **Primary purpose**: Python modular novel generation framework and UI studio.
- **Primary target**: Fiction (Novels).

---

## Important Paths
- `novel_writer/main.py`: Main orchestration script managing the novel generation workflow.
- `novel_writer/generators/`: Modular generators for plot, characters, chapters, and scenes.
- `novel_writer/models/`: Data models for stories, characters, chapters, and world settings.
- `novel_writer/settings/`: Model configurations and system settings.
- `novel_writer/studio/`: Web studio UI components.

---

## Workflow
Premise Input 
→ World & Character Model Initialization (`novel_writer/models/`) 
→ Plot Architecture Generation 
→ Scene-by-Scene Generation (`novel_writer/generators/`) 
→ Chapter Assembly 
→ Manuscript Export.

---

## Inputs and Outputs

```text
Stage: Novel Generation
Input: Premise, genre, character archetypes
Process: Sequential execution of plot generator, character generator, and chapter generators
Output: Novel manuscript files
Used by next stage: Export
```

---

## Prompt Inventory

### Prompt: Scene Generation Prompt
- **File**: `novel_writer/generators/`
- **Purpose**: Generates scene prose grounded in character relationships and setting constraints.
- **Required inputs**: Scene beats, active characters, setting description.
- **Expected output**: Scene draft prose.
- **Important constraints**: Maintain consistent narrative point of view.
- **Downstream consumer**: Chapter assembler.

---

## Context / Memory Strategy
Object-oriented data model tracking story state, characters, and chapter metadata in memory and JSON serialization.

---

## Editing Strategy
- **Developmental editing**: Absent.
- **Continuity**: Basic object-model state tracking.
- **Fact checking / Line editing / Copy editing / Proofreading**: Absent.

---

## Export / Assembly Strategy
- **Manuscript source format**: Text / Markdown.
- **Chapter organization**: Python object models serialized to disk.
- **Assembly method**: Python file joiner.
- **Output formats**: Text, Markdown.
- **Scripts/tools required**: Python 3.

---

## Strongest Ideas
1. **Object-Oriented Story Data Models**: Clean Python dataclasses representing Characters, Scenes, Chapters, and World Lore.

---

## Weaknesses
- Limited editorial passes and lack of anti-AI prose suppression.

---

## Reusable Knowledge
- Object-oriented data modeling schema for narrative state management.
"""

# 17. bookgen
reports["bookgen"] = """# Repository Report: bookgen

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
"""

# 18. poison01022-ai-book-pipeline
reports["poison01022-ai-book-pipeline"] = """# Repository Report: poison01022-ai-book-pipeline

## Repository
- **Name**: poison01022-ai-book-pipeline
- **URL**: https://github.com/poison01022/ai-book-pipeline
- **Commit**: `26912309`
- **Status**: SUCCESS
- **Primary purpose**: Experimental reinforcement learning and multi-agent search pipeline for novel generation.
- **Primary target**: Fiction (Experimental Novel Generation).

---

## Important Paths
- `agents/ai_writer.py`: AI writing agent script.
- `agents/ai_reviewer.py`: AI review and evaluation script.
- `agents/human_editor.py`: Human-in-the-loop editorial review interface.
- `rl_search/`: Reinforcement learning and tree-search algorithms for exploring narrative paths.
- `storage/`: Narrative state and vector storage.
- `main.py`: Pipeline entry point.

---

## Workflow
Premise Input 
→ Tree Search Narrative Path Exploration (`rl_search/`) 
→ Drafting (`ai_writer.py`) 
→ Automated Review (`ai_reviewer.py`) 
→ Human-in-the-loop Editorial Gate (`human_editor.py`) 
→ Final Storage (`storage/`).

---

## Inputs and Outputs

```text
Stage: RL Search & Drafting
Input: Premise, narrative branch options
Process: rl_search explores optimal plot paths → ai_writer.py drafts scene
Output: Scene candidate
Used by next stage: Review & Human Gate

Stage: Human-in-the-Loop Review
Input: Drafted scene candidate + AI reviewer score
Process: human_editor.py prompts user for approval or branch modification
Output: Approved scene
Used by next stage: Next branch search
```

---

## Prompt Inventory
- `agents/ai_writer.py`: Drafting prompt template.
- `agents/ai_reviewer.py`: Quality evaluation prompt template.

---

## Context / Memory Strategy
Uses `storage/` for narrative graph and vector memory storage.

---

## Editing Strategy
- **Developmental editing**: Assisted via tree-search plot exploration.
- **Continuity / Line / Copy / Proofreading**: Handled via human-in-the-loop gate (`human_editor.py`).

---

## Export / Assembly Strategy
- **Manuscript source format**: Text / Python storage.
- **Chapter organization**: Graph/tree branches.
- **Assembly method**: Python script.
- **Output formats**: Text.
- **Scripts/tools required**: Python 3.

---

## Strongest Ideas
1. **Reinforcement Learning / Tree-Search Plot Exploration**: Evaluating multiple branching narrative options before committing to prose.
2. **Explicit Human-in-the-Loop Gating**: Formal stopping point requiring human approval before advancing narrative state.

---

## Weaknesses
- Minimalist/experimental codebase with limited prompt engineering depth.

---

## Reusable Knowledge
- Branching plot search concept and Human-in-the-loop checkpointing pattern.
"""

# Write out all individual reports
for repo_name, report_content in reports.items():
    file_path = os.path.join(SUMMARIES_DIR, f"{repo_name}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"Generated summary: {file_path}")

print("All 18 repository reports successfully generated in summaries/")
