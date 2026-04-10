# Task: Queue + Skip Feature

## auto_pipeline.py — Skip Logic
- `[x]` Add `_find_existing_project(video_id)` method
- `[x]` Modify `phase1_fetch_info_and_transcript` — skip if transcript exists
- `[x]` Modify `start_video_download` — skip if video exists
- `[x]` Modify `phase2_split` — skip if chapters exist

## auto_pipeline_tab.py — Queue UI
- `[x]` Add queue data structures (`_queue`, `_queue_lock`)
- `[x]` Replace URL multi-line input → single line + Add button
- `[x]` Add QListWidget for queue display
- `[x]` Add queue management methods (add, remove, clear, refresh, retry)
- `[x]` Add Run Queue / Run Merge / Retry Failed buttons
- `[x]` Remove Save Config button, remove old multi-URL dialog
- `[x]` New `_run_queue()` loop — process pending items, allow adding while running
- `[x]` Modify `_run_single` — raise errors for queue error tracking
- `[x]` Modify `_on_pipeline_done` / `_set_running` for queue mode
- `[x]` Add `_sig_queue_refresh` signal for thread-safe queue UI updates

## Verify
- `[x]` py_compile — no syntax errors
- `[x]` Module imports OK
- `[x]` Git backup
