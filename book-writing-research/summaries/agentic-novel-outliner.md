# Repository Report: agentic-novel-outliner

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
