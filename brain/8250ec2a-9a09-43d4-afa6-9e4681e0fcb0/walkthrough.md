# Walkthrough: Location Reference Toggle

## What Changed

### 1. UI — [video_prompt_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py)

- Added `Location Ref` checkbox (default **ON**) next to Safety/Quality/Historical
- Tooltip: "ON = tạo location reference file (Step 2c) / OFF = mô tả location inline trong prompt"
- Passed as `constraints["location_ref"]` to pipeline

### 2. Pipeline — [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

**6 change points:**

| # | Where | What |
|---|---|---|
| 1 | `run()` | Skip Step 2c → mark "Skipped (inline mode)" |
| 2 | `STEP4_USER_TEMPLATE_INLINE` | New template — no `[Location-Label]`, environment described per shot type |
| 3 | `_process_sequence_step3()` | Runtime `.replace()` on Step 3 prompt: `location_anchor` instead of `locked_location` |
| 4 | `_build_mini_bible()` | Skip location refs when inline mode |
| 5 | `_process_sequence_step4()` | Select template + use `location_anchor` for location field |
| 6 | (auto) | Sheet 2 location rows auto-skipped (empty `locations_data`) |

## Behavior Summary

| | `Location Ref = ON` | `Location Ref = OFF` |
|---|---|---|
| Step 2c | Runs → creates location labels | **Skipped** |
| Step 3 | `locked_location` = label ref | `location_anchor` = descriptive text |
| Step 4 prompt | `[Tigris River - Mid-Stream]` bracket | Natural prose: "turbulent black river water beneath rough timber logs" |
| Step 4 template | `STEP4_USER_TEMPLATE` | `STEP4_USER_TEMPLATE_INLINE` |
| Excel Sheet 1 Location col | Label | Descriptive anchor |
| Excel Sheet 2 | Character + Location rows | Character rows only |

## Key Design Decision

The inline template instructs LLM to **adapt environment description to shot type**:
- **Wide Shot** → full panorama (landscape, architecture, sky)
- **Medium Shot** → immediate surroundings (walls, objects, ground)
- **Close-up** → only what camera sees (texture, object surface) + subtle ambient hints

This avoids the current problem where every scene (including close-ups) gets the same generic `[Location-Label]`.

## Testing
- Both files pass syntax check ✅
- Feature is backward-compatible: default = ON = current behavior unchanged
