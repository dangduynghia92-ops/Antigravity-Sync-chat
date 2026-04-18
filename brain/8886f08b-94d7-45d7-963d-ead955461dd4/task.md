# Fix Blueprint Data Loss & Optimize Pipeline

## Phase 1: Data Loss Fix (DONE)
- [x] Bug 1: Fix `_strip_source_tags()` to recognize `{"fact", "source"}` format
- [x] Bug 2: Add array-safe guard to correction application code
- [x] Bug 3: Harden Reality Check prompt for array field corrections
- [x] Verify fixes with offline test

## Phase 2: Optimize Step 5 Enrichment (DONE)
- [x] Remove Step 5a (`verify_specs_google`) + cleanup `_SPEC_NICHES`
- [x] Reorder: Wave 1 (5b + 5c parallel) → Wave 2 (5d rhetoric sequential)
- [x] Verify compilation passes
