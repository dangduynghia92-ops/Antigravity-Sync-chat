# Video Pipeline Hardening — Walkthrough

## Overview
Refactored the video prompt pipeline from a single-file, mechanical assembly system into a **multi-chapter, LLM-driven prompt writing pipeline** with label consistency enforcement and location style isolation.

## Changes Made

### 1. Style File (`Chibi Storybook Historical.txt`)
- Added `=== LOCATION STYLE ===` section → background-only style rules
- Ensures location reference images have **no character appearance**

### 2. Pipeline Core (`video_pipeline.py`)

#### Architecture: 6-Step Pipeline
```
Step 0: Parse + Merge    → Multi-file with chapter markers + timing offsets
Step 1: Semantic Chunking → Group sentences into sequences (unchanged logic)
Step 2a: Characters       → Multi-angle sheet_prompt (front, 3/4, side)
Step 2b: Locations        → (unchanged)
 ↓ Label Extraction       → Extract valid_labels as "source of truth"
Step 3: Scene Design      → 1 LLM call per sequence (was: batched)
Step 4: Prompt Writing    → NEW: LLM writes natural flat_prompts
Step 5: Export            → Excel with Chapter column + location_style
```

#### Key Changes
| Feature | Before | After |
|---|---|---|
| Input | Single file | Multi-file (`srt_paths: List[str]`) |
| Step 3 granularity | Batched (60s chunks) | 1 call per sequence |
| Prompt generation | Python string concatenation | LLM writes natural prose |
| Label enforcement | None | Valid label list + fuzzy matching |
| Costume handling | None | `costume_note` per scene |
| Location ref style | Same as character style | Separate `LOCATION STYLE` |
| Character sheet | Single pose | 3-view reference sheet |
| Excel columns | No chapter info | Chapter column added |

#### New Helper Functions
- `_parse_style_section()` — generic section extractor
- `_parse_location_style()` — extracts location-only style
- `_extract_valid_labels()` — builds label whitelist from Step 2
- `_build_labels_block()` — generates constraint text for LLM
- `_fuzzy_match()` — corrects drifted labels
- `_validate_scene_labels()` — enforces label consistency
- `_build_mini_bible()` — targeted reference per sequence
- `_build_scene_context()` — prev/next sequence context
- `_process_sequence_step3()` — per-sequence scene design
- `_process_sequence_step4()` — per-sequence prompt writing

### 3. UI (`video_prompt_tab.py`)
- Files in the **same folder** are automatically grouped into **one pipeline**
- Each folder group runs as a single multi-chapter project
- All items in a group get the same status update
- Single files still work independently (backward compatible)

## Validated
- ✅ `import core.video_pipeline` — no syntax errors
- ✅ `import ui.video_prompt_tab` — no syntax errors
- ⏳ Real dataset test (Baldwin IV) pending

## Files Modified
- `core/video_pipeline.py` — Major refactor
- `ui/video_prompt_tab.py` — Folder grouping logic
- `video_styles/Chibi Storybook Historical.txt` — Location style section
