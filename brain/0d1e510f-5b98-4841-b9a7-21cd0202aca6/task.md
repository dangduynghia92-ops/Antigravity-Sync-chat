# Source Map Implementation — Biography Pipeline

## Phase 1: Prompt
- [/] Update `system_narrative_phase_plan_biography.txt` — add `_source_map` to output schema

## Phase 2: Code — rewriter.py
- [ ] `generate_narrative_phase_plan` — validate `_source_map` after AI returns, raise if missing
- [ ] `validate_phase_plan_sub_keys` — update `_source_map` when promoting/demoting items
- [ ] `_extract_chapter_blueprint` — add `source_map` param, use paths for biography, raise if missing
- [ ] `write_from_blueprint` — add `source_map` param, enforce for biography body chapters

## Phase 3: Code — script_creation_tab.py
- [ ] `_run_shared_fw_pipeline` — extract `_source_map` from phase plan, pass to write_from_blueprint

## Phase 4: Verification
- [ ] Git commit
- [ ] Test with Galileo biography
