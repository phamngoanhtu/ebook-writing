# Prompt Patterns in Long-Form Book Writing

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
