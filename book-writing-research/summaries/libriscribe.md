# Repository Report: libriscribe

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
