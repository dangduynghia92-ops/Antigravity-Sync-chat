# Audit: Changes Affecting Biography Pipeline

All changes in `core/rewriter.py` (uncommitted) that touch code used by biography.

---

## 1. `_extract_style_for_framework` — Fallback removed → RuntimeError

**Before:** If framework not found → return full style JSON (silent fallback)
**After:** If framework not found → `raise RuntimeError`

> [!WARNING]
> **Impact on biography:** If framework name doesn't match exactly → crash instead of fallback.
> Previously safe, now dangerous if there's any name mismatch.

---

## 2. `_extract_chapter_blueprint` — Hook bypass removed

**Before:**
```python
ch_type = chapter_outline.get("chapter_type", "body")
if ch_type == "hook":
    chapter_bp = blueprint  # FULL blueprint
else:
    chapter_bp = _extract_chapter_blueprint(blueprint, chapter_outline)
```

**After:**
```python
# ALL chapters go through filtering — no exceptions
chapter_bp = _extract_chapter_blueprint(blueprint, chapter_outline)
```

> [!CAUTION]
> **Impact on biography:** Biography hook chapters now go through the filter instead of getting FULL blueprint. Hook chapters may receive LESS data than before.

---

## 3. `_extract_chapter_blueprint` — Fallback removed → RuntimeError

**Before:**
```python
_always_keys = {"core_identity", "personal_profile"}
if set(result.keys()) <= _always_keys:
    return blueprint  # silent fallback to full
```

**After:**
```python
if not _skip_fuzzy and set(result.keys()) <= _always_keys:
    raise RuntimeError("Blueprint filter extracted NOTHING for ch...")
```

> [!CAUTION]
> **Impact on biography:** If fuzzy search finds nothing for a body chapter → CRASH instead of graceful fallback to full blueprint.

---

## 4. `_extract_chapter_blueprint` — Fuzzy search algorithm changed

**Before:** Full substring match: `kd_lower in json.dumps(item).lower()`
**After:** Keyword extraction + 2+ keyword match:
```python
keywords = [w for w in kd_item.split() if len(w) > 2 and w not in STOP_WORDS]
hits = sum(1 for kw in keywords if kw in item_text)
if hits >= min(2, len(keywords)):
```

> [!WARNING]
> **Impact on biography:** Fuzzy matching is now STRICTER (needs 2+ keyword hits vs full substring). Some `key_data` items that matched before may NOT match now → less data in filtered blueprint.

---

## 5. `_extract_chapter_blueprint` — key_data field name changed

**Before:** `key_data = chapter_outline.get("key_data", [])`
**After:** `key_data = chapter_outline.get("main_key_data", chapter_outline.get("key_data", []))`

> [!NOTE]
> **Impact on biography:** Biography outline still uses `key_data` → fallback works. But if biography gets updated to use `main_key_data` without updating outline prompt, old outlines break.

---

## 6. `_extract_chapter_blueprint` — String item matching removed

**Before:**
```python
elif isinstance(item, str) and kd_lower in item.lower():
    result.setdefault(bp_key, []).append(item)
```

**After:** This branch was removed.

> [!WARNING]
> **Impact on biography:** Blueprint sections containing plain strings (not dicts) will NO LONGER be matched by fuzzy search. Only dict items are checked now.

---

## 7. `_NICHE_OUTLINE_FIELDS` — Fields reordered + removed

**Before:** `{open_loop_resolve}` and `{open_loop_plant}` were listed under "Shared"
**After:** Moved to after Mystery section

> [!NOTE]
> **Impact on biography:** `open_loop_resolve` and `open_loop_plant` are biography fields. If the write prompt uses them, they should still work since the dict still contains them. But the reorder is suspicious — verify they're still being injected.

---

## 8. `research_blueprint_multicall` — Draft failure now crashes

**Before:** Failed drafts → use empty dict `{}`
**After:** Failed drafts → `raise RuntimeError`

> [!WARNING]
> **Impact on biography:** If any of the 3 Flash draft calls fail → entire pipeline crashes instead of continuing with partial data.

---

## 9. `research_blueprint_multicall` — Expand failure now crashes

**Before:** Failed expands → fallback to draft data
**After:** Failed expands → `raise RuntimeError`

> [!CAUTION]
> **Impact on biography:** If Pro expand fails → crash instead of using the Flash draft as fallback. This is a significant regression — the old behavior was resilient.

---

## 10. `_run_enrich_phase` — Key rotation changed

**Before:** Manual loop over `gemini_keys`, try each one
**After:** Uses `call_gemini_with_rotation`

> [!NOTE]
> **Impact on biography:** Should be equivalent behavior, just cleaner code. Low risk.

---

## Summary

| # | Change | Severity | Type |
|---|--------|----------|------|
| 1 | Framework not found → crash | ⚠️ Medium | Regression |
| 2 | Hook gets filtered blueprint | 🔴 High | Regression |
| 3 | Empty filter → crash | 🔴 High | Regression |
| 4 | Stricter fuzzy matching | ⚠️ Medium | Regression |
| 5 | key_data → main_key_data priority | 🟢 Low | Compatible |
| 6 | String items no longer matched | ⚠️ Medium | Regression |
| 7 | Field reorder | 🟢 Low | Cosmetic |
| 8 | Draft failure → crash | 🔴 High | Regression |
| 9 | Expand failure → crash | 🔴 High | Regression |
| 10 | Key rotation refactored | 🟢 Low | Neutral |

**4 high-severity regressions** that break biography's resilience and data flow.
