# Complete Pipeline Rewrite

## Flow

```
Start → Parse SRT → Load Style
  │
  ├─ Historical ON → Visual Bible (style-aware, no cache)
  ├─ CharSheet ON  → Character Pipeline (no cache, no CIVILIAN)
  │
  ├─ Generate Prompts per segment
  │   ├─ CharSheet ON  → JSON output
  │   └─ CharSheet OFF → Text output  
  │
  └─ Save CSV
```

## Files to Rewrite

### 1. [narrative_review.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/narrative_review.py)

**Remove:**
- `load_visual_bible()` — no cache
- `save_visual_bible()` — save directly in process_controller
- `generate_locations()` — merged into Visual Bible
- Cache check in `run_character_pipeline()`

**Rewrite:**
- `generate_visual_bible()` — always regenerate, accept style_content + exclude_characters
- `run_character_pipeline()` — always regenerate, 3 groups only (PROTAGONIST/NAMED/MILITARY)

---

### 2. [process_controller.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/process_controller.py)

**Rewrite section** `_process_single_project` lines 246-310:
- No cache check for either Visual Bible or Character Pipeline
- Character Pipeline first (if CharSheet ON)
- Visual Bible second (if Historical ON), excluding characters with sheets
- Pass both + style to prompt generator

**Rewrite section** `_process_loop` lines 426-441:
- Narrative mode: shared Character Pipeline, no cache

---

### 3. [prompt_generator.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/prompt_generator.py)

Already done — `_build_user_message` handles:
- Visual Bible → settings, civilians, architecture
- Character Bible → LABEL for named, uniform for military
- JSON output when character_bible present

---

### 4. Prompt Files (already updated)
- `character_scan_prompt.txt` — 3 groups, max 10
- `character_group_prompt.txt` — MILITARY focus uniform
- `narrative_review_prompt.txt` — style-aware

## Verification
- Import check
- Delete old output files, run fresh test
