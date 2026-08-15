import os

BASE_DIR = "/Users/tupham/Personal/.personal/Ernest/research/ebook-writing/book-writing-research"
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")

# 1. Design Patterns
design_patterns = """# Design Patterns in AI-Assisted Book Writing

A comparative analysis of the primary architectural design patterns discovered across the research corpus.

---

## Pattern A — Single Master Prompt / Monolithic Generation

### Description
A single extensive prompt attempts to instruct the LLM to conceive, outline, draft, and assemble an entire book or large multi-chapter section in one or two generation passes.

### Advantages
- Minimal workflow complexity; no intermediate pipeline state to manage.
- Fast execution for very short lead magnets or pamphlets (under 5,000 words).
- Zero orchestration code required.

### Disadvantages
- **Severe Context Exhaustion**: Models compress plot details, skip scenes, and summarize rather than write immersive prose.
- **Syntactic & Narrative Degeneration**: Tone flattens; later chapters become rushed and generic.
- **Zero Quality Gating**: No opportunity for structural critique, continuity checking, or line editing between chapters.

### Observed Repositories
- `AI-Prompts-for-E-book-Generation` (`README.md`)
- `KDP-Publishing-Prompt-Library` (`kdp-chapter-writing-prompt.md`)

---

## Pattern B — Sequential Prompt Pipeline (Waterfall)

### Description
A linear multi-step pipeline where the output of each stage directly forms the input to the next:
`Idea → Audience → Outline → Chapter Planning → Chapter Drafting → Post-Draft Edit → Assembly`

### Advantages
- Clear structural progression and cognitive separation of planning vs drafting.
- Easy to automate via simple scripts or CLI commands.
- Predictable execution flow with clear milestone artifacts.

### Disadvantages
- **Rigid Error Propagation**: An early flaw in the outline cascades into all downstream chapter drafts unless caught manually.
- **Context Drift**: Downstream stages may lose sight of macro themes unless explicitly re-injected.

### Observed Repositories
- `boekwriter` (`write_book.py`, `queries.yaml`)
- `LLM-book-generator` (`book_generator/orchestrator.py`)
- `libriscribe` (`src/`, `prompts/templates/`)

---

## Pattern C — Specialized Multi-Agent System (Role-Based Team)

### Description
Work is partitioned across specialized agent personas with distinct responsibilities and perspectives (e.g. Lead Architect, Scene Crafter, Dialogue Surgeon, Continuity Auditor, Critic, Proofreader).

```text
┌──────────────────────────────────────────────────────────┐
│                   Lead Orchestrator                      │
└────────┬─────────────────┬───────────────────┬───────────┘
         ▼                 ▼                   ▼
   ┌───────────┐    ┌─────────────┐     ┌──────────────┐
   │Researcher │    │Writer/Crafter│     │   Critic     │
   └───────────┘    └──────┬──────┘     └──────▲───────┘
                           │                   │
                           ▼                   │ (Iterative Feedback)
                    ┌──────────────┐           │
                    │    Editor    ├───────────┘
                    └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │ Proofreader  │
                    └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │  Publisher   │
                    └──────────────┘
```

### Advantages
- **Cognitive Depth & Role Fidelity**: Agents with narrow personas produce much sharper, less generic feedback (e.g., a Dialogue Surgeon focused only on subtext catches nuances a general writer misses).
- **Adversarial Quality Control**: The Critic/Editor role holds the Writer accountable to objective scoring rubrics.
- **Modularity**: Individual agents can be swapped, tuned, or assigned different LLM models.

### Disadvantages
- High token consumption and orchestration overhead.
- Potential for endless revision loops if convergence criteria are not strictly bounded.

### Observed Repositories
- `ai-book-pipeline` (`engine/agents/*.md`)
- `novel-template` (`.claude/agents/*.md`)
- `writing-template-for-ai` (`.ai/agents/*.md`)

---

## Pattern D — Persistent Project-Memory Architecture (Bibles & Canon)

### Description
The system decouples static and dynamic knowledge into persistent filesystem or database artifacts:
- **Immutable/Durable Canon**: World rules, magic/tech constraints, historical timeline, fixed character traits (`MEMORY.md`, `constitution.md`, `story_bible.md`).
- **Dynamic Entity State**: Character knowledge boundaries, current physical locations, item inventories, emotional wounds (`character_state.md`, `Dual-Clue Ledger`).

### Advantages
- Prevents mid-manuscript continuity decay and "hallucinated retcons".
- Enables new agent sessions or human collaborators to pick up immediately with zero knowledge loss.
- Allows strict canon mutation control (agents cannot alter established facts without explicit authorization).

### Disadvantages
- Requires rigorous state-updating discipline after every drafted scene.
- Memory files can grow large and must be structured for rapid contextual retrieval.

### Observed Repositories
- `writing-template-for-ai` (`MEMORY.md`, `BOOK_BLUEPRINT.md §8`, `.ai/rules/canon-mutation-control.md`)
- `speckit-preset-fiction-book-writing` (`constitution.md`, `speckit.continuity.md`)
- `novel-template` (`characters/*.md`, `world/*.md`)

---

## Pattern E — Rolling-Summary / Context-Compression Architecture

### Description
Maintains long-range continuity across multi-chapter manuscripts by passing a compressed sliding window of recent narrative context:
- **Macro Anchor**: Book premise + overall chapter roadmap.
- **Micro Anchor**: Detailed outline of current chapter.
- **Rolling Bridge**: 1–2 paragraph summaries of the preceding 2–3 chapters + explicit entry state.

```text
[Macro Premise + Worldview]
          +
[Rolling Summary: Ch (N-2) + Ch (N-1)]
          +
[Current Chapter Plan: Ch N (Entry State → Beats → Exit State)]
          ↓
[LLM Drafting Engine]
          ↓
[Chapter N Draft] → [Auto-Summarizer] → Updates [Rolling Summary Buffer]
```

### Advantages
- Fits cleanly inside standard LLM context windows without token bloat.
- Guarantees smooth chapter-to-chapter transitions and immediate plot momentum.
- Highly scalable to 50+ chapter books.

### Disadvantages
- Very subtle background subplots or distant foreshadowing can be dropped from the rolling summary unless tracked in a separate ledger.

### Observed Repositories
- `AI_Novel` (`app/prompts/templates.py`, `app/services/`)
- `writing-template-for-ai` (`CHANGELOG_AI.md`)
- `LLM-book-generator` (`book_generator/common_generator.py`)
- `boekwriter` (`queries.yaml: chunk` via `${parent_chunk}`)

---

## Pattern F — Human-in-the-Loop (HITL) Authoring & Quality Gating

### Description
The AI operates as a tireless co-author and diagnostic tool, but pauses at formal checkpoints to require human approval, steering, or branch selection before advancing the narrative.

### Advantages
- Maximum creative alignment with authorial intent.
- Eliminates runaway AI hallucinations or generic plot drift before significant compute is wasted.
- Keeps the author in total control of sensitive themes, voice choices, and publication decisions.

### Disadvantages
- Cannot run fully autonomously unattended; requires human availability.

### Observed Repositories
- `poison01022-ai-book-pipeline` (`agents/human_editor.py`)
- `bookgen` (`BOOKOPS_WORKFLOW.md`, `RUNBOOK.md`)
- `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.feedback.md`)
- `The-Novelists-Atelier` (`novelist-atelier-prompts.md`)
"""

# 2. Prompt Patterns
prompt_patterns = """# Prompt Patterns in Long-Form Book Writing

A structured catalog of reusable prompt design patterns extracted from the analyzed repositories.

---

## Pattern 1: Role + Objective + Context + Constraints + Output Schema

- **Problem Solved**: Unstructured, drifting, or generic LLM responses that fail to integrate into downstream pipeline steps.
- **Observed In**:
  - `writing-template-for-ai` (`book_generator_prompt.md`)
  - `boekwriter` (`queries.yaml`)
  - `libriscribe` (`prompts/templates/chapter_writer.yml`)
- **Inputs**: Persona definition, specific task goal, reference documents, negative constraints (what NOT to do), JSON/Markdown output schema.
- **Outputs**: Formatted, deterministic artifacts strictly conforming to downstream parsing requirements.
- **Why Useful**: Enforces predictable structure and prevents the LLM from hallucinating conversational filler.
- **Risks**: Over-constraining can sometimes restrict creative prose flair if schema is too rigid.

---

## Pattern 2: Current Chapter + Global Outline + Previous Chapter Summary (Anchor Sandwich)

- **Problem Solved**: Chapter-level amnesia and lack of narrative momentum in long-form generation.
- **Observed In**:
  - `AI_Novel` (`app/prompts/templates.py: novel`)
  - `LLM-book-generator` (`book_generator/fiction_generator.py`)
  - `boekwriter` (`queries.yaml: chunk`)
- **Inputs**: Macro book outline, 1-paragraph summary of immediately preceding chapter(s), current chapter beat sheet.
- **Outputs**: Chapter draft that naturally picks up unresolved physical/emotional threads and moves directly toward the next milestone.
- **Why Useful**: Creates seamless chapter transitions without requiring the entire manuscript in the prompt context.
- **Risks**: Repetition of phrases across chapter boundaries if the previous summary is too detailed.

---

## Pattern 3: Story Bible + Active Scene + Continuity Requirements

- **Problem Solved**: Characters acting out of character, using forbidden knowledge, or violating physical world rules.
- **Observed In**:
  - `writing-template-for-ai` (`.ai/rules/canon-mutation-control.md`)
  - `novel-template` (`.claude/agents/continuity-keeper.md`)
  - `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.continuity.md`)
- **Inputs**: Immutable world rules, character knowledge state, scene objective, active inventory/location facts.
- **Outputs**: Scene prose that respects all established constraints and flags any required canon mutations.
- **Why Useful**: Prevents continuity drift across long generation runs.
- **Risks**: High token overhead if the story bible is not filtered to scene-relevant facts.

---

## Pattern 4: Draft → Critic Scorecard → Targeted Revision Loop

- **Problem Solved**: Mediocre first-draft quality and lack of self-correction in raw LLM outputs.
- **Observed In**:
  - `ai-book-pipeline` (`engine/agents/critic.md` & `editor.md`)
  - `writing-template-for-ai` (`.ai/agents/marketing-narrative-consistency-auditor.md`)
- **Inputs**: Raw draft text, multi-dimensional scoring rubric (Voice, Pacing, Conflict, Dialogue, Subtext).
- **Outputs**: Numerical scorecard + line-item revision directives → revised chapter text.
- **Why Useful**: Mimics professional developmental editing by forcing the model to evaluate before rewriting.
- **Risks**: Risk of circular oscillation if scoring thresholds are unrealistically high.

---

## Pattern 5: Research Dossier → Evidence Summary → Chapter Synthesis

- **Problem Solved**: Hallucinated facts, shallow explanations, or unsourced claims in non-fiction and historical fiction.
- **Observed In**:
  - `ai-book-pipeline` (`engine/agents/researcher.md`)
  - `libriscribe` (`prompts/templates/researcher.yml`)
  - `bookgen` (`ideation/`)
- **Inputs**: Topic query, domain documentation, reference material.
- **Outputs**: Structured research brief (Key concepts, Verified facts, Case studies, Citations) passed directly to the chapter writer.
- **Why Useful**: Grounds non-fiction arguments in empirical evidence and structured pedagogy.
- **Risks**: Tendency for the writer to summarize the research dossier as an academic list rather than narrative prose.

---

## Pattern 6: Multi-Tier Editorial Hierarchy (Developmental before Line/Copy)

- **Problem Solved**: Wasting time polishing sentences in scenes that should be structurally cut or relocated.
- **Observed In**:
  - `The-Novelists-Atelier` (`novelist-atelier-prompts.md`)
  - `writing-template-for-ai` (`.ai/rules/editorial-pass.md`)
- **Inputs**: Draft manuscript.
- **Outputs**: Tier 1 (Macro structure, plot integrity, character arcs) → Tier 2 (Scene rhythm, dialogue subtext) → Tier 3 (Prose cadence, copy-editing, proofreading).
- **Why Useful**: Ensures editorial effort aligns with professional publishing workflow sequences.
- **Risks**: Requires multi-pass workflow execution.

---

## Pattern 7: Explicit Anti-AI Prose Suppression Filter

- **Problem Solved**: Recognizable, repetitive AI writing patterns ("delve", "tapestry", "beacon", "testament", excessive symmetry, moralizing conclusions).
- **Observed In**:
  - `writing-template-for-ai` (`.ai/agents/writing-prose-suppression.md`)
  - `The-Novelists-Atelier` (`novelist-atelier-prompts.md §14`)
  - `bookgen` (`STYLE_GUIDE.md`)
- **Inputs**: Draft chapter prose.
- **Outputs**: Sanitized, natural human-like prose with banned tropes replaced by organic phrasing and varied syntax.
- **Why Useful**: Elevates manuscript quality from "obviously AI-generated" to indistinguishable from professional human authors.
- **Risks**: Overly aggressive filtering might flag legitimate technical vocabulary.

---

## Pattern 8: Mathematical Word-Budget Allocation Cascade

- **Problem Solved**: Wildly unpredictable chapter lengths, bloated middles, or abrupt endings.
- **Observed In**:
  - `boekwriter` (`queries.yaml: chapters`, `chapter-outline`, `chunk`)
  - `writing-template-for-ai` (`BOOK_BLUEPRINT.md §2`)
- **Inputs**: Total manuscript target (e.g. 50,000 words), number of chapters, number of outline points per chapter.
- **Outputs**: Strict min/max word budget constraints allocated to every individual chunk generation prompt.
- **Why Useful**: Produces manuscripts with balanced pacing and predictable chapter scale.
- **Risks**: Can cause unnatural text trimming if the LLM struggles to meet exact bounds.
"""

with open(os.path.join(KNOWLEDGE_DIR, "design-patterns.md"), "w", encoding="utf-8") as f:
    f.write(design_patterns)

with open(os.path.join(KNOWLEDGE_DIR, "prompt-patterns.md"), "w", encoding="utf-8") as f:
    f.write(prompt_patterns)

print("Generated design-patterns.md and prompt-patterns.md.")
