# Fix Language Mixing + Full Language Names

## Problem
1. Niche rules and `system_tts_verify.txt` have English-only content used for all languages
2. Language codes (`en`, `es`) used everywhere — confusing in UI and folders

## Solution

### 1. Rename Folders: `en` → `english`, `es` → `spanish`

```
prompts/
  english/                    ← was en/
    system_analyze.txt
    system_narrative_rewrite.txt
    system_review.txt
    system_rewrite.txt
    system_tts_cleanup.txt    ← already exists (copy from base)
    system_tts_verify.txt     ← NEW (English verify examples)
  spanish/                    ← was es/
    system_analyze.txt
    system_narrative_rewrite.txt
    system_review.txt
    system_rewrite.txt
    system_tts_cleanup.txt    ← already correct
    system_tts_verify.txt     ← NEW (Spanish verify examples)
  tts_niche_rules/
    english/                  ← NEW
      firearms.txt            
      history.txt             
    spanish/                  ← NEW
      firearms.txt            ← move current firearms.txt here
      history.txt             ← NEW (research + write)
  system_tts_detect_niche.txt ← shared (no lang needed)
  ... other shared prompts
```

### 2. UI Dropdown: Full Names

#### [MODIFY] [tts_tab.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/tts_tab.py)
- Dropdown: `["english", "spanish"]` instead of `["en", "es"]`
- Label: `"Language:"` instead of `"Lang:"`

#### Also check other tabs that use language dropdown

### 3. Code: Map Full Names

#### [MODIFY] [tts_cleanup.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/tts_cleanup.py)
- `_load_prompt(name, lang)` → `lang` is now `"english"` or `"spanish"`
- `load_niche_rules(niche, lang)` → add `lang` param, try `tts_niche_rules/{lang}/{niche}.txt` first

#### [MODIFY] [rewriter.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)
- Same `_load_prompt` pattern — `lang` is `"english"` or `"spanish"`

### 4. New Files to Create

| File | Description |
|---|---|
| `english/system_tts_verify.txt` | Copy from base, already correct |
| `spanish/system_tts_verify.txt` | Spanish examples: `1942 → mil novecientos cuarenta y dos` |
| `tts_niche_rules/english/firearms.txt` | English firearms rules with English pronunciations |
| `tts_niche_rules/english/history.txt` | Move current `history.txt` |
| `tts_niche_rules/spanish/firearms.txt` | Move current `firearms.txt` (already Spanish) |
| `tts_niche_rules/spanish/history.txt` | Research + write Spanish history rules |

### 5. Cleanup
- Delete old `prompts/en/` and `prompts/es/` folders after migration
- Delete old `tts_niche_rules/firearms.txt` and `tts_niche_rules/history.txt`
