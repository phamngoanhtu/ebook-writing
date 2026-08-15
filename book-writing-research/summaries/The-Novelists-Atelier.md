# Repository Report: The-Novelists-Atelier

## Repository
- **Name**: The-Novelists-Atelier
- **URL**: https://github.com/f5alcon/The-Novelists-Atelier
- **Commit**: `e0056002`
- **Status**: SUCCESS
- **Primary purpose**: Comprehensive 2,400+ line editorial analysis and manuscript critique prompt suite.
- **Primary target**: Editing only (Fiction novels & memoirs).

---

## Important Paths
- `novelist-atelier-prompts.md`: Massive master reference guide containing 16 distinct categories of editorial prompts:
  - Category 1: Manuscript-Level Analysis (22-pass deep editorial report outputting self-contained HTML/PDF scorecards).
  - Category 2: Style & Voice (Authorial voice fingerprinting, tone drift, dialogue voice).
  - Category 3: Developmental Editing (Three-act plot structure, midpoint shifts, climax integrity).
  - Category 4: Copy Editing (Grammar, punctuation, repetitive phrasing, formatting).
  - Category 5: Line Editing (Sentence cadence, prose tightening, sensory texture).
  - Category 6: Character (Arc consistency, motivation tracking, internal vs external conflict).
  - Category 7: World-Building (Lore consistency, timeline validation, rule enforcement).
  - Category 8: Location & Setting (Sensory immersion, spatial logic, atmosphere).
  - Category 9: Punch & Impact (Scene climaxes, emotional resonance, thematic payoffs).
  - Category 10: Chapter-Level Review (Pacing heatmaps, chapter hooks, exit states).
  - Category 11: Paragraph-Level (Flow, transitions, exposition distribution).
  - Category 12: Sentence-Level (Rhythm, syntactic variety, active vs passive voice).
  - Category 13: Tension & Engagement (Micro-tension, stakes escalation, mystery ledger).
  - Category 14: Prose & Style Audits (Cliche detection, sensory balance radar).
  - Category 15: Reader Experience (Emotional journey mapping, cognitive load).
  - Category 16: Genre-Specific (Mystery, Thriller, Romance, Sci-Fi, Fantasy rubrics).

---

## Workflow
Manuscript Draft Input 
→ Category 1: 22-Pass Full Manuscript Editorial Audit 
→ Macro Developmental Pass (Plot structure, pacing heatmap, character arcs) 
→ Chapter & Scene Review (Tension curves, scene goals, entry/exit states) 
→ Line & Sentence Surgery (Cadence, dialogue subtext, prose tightening) 
→ Micro Copy Edit & Consistency Verification 
→ Self-Contained HTML/PDF Diagnostic Report Generation.

---

## Inputs and Outputs

```text
Stage 1: Full Manuscript Analysis
Input: Full manuscript text (.txt, .docx, .md), 2-4 sentence synopsis
Process: 22-Pass Editorial Analysis prompt (novelist-atelier-prompts.md §1)
Output: Single self-contained HTML report with cover page, TOC, pacing heatmap, tension chart (SVG), character arc timeline, scorecard, and color-coded severity flags (🔴 Critical / 🟡 Important / 🟢 Minor)
Used by next stage: Targeted Developmental & Line Revisions

Stage 2: Targeted Craft Revisions
Input: Specific problematic chapter or scene identified in report
Process: Specialized category prompts (e.g. Dialogue Surgery, Pacing Heatmap, Tension Audit)
Output: Line-by-line editorial feedback and revised text options
Used by next stage: Final Proofreading & Publication
```

---

## Prompt Inventory

### Prompt: 22-Pass Full Manuscript Editorial Analysis
- **File**: `novelist-atelier-prompts.md` (§1)
- **Purpose**: Conducts the most rigorous multi-pass editorial diagnosis in the entire literature, scoring plot, pacing, character arcs, theme, world-building, stakes, dialogue, and prose.
- **Required inputs**: `[MANUSCRIPT TITLE]`, `[SYNOPSIS]`, `[MANUSCRIPT TEXT]`.
- **Expected output**: Comprehensive self-contained HTML document with embedded CSS, SVG charts, tables, and color-coded recommendations.
- **Important constraints**: Requires large-context LLMs (Claude Opus/Sonnet); high token budget.
- **Downstream consumer**: Author revision roadmap.

### Prompt: Pacing Heatmap & Tension Arc Auditor
- **File**: `novelist-atelier-prompts.md` (§10 & §13)
- **Purpose**: Creates a chapter-by-chapter table rating Tension (1–10), Pacing Rating (Too Fast/Fast/Good/Slow/Draggy), Scene Types, and Energy Level.
- **Required inputs**: Chapter texts.
- **Expected output**: Structured pacing heatmap table + top 10 ranked pacing fixes.
- **Important constraints**: Evaluates action-to-reflection balance and identifies energy valleys.
- **Downstream consumer**: Developmental rewriting pass.

---

## Context / Memory Strategy
Designed for large-window LLMs processing entire manuscripts or long excerpts in single or multi-turn editorial sessions. Provides structured synopsis and context injection headers.

---

## Editing Strategy
- **Developmental editing**: Extremely thorough 22-pass structural analysis.
- **Continuity**: Pass 5 World-Building Continuity Scan & Pass 3 Character Arc Consistency.
- **Fact checking**: Setting and timeline verification.
- **Line editing**: Category 5 & Category 12 (Sentence rhythm, syntactic variety, active verbs).
- **Copy editing**: Category 4 (Grammar, repetitive phrases, formatting).
- **Proofreading**: Final polish passes.
- **Style review**: Category 2 & Category 14 (Prose & style audits, sensory balance radar).

---

## Export / Assembly Strategy
- **Manuscript source format**: Text / Markdown / Word DOCX.
- **Chapter organization**: Full manuscript or chapter-by-chapter analysis.
- **Assembly method**: Output generated as standalone HTML reports printable directly to PDF.
- **Output formats**: HTML, PDF, Markdown.
- **Scripts/tools required**: Web browser for HTML-to-PDF rendering.

---

## Strongest Ideas
1. **22-Pass Editorial Analysis Matrix**: The most comprehensive editorial framework available, covering macro architecture down to syllable rhythm.
2. **Interactive HTML/PDF Diagnostic Reporting**: Generating beautiful, executive-ready HTML audit reports with SVG tension charts and color-coded issue severity.
3. **Pacing Heatmap Table**: Objective quantification of narrative momentum across every chapter.

---

## Weaknesses
- Focused purely on editing/critique; does not include drafting or generation workflows.
- Very high token consumption when analyzing full manuscripts.

---

## Reusable Knowledge
- The complete 22-pass editorial rubric and inspection criteria.
- HTML/SVG report generation prompt patterns.
- Pacing heatmap evaluation rubric.
