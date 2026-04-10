# Dual-Framework Parallel Execution — Implementation Plan

## Goal
Auto-select top 2 frameworks (score ≥ 8.5) → run Steps 5-8 in parallel → output 2 script versions.

## Directory Structure

```
output_dir/
├── _pipeline/                          ← shared (steps 1-3.5)
│   ├── _merged.txt
│   ├── _original_framework.json
│   ├── _blueprint.json
│   ├── _enrichment.json
│   └── _rankings.json
│
├── v1_Investigative_Deep_Dive/         ← framework 1 output
│   ├── _pipeline/
│   │   ├── _renew_outline.json
│   │   ├── _audit.json
│   │   └── _review.json
│   ├── ch_01_*.txt
│   ├── ch_02_*.txt
│   └── FULL_SCRIPT.txt
│
└── v2_Zoom_Lens/                       ← framework 2 output
    ├── _pipeline/
    │   ├── _renew_outline.json
    │   ├── _audit.json
    │   └── _review.json
    ├── ch_01_*.txt
    ├── ch_02_*.txt
    └── FULL_SCRIPT.txt
```

## Proposed Changes

### UI — `rewrite_style_tab.py`

#### Step 4 logic change (L2277-2382)

**Current**: Popup → user picks 1 framework → `selected_fw` (string)

**New logic** (when `user_framework == "Auto (detect & switch)"`):
1. AI ranks frameworks (unchanged)
2. Filter: `top_fws = [r for r in rankings if r['score'] >= 8.5][:2]`
3. Cases:
   - `len(top_fws) == 0` → log error, ask user via popup (fallback to current behavior)
   - `len(top_fws) == 1` → auto-select, continue single-thread (current flow)
   - `len(top_fws) == 2` → auto-select both, log info, split into 2 threads

#### Steps 5-8: Extract into reusable function

Extract current steps 5-8 (L2384-2618) into:
```python
def _run_framework_pipeline(
    self, fw_name, blueprint, style_json_raw, 
    output_dir, pipeline_dir, endpoints, 
    lang, tier, log_api, _stopped, log, ...
):
    """Run steps 5-8 for a single framework."""
```

#### Parallel execution (when 2 frameworks selected)

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=2, thread_name_prefix="fw") as pool:
    fut1 = pool.submit(_run_framework_pipeline, top_fws[0], ...)
    fut2 = pool.submit(_run_framework_pipeline, top_fws[1], ...)
    # Wait for both
    for fut in as_completed([fut1, fut2]):
        fut.result()  # raise exceptions if any
```

#### Output directory naming

```python
def _fw_dir_name(idx, fw_name):
    safe = fw_name.replace(" ", "_").replace(".", "")
    return f"v{idx}_{safe}"
# Example: "v1_The_Investigative_Deep_Dive"
```

> [!WARNING]
> Each thread needs its own `APIClient` instances (thread-safe). Current pattern already creates new `APIClient` per step — this is correct.

> [!IMPORTANT]  
> `_stopped()` check must work across both threads. Current `threading.Event` is thread-safe — OK.

## Key Design Decisions

1. **No popup for dual-framework** — auto-selects silently, logs both choices
2. **Popup fallback** — if no framework scores ≥ 8.5, fall back to popup (current behavior)
3. **Single framework = no directory nesting** — if only 1 qualifies, use current flat output (no `v1_` prefix)
4. **Shared data** — blueprint, enrichment, rankings stay in parent `_pipeline/`
5. **Independent stop** — user can stop both threads with the same stop button

## Verification
- Test with Lepanto (expect 2+ frameworks ≥ 8.5)
- Test with content that only matches 1 framework
- Verify shared files not duplicated
- Verify both threads can write without conflicts
