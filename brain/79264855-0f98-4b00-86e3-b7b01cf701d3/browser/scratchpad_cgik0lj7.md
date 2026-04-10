# ScrapeCreators YouTube Transcript API Documentation

## API Endpoint
- **URL**: `https://api.scrapecreators.com/v1/youtube/video/transcript`
- **Method**: `GET`
- **Cost**: 1 credit per request

## Authentication
- **Header**: `x-api-key`
- **Format**: `x-api-key: <YOUR_API_KEY>`

## Request Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | The full URL of the YouTube video or short. |
| `language` | string | No | 2-letter language code (e.g., 'en', 'vi', 'fr'). |

## Response Format (JSON)
The API returns a JSON object with the following structure:
- `videoId`: (string) The ID of the YouTube video.
- `type`: (string) Type of content (e.g., "video").
- `url`: (string) The original URL.
- `transcript`: (array) A list of transcript segments. Each segment contains:
    - `text`: (string) The spoken text.
    - `startMs`: (string) Start time in milliseconds.
    - `endMs`: (string) End time in milliseconds.
    - `startTimeText`: (string) Formatted start time (e.g., "0:00").
- `transcript_only_text`: (string) The full transcript text concatenated.
- `language`: (string) The detected or requested language (e.g., "English").

## Example cURL
```bash
curl "https://api.scrapecreators.com/v1/youtube/video/transcript?url=https://www.youtube.com/watch?v=VIDEO_ID" \
-H "x-api-key: YOUR_API_KEY"
```
