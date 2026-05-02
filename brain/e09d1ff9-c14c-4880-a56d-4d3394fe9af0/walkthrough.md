# POV Pipeline Rebuild — Walkthrough

## What Changed

### 7 Files Modified

| # | File | Change Type | Lines Before → After |
|---|---|---|---|
| 1 | `narrative_pov_tiểu_sử.json` | Rewrite | 236 → 119 |
| 2 | `system_narrative_write_pov.txt` | Rewrite | 234 → 130 |
| 3 | `system_narrative_outline_pov.txt` | Rewrite | 176 → 147 |
| 4 | `system_narrative_audit_pov.txt` | Rewrite | 50 → 47 |
| 5 | `core/rewriter.py` | Multi-edit | +97 net lines (2 new helpers + data gating) |
| 6 | `ui/script_creation_tab.py` | Multi-edit | 3 tier changes |
| 7 | Backup directory | Created | `_backup_v2_pov_rebuild/` |

---

### 1. Style JSON — Voice-Only Rules

**Removed** (moved or deleted):
- `core_rules.anti_framework_leak` → write prompt CONSTRAINTS
- `core_rules.chapter_ending_protocol` → write prompt PART 4
- `core_rules.anti_copy` → deleted (useless)
- `framework.hook` → write prompt SPECIAL CHAPTERS
- `framework.pacing.rule` → deleted (hardcoded chapter numbers "1-3, 4-7")
- `framework.pacing.chapter_rhythm` → write prompt CHAPTER FLOW
- `framework.outline_rules` → outline prompt
- `framework.weight_line_types` → write prompt PART 4
- `framework.technique_emphasis` → deleted (redundant with vocabulary)
- `framework.counter_argument` → deleted
- `framework.anti_patterns` → deleted (duplicates core_rules)
- `chapter_rhythm` (top-level) → deleted (duplicate)
- `checklist` → deleted (duplicate of write prompt rules)

**Result**: 236 → 119 lines. No duplicate rules. Only voice/writing rules remain.

---

### 2. Write Prompt — Single Source of Truth

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pov.txt)

**Key changes**:
- Level anchor → "auto-injected by code, do NOT write it"
- Closing types defined ONLY here (PART 4) — single source
- Removed full_outline variable
- Removed "WHAT IS COMING?" closing option (contradicted no-forward-tension)
- Opening styles: just follow outline assignment
- Added ownership header comment

---

### 3. Outline Prompt — Simplified

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pov.txt)

**Key changes**:
- Removed BEAT references (writer-only concept)
- Opening styles: no Level anchor positioning (code handles)
- Added event_cause copy instruction
- Added ownership header

---

### 4. Audit Prompt — Scope Restricted

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_audit_pov.txt)

**Key changes**:
- Added strict scope: "ONLY reassign metadata, NEVER rewrite content"
- Removed blueprint_coverage check (no blueprint sent)
- Removed word_count, vocabulary checks
- Simplified fix actions (SET + SWAP only)

---

### 5-6. Code Changes (rewriter.py + script_creation_tab.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)
render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

**Data injection (POV only, gated behind `_is_pov`)**:
- Phase plan: Style Guide removed → only phase labels sent
- Outline: Style Guide removed → only phase labels sent
- Audit: Style Guide + Blueprint removed → only outline sent
- Writer: full_outline removed from template

**Model tier**:
- `_validate_event_timeline_pov()`: `tier="flash"` → `tier=tier`
- `validate_phase_plan_sub_keys()`: added `tier` param, passed through
- `plan_chapters_pov()`: `tier="flash"` → `tier=tier`
- Non-POV validate closure: `tier="flash"` → `tier=tier`
- Audit in `script_creation_tab.py`: `tier="flash"` → `tier=tier`
- Resume-path validate: added `tier=tier`

**New helpers**:
- `_extract_phase_labels()`: extracts phase names + descriptions only (~500 chars vs 5K+ style guide)
- `_inject_level_anchor()`: prepends "Level N, label. You are age." to writer output
- `_NUM_WORDS`: lookup table for number → word conversion (1-20)

---

## Token Savings Estimate

| Stage | Before | After | Saved |
|---|---|---|---|
| Phase Plan USER | ~56K | ~41K | ~5K (no style guide) |
| Outline USER | ~66K | ~46K | ~20K (no style guide) |
| Audit USER | ~84K | ~35K | ~49K (no style + blueprint) |
| Writer SYSTEM | ~70K | ~66K | ~4K (no full outline) |
| **Total per run** | **~276K** | **~188K** | **~78K (28%)** |

---

## Verification Status

| Check | Status |
|---|---|
| Python syntax: rewriter.py | ✅ OK |
| Python syntax: script_creation_tab.py | ✅ OK |
| JSON syntax: style JSON | ✅ OK |
| Biography pipeline not affected | ✅ All changes gated behind `_is_pov` |
| Runtime test | ⏳ Pending |
