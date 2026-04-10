# Migration: Download Backend to pytubefix + youtube-transcript-api

## Goal
Replace yt-dlp as primary downloader with:
- **`pytubefix`** → video download, video info, thumbnail
- **`youtube-transcript-api`** → transcript download
- **`yt-dlp`** → fallback only

## Test Results

| Feature | Library | Result |
|---|---|---|
| Video info (title, length, author) | pytubefix | ✅ Works |
| Thumbnail URL | pytubefix | ✅ `yt.thumbnail_url` → `https://i.ytimg.com/vi/{id}/sddefault.jpg` |
| Video 1080p stream | pytubefix | ✅ itag 137 (mp4), 248 (webm), 399 (av01) |
| Captions | pytubefix | ✅ `yt.captions['a.en']` |
| Transcript (380 snippets) | youtube-transcript-api | ✅ `text + start + duration` |
| Proxy | pytubefix | ✅ `proxies={"https": "..."}` |

## Proposed Changes

### [MODIFY] [yt_downloader.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/yt_downloader.py)

#### Functions to migrate:

| Function | Current (yt-dlp) | New (primary) | Fallback |
|---|---|---|---|
| `get_video_info()` | subprocess yt-dlp | `pytubefix.YouTube` | yt-dlp |
| `download_video()` | subprocess yt-dlp | `pytubefix` stream download | yt-dlp |
| `download_thumbnail_file()` | yt-dlp metadata + requests | `yt.thumbnail_url` + requests | yt-dlp |
| `get_transcript_ytdlp()` | subprocess yt-dlp json3 | `youtube-transcript-api` | yt-dlp → ScrapeCreators |
| `scan_playlist()` | subprocess yt-dlp | `pytubefix.Playlist` | yt-dlp |

#### Functions unchanged:
- `extract_channel_name()`, `normalize_timestamp()`, `extract_timestamps()`, `build_transcript_file()`
- All Excel functions (`save_scan_to_excel`, `load_excel_*`, `update_excel_*`)
- `_format_transcript()`, `_format_upload_date()`, `_format_duration()`

### [MODIFY] [video_cutter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/video_cutter.py)

- Video download in cutter also uses yt-dlp subprocess → migrate to pytubefix
- Keep yt-dlp as fallback

## User Review Required

> [!IMPORTANT]
> This is a large refactoring (5+ functions in `yt_downloader.py`). 
> Do you want me to migrate all at once or one function at a time?

> [!WARNING]
> `pytubefix` depends on `nodejs-wheel-binaries` (41MB) → bundles Node.js automatically.
> Cookie file support is NOT available in pytubefix (uses OAuth instead).
> Current cookie manager system will only be used for yt-dlp fallback.

## Verification Plan

### Automated Tests
1. Test `get_video_info()` with pytubefix → verify title, length, chapters
2. Test `download_video()` → verify 1080p video-only download
3. Test `download_thumbnail_file()` → verify image saved
4. Test transcript download → verify text content
5. Test fallback to yt-dlp when pytubefix fails
