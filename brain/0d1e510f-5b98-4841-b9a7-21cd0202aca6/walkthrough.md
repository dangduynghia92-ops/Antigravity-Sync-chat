# Walkthrough: Unified Source Map for All Narrative Niches

## What Changed

### Architecture: Before → After

```
BEFORE (3 strategies, 270 lines):
├── Biography → source_map paths (55 lines)
├── Battle → section matching + fuzzy keyword search (100 lines)
├── Pirate → _PHASE_SECTIONS dict + fuzzy keyword search (60 lines)
└── Fuzzy search (76 lines, shared)

AFTER (1 unified flow, 90 lines):
├── Step 1: _NICHE_ALWAYS_INCLUDE[niche] → inject texture sections
├── Step 2: source_map path resolution (UNIVERSAL)
├── Step 3: niche section matching (outline metadata → blueprint)
│   ├── _extract_bio_section_matches()   (existing)
│   ├── _extract_battle_section_matches() (new)
│   └── _extract_pirate_section_matches() (new)
└── No fuzzy search needed
```

### Commits

| Commit | Description |
|---|---|
| `59c2a93` | Biography: add texture sections + coverage checklist rule #10 |
| `5994eed` | Workflow: add L8 lesson + update niche registry |
| `752b1da` | **MAIN**: unified source_map for all niches (-42 net lines) |

### Files Modified

| File | Change |
|---|---|
| [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py) | Refactored `_extract_chapter_blueprint` (270→90 lines), added 2 helper functions, generalized validation |
| [phase_plan_battle.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_battle.txt) | Added `_source_map` schema + rules #9-#10 |
| [phase_plan_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pirate.txt) | Added `_source_map` schema + rules #10-#11 |
| [phase_plan_biography.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_biography.txt) | Added coverage checklist rule #10 |
| [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py) | Updated comment (already generic) |
| [new-niche.md](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/.agent/workflows/new-niche.md) | Added L8 lesson + updated registry |

## Verification Status

- ✅ Biography: tested with Galileo pipeline (12/13 chapters, ch13 crash fixed)
- ⏳ Battle v2: needs test run to verify source_map output
- ⏳ Pirate: needs test run after battle confirms pattern

## Key Design Decisions

1. **Fuzzy search removed entirely** — source_map provides precise paths; niche section matching handles outline metadata fields
2. **Strict mode for all niches** — no source_map = RuntimeError (fail-fast)
3. **Always-include keys in config dict** — not hardcoded per-branch, easy to update per-niche
4. **Section matching helpers preserved** — outline metadata fields (commanders_featured, life_phase_covered, etc.) are independent from source_map and provide additional filter precision
