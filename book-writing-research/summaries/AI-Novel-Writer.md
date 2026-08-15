# Repository Report: AI-Novel-Writer

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
