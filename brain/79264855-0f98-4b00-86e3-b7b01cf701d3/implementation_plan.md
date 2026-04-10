# YouTube Downloader & Scanner Tab

Thêm tab "📥 YouTube" vào ứng dụng, cho phép scan channel/playlist và download video.

### Tools:
- **yt-dlp** → scan channel/playlist, download video/thumbnail, lấy info video
- **ScrapeCreators API** → **chỉ** dùng cho lấy transcript

## Proposed Changes

### [NEW] [yt_downloader.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/yt_downloader.py)

**yt-dlp functions:**
- `scan_playlist(url, log_cb)` → `yt-dlp --flat-playlist --dump-json` → trả `list[dict]` gồm `{title, duration, view_count, url, id}`
- `download_video(url, save_dir, options, progress_cb, log_cb)` → download video + thumbnail
  - Options: `download_thumbnail`, `audio_only`
- `get_ytdlp_version()` / `update_ytdlp()`

**ScrapeCreators function:**
- `get_transcript(url, api_key, language=None)` → `GET https://api.scrapecreators.com/v1/youtube/video/transcript`
  - Header: `x-api-key`, Params: `url`, `language`
  - Returns: `transcript_only_text` string + `transcript` array

---

### [NEW] [youtube_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/youtube_tab.py)

2 sub-tab (QTabWidget lồng):

**Sub-tab 1: 📥 Download** — URL input + Add/Paste, Bulk Add TXT, Options (Save to, ☑ Thumbnail, ☑ Transcript, ☑ Audio Only), Download Queue table, Start/Stop/Clear/Open Folder

**Sub-tab 2: 🔍 Scanner** — URL input + Scan, Results table (✓/Title/Duration/Views/URL), Export Excel/TXT, Copy URLs, Add Selected to Download

**Shared:** LogSection + yt-dlp version label + Update button + ScrapeCreators API Key input

---

### [MODIFY] [main_window.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/main_window.py)
- Thêm `YouTubeTab` vào tab widget

### [MODIFY] [requirements.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/requirements.txt)
- Thêm `yt-dlp>=2024.0.0`, `openpyxl>=3.1.0`

## Verification Plan
1. Chạy app → tab "📥 YouTube" hiển thị
2. Scanner: paste URL channel → Scan → bảng hiện danh sách video
3. Download: add URL → Start → video + thumbnail tải về
4. Transcript: nhập API key + URL → transcript tải về dạng .txt
