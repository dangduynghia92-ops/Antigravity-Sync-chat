# Resume & Checkpoint — Top/List Mode Extension

## Context
Narrative mode already has resume + checkpoint saving. Top/List mode (`_do_renew_style`) needs the same.

**Key insight**: Steps 5-8 (outline→audit→write→review→merge) already use `_run_shared_fw_pipeline` which has `resume=True` support. Only Steps 1-4 need new checkpoint logic.

---

## Proposed Changes

### 1. Save `_resume.json` in Top/List pipeline

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

In `_do_renew_style` → `_run()`, right after `os.makedirs(pipeline_dir)` (line ~3288):

```python
_resume_meta = {
    "mode": "Top/List Review",
    "type": "rewrite",
    "niche": _niche,
    "style": style_info,
    "lang": lang,
    "started_at": datetime.now().isoformat(timespec="seconds"),
}
_resume_path = os.path.join(pipeline_dir, "_resume.json")
with open(_resume_path, "w", encoding="utf-8") as f:
    json.dump(_resume_meta, f, indent=2, ensure_ascii=False)
```

---

### 2. Checkpoint detection in Steps 1-4

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

Add `resume=False` param to `_do_renew_style`. When `resume=True`, check files before each step:

| Step | Checkpoint file | Resume action |
|---|---|---|
| Step 2: Detect | `_detection.json` | Load → skip detect |
| Step 3: Blueprint | `_blueprint.json` | Load → skip extract |
| Step 3.5: Enrich | `_enrichment.json` | Load → skip enrich |
| Step 4: Framework | `_rankings.json` | Load → skip ranking |

---

### 3. Update `_do_resume` for Top/List

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

Remove mode restriction. Handle both:
- `mode == "Narrative"` + `type == "new_content"` → existing resume logic
- `mode == "Top/List Review"` + `type == "rewrite"` → call `_do_renew_style` with `resume=True`

For Top/List resume: need to re-build `checked` chapters from source files.
**Problem**: Top/List rewrite starts from input chapters (checked files) — but resume may not have these loaded.
**Solution**: When `type == "rewrite"`, require user to have the input folder loaded in the tree, OR skip Steps 1-3 if blueprint already exists.

**Simpler approach**: Top/List resume only needs `_blueprint.json` (already saved). Steps 1-3 produce the blueprint. If blueprint exists → skip to Step 4+.

---

### 4. Pass `resume` through to `_run_fw_pipeline`

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

In `_run_fw_pipeline` (line ~3498), pass `resume=resume` to `_run_shared_fw_pipeline`.

---

## Checkpoint file summary (both modes)

| File | Saved by | Used for resume |
|---|---|---|
| `_resume.json` | Step 0 (both modes) | Mode/type detection |
| `_detection.json` | Step 2 (Top/List only) | Skip framework detection |
| `_blueprint.json` | Step 3 (Top/List) / Step 1 (Narrative) | Skip blueprint extraction |
| `_enrichment.json` | Step 3.5 (Top/List) | Skip enrichment |
| `_rankings.json` | Step 4 (both) | Skip framework ranking |
| `_phase_plan.json` | Step A1 (Narrative bio) | Skip phase planning |
| `_phase_plan_validated.json` | Step A2 | Skip validation |
| `_phase_plan_final.json` | Step A3 | Skip split |
| `_renew_outline.json` | Step B | Skip outline generation |
| `_renew_outline_audited.json` | Step C | Skip audit |
| `ch_XX_*.txt` | Step D | Skip written chapters |
| `FULL_SCRIPT.txt` | Step F | Skip entire version |

## Verification
1. Run Top/List rewrite → Stop at Step 5 → Resume → verify Steps 1-4 skip
2. Run Top/List rewrite → Stop at ch.3 → Resume → verify ch.1-2 loaded, ch.3 re-written
