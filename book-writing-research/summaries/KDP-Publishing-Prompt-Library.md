# Repository Report: KDP-Publishing-Prompt-Library

## Repository
- **Name**: KDP-Publishing-Prompt-Library
- **URL**: https://github.com/kannfrank02-code/KDP-Publishing-Prompt-Library
- **Commit**: `45063f4a`
- **Status**: SUCCESS
- **Primary purpose**: Curated prompt library for Amazon Kindle Direct Publishing (KDP) ideation, writing, keywords, descriptions, and launch marketing.
- **Primary target**: Publishing only & Commercial Non-fiction.

---

## Important Paths
- `kdp-book-idea-generator.md`: Prompts for generating profitable KDP book niches, high-demand topics, and low-competition angles.
- `kdp-keyword-research-prompt.md`: Prompts for Amazon search keyword extraction, 7-keyword backend optimization, and category selection.
- `kdp-book-outline-prompt.md`: Prompts for reader-problem solving outlines and non-fiction chapter logic.
- `kdp-chapter-writing-prompt.md`: Prompts for actionable, engaging non-fiction chapter drafting.
- `kdp-book-description-prompt.md`: Prompts for copywriting high-converting Amazon sales descriptions (Hook, Story/Problem, Bullet Benefits, CTA).
- `kdp-journal-creation-prompt.md`: Prompts for low-content and guided journal creation.
- `kdp-content-repurposing-prompt.md`: Prompts for repurposing book chapters into lead magnets, social posts, and email sequences.

---

## Workflow
Niche & Idea Generation (`kdp-book-idea-generator.md`)
→ Keyword & Category Research (`kdp-keyword-research-prompt.md`)
→ Outline Creation (`kdp-book-outline-prompt.md`)
→ Chapter Writing (`kdp-chapter-writing-prompt.md`)
→ Book Description Copywriting (`kdp-book-description-prompt.md`)
→ Content Repurposing & Launch (`kdp-content-repurposing-prompt.md`).

---

## Inputs and Outputs

```text
Stage 1: Commercial Positioning
Input: Target audience, general topic area
Process: Idea generator + Keyword research prompts
Output: Validated book title, subtitle, 7 backend search keywords, 3 Amazon categories
Used by next stage: Outlining & Description Copywriting

Stage 2: Outlining & Drafting
Input: Validated title, target audience pain points
Process: Book outline prompt → Chapter writing prompt
Output: Chapter drafts focused on solving specific reader problems
Used by next stage: Publishing Copy

Stage 3: Sales Copy & Metadata
Input: Book contents, core benefits, author bio
Process: Book description prompt
Output: Amazon HTML sales page description (Headline, Body bullets, Social proof, Urgency CTA)
Used by next stage: KDP Dashboard Publishing
```

---

## Prompt Inventory

### Prompt: KDP High-Converting Book Description
- **File**: `kdp-book-description-prompt.md`
- **Purpose**: Generates Amazon product page sales copy formatted with Amazon-supported HTML tags (`<h2>`, `<b>`, `<i>`, `<ul>`).
- **Required inputs**: Book title, Target reader, 3 major reader problems, 3 major solutions/benefits.
- **Expected output**: Compelling Amazon product page copy with headline, hook, bullet points, and CTA.
- **Important constraints**: Must adhere to Amazon HTML formatting limitations.
- **Downstream consumer**: Amazon KDP Publishing Dashboard.

### Prompt: KDP 7-Backend Keyword Optimizer
- **File**: `kdp-keyword-research-prompt.md`
- **Purpose**: Generates 7 keyword phrases (under 50 characters each) optimized for Amazon buyer search intent.
- **Required inputs**: Book topic, niche, audience.
- **Expected output**: 7 unique keyword strings avoiding repetition of title words.
- **Important constraints**: No trademarked terms, no subjective claims like "best seller".
- **Downstream consumer**: KDP Metadata Setup.

---

## Context / Memory Strategy
No meaningful persistent-context mechanism identified (collection of standalone prompt templates).

---

## Editing Strategy
Absent (all editing categories unsupported in this prompt collection).

---

## Export / Assembly Strategy
- **Manuscript source format**: Markdown / Text.
- **Chapter organization**: Standalone prompts.
- **Assembly method**: Manual copy-paste into word processor or KDP portal.
- **Output formats**: Amazon KDP metadata fields, Markdown.
- **Scripts/tools required**: None.

---

## Strongest Ideas
1. **Commercial Amazon KDP Metadata Optimization**: High-converting sales copy prompts structured specifically for Amazon's formatting rules.
2. **Backend Keyword Selection Logic**: Focus on buyer intent, search volume, and non-redundancy with book title/subtitle.
3. **Content Repurposing Framework**: Converting finished book chapters into promotional assets.

---

## Weaknesses
- No drafting pipeline, context management, or manuscript editing tools.
- Simple single-turn prompt templates.

---

## Reusable Knowledge
- Amazon sales copy formula (Hook → Agitation → Solution → Feature Bullets → Risk Reversal → CTA).
- KDP backend keyword research prompt pattern.
