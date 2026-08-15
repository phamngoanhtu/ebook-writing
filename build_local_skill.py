import os

SKILL_DIR = "/Users/tupham/Personal/.personal/Ernest/research/ebook-writing/.agents/skills/ebook-writer"
REF_DIR = os.path.join(SKILL_DIR, "references")
TPL_DIR = os.path.join(SKILL_DIR, "templates")

os.makedirs(REF_DIR, exist_ok=True)
os.makedirs(TPL_DIR, exist_ok=True)

# 1. SKILL.md
skill_md = """---
name: ebook-writer
description: >-
  Comprehensive end-to-end framework for authoring, planning, outlining, drafting,
  editing, continuity tracking, quality gating, and publishing high-quality fiction
  and non-fiction eBooks and print manuscripts. Synthesizes fractal scene architecture,
  anti-AI prose suppression, two-tier persistent memory, 22-pass editorial analysis,
  mathematical word budgeting, and multi-format publication (EPUB/PDF/DOCX).
---

# E-Book Writer Skill (Master Workflow Framework)

This skill equips the agent with a production-grade, end-to-end system for writing and publishing commercial and literary eBooks. It synthesizes proven design patterns from 18 specialized repositories into an actionable, multi-stage authoring engine.

---

## Core Principles & Non-Negotiables

1. **Architecture Before Prose**: Never write chapter prose without a validated 12-section `BOOK_BLUEPRINT.md` and chapter-level beat sheets.
2. **Two-Tier State Management**: Maintain absolute continuity via `MEMORY.md` (durable canon & world rules) and `CHANGELOG_AI.md` (session handoff & entry/exit states).
3. **Strict Canon Mutation Control**: Never alter established facts, character traits, or past timeline events without an explicit authorized canon update.
4. **Fractal Scene Architecture**: Every scene must complete a circuit of change: Goal → Conflict → Disaster (Action) followed by Reaction → Dilemma → Decision (Sequel).
5. **Zero AI Cliché Policy**: Actively suppress recognizable AI writing patterns ("delve", "tapestry", "beacon", "testament", emotional moralizing, syntactic symmetry).
6. **Tiered Editorial Quality Gates**: Always separate Developmental Editing (structure, pacing, arcs) from Line Editing (cadence, subtext) and Copy Editing (grammar, terms).

---

## End-to-End BookOps Lifecycle

```text
Phase 1: Project Conception & Market Validation
  ↓
Phase 2: Master Book Blueprint Generation (BOOK_BLUEPRINT.md)
  ↓
Phase 3: Story Bible & Character System Setup (MEMORY.md)
  ↓
Phase 4: Hierarchical Outlining & Mathematical Word Budgeting
  ↓
Phase 5: Chapter-by-Chapter Drafting (with Triple Anchor Context)
  ↓
Phase 6: Multi-Stage Quality Gates & Anti-AI Prose Suppression
  ↓
Phase 7: Developmental, Line, and Dialogue Surgery Passes
  ↓
Phase 8: Manuscript Assembly & Export (Markdown / EPUB / PDF / DOCX)
  ↓
Phase 9: Amazon KDP Metadata & Launch Preparation
```

---

## Phase 1: Project Conception & Briefing

### Required Inputs
Collect or prompt the user for the foundational brief:
- **Title / Working Concept**: Core topic or high-concept hook.
- **Genre & Target Audience**: Reader avatar, knowledge level, and desired transformation.
- **Category (Fiction vs Non-Fiction)**:
  - *Fiction*: Protagonist want vs need, antagonist force, core theme, narrative POV.
  - *Non-Fiction*: Core thesis, reader pain points, target skill acquisition, comparable books.
- **Target Scale**: Total target word count (e.g. 25,000 / 50,000 / 80,000 words), number of parts/chapters.

---

## Phase 2: Master Book Blueprint

Generate `BOOK_BLUEPRINT.md` adhering to the standard 12-section structure:
1. **§1. Executive Concept**: One-sentence premise, one-paragraph hook, back-cover positioning, core reader promise.
2. **§2. Target Length & Format**: Total word count, chapter-count philosophy, format recommendation (eBook-first, print).
3. **§3. Reader Experience Design**: Emotional/cognitive milestones at 10 pages, 25%, midpoint, and climax.
4. **§4. Macro Structure**: Act breaks / Thesis progression, major turning points, escalation path.
5. **§5. Character System / Domain Model**: Principal characters (want, need, flaw, arc, voice) or Non-fiction framework modules.
6. **§6. Chapter-by-Chapter Plan**: Entry state → Core dramatic/pedagogical beat → Exit state for every chapter.
7. **§7. Style Guide**: Narrative POV, tense, tone register, sentence rhythm rules, banned patterns.
8. **§8. Dual-Clue / Subplot Ledger**: Tracking surface events vs hidden depths/open threads.
9. **§9. Production Assumptions**: Manuscript layout convention (`manuscript/chapters/chNN.md`), front/back matter.
10. **§10. Quality Gates**: 6 mandatory gates per chapter before marking complete.
11. **§11. Risk Review**: Top story, pacing, and clarity risks with one-sentence mitigations.
12. **§12. Drafting Instructions**: Order of execution and session handoff rules.

*(See full template in [references/book_blueprint_template.md](./references/book_blueprint_template.md))*

---

## Phase 3: Context & Two-Tier Memory Setup

Initialize the project filesystem:
```text
project-root/
├── BOOK_BLUEPRINT.md
├── MEMORY.md
├── CHANGELOG_AI.md
├── STYLE_GUIDE.md
├── manuscript/
│   ├── manifest.md
│   └── chapters/
│       ├── ch01.md
│       └── ...
├── characters/
├── world/
└── build/
```

- **`MEMORY.md`**: Store canonical facts (world rules, magic/tech limits, established timeline events, character traits).
- **`CHANGELOG_AI.md`**: Log session transitions:
  ```markdown
  ## Chapter NN Handoff
  - **Entry State**: Where characters were / what reader knew.
  - **Key Shifts**: Permanent changes that occurred.
  - **Exit State**: Ending location, active emotional tone, new knowledge.
  - **Open Threads / Clues**: Pending setups requiring future payoffs.
  - **Next Step**: Explicit prompt instruction for Chapter NN+1.
  ```

---

## Phase 4: Hierarchical Outlining & Word Budgeting

1. **Calculate Word Budgets**:
   $$\text{Budget per Chapter} = \frac{\text{Total Target Words}}{\text{Number of Chapters}}$$
   $$\text{Budget per Scene/Item} = \frac{\text{Chapter Budget}}{\text{Number of Scenes/Items}}$$
2. **Breakdown Chapters into Discrete Beats**:
   - *Fiction*: Scene 1 (Setup → Conflict → Disaster) → Scene 2 (Reaction → Dilemma → Decision).
   - *Non-Fiction*: Hook/Problem → Core Principle → Case Study/Example → Action Steps → Recap.

---

## Phase 5: Chapter Drafting Protocol (Triple Anchor)

When prompting or executing drafting for Chapter $N$, assemble the **Triple Anchor Context**:
1. **Macro Anchor**: Book premise + overall chapter roadmap.
2. **Rolling Bridge**: Summary of Chapter $N-1$ from `CHANGELOG_AI.md` (entry state & emotional momentum).
3. **Micro Anchor**: Chapter $N$ beat sheet from `BOOK_BLUEPRINT.md §6`.

### Drafting Prompt Template
```markdown
You are drafting Chapter [NN]: "[Title]" for the book "[Book Title]".

CONTEXT:
1. Worldview / Core Thesis: [Summary from MEMORY.md]
2. Previous Chapter Exit State: [Summary from CHANGELOG_AI.md]
3. Current Chapter Goal & Beats: [Beat plan from BOOK_BLUEPRINT.md §6]
4. Word Budget: [Min Words] - [Max Words] words.

STRICT CONSTRAINTS:
- Follow Style Guide: POV [POV], Tense [Tense], Tone [Tone].
- Complete Fractal Scene Circuits: Every scene must permanently shift the entry state.
- Suppress AI Writing Clichés: Do NOT use "delve", "tapestry", "beacon", "testament", or neat moralizing summaries.
- Focus on sensory texture (sound, smell, touch) and dialogue subtext.

Draft the full chapter in clean Markdown.
```

---

## Phase 6: Quality Gates & Anti-AI Prose Suppression

Every drafted chapter must pass 6 Quality Gates:

1. **Gate 1 — Scene Circuit Check**: Does every scene complete a circuit of change? (Entry state $\neq$ Exit state).
2. **Gate 2 — Character Hierarchy & Voice**: Are principal characters driving the action? Does dialogue contain distinct acoustic rhythm?
3. **Gate 3 — Anti-AI Prose Suppression**: Audit text against [references/anti_ai_prose_rules.md](./references/anti_ai_prose_rules.md). Strip out symmetry, artificial eloquence, and banned vocabulary.
4. **Gate 4 — Multi-Persona Editorial Pass**: Run narratological, psychological, and pacing checks.
5. **Gate 5 — Blueprint & Canon Continuity**: Verify alignment with `BOOK_BLUEPRINT.md` and `MEMORY.md`.
6. **Gate 6 — Session Handoff Logged**: Record entry/exit states and open threads in `CHANGELOG_AI.md`.

---

## Phase 7: Multi-Pass Editorial Refinement

Use the specialized review rubrics from [references/editorial_rubric_22_pass.md](./references/editorial_rubric_22_pass.md):
- **Developmental Pass**: Plot structure integrity (Inciting incident, Midpoint reversal, Climax tension), Pacing heatmap.
- **Dialogue Surgery Pass**: Strip on-the-nose exposition, inject conversational subtext and non-verbal beats.
- **Line Editing Pass**: Sentence length variety, active verb cadence, tightening word count by 10–15%.
- **Copy Editing & Proofreading**: Terminology consistency, punctuation, formatting lock.

---

## Phase 8: Manuscript Assembly & Multi-Format Export

1. **Compile Manifest**: Order all chapters in `manuscript/manifest.md`.
2. **Export Targets**:
   - **EPUB / PDF (via Pandoc)**:
     ```bash
     pandoc -s -o build/book.epub --toc --metadata-file=metadata.yaml manuscript/chapters/*.md
     ```
   - **PDF (via LaTeX)**: For technical books with math/tables using `template.tex`.
   - **DOCX**: For traditional publishing workflows and agent submissions.

---

## Phase 9: KDP Publishing & Launch

1. **Amazon Metadata Formulation**:
   - 7 Backend Search Keyword strings (under 50 characters, high buyer intent).
   - 3 Target Amazon BISAC categories.
2. **High-Converting Book Description**:
   - Headline Hook $\rightarrow$ Emotional Agitation $\rightarrow$ Core Solution $\rightarrow$ Bulleted Feature/Benefits $\rightarrow$ Risk-Reversal CTA.
3. **Launch Execution**:
   - Pre-publication proofing checklist ([references/kdp_publishing_checklist.md](./references/kdp_publishing_checklist.md)).
   - Back-matter lead magnets and reader review request.

---

## Quick Command Reference

| Action | Recommended Tool / File |
| :--- | :--- |
| **Start Project** | Initialize `BOOK_BLUEPRINT.md` from `references/book_blueprint_template.md` |
| **Check Canon** | Verify against `MEMORY.md` and `references/canon_mutation_protocol.md` |
| **Draft Chapter** | Run Triple-Anchor prompt with word budget |
| **Sanitize Prose** | Apply `references/anti_ai_prose_rules.md` |
| **Audit Manuscript**| Execute 22-pass review from `references/editorial_rubric_22_pass.md` |
| **Build Book** | Compile `manuscript/manifest.md` via Pandoc/DOCX build script |
"""

# 2. references/anti_ai_prose_rules.md
anti_ai_md = """# Anti-AI Prose Suppression Rules & Style Protocols

A rigorous guide for detecting and eradicating telltale AI writing patterns, clichés, structural symmetry, and artificial dialogue.

---

## 1. Banned Vocabulary & Telltale AI Clichés

Replace these overused AI words with specific, grounded, and organic human phrasing:

| Banned AI Word / Phrase | Why It Fails | Organic Replacement Strategy |
| :--- | :--- | :--- |
| **delve / delving** | Universal AI filler verb | Use concrete action verbs: *examined, dug into, searched, probed, inspected*. |
| **tapestry / rich tapestry** | Pretentious AI metaphor for complexity | Describe the concrete physical or social elements directly. |
| **beacon (of hope/light)** | Melodramatic cliché | Ground the emotion in character behavior or tangible setting details. |
| **testament (a testament to)** | Abstract moralizing | Show the evidence or consequence rather than editorializing. |
| **palpable (the tension was palpable)** | Telling rather than showing | Show physical physical reactions: sweating palms, rigid shoulders, silence. |
| **shivers down spine** | Physical cliché | Describe visceral, unexpected physiological sensations. |
| **dance / danced (shadows danced)** | Overused poetic crutch | Use dynamic verbs: *flickered, shifted, darted, stretched*. |
| **symphony / cacophony** | Overused auditory trope | Name the exact acoustic sounds: *the scrape of iron, the hum of fluorescent bulbs*. |
| **labyrinth / labyrinthine** | Lazy shortcut for complex settings | Map the physical architecture (corridors, dead ends, cracked masonry). |
| **unwavering / steadfast** | Flat character praise | Show character resolve through difficult, costly choices. |

---

## 2. Structural & Syntactic Anti-Patterns to Eradicate

### A. The "Moralizing Summary" Ending
- **AI Habit**: Ending chapters or scenes with neat philosophical summaries (e.g., *"And in that moment, she realized that true courage was not the absence of fear, but the triumph over it."*).
- **Rule**: **ABSOLUTELY FORBIDDEN.** End on immediate physical actions, unresolved dilemmas, unanswered questions, or sensory images.

### B. Syntactic Symmetry & "The Rule of Threes"
- **AI Habit**: Generating lists of exactly three items or three symmetrical adjectives (e.g., *"He was brave, loyal, and determined."* or *"A world of blood, iron, and shadows."*).
- **Rule**: Break symmetry. Use 1 strong detail or 2 asymmetrical elements. Vary sentence length from 3 words to 35 words.

### C. Hyper-Articulate Dialogue
- **AI Habit**: Characters speaking in complete, grammatically flawless paragraphs that sound like written essays.
- **Rule**: Human speech is fragmented, interrupted, defensive, and subtextual. Characters should rarely say exactly what they mean. Use ellipsis, pauses, incomplete thoughts, and non-verbal reactions.

### D. Continuous Metaphor Stacking
- **AI Habit**: Piling multiple metaphors in a single descriptive paragraph (e.g., storm as rage $\rightarrow$ ocean as grief $\rightarrow$ lightning as revelation).
- **Rule**: Limit to one dominant, original metaphor per major scene, or rely entirely on precise literal sensory details.

---

## 3. The 5-Step Prose Sanitization Pass

1. **Grep & Replace**: Search for the top 20 AI keywords and replace them.
2. **Cadence Scan**: Read paragraphs aloud. If 3 consecutive sentences have identical word counts or grammatical structure (Subject-Verb-Object), rewrite at least one.
3. **Dialogue Subtext Surgery**: Cut the first 25% and last 25% of dialogue exchanges (remove hellos, goodbyes, and obvious explanations).
4. **Active Verb Tightening**: Convert passive constructions (*"There was a sound of footsteps echoing"*) to active voice (*"Footsteps echoed across the flagstones"*).
5. **Show vs Tell Audit**: Convert abstract emotional labels (*"He felt terrified"*) into concrete physical behavior (*"His knuckles whitened against the doorframe"*).
"""

# 3. references/editorial_rubric_22_pass.md
editorial_md = """# 22-Pass Full Manuscript Editorial Analysis Rubric

An exhaustive framework for diagnosing narrative, structural, and line-level manuscript quality.

---

## Part 1: Macro & Developmental Structure

- **Pass 1 — Plot Structure & 3-Act Integrity**: Verify setup, inciting incident, plot point 1, midpoint reversal, all-is-lost moment (75%), climax, and resolution. Rate 1–10.
- **Pass 2 — Pacing Heatmap**: Construct chapter-by-chapter table: `Chapter | Tension (1-10) | Pacing Rating | Scene Types | Energy Level`. Identify momentum valleys.
- **Pass 3 — Character Arc Completeness**: Map protagonist and antagonist trajectory: Want vs Need, Ghost/Wound, Midpoint awakening, Climax choice.
- **Pass 4 — Thematic Coherence**: Ensure the core thematic argument is contested throughout and resolved in the climax without being preachy.
- **Pass 5 — Stakes Escalation**: Check that personal and external stakes continuously increase, reaching their absolute highest point at the climax.
- **Pass 6 — Subplot Integration**: Verify every secondary plot thread connects to the main spine and resolves cleanly.

---

## Part 2: World-Building & Continuity

- **Pass 7 — World-Building Continuity Scan**: Check physical geography, room layouts, travel times, technology/magic rules, and social laws.
- **Pass 8 — Timeline & Chronology Audit**: Verify sequence of days, dates, seasons, and elapsed time across chapters.
- **Pass 9 — Character Knowledge Tracking**: Ensure characters never act on information they have not yet learned on-page.
- **Pass 10 — Object & Inventory Tracking**: Track physical items, weapons, keys, and wounds across scene transitions.

---

## Part 3: Scene Craft & Micro-Tension

- **Pass 11 — Fractal Scene Circuit**: Verify every scene has Goal $\rightarrow$ Conflict $\rightarrow$ Disaster (Action) or Reaction $\rightarrow$ Dilemma $\rightarrow$ Decision (Sequel).
- **Pass 12 — Micro-Tension & Hook Integrity**: Ensure every scene opening hooks reader curiosity and every scene ending carries narrative momentum.
- **Pass 13 — Atmosphere & Setting Immersion**: Check multi-sensory balance (sound, smell, temperature, texture) vs generic visual description.
- **Pass 14 — Character Hierarchy & Scene Ownership**: Verify principal characters dominate scene focus and dialogue oxygen.

---

## Part 4: Dialogue & Subtext

- **Pass 15 — Acoustic Voice Differentiation**: Ensure each character's dialogue is distinguishable without speaker tags.
- **Pass 16 — Subtext & Exposition Stripping**: Remove on-the-nose explanations and replace with conversational evasion and conflict.
- **Pass 17 — Dialogue Pacing & Beat Action**: Balance spoken lines with physical character actions and environmental interaction.

---

## Part 5: Line Editing & Prose Aesthetics

- **Pass 18 — Sentence Cadence & Syntactic Variety**: Audit sentence length variation, rhythm, and structural diversity.
- **Pass 19 — Anti-AI Cliché & Trope Suppression**: Sanitize all generic AI metaphors and repetitive vocabulary.
- **Pass 20 — Concision & Deadwood Trimming**: Trim 10–15% unnecessary wordiness, weak qualifiers, and filter verbs (*saw, heard, felt*).

---

## Part 6: Copy Editing & Publishing Lock

- **Pass 21 — Terminology & Capitalization Lock**: Enforce consistency across names, places, and world glossary terms.
- **Pass 22 — Final Proofreading & Layout Integrity**: Check header levels, page breaks, front matter, back matter, and table of contents.
"""

# 4. references/book_blueprint_template.md
blueprint_tpl = """# Master Book Blueprint Template (`BOOK_BLUEPRINT.md`)

Use this template to generate the comprehensive master architecture for any fiction or non-fiction book project.

```markdown
# BOOK_BLUEPRINT.md: [Book Title]

## §1. Executive Concept
- **One-Sentence Premise**: [Core high-concept hook]
- **One-Paragraph Premise**: [Expanded narrative/educational premise]
- **Back-Cover Positioning**: [Commercial blurb aimed at target readers]
- **Core Promise to the Reader**: [What the reader will feel or master]
- **Comparable Books (Comp Titles)**: [Title 1, Title 2] — and how this book differs.

## §2. Target Length and Format
- **Total Word Count Target**: [e.g. 50,000 words (Acceptable Range: 45,000 - 55,000)]
- **Number of Parts / Acts**: [e.g. 3 Acts / 4 Parts]
- **Number of Chapters**: [e.g. 15 Chapters]
- **Average Chapter Length**: [e.g. 3,000 - 3,500 words]
- **Format Delivery**: [eBook, Paperback, Hardcover]

## §3. Reader Experience Design
- **First 10 Pages**: [What the reader experiences immediately]
- **25% Mark (End of Act 1 / Foundation)**: [Key understanding / commitment]
- **50% Mark (Midpoint Turn)**: [Major shift in stakes or paradigm]
- **75% Mark (All-Is-Lost / Final Synthesis)**: [Deepest crisis or critical integration]
- **Final 10% (Climax & Resolution)**: [Emotional catharsis or actionable takeaway]

## §4. Macro Structure
[For Fiction: 3-Act Structure / Hero's Journey / 7-Point Breakdown]
[For Non-Fiction: Problem Agitation → Core Thesis → Framework → Case Studies → Action Plan]

## §5. Character System / Domain Framework
[For Fiction: Detailed profiles for Protagonist, Antagonist, Major Secondary (Want, Need, Flaw, Arc, Voice)]
[For Non-Fiction: Core modular frameworks, pedagogical pillars, terminology]

## §6. Chapter-by-Chapter Plan
### Chapter 01: [Working Title]
- **Word Budget**: [e.g. 3,200 words]
- **Dramatic / Pedagogical Purpose**: [Core objective]
- **Entry State**: [Initial status of character / reader knowledge]
- **Key Scenes / Subsections**: [Beat 1, Beat 2, Beat 3]
- **Exit State**: [Permanent transformation by end of chapter]
- **Continuity Notes**: [Objects, secrets, facts established]

### Chapter 02: [Working Title]
... [Continue for all chapters]

## §7. Style Guide
- **Narrative POV**: [First Person / Third Person Limited / Second Person]
- **Tense**: [Past / Present]
- **Tone & Register**: [e.g. Gritty, conversational, authoritative, lyrical]
- **Prose Rules**: [Banned tropes, rhythm rules, sentence length variety]

## §8. Dual-Clue / Subplot Ledger
| Clue / Subplot Thread | Surface Reading | Deeper Truth | Introduced In | Resolved In | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [Thread Name] | [What it looks like] | [What it actually means] | Ch 02 | Ch 14 | Open |

## §9. Production Assumptions
- **Source Layout**: Markdown chapters in `manuscript/chapters/chNN.md`
- **Front Matter**: Title page, Copyright, Dedication, Epigraph, Table of Contents
- **Back Matter**: Acknowledgments, Author Note, Lead Magnet CTA, Index
- **Compilation Engine**: Pandoc (EPUB/PDF), LaTeX (Technical PDF), or DOCX

## §10. Quality Gates
1. Scene Circuit Check (Entry State $\neq$ Exit State)
2. Character Hierarchy & Voice Check
3. Anti-AI Prose Suppression Filter Applied
4. Multi-Persona Editorial Pass
5. Blueprint & Canon Continuity Validated
6. Session Handoff Logged in `CHANGELOG_AI.md`

## §11. Risk Review
- **Story / Thesis Risk**: [Potential flaw] $\rightarrow$ *Mitigation: [Solution]*
- **Pacing Risk**: [Potential sag] $\rightarrow$ *Mitigation: [Solution]*
- **Continuity Risk**: [Complex thread] $\rightarrow$ *Mitigation: [Solution]*

## §12. Drafting Instructions
- Order of drafting: Sequential (Ch 01 through Ch NN).
- Session memory procedure: Read `MEMORY.md` and last entry of `CHANGELOG_AI.md` before drafting each chapter.
```
"""

# 5. references/canon_mutation_protocol.md
canon_md = """# Canon Mutation Control & State Management Protocol

Rules governing how the agent interacts with, preserves, and modifies story canon and persistent memory.

---

## 1. The Canon Hierarchy

1. **Level 1 — Immutable World Laws (`MEMORY.md`)**: Physical constants, magic rules, historical dates, and foundational lore. Cannot be changed without explicit human approval.
2. **Level 2 — Character & Entity State (`characters/*.md`)**: Dynamic attributes (injuries, knowledge, inventory, emotional state). Updated after every scene/chapter.
3. **Level 3 — Session State (`CHANGELOG_AI.md`)**: Rolling handoffs, recent chapter exit states, and open thread ledgers.

---

## 2. Canon Mutation Rules

- **No Hallucinated Retcons**: An agent drafting Chapter 10 cannot alter facts established in Chapter 2. If a plot contradiction arises, the agent must pause and flag it.
- **Explicit Canon Patches**: If an author decides to change a character's backstory or world rule mid-manuscript:
  1. Update `MEMORY.md` with a dated entry.
  2. Create a refactor task in `CHANGELOG_AI.md` listing all prior chapters that require revision.
- **Knowledge Boundary Enforcement**: Characters may only speak of or act on events they witnessed or were informed of on-page.

---

## 3. Session Handoff Procedure

After every drafted chapter, append the following block to `CHANGELOG_AI.md`:

```markdown
## [Date] — Chapter [NN] Completed
- **File**: `manuscript/chapters/chNN.md`
- **Word Count**: [Actual words] vs [Budgeted words]
- **Entry State**: [Brief recap of character position/mindset]
- **Key Actions / Shifts**: [Permanent plot/argument developments]
- **Exit State**: [Final character status, physical setting, active emotion]
- **Established Canon**: [New characters, places, or rules introduced]
- **Open Threads / Clues**: [Active unresolved setups]
- **Quality Gates Status**: [All 6 Gates Passed ✓]
- **Next Action**: [Draft Chapter NN+1: "[Title]"]
```
"""

# 6. references/kdp_publishing_checklist.md
kdp_md = """# Amazon KDP Publishing & Metadata Checklist

A production checklist for preparing and launching manuscripts on Amazon Kindle Direct Publishing.

---

## 1. Amazon Metadata Requirements

- **Primary Title**: Exact match with book cover and title page.
- **Subtitle**: Clear reader benefit or genre keyword phrase.
- **Author Name / Contributor Bio**: Author name and 150-word authoritative bio.
- **7 Backend Search Keywords**:
  - Max 50 characters per string.
  - Combine long-tail buyer search queries.
  - Do NOT repeat words from the title/subtitle.
  - Do NOT include subjective claims ("bestseller", "free") or competitor brand names.
- **Amazon Categories**: 3 highly targeted BISAC categories with low competition and active sales.

---

## 2. High-Converting Book Description Formula

```html
<h2>[Compelling Attention-Grabbing Headline Hook]</h2>

<p>[Emotional Agitation / Story Setup — 2-3 sentences outlining the central conflict or reader frustration.]</p>

<p><strong>Inside [Book Title], you will discover:</strong></p>

<ul>
  <li><strong>[Benefit Hook 1]:</strong> [Specific result or narrative payoff]</li>
  <li><strong>[Benefit Hook 2]:</strong> [Specific result or narrative payoff]</li>
  <li><strong>[Benefit Hook 3]:</strong> [Specific result or narrative payoff]</li>
  <li><strong>[Benefit Hook 4]:</strong> [Specific result or narrative payoff]</li>
</ul>

<p>[Risk-Reversal / Urgency statement]</p>

<p><strong>[Call to Action: Scroll up and click "Buy Now" or "Read with Kindle Unlimited" today!]</strong></p>
```

---

## 3. Pre-Publishing Quality Checklist

- [ ] Front matter included (Title page, Copyright, Dedication, Table of Contents).
- [ ] Chapter headings formatted with consistent Markdown / HTML tags (`# Chapter N` or `<h1>`).
- [ ] Table of Contents active with working internal hyperlinks.
- [ ] Back matter included (Acknowledgments, Author Bio, Readers' Group Discussion, Review Request).
- [ ] Cover image formatted at 2560 x 1600 pixels (1.6:1 aspect ratio) in RGB format.
- [ ] EPUB / PDF validated without formatting errors or broken page breaks.
"""

# 7. templates/manifest.md
manifest_tpl = """# Manuscript Manifest

Governs the compilation order of manuscript files.

```markdown
# Front Matter
manuscript/frontmatter/title.md
manuscript/frontmatter/copyright.md
manuscript/frontmatter/dedication.md
manuscript/frontmatter/toc.md

# Main Body
manuscript/chapters/ch01.md
manuscript/chapters/ch02.md
manuscript/chapters/ch03.md

# Back Matter
manuscript/backmatter/acknowledgments.md
manuscript/backmatter/author_bio.md
manuscript/backmatter/lead_magnet.md
```
"""

# Write all files
with open(os.path.join(SKILL_DIR, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write(skill_md)

with open(os.path.join(REF_DIR, "anti_ai_prose_rules.md"), "w", encoding="utf-8") as f:
    f.write(anti_ai_md)

with open(os.path.join(REF_DIR, "editorial_rubric_22_pass.md"), "w", encoding="utf-8") as f:
    f.write(editorial_md)

with open(os.path.join(REF_DIR, "book_blueprint_template.md"), "w", encoding="utf-8") as f:
    f.write(blueprint_tpl)

with open(os.path.join(REF_DIR, "canon_mutation_protocol.md"), "w", encoding="utf-8") as f:
    f.write(canon_md)

with open(os.path.join(REF_DIR, "kdp_publishing_checklist.md"), "w", encoding="utf-8") as f:
    f.write(kdp_md)

with open(os.path.join(TPL_DIR, "manifest.md"), "w", encoding="utf-8") as f:
    f.write(manifest_tpl)

print("Master E-Book Writer Skill and references successfully generated!")
