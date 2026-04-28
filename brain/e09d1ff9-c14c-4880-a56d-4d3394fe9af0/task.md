# Video Pipeline Redesign — Task List

## Phase 1: Style File ✅
- [x] Add `=== LOCATION STYLE ===` section to `Chibi Storybook Historical.txt`
- [x] Generic `_parse_style_section()` helper

## Phase 2: Pipeline Core (`video_pipeline.py`) ✅
- [x] `__init__` accepts `srt_paths: List[str]`
- [x] Step 0: Multi-file parse + merge with chapter markers + timing offset
- [x] Step 2a: Multi-angle character sheet prompt
- [x] Label extraction after Step 2 (`_extract_valid_labels`)
- [x] Step 3: 1 call per sequence + `costume_note` + label validation
- [x] Step 4: LLM writes flat_prompts + mini-bible + prev/next context
- [x] Step 5: Export with Chapter col, LOCATION STYLE for backgrounds
- [x] `run()` updated with 6-step flow + label extraction
- [x] Import test ✅

## Phase 3: UI (`video_prompt_tab.py`) ✅
- [x] Folder group → all files in same folder = 1 pipeline
- [x] Single file → 1 pipeline (backward compat)
- [x] Status updates for all items in group
- [x] Import test ✅

## Phase 4: Verify
- [ ] Run on Baldwin IV dataset
- [ ] Check label consistency across chapters
- [ ] Check flat_prompt quality
