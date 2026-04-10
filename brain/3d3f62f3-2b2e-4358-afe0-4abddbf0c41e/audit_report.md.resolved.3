# Style Analyzer Data Collection Audit

## Pipeline Overview

```
scan_script_files() → group by folder
    ↓
For each script folder:
    Step 1a: analyze_overview()    — ALL chapters → 1 API call → Voice DNA
    Step 1b: analyze_chapter_detail() — per chapter, PARALLEL → Method Analysis
    Save: _STYLE_ANALYSIS.json (overview + chapter_details)
    ↓
Step 3: cross_chapter_analysis()  — Python, no API → statistics
Step 4a: synthesize (Phase 1)     — foundation: core_rules, techniques, openings, closings
Step 4b: synthesize (Phase 2)     — frameworks: using Phase 1 output
    ↓
_inject_computed_sections()       — Python: diversity_rules + content_patterns
Save: _STYLE_GUIDE.json
```

---

## Issues Found

### 🔴 Issue 1: Chapter order lost in parallel processing

**Location:** [style_tab.py:726-741](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/style_tab.py#L726-L741)

```python
with ThreadPoolExecutor(max_workers=threads) as executor:
    for future in as_completed(futures):  # ← completion order, NOT chapter order
        result = future.result()
        if result:
            chapter_details.append(result)  # ← appended in random order
```

`as_completed()` returns results in **whatever order they finish**, not chapter sequence. This means:
- Cross-chapter analysis compares "consecutive" chapters that aren't actually consecutive
- Opening diversity "consecutive_same_openings" count is meaningless
- Transition analysis between chapters is incorrect

**Fix:** Sort `chapter_details` by chapter name/index before saving.

---

### 🟡 Issue 2: Overview sends ALL chapter content in one request

**Location:** [style_analyzer.py:146-152](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/style_analyzer.py#L146-L152)

```python
for filename, content in file_contents:
    total_chars += len(content)
    user_parts.append(f"=== SCRIPT: {filename} ===\n{content}\n")
```

For a script with 11 chapters × ~600 words = ~40,000 chars + prompt → could hit token limits on Flash tier. No truncation or splitting logic.

**Impact:** API may silently truncate input → overview misses later chapters → voice DNA is incomplete.

---

### 🟡 Issue 3: Technique names not normalized

**Location:** [cross_chapter_analysis()](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/style_analyzer.py#L248-L279)

The AI uses inconsistent names for the same technique:
- "Contrast" vs "Juxtaposition" vs "Character Juxtaposition" vs "Systematic Contrast"
- "Metaphor" vs "Symbolic Metaphor" vs "Metaphorical Framing"

Cross-chapter analysis counts each as a separate technique → statistics are fragmented.

**Fix:** Add a normalization step (fuzzy match or mapping dict) before counting.

---

### 🟢 Issue 4: Detail prompt doesn't specify technique naming convention

**Location:** [system_style_detail.txt:26](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_style_detail.txt#L26)

```
- method: The technique name (contrast, suspense, metaphor, foreshadowing, etc.)
```

The prompt lists examples but doesn't enforce using ONLY these exact names. AI freely invents new names.

**Fix:** Add a "TECHNIQUE VOCABULARY" section with a fixed list of canonical names.

---

### 🟢 Issue 5: Cached analysis may be stale

**Location:** [style_tab.py:644-657](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/style_tab.py#L644-L657)

Cache loads `_STYLE_ANALYSIS.json` if it exists. If the prompt was updated (e.g., `content_focus` was added), old cached data won't have `content_focus` → cross-chapter analysis sees empty data.

The `force_reanalyze` flag exists ✅ but the user must manually check it.

---

## What IS Collected (per chapter)

| Data | Collected? | By Step | Quality |
|------|-----------|---------|---------|
| Opening principle + method + purpose | ✅ | Detail | Good |
| Technique name | ✅ | Detail | ⚠ Inconsistent naming |
| Technique position | ✅ | Detail | Good |
| Technique count per chapter | ✅ | Detail | Good |
| Technique purpose | ✅ | Detail | Good |
| POV shifts: count, from/to, position | ✅ | Detail | Good |
| Closing principle + method | ✅ | Detail | Good |
| Pacing | ✅ | Detail | Good |
| Content focus dimensions | ✅ | Detail | Good |
| Data types used | ✅ | Detail | Good |
| Depth pattern | ✅ | Detail | Good |
| Voice/tone patterns | ✅ | Overview | Good |
| Sentence rhythm | ✅ | Overview | Good |
| Vocabulary strategy | ✅ | Overview | Good |
| Emotional architecture | ✅ | Overview | Good |
| Structural proportions | ✅ | Overview | Good |

## Summary

The prompts collect **comprehensive data**. The main issues are:
1. **Chapter ordering** — critical bug that corrupts cross-chapter analysis
2. **Technique normalization** — fragmented statistics
3. **Token limits** — unhandled for large scripts
