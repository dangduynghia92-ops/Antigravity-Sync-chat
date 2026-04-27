# Video Prompt Pipeline — Walkthrough

## Files Created

| File | Description |
|---|---|
| [srt_sentence_parser.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/srt_sentence_parser.py) | SRT → Sentences with linear interpolation timing |
| [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py) | 4-step pipeline orchestrator with LLM system prompts |
| [video_prompt_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py) | UI tab: Config + Pipeline Progress + Actions + Log |

## Files Modified

| File | Change |
|---|---|
| [main_window.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/main_window.py) | Added `VideoPromptTab` as Tab 3 |

## Architecture

```
SRT File → [Step 0] Python Parse → _step0_sentences.json
         → [Step 1] LLM Chunking → _step1_sequences.json
         → [Step 2a] LLM Characters → _step2_characters.json
         → [Step 2b] LLM Locations → _step2_visual_bible.json
         → [Step 3] LLM Storyboard → _step3_scenes.json (batched, threaded)
         → [Step 4] Python Assembly → _step4_final_prompts.json
```

## Key Decisions

- **System prompts embedded** in `video_pipeline.py` (not external .txt files) — keeps pipeline self-contained
- **Checkpoint/Resume**: Each step checks for existing file → skips if found. "Resume" = same as "Run"
- **2-Tier model**: B2 uses Pro (characters/locations need depth), B1/B3 use Flash
- **Tail Correction**: ≤10% timing error auto-fixed, >10% rejected + retried
- **audio_sync validation**: Warns if coverage <50% of full_text

## Verification

```
✅ Import check: all 3 modules import successfully
```
