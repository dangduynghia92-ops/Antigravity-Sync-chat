# Battle Niche v2 — Pipeline Unification Walkthrough

## Goal
Transition the battle niche from a single-prompt Deep-Dive system to a full pipeline matching biography's architecture: **Research Blueprint → Phase Plan → Validate Sub-keys → Outline → Write**.

## Architecture Decision

| Layer | Biography | Battle v2 |
|-------|-----------|-----------|
| Pipeline | 5-step: blueprint → phase_plan → validate → outline → write | **Same 5-step pipeline** |
| Content rules | Person-focused (ANCHOR→TWIST, life phases, dual_nature) | **Battle-specific** (in-medias-res hook, battle phases, weapon rules) |
| Framework | Multi-framework (5 options) | **Single framework**: "Giải Mã Chiến Trường" |
| Chapter design | `chapter_structure` layer (8 types) | **Phase = structure** (6 phases define writing approach) |
| Data classification | `main_key_data` (scene) + `sub_key_data` (texture) | **Same system** |

## Changes Made

### Style JSON: [narrative_phân_tích_trận_đánh_v2.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_phân_tích_trận_đánh_v2.json)
- Single framework "Giải Mã Chiến Trường" with 6 phases
- HEAD phases (Bối Cảnh, Dàn Quân) = analytical, HEART phases (Giao Tranh, Quyết Định) = visceral
- Deep-Dive techniques: central question engine, information withholding, climax revisited
- Scene hierarchy: main_key_data → full scenes, sub_key_data → fast bridges
- `pipeline_features.phase_plan = true` enables the full pipeline

---

### New Prompts (5 files)

#### [system_narrative_phase_plan_battle.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_battle.txt)
Maps blueprint data → 6 phases. Classifies events as main_key_data (scene-worthy) vs sub_key_data (texture). Based on biography phase_plan structure but with battle-specific classification criteria.

#### [system_validate_sub_key_battle.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_validate_sub_key_battle.txt)
3-test validation (Scene, Turning Point, Causal Independence) with battle-specific criteria. Includes calibration examples comparing "wind shifted" (KEEP) vs "wind blew smoke into gunners' faces" (PROMOTE).

#### [system_research_blueprint_battle.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_research_blueprint_battle.txt)
For New Content mode — AI researches a battle topic. Data fields match existing `extract_blueprint_battle` schema plus new fields: `chronological_campaign_phases`, `climactic_turning_points`, `texture_and_hooks`.

#### [system_narrative_outline_battle_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_battle_v2.txt)
Phase-based outline. Key additions vs v1:
- `main_key_data` / `sub_key_data` per chapter (from phase plan)
- `question_answered` + `question_opened` fields (question engine)
- Phase determines writing style (HEAD/HEART)
- Information withholding rules

#### [system_narrative_write_battle_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_battle_v2.txt)
Deep-Dive battle write as base, adapted for v2:
- Scene hierarchy: main_key_data → scenes, sub_key_data → bridges
- Question engine execution
- Phase-based writing style (HEAD analytical / HEART visceral)
- All Deep-Dive techniques preserved: required elements, weapon rules, adrenaline test, spoken rhythm

---

### Engine Code Changes

#### [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

**Key changes:**
1. `_NICHE_PROMPT_MAP`: Battle entries added for `narrative_phase_plan` and new `narrative_validate_sub_key`. V2 routing via `"phân tích trận đánh"` key.
2. `_get_niche_prompt`: **Longest-match-first** logic — prevents "trận" matching before "phân tích trận đánh".
3. `validate_phase_plan_sub_keys`: Added `niche` param. Niche-aware prompt loading + niche-aware blueprint excerpt builder (battle uses `battle_phases`, `commanders`, `technology_and_weapons`; biography uses `life_phases`, `conflicts`).

#### [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

**Key change:** Replaced `_is_biography` hardcode with `pipeline_features.phase_plan` check from style JSON. Any niche with `"phase_plan": true` in its style JSON now runs the full pipeline.

---

## Verification

| Test | Result |
|------|--------|
| JSON validation | ✅ All valid |
| Python syntax (rewriter.py) | ✅ OK |
| Python syntax (script_creation_tab.py) | ✅ OK |
| Niche routing: v2 niche → v2 prompts | ✅ `system_narrative_outline_battle_v2.txt` |
| Niche routing: v1 niche → v1 prompts | ✅ `system_narrative_outline_battle.txt` |
| Backward compatibility | ✅ v1 battle styles unchanged |

## Remaining
- E2E test with sample battle topic to validate full pipeline execution
