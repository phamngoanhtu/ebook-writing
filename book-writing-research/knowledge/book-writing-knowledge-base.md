# Comprehensive Book Writing & Publishing Knowledge Base

A synthesized, capability-driven knowledge base extracted and normalized from 18 specialized repositories. Every technique is traceable to its verified source repository and commit.

---

## 1. Book Ideation

### Core Methods & Workflows
- **Commercial Niche & Demand Extraction**: Systematic brainstorming of high-demand / low-competition topic angles based on Amazon search volume and buyer problem urgency.
  - *Source*: `KDP-Publishing-Prompt-Library` (`kdp-book-idea-generator.md`, commit `45063f4a`)
- **Executive Premise Synthesis**: Structuring ideas into three escalating tiers: One-sentence logline, One-paragraph commercial hook, and Back-cover positioning copy.
  - *Source*: `writing-template-for-ai` (`book_generator_prompt.md` §1, commit `b28fd189`)
- **Theme-First Ideation**: Deriving the dramatic premise and title directly from a central philosophical question or dilemma.
  - *Source*: `bookwiz-ai-prompts` (`text/theme.txt`, `text/title.txt`, commit `45bbdf4e`)
- **Repurposing Existing Content**: Consolidating dispersed blog posts, articles, or webinar transcripts into a unified book concept.
  - *Source*: `AI-Prompts-for-E-book-Generation` (`README.md` Prompt #5, commit `c8f18c34`)
- **Interactive Premise Pressure-Testing**: AI-guided interview eliciting unique angles, genre mashups, and reader value propositions before outlining begins.
  - *Source*: `novel-template` (`.claude/agents/idea-excavator.md`, commit `714f4673`)

---

## 2. Audience and Positioning

### Core Methods & Workflows
- **Reader Experience Design (RED)**: Explicitly mapping what the reader must feel in the first 10 pages, understand by 25%, experience at the midpoint turn, and remember after finishing.
  - *Source*: `writing-template-for-ai` (`BOOK_BLUEPRINT.md` §3, commit `b28fd189`)
- **Avatar Pain-Point & Transformation Mapping**: Defining the target reader's current entry state (struggles, frustrations) vs desired exit state (transformation, mastery, emotional release).
  - *Source*: `bookgen` (`ideation/`, `BOOKOPS_WORKFLOW.md`, commit `a4578467`)
- **Amazon Commercial Category & Backend Metadata**: Selecting 3 niche Amazon BISAC categories and generating 7 high-intent backend keyword strings.
  - *Source*: `KDP-Publishing-Prompt-Library` (`kdp-keyword-research-prompt.md`, commit `45063f4a`)
- **Comparable Titles & Market Differentiation**: Documenting 3 comparable titles (comp titles) and stating explicitly how this manuscript differs.
  - *Source*: `writing-template-for-ai` (`book_generator_prompt.md` §1, commit `b28fd189`)

---

## 3. Research & Factual Grounding

### Core Methods & Workflows
- **Structured Research Dossiers**: Upfront gathering of verified domain facts, historical timelines, and case studies before chapter drafting.
  - *Source*: `ai-book-pipeline` (`engine/agents/researcher.md`, commit `10fd3224`)
- **Fiction vs Non-Fiction Grounding**:
  - *Non-Fiction*: Extracting empirical data, statistical evidence, and pedagogical case studies (`boekwriter` `queries.yaml`, commit `4c4abd45`).
  - *Fiction*: Period-accurate terminology, physical spatial logic, weapon/technology specifications (`libriscribe` `prompts/templates/researcher.yml`, commit `c4c6ac7f`).
- **Internal Fact & Lore Validation**: Automated fact-checker scanning chapter drafts against research dossiers to prevent hallucinated contradictions.
  - *Source*: `libriscribe` (`prompts/templates/fact_checker.yml`, commit `c4c6ac7f`)

---

## 4. World Building (Fiction)

### Core Methods & Workflows
- **Modular World Dossiers**: Clean filesystem partitioning into `locations.md`, `rules.md`, `factions.md`, `technology.md`, and `magic.md`.
  - *Source*: `novel-template` (`world/*.md`, commit `714f4673`)
- **Narrative Constitution**: Formally defining the immutable laws of the universe, magic costs, technology limits, and social structures.
  - *Source*: `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.constitution.md`, commit `4764c888`)
- **Sensory World-Building**: Prompting for acoustic, olfactory, and tactile environmental textures rather than static visual descriptions.
  - *Source*: `The-Novelists-Atelier` (`novelist-atelier-prompts.md` §7 & §8, commit `e0056002`)

---

## 5. Character Design

### Core Methods & Workflows
- **Conscious Want vs Unconscious Need**: Defining character internal lack, fatal flaw, ghost/wound, and transformational arc.
  - *Source*: `writing-template-for-ai` (`book_generator_prompt.md` §5, commit `b28fd189`)
- **Character Hierarchy & Scene Oxygen Distribution**: Enforcing principal character dominance and preventing background characters from hijacking scenes.
  - *Source*: `writing-template-for-ai` (`.ai/agents/writing-character-hierarchy.md`, commit `b28fd189`)
- **Dynamic Character Knowledge & State Tracking**: Real-time logging of what secrets a character knows, their active inventory, physical injuries, and emotional status per chapter.
  - *Source*: `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.continuity.md`, commit `4764c888`)
- **Acoustic Voice Fingerprinting**: Specifying unique dialogue syntax, vocabulary patterns, pacing, and conversational avoidance traits per character.
  - *Source*: `novel-template` (`.claude/agents/dialogue-surgeon.md`, commit `714f4673`)

---

## 6. Book Architecture

### Core Methods & Workflows
- **Macro 12-Section Blueprint**: Formal architecture encompassing Executive Concept, Target Length, Reader Experience, Macro Structure, Character System, Chapter Plans, Style Guide, Dual-Clue Ledger, Production Assumptions, Quality Gates, Risk Review, and Drafting Instructions.
  - *Source*: `writing-template-for-ai` (`BOOK_BLUEPRINT.md`, commit `b28fd189`)
- **Classical Narrative Pattern Frameworks**: Embedding proven storytelling engines (Save the Cat, Hero's Journey, 7-Point Story Structure, Dan Harmon Story Circle).
  - *Source*: `novel-template` (`patterns/*.md`, commit `714f4673`)
- **Thesis-Driven Non-Fiction Progression**: Structuring non-fiction as: Problem Agitation → Core Paradigm Shift → Pedagogical Framework → Case Studies → Action Steps → Synthesis.
  - *Source*: `bookgen` (`BOOKOPS_WORKFLOW.md`, commit `a4578467`)

---

## 7. Outline Generation

### Core Methods & Workflows
- **Hierarchical 3-Tier Outlining**:
  - Tier 1: Macro Act / Section Milestones
  - Tier 2: Chapter Breakdown with Core Dramatic Purpose
  - Tier 3: Scene-by-Scene Beat Sheets
  - *Source*: `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.outline.md`, commit `4764c888`)
- **Word-Budgeted Chapter Outlining**: Assigning explicit mathematical word budgets to each chapter and outline item.
  - *Source*: `boekwriter` (`queries.yaml: chapters`, commit `4c4abd45`)
- **Format-Specific Outlining Engines**: Separate outlining logic for Fiction, Non-Fiction, Children's Books, and Short Stories.
  - *Source*: `agentic-novel-outliner` (`src/agents/`, commit `c56ec398`)

---

## 8. Chapter Planning

### Core Methods & Workflows
- **Entry State → Circuit of Change → Exit State**: Defining what characters know and feel when entering the chapter vs what permanently shifts by the end.
  - *Source*: `writing-template-for-ai` (`book_generator_prompt.md` §6, commit `b28fd189`)
- **Pedagogical Item Breakdown**: Planning non-fiction chapters as discrete 1-sentence learning objectives with assigned word budgets and planned visual aids (tables/diagrams).
  - *Source*: `boekwriter` (`queries.yaml: chapter-outline`, commit `4c4abd45`)
- **Dual-Surface Mystery Planning**: Planning surface events vs deeper clue placement for mystery/thriller chapters.
  - *Source*: `writing-template-for-ai` (`BOOK_BLUEPRINT.md` §8, commit `b28fd189`)

---

## 9. Chapter Drafting

### Core Methods & Workflows
- **Fractal Scene Architecture**: Structuring every scene around a complete circuit: Goal → Conflict → Disaster (Action) followed by Reaction → Dilemma → Decision (Sequel).
  - *Source*: `writing-template-for-ai` (`.ai/agents/writing-fractal-scene-architect.md`, commit `b28fd189`)
- **Sequential Chunk Drafting with Parent Anchor**: Ingesting the immediately preceding text chunk (`${parent_chunk}`) to ensure seamless continuity during technical/academic drafting.
  - *Source*: `boekwriter` (`queries.yaml: chunk`, commit `4c4abd45`)
- **Genre-Specific Style Directives**: Injecting commercial pacing constraints (e.g. webnovel 200-word hook + cliffhanger, hard sci-fi mathematical consistency, romance emotional tension).
  - *Source*: `AI_Novel` (`app/prompts/templates.py: template_instructions`, commit `1cd51473`)
- **Anti-AI Prose Suppression at Generation Time**: Banning generic tropes ("delve", "tapestry", "shivers down spine") during the drafting prompt.
  - *Source*: `writing-template-for-ai` (`.ai/agents/writing-prose-suppression.md`, commit `b28fd189`)

---

## 10. Long-Context and Continuity Management

### Core Methods & Workflows
- **Two-Tier Memory Architecture (`MEMORY.md` + `CHANGELOG_AI.md`)**:
  - *Tier 1 (`MEMORY.md`)*: Immutable canon, durable facts, world rules.
  - *Tier 2 (`CHANGELOG_AI.md`)*: Session handoff log recording entry state, exit state, quality gate results, open threads, and next steps.
  - *Source*: `writing-template-for-ai` (`MEMORY.md`, `CHANGELOG_AI.md`, commit `b28fd189`)
- **Canon Mutation Control Protocol**: Strict governance preventing the AI from changing established character rules, geography, or past events without an explicit authorized canon patch.
  - *Source*: `writing-template-for-ai` (`.ai/rules/canon-mutation-control.md`, commit `b28fd189`)
- **Rolling Recent-Chapter Context Window**: Passing a 2-chapter sliding summary buffer forward to each new generation step.
  - *Source*: `AI_Novel` (`app/prompts/templates.py`, commit `1cd51473`)
- **Multi-Factor Continuity Audit**: Cross-checking draft text against Timeline, Character Knowledge, Object Locations, and World Rules.
  - *Source*: `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.continuity.md`, commit `4764c888`)

---

## 11. Developmental Editing

### Core Methods & Workflows
- **22-Pass Full Manuscript Editorial Audit**: Comprehensive evaluation of Plot Structure, Pacing, Character Arcs, Theme, World Continuity, Stakes Escalation, Subplots, and Dialogue Integrity, outputting an HTML/PDF scorecard.
  - *Source*: `The-Novelists-Atelier` (`novelist-atelier-prompts.md` §1, commit `e0056002`)
- **Three-Act Dramatic Tension Curve Analysis**: Verifying inciting incident placement, midpoint reversal strength, and climax escalation.
  - *Source*: `novel-template` (`.claude/agents/developmental-editor.md`, commit `714f4673`)
- **Scored Critic-Feedback Loop**: Formal 5-factor scoring (Voice, Pacing, Conflict, Dialogue, Coherence) driving targeted structural rewrites.
  - *Source*: `ai-book-pipeline` (`engine/agents/critic.md`, commit `10fd3224`)

---

## 12. Chapter-Level Editing

### Core Methods & Workflows
- **Pacing Heatmap Table**: Tabulating Chapter | Tension (1–10) | Pacing Rating | Scene Types | Energy Level to identify narrative valleys.
  - *Source*: `The-Novelists-Atelier` (`novelist-atelier-prompts.md` §10, commit `e0056002`)
- **Scene Goal & Exit State Validation**: Checking whether every scene achieves its dramatic objective and moves the overall story forward.
  - *Source*: `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.pacing.md`, commit `4764c888`)
- **Dialogue Surgery**: Stripping out conversational pleasantries and on-the-nose exposition to maximize subtext and vocal differentiation.
  - *Source*: `novel-template` (`.claude/agents/dialogue-surgeon.md`, commit `714f4673`)

---

## 13. Line Editing

### Core Methods & Workflows
- **Prose Cadence & Sentence Variety**: Eliminating monotonous subject-verb-object structures and balancing sentence lengths.
  - *Source*: `The-Novelists-Atelier` (`novelist-atelier-prompts.md` §5 & §12, commit `e0056002`)
- **Semantic Gradient & Word Choice**: Replacing vague modifiers with precise, evocative verbs and sensory nouns.
  - *Source*: `writing-template-for-ai` (`.ai/agents/writing-semantic-gradient.md`, commit `b28fd189`)
- **Tightening & Wordiness Reduction**: Trimming 15–20% of deadwood prose without sacrificing authorial voice.
  - *Source*: `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.polish.md`, commit `4764c888`)

---

## 14. Copy Editing

### Core Methods & Workflows
- **Terminology & Capitalization Consistency**: Enforcing global project rules for fantasy/sci-fi terms, technical concepts, and character names.
  - *Source*: `speckit-preset-fiction-book-writing` (`fiction-book-writing/commands/speckit.glossary.md`, commit `4764c888`)
- **Grammar, Punctuation, and Syntax Auditing**: Dedicated line-item correction of comma splices, dangling modifiers, and tense drift.
  - *Source*: `ai-book-pipeline` (`engine/agents/proofreader.md`, commit `10fd3224`)
- **Style Guide Rule Enforcement**: Checking prose against formal style constraints (`STYLE_GUIDE.md`).
  - *Source*: `bookgen` (`STYLE_GUIDE.md`, commit `a4578467`)

---

## 15. Proofreading

### Core Methods & Workflows
- **Post-Revision Proofreading Lock**: Executing a final sanity check strictly after all developmental and line edits are frozen.
  - *Source*: `writing-template-for-ai` (`.ai/rules/editorial-pass.md`, commit `b28fd189`)
- **Pre-Publishing Verification Checklist**: Multi-item inspection (TOC links, header formatting, page breaks, front/back matter presence).
  - *Source*: `AI-Prompts-for-E-book-Generation` (`README.md` Prompt #10, commit `c8f18c34`)

---

## 16. Manuscript-Level Coherence

### Core Methods & Workflows
- **Dual-Clue & Subplot Resolution Audit**: Verifying that every planted clue, mystery, and minor character arc is cleanly resolved or deliberately kept open.
  - *Source*: `writing-template-for-ai` (`BOOK_BLUEPRINT.md` §8, commit `b28fd189`)
- **Timeline & Chronology Scan**: Ensuring story days, dates, travel times, and seasons match across all chapters.
  - *Source*: `The-Novelists-Atelier` (`novelist-atelier-prompts.md` Pass 5, commit `e0056002`)
- **Character Arc Completeness Audit**: Mapping each character's journey from opening chapter to climax to ensure transformation is earned.
  - *Source*: `The-Novelists-Atelier` (`novelist-atelier-prompts.md` Pass 3, commit `e0056002`)

---

## 17. Introduction and Conclusion

### Core Methods & Workflows
- **The First 10 Pages Hook**: Establishing protagonist empathy, active dilemma, and atmospheric tone within the opening pages.
  - *Source*: `writing-template-for-ai` (`BOOK_BLUEPRINT.md` §3, commit `b28fd189`)
- **Non-Fiction Opening Promise**: Clearly stating what skills or insights the reader will acquire and why previous approaches failed.
  - *Source*: `AI-Prompts-for-E-book-Generation` (`README.md`, commit `c8f18c34`)
- **Closing Emotional Synthesis & Call to Action**: Crafting memorable thematic resonance for fiction or actionable next steps for non-fiction.
  - *Source*: `bookgen` (`BOOKOPS_WORKFLOW.md`, commit `a4578467`)

---

## 18. Front and Back Matter

### Core Methods & Workflows
- **Front Matter Architecture**: Title page, Copyright notice, Dedication, Epigraph, Table of Contents, Foreword/Preface.
  - *Source*: `writing-template-for-ai` (`BOOK_BLUEPRINT.md` §9, commit `b28fd189`)
- **Back Matter & Funnel Marketing**: Acknowledgments, Author Bio, Readers' Discussion Guide, Lead Magnet CTA, Backend Upsells.
  - *Source*: `bookgen` (`monetization/`, `marketing/`, commit `a4578467`)
- **Technical Front Matter & Visual Headpieces**: Automated chapter headpiece illustrations and LaTeX `booktabs` environments.
  - *Source*: `boekwriter` (`template.tex`, `queries.yaml: headpiece`, commit `4c4abd45`)

---

## 19. Markdown Manuscript Architecture

### Core Methods & Workflows
- **Standardized Directory Architecture**:
  ```text
  project-root/
  ├── BOOK_BLUEPRINT.md
  ├── MEMORY.md
  ├── CHANGELOG_AI.md
  ├── manuscript/
  │   ├── manifest.md
  │   └── chapters/
  │       ├── ch01.md
  │       ├── ch02.md
  │       └── ...
  ├── characters/
  ├── world/
  ├── research/
  ├── build/
  └── scripts/
      └── build.sh
  ```
  - *Source*: `writing-template-for-ai` (`manuscript/manifest.md`, commit `b28fd189`) and `novel-template` (commit `714f4673`)

---

## 20. Publishing and Export

### Core Methods & Workflows
- **Pandoc Multi-Format Compilation**: Shell-scripted assembly of Markdown chapters into EPUB, PDF (via LaTeX engine), and HTML.
  - *Source*: `writing-template-for-ai` (`scripts/build.sh`, commit `b28fd189`)
- **Direct LaTeX Compilation with SVG Diagrams**: Python orchestrator assembling LaTeX source with embedded SVG figures and compiling via `pdflatex`.
  - *Source*: `boekwriter` (`write_book.py`, `template.tex`, commit `4c4abd45`)
- **Automated DOCX Document Assembly**: Python `python-docx` builder applying custom styles, running headers, margins, and page breaks.
  - *Source*: `LLM-book-generator` (`book_generator/docx_builder.py`, commit `a87646e6`)
- **KDP-Ready Package Generation**: Makefile targets compiling print interior PDF, Kindle EPUB, and Amazon metadata packages.
  - *Source*: `bookgen` (`Makefile`, `bookops.py`, commit `a4578467`)
