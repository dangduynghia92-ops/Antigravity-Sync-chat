# Auto Pipeline — Audit Report

## Methodology
Full cross-audit of `core/auto_pipeline.py` and `ui/auto_pipeline_tab.py` against the 3 existing tabs:
- **YouTube tab** (`ui/youtube_tab.py`) — Download flow
- **Chapter tab** (`ui/chapter_tab.py`) — Split flow  
- **Style Rewrite tab** (`ui/rewrite_style_tab.py`) — Rewrite delegation

---

## ✅ No Duplication Issues Found

The new code **reuses** all existing functions with zero code duplication:

| Module | Functions Reused | Verified |
|--------|-----------------|----------|
| `yt_downloader.py` | `get_video_info`, `get_transcript_ytdlp`, `get_transcript`, `download_video`, `download_thumbnail_file`, `extract_timestamps`, `build_transcript_file`, `safe_filename` | ✅ |
| `chapter_splitter.py` | `classify_script_type`, `split_chapters`, `verify_chapters`, `punctuate_chapters`, `save_chapters`, `merge_chapters`, `save_summary` | ✅ |
| `rewrite_style_tab.py` | `_do_renew_review`, `_do_renew_style`, `_do_cut_video_for_group` (via delegation) | ✅ |
| `api_client.py` | `APIClient` | ✅ |
| `config_manager.py` | `load_api_keys`, `save_config`, `load_config` | ✅ |

---

## 🐛 Bugs Found & Fixed

### Bug 1: Transcript Parser Header Mismatch (CRITICAL)
- **File**: [auto_pipeline.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/auto_pipeline.py)
- **Issue**: Parser searched for `"Timestamps:"` and `"Transcript:"` but `build_transcript_file()` outputs `"Timestamp"` and `"Transcript"` (no colon, singular)
- **Impact**: Phase 2 would silently fail to extract transcript text, treating entire file as raw content
- **Fix**: Case-insensitive matching with `stripped.lower().startswith("timestamp")`

### Bug 2: Parent Widget Traversal Broken (CRITICAL)
- **File**: [auto_pipeline_tab.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py) `_get_rewrite_tab()`
- **Issue**: `.parent()` returns a QObject, but `hasattr(widget, 'parent')` is always True for any QObject — need `callable()` check to avoid infinite loop
- **Impact**: Could crash or loop forever when looking for MainWindow
- **Fix**: Added `callable(widget.parent)` guard

### Bug 3: Main Thread UI Deadlock (CRITICAL)
- **File**: [auto_pipeline_tab.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py) `_on_run()`
- **Issue**: `_mode_event.wait()` was called on the main thread, blocking the entire Qt event loop. The signal `_sig_ask_mode` would emit to show a dialog, but the dialog could never display because the main thread was blocked waiting
- **Impact**: App would freeze permanently when entering multiple URLs
- **Fix**: Moved the mode selection dialog inline before spawning the worker thread

### Bug 4: Output Directory State Conflict (MEDIUM)
- **File**: [auto_pipeline_tab.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py) `_run_rewrite()`
- **Issue**: `rw_tab._txt_output.setText()` was called but `_group_path` wasn't set, causing `_resolve_output_dir()` to fall back incorrectly
- **Impact**: Rewrite output could go to wrong directory
- **Fix**: Save/restore both `_txt_output` and `_group_path` on the rewrite tab

### Bug 5: Unused `_show_mode_dialog` Signal (MINOR)
- **File**: `_sig_ask_mode` signal and `_show_mode_dialog` slot were defined but became dead code after Bug 3 fix
- **Status**: Kept for potential future use (no harm)

---

## ✅ Verified Correct (No Issues)

| Area | Check | Status |
|------|-------|--------|
| Download flow | Same 3-tier transcript fallback as YouTube tab | ✅ |
| `build_transcript_file` params | All 5 params match exactly | ✅ |
| Chapter file naming | `save_chapters()` → `"Chapter N - Title.txt"`, `build_chapter_dicts()` filters `startswith("Chapter ")` | ✅ |
| `_task_counter` / `_jobs` | Both initialized in `RewriteStyleTab.__init__` | ✅ |
| `_do_cut_video_for_group` | Exists in `RewriteStyleTab` (line 1056) | ✅ |
| Threading model | Worker thread → signals for UI updates | ✅ |
| Stop/cancel propagation | `stop_event` + `_watch_stop` thread monitors `_stop_flag` | ✅ |
| Config sync | All 15+ widgets properly synced to RewriteStyleTab | ✅ |
