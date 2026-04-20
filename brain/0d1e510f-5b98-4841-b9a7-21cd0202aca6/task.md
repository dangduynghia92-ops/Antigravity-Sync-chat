# Source Map Implementation — All Niches

## Phase 1-5: Biography Source Map + Coverage Fixes ✅

## Phase 6: Unified Source Map
- [x] Battle v2: add `_source_map` to phase plan prompt (rule #9 + #10)
- [x] Pirate: add `_source_map` to phase plan prompt (rule #10 + #11)
- [x] Code: refactor `_extract_chapter_blueprint` to niche-agnostic
  - [x] `_NICHE_ALWAYS_INCLUDE` config dict
  - [x] Universal source_map path resolution
  - [x] `_extract_battle_section_matches()` helper
  - [x] `_extract_pirate_section_matches()` helper
  - [x] Remove fuzzy search (76 lines)
- [x] Code: generalize `generate_narrative_phase_plan` validation
- [x] Git commit: `752b1da`
- [ ] Test battle v2 pipeline
- [ ] Test pirate pipeline
