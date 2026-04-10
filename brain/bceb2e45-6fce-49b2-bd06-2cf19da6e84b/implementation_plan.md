# Resume Pipeline Feature — Auto Pipeline Tab

## Problem
When the rewrite pipeline fails mid-run (e.g., v2 timeout at step 9), all cached data (steps 1-8) is on disk in `_pipeline/` but there's no way to resume from the failure point. User must re-run everything from scratch, wasting tokens and time.

## User Requirements
- **Resume button**: Hidden by default → only appears after pipeline completes with failures
- **Behavior**: Resumes from the failed step, reusing all cached `_pipeline/*.json` files
- **Scope**: Applies to the 12-step rewrite pipeline (Phase 3) — not Phase 1/2 (those already have skip logic)

## Proposed Changes

### Component 1: Rewrite Pipeline — Add Cache-Aware Steps

#### [MODIFY] [rewrite_style_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_style_tab.py)

The `_do_renew_review()` function runs steps 1-12. Each step already saves output to `_pipeline/` dir. Changes:

1. **At the start of each step**, check if the output file already exists:
   - Step 2: `_detection.json` → skip detection
   - Step 3: `_blueprint_raw.json` → skip extraction
   - Step 4: `_rankings.json` → skip ranking
   - Step 5: `_blueprint.json` + `_spec_verification.json` + `_price_enrichment.json` + `_rhetoric_transform.json` → skip reality check
   - Step 6: `_completeness_check.json` → skip completeness
   - Step 8: `_review_outline.json` → skip outline creation
   - Step 9: `_review.json` (audit result) → skip audit
   - Step 10: Check per-chapter .txt files exist → skip writing done chapters
   - Step 11: `_review.json` (cross-review) → skip
   - Step 12: `FULL_SCRIPT.txt` → skip merge

2. **New parameter**: `resume_mode: bool = False` on `_do_renew_review()`
   - When `True`, enable cache-checking at each step
   - When `False` (default), normal behavior — no change to existing flow

3. **Load cached data correctly**: When a step is skipped, load the JSON from disk and set the in-memory variables so subsequent steps work properly. Example:
   ```python
   # Step 3: Blueprint extraction
   bp_path = os.path.join(pipeline_dir, "_blueprint_raw.json")
   if resume_mode and os.path.isfile(bp_path):
       with open(bp_path, "r", encoding="utf-8") as f:
           blueprint = json.load(f)
       log("Step 3/12: ⏭ Using cached blueprint")
   else:
       # ... existing extraction code ...
   ```

---

### Component 2: V2 Failure Tracking

#### [MODIFY] [rewrite_style_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_style_tab.py)

Currently v2 spawns as a daemon thread with no result tracking. Fix:

1. **Track v2 thread and result**: After `_v2_thread.start()`, store it
2. **After v1 completes**, check if v2 thread finished successfully
3. **Return failure info**: Report which version(s) failed and at which step

#### [MODIFY] [auto_pipeline_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py)

1. **Add `_resume_info` state**: Stores the failed job's details (project_dir, version, failed_step, config snapshot)
2. **Pass `resume_mode=True`** when calling `_run_rewrite()` for resume

---

### Component 3: Resume Button UI

#### [MODIFY] [auto_pipeline_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py)

1. **Add Resume button** in the button row (after Stop, before Open Output):
   - Text: `"🔄 Resume"`  
   - Style: Blue/cyan color, hidden by default
   - `setVisible(False)` at init

2. **Show Resume button** in `_on_pipeline_done()`:
   - Check if any queue items have `status == "error"` or if v2 failed
   - If yes → `self._btn_resume.setVisible(True)`

3. **Resume click handler** `_on_resume()`:
   - Rebuild config from saved state
   - Call `_run_rewrite()` with `resume_mode=True`
   - Re-hide the button

4. **Hide Resume button** when:
   - User clicks "Run Queue" (new run)
   - User modifies the queue (adds/clears URLs)

---

## Open Questions

> [!IMPORTANT]
> **Scope clarification**: Should Resume only handle v2 failures, or also handle v1 failures? In the log example, v1 completed fine and only v2 failed. But in theory v1 could also fail.
> 
> **Current plan**: Resume handles ANY version that failed — detects which version dirs have incomplete output and resumes only those.

> [!WARNING]
> **Queue item re-run**: If the error happened at Phase 1 or 2 (not Phase 3), the Resume button won't help since those phases already have skip logic built into `_on_run`. Should Resume just re-trigger `_on_run` for error items?

## Verification Plan

### Manual Testing
1. Run a pipeline with a known flaky API endpoint
2. Wait for v2 to timeout
3. Click Resume
4. Verify: v1 output untouched, v2 resumes from failed step, v2 completes successfully
5. Verify: Resume button hides after successful completion
