# Resume Pipeline Feature — Walkthrough

## What Changed

### 1. Resume Button (UI)
**File**: [auto_pipeline_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py)

- Added **🔄 Resume** button (cyan, hidden by default) in the button row
- **Appears** automatically when `_on_pipeline_done()` detects error items
- **Behavior**: Resets all `error` queue items → `pending`, sets `_resume_mode = True`, re-runs queue
- **Hides** when user clicks "Run Queue" (fresh run)

### 2. Cache Preloader
**File**: [auto_pipeline_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py)

Method `_preload_resume_cache()`:
- Scans `_pipeline/` for cached JSON artifacts
- Loads `_blueprint_raw.json` → sets `_cached_blueprint` in job dict
- This triggers the **existing v2 skip pattern** in `_do_renew_review()`, automatically skipping Steps 1-3
- Reconstructs `_cached_full_text` from chapter dicts

### 3. Steps 8-9 Cache Check  
**File**: [rewrite_style_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_style_tab.py)

Before Step 8:
- Checks for `_review_outline_audited.json` (Step 9 output)
- If found: loads cached outline, skips **both** Step 8 (outline creation, Pro tier) and Step 9 (audit, Flash tier)
- If not found: runs normally

## Resume Flow

```
Pipeline run → v2 fails at Step 9 (timeout)
                    ↓
           _on_pipeline_done() detects error
                    ↓
           Resume button appears (🔄)
                    ↓
           User clicks Resume
                    ↓
        _on_resume() resets error → pending
         _resume_mode = True
                    ↓
        _run_queue_loop() picks up pending items
                    ↓
        Phase 1-2: Auto-skip (files already exist)
                    ↓
        Phase 3: _preload_resume_cache() loads blueprint
                    ↓
        Steps 1-3: ⏭ Skipped (cached blueprint)
        Steps 4:   Re-runs (ranking, flash tier, cheap)
        Steps 5-7: Re-runs (reality check, cheap)
        Steps 8-9: ⏭ Skipped IF audited outline exists
        Steps 10+:  Runs (chapter writing — the actual output)
```

## What's SKIPPED vs RE-RUN

| Step | Cost | Resume behavior |
|------|------|----------------|
| 1 (concat text) | Free | ⏭ Skipped (cached) |
| 2 (detect framework) | Flash | ⏭ Skipped (cached) |
| 3 (extract blueprint) | **Pro** | ⏭ Skipped (cached) |
| 4 (rank frameworks) | Flash | 🔄 Re-runs |
| 5 (reality check) | Flash | 🔄 Re-runs |
| 5a-5d (enrichment) | Mixed | 🔄 Re-runs |
| 6 (completeness) | Flash | 🔄 Re-runs |
| 7 (convert units) | Free | 🔄 Re-runs |
| 8 (create outline) | **Pro** | ⏭ Skipped (if audit exists) |
| 9 (audit outline) | Flash | ⏭ Skipped (if audit exists) |
| 10-12 (write) | **Pro** | 🔄 Re-runs |

> [!NOTE]  
> Steps 5-7 re-run because wrapping 350+ lines in an if-block would require re-indenting the entire block. The cost is minimal (Flash tier only).

## Files Changed

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_style_tab.py)
