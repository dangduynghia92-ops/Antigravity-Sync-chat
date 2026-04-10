# Download Backend Migration

## 1. Transcript Download (youtube-transcript-api)
- [x] Migrate `get_transcript_ytdlp()` → use `youtube-transcript-api` as primary
- [x] Keep yt-dlp as fallback, then ScrapeCreators
- [x] Test transcript download

## 2. Video Info (pytubefix)
- [x] Migrate `get_video_info()` → use `pytubefix.YouTube` as primary
- [x] Keep yt-dlp as fallback
- [x] Test video info retrieval

## 3. Thumbnail Download (pytubefix)
- [x] Migrate `download_thumbnail_file()` → use `yt.thumbnail_url` + requests
- [x] Keep yt-dlp fallback
- [x] Test thumbnail download

## 4. Video Download (pytubefix)
- [x] Migrate `download_video()` → use pytubefix stream download
- [x] Migrate video download in `video_cutter.py`
- [x] Keep yt-dlp as fallback
- [x] Test video download

## 5. Playlist Scan (pytubefix)
- [x] Migrate `scan_playlist()` → use `pytubefix.Playlist`
- [x] Keep yt-dlp as fallback
- [x] Test playlist scan
