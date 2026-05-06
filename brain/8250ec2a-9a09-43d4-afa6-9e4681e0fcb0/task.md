# Location Reference Toggle — Task Tracker

## Phase 1: UI
- [x] Add `Location Ref` checkbox to config area
- [x] Pass to constraints dict

## Phase 2: Pipeline — video_pipeline.py
- [x] `run()`: skip Step 2c when `location_ref=False`
- [x] Step 3 prompt: alt rule for `location_anchor`
- [x] Step 4 template: `STEP4_USER_TEMPLATE_INLINE`
- [x] Step 4 `_build_mini_bible()`: branch for inline mode
- [x] Step 4 `_process_sequence_step4()`: select template + location field

## Phase 3: Verify
- [x] Syntax check all files ✅
