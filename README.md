# AI-Assisted eBook Writing & Publishing Framework

[![Public Repository](https://img.shields.io/badge/GitHub-Public-brightgreen)](https://github.com/phamngoanhtu/ebook-writing)
[![Skill Enabled](https://img.shields.io/badge/Agent%20Skill-ebook--writer-blue)](.agents/skills/ebook-writer/SKILL.md)

An end-to-end framework and research corpus for planning, outlining, drafting, continuity tracking, quality-gated editing, and multi-format publishing of fiction and non-fiction eBooks and print manuscripts.

Synthesizes best practices from 18 specialized repositories into an actionable, agentic authoring system.

---

## 🤖 For AI Agents: Activate the `ebook-writer` Skill

If you are an AI Coding / Writing Agent (Antigravity, Claude Code, Cursor, Codex, Gemini):
**You MUST load and follow the master skill instructions in [`.agents/skills/ebook-writer/SKILL.md`](.agents/skills/ebook-writer/SKILL.md).**

### Quick Skill Reference
- **Master Workflow Manual**: [`.agents/skills/ebook-writer/SKILL.md`](.agents/skills/ebook-writer/SKILL.md)
- **12-Section Book Blueprint Specification**: [`.agents/skills/ebook-writer/references/book_blueprint_template.md`](.agents/skills/ebook-writer/references/book_blueprint_template.md)
- **Anti-AI Prose Suppression Rules**: [`.agents/skills/ebook-writer/references/anti_ai_prose_rules.md`](.agents/skills/ebook-writer/references/anti_ai_prose_rules.md)
- **22-Pass Editorial Quality Rubric**: [`.agents/skills/ebook-writer/references/editorial_rubric_22_pass.md`](.agents/skills/ebook-writer/references/editorial_rubric_22_pass.md)
- **Two-Tier Canon & Memory Protocol**: [`.agents/skills/ebook-writer/references/canon_mutation_protocol.md`](.agents/skills/ebook-writer/references/canon_mutation_protocol.md)
- **Amazon KDP Metadata & Publishing Checklist**: [`.agents/skills/ebook-writer/references/kdp_publishing_checklist.md`](.agents/skills/ebook-writer/references/kdp_publishing_checklist.md)

---

## 📚 Core Framework Pillars

1. **Fractal Scene Architecture**: Every scene must complete a formal circuit of change: Goal → Conflict → Disaster (Action) and Reaction → Dilemma → Decision (Sequel).
2. **Two-Tier Persistent Memory**: Separates immutable world rules (`MEMORY.md`) from incremental session handoffs (`CHANGELOG_AI.md`) to prevent mid-book continuity amnesia.
3. **Anti-AI Prose Suppression**: Actively eradicates overused AI vocabulary (*"delve"*, *"tapestry"*, *"beacon"*, *"testament"*), syntactic symmetry, and moralizing conclusions.
4. **Mathematical Word Budgeting**: Cascades total book word count targets downward to chapters, outline items, and chunk drafting prompts.
5. **22-Pass Editorial Quality Gates**: Rigorous multi-pass review covering plot structure, pacing heatmaps, character arcs, dialogue surgery, and line-level cadence.
6. **Multi-Format Publication**: Out-of-the-box manifests for Pandoc (EPUB/PDF), LaTeX (`pdflatex` with SVG/tables), and Python DOCX generation.

---

## 📂 Repository Structure

```text
.
├── README.md                                    # Root repository overview & agent entry point
├── .agents/
│   └── skills/
│       └── ebook-writer/                        # Master executable Skill for AI agents
│           ├── SKILL.md                         # Main workflow instructions & execution guide
│           ├── references/                      # Reference guides (Anti-AI, Blueprint, Editorial, Canon, KDP)
│           └── templates/                       # Manifest and state templates
│
└── book-writing-research/                       # Extracted research corpus from 18 repositories
    ├── summaries/                               # 18 deep-dive repository reports
    ├── knowledge/                               # Synthesized knowledge base, design patterns & handoff
    │   ├── book-writing-knowledge-base.md       # 20 Capability taxonomy sections
    │   ├── design-patterns.md                   # Architectural design patterns (A through F)
    │   ├── prompt-patterns.md                   # 8 Reusable prompt formulas
    │   └── HANDOFF.md                           # Research handoff documentation
    ├── matrices/                                # Cross-repository capability matrix
    │   └── repository-capability-matrix.md
    └── evidence/                                # Provenance manifest of all analyzed repositories
        └── repository-manifest.md
```

---

## 🚀 How to Start Writing an eBook

1. **Initialize the Project**:
   Create your project directory using the layout in `templates/manifest.md`.
2. **Generate the Master Blueprint**:
   Execute Phase 2 from [SKILL.md](.agents/skills/ebook-writer/SKILL.md) to generate `BOOK_BLUEPRINT.md`.
3. **Draft with Triple-Anchor Context**:
   Draft chapters using Macro Worldview + Rolling Recent Summary (`CHANGELOG_AI.md`) + Chapter Beat Plan.
4. **Run Quality Gates & Prose Sanitization**:
   Audit text against [anti_ai_prose_rules.md](.agents/skills/ebook-writer/references/anti_ai_prose_rules.md) and log exit states in `CHANGELOG_AI.md`.
5. **Compile & Publish**:
   Assemble chapters via Pandoc or LaTeX and format KDP sales copy using [kdp_publishing_checklist.md](.agents/skills/ebook-writer/references/kdp_publishing_checklist.md).

---

## 📜 License

MIT License. Feel free to adapt and use for commercial and personal book authoring.
