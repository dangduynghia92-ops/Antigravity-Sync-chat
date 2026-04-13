# Walkthrough: Pirate History Niche Pipeline

## Summary

Added complete narrative pipeline for **"Lịch Sử Hải Tặc"** (Pirate History) niche with **2 independent frameworks**:
- **Chiến Hạm Huyền Thoại** — for legendary ships/warships
- **Thành Trì Vô Luật** — for pirate havens/ports/strongholds

## Files Created

### Style JSON
- [narrative_lịch_sử_hải_tặc.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_lịch_sử_hải_tặc.json) — 41KB, 2 frameworks × 6 steps each, with 4 pirate-specific mandatory rules (Money Angle, Pirate Medicine, Anti-Hero Engine, Micro-Hook)

### Prompts (7 files)
| File | Size | Purpose |
|------|------|---------|
| [system_research_blueprint_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_research_blueprint_pirate.txt) | 12.7KB | 15-section blueprint with dual `anatomy_specs` (ship vs location) |
| [system_narrative_phase_plan_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pirate.txt) | 7.4KB | 6-phase mapping, hook = 3 items (shocking_fact, myth_busted, title_card) |
| [system_validate_sub_key_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_validate_sub_key_pirate.txt) | 6.4KB | 3 tests + 7 pirate anti-patterns + 6 calibration examples |
| [system_narrative_outline_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pirate.txt) | 12KB | Pirate-specific chapter fields + question engine + micro-hooks |
| [system_narrative_audit_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_audit_pirate.txt) | 6.6KB | 14 audit checks inc. Money Angle, Anti-Hero, Pirate Medicine |
| [system_narrative_write_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pirate.txt) | 21.8KB | Full writer prompt with pirate-specific mandatory rules |
| [system_narrative_review_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_review_pirate.txt) | 4.3KB | Cross-chapter review with pirate compliance summary |

## Code Changes

### [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

All changes are **additive** (adding `elif` branches, adding dict entries). Zero modifications to existing battle/biography logic.

| Change | Lines | What |
|--------|-------|------|
| Dispatch Maps | ~80-250 | +36 entries (6 keywords × 6 maps) |
| Research Sections | ~1900-1990 | 3 new `_PIRATE_RESEARCH_SECTION_*` constants + `_RESEARCH_SECTIONS_PIRATE` |
| Research Map | ~1930 | +6 entries in `_NICHE_RESEARCH_MAP` |
| Research Prompt Map | ~1672 | +6 entries in `_RESEARCH_PROMPT_MAP` |
| Niche Detection | ~377 | `_is_pirate = "pirate_phases" in blueprint` in `_extract_chapter_blueprint()` |
| Hook Strategy | ~3855 | `elif _is_pirate:` branch in `write_from_blueprint()` → filtered (lean) |
| Validate Excerpt | ~3301 | `elif _is_pirate:` branch with `pirate_phases`, `key_figures`, `climactic_events`, `anatomy_specs` |
| Outline Fields | ~586 | +8 pirate-specific placeholder fields |
| Key Normalization | ~1944 | +6 pirate key variants |

## Verification Results

```
=== STYLE JSON VALIDATION ===
  OK JSON valid: 41,332 bytes
  OK Frameworks: ['Chiến Hạm Huyền Thoại', 'Thành Trì Vô Luật']

=== PROMPT FILES VALIDATION ===
  OK All 7 files present

=== DISPATCH MAP VALIDATION ===
  OK All 6 maps × 6 keywords = 36 entries verified

=== RESEARCH MAP VALIDATION ===
  OK 3 sections confirmed

=== KEY NORMALIZATION VALIDATION ===
  OK 6 normalizations confirmed

=== REGRESSION CHECK ===
  OK biography keywords intact
  OK battle keywords intact
```

## Next Steps

1. **Smoke test** — Run the pipeline with a Ship topic (e.g., "Queen Anne's Revenge") to validate end-to-end
2. **Prompt tuning** — Review AI output quality and adjust prompt details
3. **Consider 3rd framework** — "Tiểu Sử Hải Tặc" (Pirate Biography) for individual pirates like Blackbeard, Anne Bonny
