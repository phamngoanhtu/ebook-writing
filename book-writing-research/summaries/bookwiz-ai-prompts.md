# Repository Report: bookwiz-ai-prompts

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
