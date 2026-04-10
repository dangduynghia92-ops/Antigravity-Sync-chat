# ScrapeCreators API Documentation Task

## Goal
Find all YouTube-related API endpoints from ScrapeCreators to support video/channel scanning and transcript retrieval.

## Checklist
- [x] Navigate to ScrapeCreators Docs
- [x] Explore sidebar for YouTube endpoints
- [x] Catalog YouTube Video endpoints (Transcript, Details, etc.)
- [x] Catalog YouTube Channel endpoints
- [x] Catalog YouTube Playlist endpoints
- [x] Catalog YouTube Search endpoints
- [x] Summarize all findings

## Findings
### YouTube Endpoints Found:
1.  **Channel Details** (GET `/v1/youtube/channel`)
2.  **Channel Videos** (GET `/v1/youtube/channel-videos`)
3.  **Channel Shorts** (GET `/v1/youtube/channel/shorts`)
4.  **Video/Short Details** (GET `/v1/youtube/video`)
5.  **Transcript** (GET `/v1/youtube/video/transcript`)
6.  **Search** (GET `/v1/youtube/search`)
7.  **Search by Hashtag** (GET `/v1/youtube/search/hashtag`)
8.  **Comments** (GET `/v1/youtube/video/comments`)
9.  **Trending Shorts** (GET `/v1/youtube/shorts/trending`)
10. **Playlist** (GET `/v1/youtube/playlist`)
11. **Community Post Details** (GET `/v1/youtube/community-post`)

---
### Detailed Catalog:

#### 1. Channel Endpoints
- **Channel Details** (GET `/v1/youtube/channel`)
  - **Description**: Get comprehensive channel information including stats and metadata.
  - **Parameters**: `channelId` (string), `url` (string), or `handle` (string).
- **Channel Videos** (GET `/v1/youtube/channel-videos`)
  - **Description**: Get a list of videos from a channel.
  - **Parameters**: `channelId` (string, required), `continuationToken` (string, optional).
- **Channel Shorts** (GET `/v1/youtube/channel/shorts`)
  - **Description**: Get a list of shorts from a channel.
  - **Parameters**: `handle` (string, required).

#### 2. Video Endpoints
- **Video/Short Details** (GET `/v1/youtube/video`)
  - **Description**: Get details for a specific video or short.
  - **Parameters**: `url` (string, required).
- **Transcript** (GET `/v1/youtube/video/transcript`)
  - **Description**: Get the transcript of a video or short.
  - **Parameters**: `url` (string, required).
- **Comments** (GET `/v1/youtube/video/comments`)
  - **Description**: Get comments for a video.
  - **Parameters**: `url` (string, required), `continuationToken` (string, optional).
- **Trending Shorts** (GET `/v1/youtube/shorts/trending`)
  - **Description**: Get trending shorts.
  - **Parameters**: None (Wait, I should double check if region is possible, but docs show none).

#### 3. Search Endpoints
- **Search** (GET `/v1/youtube/search`)
  - **Description**: Search for videos, channels, or playlists.
  - **Parameters**: `query` (string, required).
- **Search by Hashtag** (GET `/v1/youtube/search/hashtag`)
  - **Description**: Search videos by hashtag.
  - **Parameters**: `hashtag` (string, required).

#### 4. Miscellaneous Endpoints
- **Playlist** (GET `/v1/youtube/playlist`)
  - **Description**: Get videos in a playlist.
  - **Parameters**: `url` (string, required).
- **Community Post Details** (GET `/v1/youtube/community-post`)
  - **Description**: Get details of a community post.
  - **Parameters**: `url` (string, required).
