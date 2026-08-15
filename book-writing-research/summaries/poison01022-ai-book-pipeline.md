# Repository Report: poison01022-ai-book-pipeline

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
