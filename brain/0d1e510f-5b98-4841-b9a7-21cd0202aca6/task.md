# Prompt Optimization: All Narrative Niches

## Template Markers
- [x] `biography.txt` — 8 structures + hook/end markers
- [x] `battle.txt` — 7 structures + hook/end markers
- [x] `battle_v2.txt` — hook/end markers only (phase-based, no structures)
- [x] `mystery.txt` — 8 structures + hook/end markers
- [x] `pirate.txt` — 5 structures + hook/end markers
- [x] `pirate_haven.txt` — 6 structures + hook/end markers

## Rewriter Code
- [x] Restructure `_BODY_STRUCTURES` as niche-keyed dict (5 niches)
- [x] Update `_apply_chapter_type_filter` with `niche` param + substring matching
- [x] Update call site in `write_from_blueprint` to pass `niche`
- [x] Fix niche key matching (substring, not exact — consistent with `_get_niche_prompt`)

## Git
- [x] Committed all changes
