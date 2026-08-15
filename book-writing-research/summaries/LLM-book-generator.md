# Repository Report: LLM-book-generator

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
