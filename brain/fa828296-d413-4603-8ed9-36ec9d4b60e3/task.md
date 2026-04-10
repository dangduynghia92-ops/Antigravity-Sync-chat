# Pipeline Restoration & Optimization

## Completed
- [x] Restore `core/auto_pipeline.py` from bytecode
- [x] Fix imports (`core.yt_utils` → `core.yt_downloader`)
- [x] Fix `classify_script_type` key (`type` → `script_type`)
- [x] Fix `verify_chapters` return type (dict, not list)
- [x] Fix all Phase 2 function signatures (audit 14 calls)
- [x] Re-apply: imports, Step 5a, image download
- [x] Re-apply: log forwarding, cached values, dual-framework
- [x] Setup git backup + auto-commit workflow
- [x] Parallelize video cutting with rewrite

## In Progress
- [/] Parallelize pipeline steps for speed
  - [ ] Step 5a + 5b run in parallel (after Step 5)
  - [ ] Image download parallel with writing (Step 9-10)
  - [ ] Dual-framework v1 ↔ v2 parallel
