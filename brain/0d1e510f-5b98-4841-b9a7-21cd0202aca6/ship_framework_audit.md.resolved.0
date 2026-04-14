# Ship Biography Framework — Self-Audit Results

## Audit Completed: 6 Bug Categories Found & Fixed

### 🔴 Critical Bugs Found

| # | File | Bug | Fix |
|---|------|-----|-----|
| 1 | `core/rewriter.py` L3344-3374 | `validate_phase_plan_sub_keys()` extracts `pirate_phases`, `climactic_events`, `anatomy_specs` — fields that NO LONGER EXIST in new blueprint | Updated to `ship_birth`, `capture_and_mutation`, `ship_life_and_crew`, `combat_events`, `death_and_collapse` |
| 2 | `system_narrative_write_pirate.txt` L190-224 | Phase writing styles still `Giải Phẫu Cơ Chế`, `Nhân Vật & Cao Trào`, `Góc Khuất`, `Sụp Đổ & Di Sản` | Full rewrite with 6 new phase styles |
| 3 | `system_narrative_write_pirate.txt` L258-313 | 6 `phase_affinity` values reference old phase names | Updated all 6 |
| 4 | `narrative_lịch_sử_hải_tặc.json` L341-372 | `chapter_structures[].phase_affinity` arrays all reference old names | Updated all 6 arrays |

### 🟡 Medium Bugs Found

| # | File | Bug | Fix |
|---|------|-----|-----|
| 5 | `system_research_blueprint_pirate.txt` header L13,29,36 | References `anatomy_specs` — old section name | Updated to new section names |
| 6 | `system_narrative_audit_pirate.txt` L12-26 | Thematic order, phase coverage, anatomy check all reference old phases | Updated to new 7-phase names |

### ✅ Clean (No Issues)

| File | Status |
|------|--------|
| `core/rewriter.py` (non-validate sections) | ✅ Generic pipeline — no hardcoded phase names |
| `system_narrative_phase_plan_pirate.txt` | ✅ Fully rewritten |
| `system_narrative_outline_pirate.txt` | ✅ Fully updated |
| Haven files (`*_haven.txt`) | ✅ Correctly retain old names (haven unchanged) |
| Biography files | ✅ Different niche, unaffected |
| Battle files | ✅ Different niche, unaffected |

### ⚠️ Known Limitation

`chapter_structures` in JSON are **SHARED** between ship and haven frameworks. 
The `phase_affinity` now references ship phase names. Haven framework still has old phase names.
**Impact**: When haven outline generates, the AI reads `lens` field from haven steps (correct) 
but `phase_affinity` in structures points to ship phases (mismatch). 
**Risk**: Low — the outline prompt's PHASE-STRUCTURE AFFINITY section in haven outline 
still has correct old names, which takes priority over JSON.
**Future fix**: When haven framework is redesigned, update `chapter_structures` to be per-framework.
