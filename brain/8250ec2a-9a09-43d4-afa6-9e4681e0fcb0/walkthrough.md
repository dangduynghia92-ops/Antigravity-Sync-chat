# Walkthrough: Step 0 SRT+TXT Alignment

## What Changed

### 1. Core Functions — [srt_sentence_parser.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/srt_sentence_parser.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/srt_sentence_parser.py)

**New functions added (~280 lines):**
- `correct_srt_with_txt()` — Sends SRT cues + TXT original to LLM for text correction. Returns corrected `SRTSegment` list with original timing + fixed text. Includes automatic retry with error details on verify failure.
- `verify_corrected_srt()` — 5-check code verification: cue count, timecode integrity, word count ratio (±15%), proper noun preservation, empty cue detection.
- `save_as_srt()` — Writes corrected segments to standard SRT file format.
- `VerifyResult` dataclass — Holds verification result + list of error messages.

### 2. Pipeline Integration — [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

- **Constructor**: Added `chapter_pairs: List[dict]` parameter
- **Step 0 Phase A**: New alignment phase before parsing:
  - Creates `aligned/` folder next to output
  - Per-chapter: parse SRT → read TXT → LLM correct → verify → save to `aligned/`
  - Skips already-aligned chapters (file-based checkpoint)
  - Replaces `srt_paths` with aligned files for Phase B
- **Step 0 Phase B**: Existing parsing logic unchanged

### 3. UI Overhaul — [video_prompt_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py)

- **Tree columns**: `[Name, Style, Status, Progress]` → `[Chapter, SRT, TXT, Status]`
- **Scan logic**: Scans `.srt` files first, auto-pairs `.txt` by matching basename. Missing TXT shown in red.
- **Run validation**: Blocks pipeline if any chapter missing TXT pair
- **Removed**: Apply Style / Apply All buttons (style set via global combo)
- **Data format**: Tree items now store `{"srt_path", "txt_path", "basename"}` dict

## Data Flow

```
User scans folder with SRT + TXT files
    ↓
UI: Shows [Chapter | ✅ SRT | ✅/❌ TXT | Status]
    ↓
User clicks Run → validation checks all pairs
    ↓
Step 0 Phase A (per-chapter):
    SRT cues + TXT text → LLM → corrected text → code verify
    → save to aligned/ch_XX.srt
    ↓
Step 0 Phase B:
    Parse aligned/*.srt → sentences (punctuation now exists)
    ↓
Steps 1-5: unchanged
```

## Testing
- All 3 files pass syntax check ✅
- Awaiting runtime test with Saladin ch_01 SRT+TXT pair
