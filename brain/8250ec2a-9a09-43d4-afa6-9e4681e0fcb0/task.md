# Step 0: SRT + TXT Alignment — Task Tracker

## Phase 1: Core Functions (srt_sentence_parser.py)
- [x] `save_as_srt()` — write corrected segments to SRT file
- [x] `correct_srt_with_txt()` — LLM correction (text fix + punctuation)
- [x] `verify_corrected_srt()` — code-based verification
- [x] LLM retry logic on verify fail

## Phase 2: Pipeline Integration (video_pipeline.py)
- [x] Constructor: accept `chapter_pairs`
- [x] Step 0 flow: aligned/ folder + per-chapter checkpoint
- [x] Parse aligned SRTs → sentences (existing parser)

## Phase 3: UI (video_prompt_tab.py)
- [x] Tree: 4 columns [Chapter | SRT | TXT | Status]
- [x] Scan: SRT first → auto-pair TXT
- [x] Validation: block run if missing TXT
- [x] Remove Style column/buttons
- [x] Update `_get_projects()` data structure
- [x] Update `_add_srt_files()` for new format

## Phase 4: Verify
- [ ] Test with Saladin ch_01 SRT+TXT
- [ ] Syntax check all modified files ✅ (done)
