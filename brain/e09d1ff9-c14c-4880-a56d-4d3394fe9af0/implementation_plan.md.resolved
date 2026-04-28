# Video Pipeline — Multi-Chapter Project Mode + Prompt Quality Fixes

## Problem Statement

The pipeline currently processes each chapter file **independently** through all 4 steps. For biography/historical videos with multiple chapters, this causes:
1. **No cross-chapter character consistency** — each chapter generates its own character set
2. **No age variants detected** — each chapter only sees one life stage
3. **Location prompts include character descriptions** — `mandatory_style` contains character appearance rules that leak into location reference prompts
4. **Character sheets lack multi-angle views** — prompt template was oversimplified

## Proposed Changes

### 1. Multi-Chapter Merge (Architecture Change)

Currently: `Chapter1 → [Step0→4]` → `Chapter2 → [Step0→4]` → ...
Proposed: `ALL Chapters → Step0 merge → Step1→4 once`

#### Flow:

```
Step 0: Parse each file individually (SRT/TXT)
        → Merge all sentences into one stream
        → Add chapter markers: {chapter_id: 1, chapter_name: "..."}
        → Renumber sentence_ids sequentially

Step 1: Semantic chunking on MERGED text
        → Each sequence knows which chapter it belongs to
        → LLM sees the FULL story timeline

Step 2: Character/Location analysis on MERGED text
        → LLM sees ALL chapters → correctly identifies age variants
        → Characters are shared across all chapters
        → Locations are shared across all chapters

Step 3: Storyboarding (batched as before)

Step 4: Assembly → ONE Excel file for the entire project
```

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

- Change `__init__` to accept `srt_paths: List[str]` instead of `srt_path: str`
- Modify `_run_step0` to parse each file and merge with chapter markers
- All subsequent steps operate on the merged data
- Output goes to a single project folder

#### [MODIFY] [video_prompt_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py)

- When running a folder group, collect all file paths and pass as one pipeline
- Single files still run independently

---

### 2. Fix Location Prompt (No Character Style)

> [!WARNING]
> Current `mandatory_style` contains: "round white faces with oval dot eyes and expressive eyebrows and mouth shapes and no nose, compact stylized body proportions..."
> This causes AI to generate **characters inside location images**.

#### Fix in `_export_excel` Reference Images sheet:

**For Character/Faction prompts:** Prepend full `mandatory_style` (includes character appearance)
**For Location prompts:** Use a **location-only style** that strips character appearance rules:

```
Location style: "Stylized historical animation illustration, detailed painterly backgrounds, 
scene-driven natural palette, scene-driven lighting, professional animation quality, 
clean consistent design, full frame, no border, no text, no watermark, 16:9 aspect ratio. 
NO characters, NO people, empty scene only."
```

#### [MODIFY] [Chibi Storybook Historical.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/video_styles/Chibi%20Storybook%20Historical.txt)

- Add `=== LOCATION STYLE ===` section with background-only keywords
- Pipeline parses this section for location reference prompts

---

### 3. Fix Character Sheet — Multi-Angle Views

#### Fix in `STEP2_CHARACTERS_SYSTEM_PROMPT`:

Change `sheet_prompt` template from:
```
"Character reference on clean white background. [visual_description]. Label '[label]'."
```
To:
```
"Character reference sheet on clean white background. Three neutral standing views: front view, 3/4 angle, side profile. [visual_description]. Label '[label]'."
```

---

### 4. Fix Age Variants

With multi-chapter merge (fix #1), the LLM in Step 2a will see the FULL story timeline and correctly identify that Baldwin IV appears as:
- `Jerusalem-King-A-Child` (chapters 1-2)
- `Jerusalem-King-A-Teen` (chapters 3-4)  
- `Jerusalem-King-A-Adult` (chapters 5-7)
- `Jerusalem-King-A-Elder` (chapters 8-11)

No additional prompt changes needed — the AGE VARIANT RULE already exists in the system prompt. It just wasn't working because each chapter was processed in isolation.

## Open Questions

> [!IMPORTANT]
> **Token limit concern**: Merging all 11 chapters (~1700 words total) into one Step 2 call should be fine (well under the 5000 word limit). But for very long scripts, should we add a fallback to split into 2 passes?

> [!IMPORTANT]
> **Chapter column in Excel**: With merged processing, should the Excel output include a "Chapter" column so you know which chapter each scene belongs to?

## Verification Plan

### Automated Tests
- Run pipeline on the same Baldwin IV dataset with multi-chapter merge
- Compare character count: should have age variants across chapters
- Check location prompts: should NOT contain character appearance keywords
- Check character sheet prompts: should include "front, 3/4, side"

### Manual Verification
- Generate reference images from the new prompts and verify:
  - Location images are empty (no characters)
  - Character sheets show multiple angles
  - Age variants have visually distinct proportions
