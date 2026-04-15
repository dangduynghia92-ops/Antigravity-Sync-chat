# Pirate Pipeline — Phase Split Walkthrough

## Changes Made

### Structural Change: Human Engine → Daily Life + Collapse Seeds

Split 1 phase into 2, creating an **8-phase lifecycle**:

```
Hook → Blueprint → Mutation → Daily Life → Apex Test → Collapse Seeds → Death → Ghost
```

### Files Modified (6 total)

| File | Changes |
|------|---------|
| `system_research_blueprint_pirate.txt` | Split section 9 into `ship_daily_operations` (§9) + `ship_collapse_signals` (§10), renumbered §10-17 → §11-18 |
| `narrative_lịch_sử_hải_tặc.json` | Added 8th step (Collapse Seeds), updated pacing/transitions/outline_rules/act_breakdown/chapter_design |
| `system_narrative_phase_plan_pirate.txt` | Rewrote DATA CLASSIFICATION (3 categories), CAUSE-EFFECT, PHASE MAPPING (8 phases), CRITICAL RULES |
| `system_narrative_outline_pirate.txt` | Added Daily Life + Collapse Seeds lenses, updated chapter mapping (8 phases), added rule 18 (Collapse Seeds ends_with) |
| `system_narrative_write_pirate.txt` | Added Daily Life ending rule, Collapse Seeds tone rule, updated SPECIFIC TECHNIQUES (8 phases) |
| `system_narrative_audit_pirate.txt` | Updated lifecycle order, phase coverage, pirate medicine check |

### Vietnamese Cleanup (bonus)

All remaining Vietnamese phase names and examples across all 6 files converted to English:
- `act_breakdown`, `chapter_design`, `anti_framework_leak` in JSON
- Section headers 6-7 in blueprint research
- SPECIFIC TECHNIQUES + SHIP-AS-PROTAGONIST in write prompt
- Chapter mapping + lifecycle order in outline prompt
- Example text in audit prompt

### Key Design Decisions

- **Daily Life** = balanced (IMMERSIVE), not one-sided dark
- **Collapse Seeds** = clinical foreboding (CLINICAL-FOREBODING)
- **Collapse Seeds ends_with** = foreboding/dread
- **Apex Test** = 80% glory, collapse only as motivation
- **Daily Life no-bridge** = inherited from old Human Engine rule
- **Pirate Medicine** moved from Daily Life → Collapse Seeds
- **Classification rule** added to blueprint: "if removing data makes Death unexplainable → Collapse Seeds"
