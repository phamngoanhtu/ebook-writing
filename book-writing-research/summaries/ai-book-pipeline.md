# Repository Report: ai-book-pipeline

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
