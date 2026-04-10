# Pipeline Rewrite — Walkthrough

## What Changed

### narrative_review.py
- **Removed**: `load_visual_bible()`, `save_visual_bible()`, `load_master_visual_bible()`, `save_master_visual_bible()`, `generate_locations()`
- **Removed**: Cache check in `run_character_pipeline()` (no more "Using cached character bible")
- **Removed**: CIVILIAN from `group_order` and emoji map
- **Kept**: `generate_visual_bible()` — always fresh, accepts `style_content` + `exclude_characters`
- **Kept**: `run_character_pipeline()` — always fresh, 3 groups (PROTAGONIST/NAMED/MILITARY)

### process_controller.py
- **Removed**: imports of `load_visual_bible`, `save_visual_bible`, `load_master_visual_bible`, `save_master_visual_bible`
- **Rewritten**: Visual Bible section — always generates fresh (no cache check)
- **Rewritten**: Save visual bible inline (simple file write)

### prompt_generator.py (from earlier)
- `_build_user_message()` — separate VISUAL BIBLE + CHARACTER BIBLE sections
- JSON output when `character_bible` present, text when not

## Verification
- ✅ All imports pass
- ✅ Zero references to removed functions in entire codebase
- ✅ No old cache logic anywhere
