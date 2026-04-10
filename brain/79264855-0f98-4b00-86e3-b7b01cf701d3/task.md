# YouTube Downloader & Scanner Tab

## Planning
- [x] Explore existing codebase structure
- [x] Understand tab pattern (build_ui, signals, config, log_section)
- [x] Write implementation plan
- [x] Get user approval

## Execution
- [x] Create `core/yt_downloader.py` — backend logic (yt-dlp + ScrapeCreators)
- [x] Create `ui/youtube_tab.py` — UI tab with 2 sub-tabs (Download + Scanner)
- [x] Register tab in `ui/main_window.py`
- [x] Update `requirements.txt` with yt-dlp, openpyxl

## Refinements
- [x] Move YouTube tab to first position
- [x] Add publish date column (yyyy-mm-dd) to scanner
- [x] Sort scan results by newest first

## Verification
- [x] Dependencies installed (yt-dlp v2026.03.13, openpyxl)
- [x] Import test passed
- [x] App launches without errors
