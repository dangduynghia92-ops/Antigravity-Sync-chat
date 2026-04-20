# Source Map Implementation — Biography Pipeline

## Phase 1: Prompt
- [x] Update `system_narrative_phase_plan_biography.txt` — add `_source_map` to output schema + rule #9

## Phase 2: Code — rewriter.py
- [x] `generate_narrative_phase_plan` — validate `_source_map` after AI returns, raise if missing
- [x] `_resolve_source_path` + `_extract_bio_section_matches` — helper functions
- [x] `_extract_chapter_blueprint` — add `source_map` param, use paths for biography, raise if missing
- [x] `write_from_blueprint` — add `source_map` param, forward to extract function

## Phase 3: Code — script_creation_tab.py
- [x] `_run_shared_fw_pipeline` — extract `_source_map` from phase plan, pass to write_from_blueprint
- [x] Review pipeline caller — load `_source_map` from `_phase_plan_final.json`, pass to write_from_blueprint

## Phase 4: Verification
- [/] Git commit
- [ ] Test with biography pipeline
