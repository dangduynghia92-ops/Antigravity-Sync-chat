# Video Prompt Pipeline — Implementation

## Phase 1: Core Modules
- [/] Examine existing codebase for reuse (srt_parser, api_client, process_controller)
- [ ] Create `core/srt_sentence_parser.py` — SRT → sentences with interpolation
- [ ] Create `core/video_pipeline.py` — Main pipeline orchestrator (4 steps)
- [ ] Create system prompts for Steps 1-3

## Phase 2: UI
- [ ] Create `ui/video_prompt_tab.py` — Tab widget
- [ ] Register tab in `ui/main_window.py`

## Phase 3: Testing
- [ ] Test SRT parser with real data
- [ ] Test full pipeline flow
