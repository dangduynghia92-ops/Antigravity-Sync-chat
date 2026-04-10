# Narrative Pipeline Audit — Final Report

## Bugs Found & Fixed

### 1. `{open_loop_plant}` / `{open_loop_resolve}` Not Injected (Mystery)
- **File**: [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py#L441-L442)
- **Bug**: Mystery writer prompt uses `{open_loop_plant}` and `{open_loop_resolve}` but they were **missing** from `_NICHE_OUTLINE_FIELDS` → AI received literal `{open_loop_plant}` text
- **Fix**: Added both to `_NICHE_OUTLINE_FIELDS`

### 2. `recommend_framework_biography()` Called For All Niches (Rewrite)
- **File**: [rewrite_style_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_style_tab.py#L3042-L3050)
- **Bug**: Rewrite tab called biography-specific pre-scoring for mystery/battle → crash on wrong prompt
- **Fix**: Rewrite now uses generic `recommend_framework()` for ALL niches

### 3. `generate_phase_plan()` Crashes Mystery/Battle
- **File**: [rewrite_style_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_style_tab.py#L1610-L1632)  
- **Bug**: Phase Plan ran for all niches but only biography has prompt → RuntimeError
- **Fix**: Guarded with `_is_biography` check — skip for non-biography niches

### 4. Audit Prompts Inconsistent Format (Mystery/Battle)
- **Files**: `system_narrative_audit_mystery.txt`, `system_narrative_audit_battle.txt`
- **Bug**: Mystery/Battle asked AI to return full outline copy (wasteful + error-prone)
- **Fix**: Unified to diff-based format matching biography

### 5. `set` Action Only Updated Existing Fields
- **File**: [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py#L3175-L3178)
- **Bug**: `if field and field in chapters[ch_idx]` blocked adding new fields
- **Fix**: Removed `field in chapters[ch_idx]` check

### 6. `research_blueprint_multicall()` Not Niche-Aware (New Content)
- **File**: [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py#L1662-L1693)
- **Bug**: Hardcoded biography research sections, used by all niches
- **Fix**: Added `_NICHE_RESEARCH_MAP`, unsupported niches get RuntimeError

---

## Function Renames

| Old Name | New Name | Scope |
|---|---|---|
| `recommend_framework_biography()` | `recommend_framework_new_content()` | New Content only |
| `generate_phase_plan()` | `generate_narrative_phase_plan()` | Shared (biography-guarded) |
| `generate_renew_outline_v2()` | `generate_narrative_outline()` | Shared |

---

## Final Pipeline State Per Niche

### Biography ✅
| Step | Function | Prompt |
|---|---|---|
| Research | `research_blueprint_multicall(niche=)` | 3 sections hardcoded |
| Extract | `extract_blueprint(niche=)` | `system_extract_blueprint_biography.txt` |
| Recommend | `recommend_framework_new_content(niche=)` (NC) / `recommend_framework()` (RW) | `system_recommend_framework_biography.txt` |
| Phase Plan | `generate_narrative_phase_plan()` | `system_narrative_phase_plan_biography.txt` |
| Outline | `generate_narrative_outline()` | `system_narrative_outline_biography.txt` |
| Audit | `audit_outline()` | `system_narrative_audit_biography.txt` (diff-based) |
| Write | `write_from_blueprint()` | `system_narrative_write_biography.txt` |
| Review | `review_narrative_full()` | `system_narrative_review_biography.txt` |

### Mystery ✅
| Step | Function | Prompt |
|---|---|---|
| Research | ❌ Not supported → RuntimeError | N/A |
| Extract | `extract_blueprint(niche=)` | Uses generic (no mystery-specific extract prompt) |
| Recommend | `recommend_framework()` | Generic AI scoring |
| Phase Plan | ⏭️ Skipped (biography only) | N/A |
| Outline | `generate_narrative_outline()` | `system_narrative_outline_mystery.txt` |
| Audit | `audit_outline()` | `system_narrative_audit_mystery.txt` (diff-based ✅) |
| Write | `write_from_blueprint()` | `system_narrative_write_mystery.txt` |
| Review | `review_narrative_full()` | `system_narrative_review_mystery.txt` |

### Battle ✅
| Step | Function | Prompt |
|---|---|---|
| Research | ❌ Not supported → RuntimeError | N/A |
| Extract | `extract_blueprint(niche=)` | Uses generic (no battle-specific extract prompt) |
| Recommend | `recommend_framework()` | Generic AI scoring |
| Phase Plan | ⏭️ Skipped (biography only) | N/A |
| Outline | `generate_narrative_outline()` | `system_narrative_outline_battle.txt` |
| Audit | `audit_outline()` | `system_narrative_audit_battle.txt` (diff-based ✅) |
| Write | `write_from_blueprint()` | `system_narrative_write_battle.txt` |
| Review | `review_narrative_full()` | `system_narrative_review_battle.txt` |

---

## Verification Results

- ✅ All 15 prompt files exist
- ✅ All function imports work (`RewriteStyleTab` loads successfully)
- ✅ No stale function names remain in codebase
- ✅ All `_NICHE_OUTLINE_FIELDS` placeholders match write prompts
- ✅ `_NICHE_PROMPT_MAP` covers all 3 niches for outline/audit/write/review
- ✅ `get_ch_range()` has default fallback in both New Content and Rewrite
