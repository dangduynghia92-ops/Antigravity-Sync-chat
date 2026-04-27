# Video Prompt Pipeline — Implementation

## Phase 1: Core Modules
- [x] Examine existing codebase for reuse (srt_parser, api_client, process_controller)
- [x] Create `core/srt_sentence_parser.py` — SRT → sentences with interpolation
- [x] Create `core/video_pipeline.py` — Main pipeline orchestrator (4 steps)
- [x] System prompts embedded in video_pipeline.py (Steps 1-3)

## Phase 2: UI
- [x] Create `ui/video_prompt_tab.py` — Tab widget
- [x] Register tab in `ui/main_window.py`

## Phase 3: Verification
- [x] Import check — all modules load OK
