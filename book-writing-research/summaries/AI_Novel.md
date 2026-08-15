# Repository Report: AI_Novel

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
