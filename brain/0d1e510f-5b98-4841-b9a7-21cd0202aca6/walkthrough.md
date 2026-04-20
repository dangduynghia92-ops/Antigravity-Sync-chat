# Source Map Implementation — Walkthrough

## What Changed

Added `_source_map` to the biography pipeline so the Phase Plan AI **declares which blueprint fields** it used for each `main_key_data` item. This replaces fuzzy keyword search with precise path-based extraction.

### Files Modified

| File | Change |
|---|---|
| [system_narrative_phase_plan_biography.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_biography.txt) | Added `_source_map` to output schema + rule #9 |
| [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py) | Added `_resolve_source_path`, `_extract_bio_section_matches` helpers; updated `_extract_chapter_blueprint` + `write_from_blueprint` |
| [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py) | Pass `_source_map` from phase plan to writer in both narrative + review pipelines |

### Data Flow (New)
```
Phase Plan AI → _source_map: {"event text": ["life_phases.X", "key_relationships.Y"]}
      ↓ saved in _phase_plan.json / _phase_plan_final.json
_extract_chapter_blueprint(source_map=...)
      ↓ lookup each main_key_data → paths → extract ONLY those sections
Writer receives precise, lean filtered blueprint
```

### Error Handling (Strict)
- Missing `_source_map` → **RuntimeError** (pipeline stops)
- Missing source entry for any key_data → **RuntimeError** (pipeline stops)
- Bad path in source_map → silently skipped (section/item may not exist)
- Battle/pirate niches → `source_map=None` → existing fuzzy search (unchanged)

### Git Commit
`40b6be3` — 6 files, 362 additions, 11 deletions

## Testing Required
1. Delete old `_phase_plan*.json` files for Galileo (they don't have `_source_map`)
2. Re-run biography pipeline
3. Check `_phase_plan.json` for `_source_map` field
4. Compare `_chapter_data/chXX_blueprint.json` sizes — should be much smaller
5. Read ch2 and ch3 — no more duplicate Vincenzo scenes
