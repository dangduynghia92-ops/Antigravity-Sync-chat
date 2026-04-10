# Download Backend Migration — Walkthrough

## Summary

Migrated 5 core functions from `yt-dlp` subprocess to **`pytubefix`** + **`youtube-transcript-api`** as primary, keeping `yt-dlp` as fallback.

## Changes Made

### [yt_downloader.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/yt_downloader.py)

| Function | Primary → | Fallback |
|---|---|---|
| `get_transcript_ytdlp()` | `youtube-transcript-api` (new `_get_transcript_api()`) | yt-dlp subprocess |
| `get_video_info()` | `pytubefix.YouTube` (new `_get_video_info_pytubefix()`) | yt-dlp subprocess |
| `download_thumbnail_file()` | `pytubefix` `yt.thumbnail_url` + requests | yt-dlp subprocess |
| `download_video()` | `pytubefix` stream download (new `_download_video_pytubefix()`) | yt-dlp subprocess |
| `scan_playlist()` | `pytubefix.Playlist` (new `_scan_playlist_pytubefix()`) | yt-dlp two-phase |

### [video_cutter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/video_cutter.py)

- `download_video()` → pytubefix primary (1080p video-only mp4), yt-dlp fallback with cookie rotation

## Test Results

| Test | Result | Details |
|---|---|---|
| Transcript (English) | ✅ | 380 segments, `(0:00) text` format |
| Transcript (invalid video) | ✅ | API fails → yt-dlp fallback → proper error |
| Video info | ✅ | title, id, description, channel_url |
| Video info (invalid) | ✅ | pytubefix fails → yt-dlp fallback |
| Thumbnail | ✅ | `thumbnail.jpg` (77,850 bytes) |
| Video download (1080p) | ✅ | `273.9 MB` mp4, video-only stream |
| Playlist scan | ✅ | 2 videos with title, date, duration, views |

## Dependencies Added

```
pip install youtube-transcript-api pytubefix
```

> [!NOTE]
> `pytubefix` includes `nodejs-wheel-binaries` (41MB, bundled Node.js for BotGuard).
> `yt-dlp` is still required as fallback but no longer the primary download engine.
