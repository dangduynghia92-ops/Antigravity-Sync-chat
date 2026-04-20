# Source Map Implementation — All Niches

## Phase 1-4: Biography Source Map ✅
- [x] Prompt + code + callers + audit + coverage fixes

## Phase 5: Coverage Gap Fixes ✅
- [x] Code: always-include texture sections
- [x] Prompt: coverage checklist rule #10

## Phase 6: Unified Source Map (Battle v2 → Pirate → Refactor)
- [/] Battle v2: add `_source_map` to phase plan prompt
- [ ] Code: refactor `_extract_chapter_blueprint` to niche-agnostic
  - [ ] `_NICHE_ALWAYS_INCLUDE` config dict
  - [ ] Universal source_map path resolution
  - [ ] Extract `_extract_battle_section_matches()` helper
  - [ ] Extract `_extract_pirate_section_matches()` helper
  - [ ] Remove fuzzy search
- [ ] Code: generalize `generate_narrative_phase_plan` validation
- [ ] Pirate: add `_source_map` to phase plan prompt
- [ ] Git commit
- [ ] Test battle v2 + verify no regression
