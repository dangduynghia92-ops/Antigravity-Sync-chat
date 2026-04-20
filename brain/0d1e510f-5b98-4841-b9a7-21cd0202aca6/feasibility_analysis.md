# Risk & Feasibility Assessment: Unified Source Map

## Blueprint Structure Comparison

| | Biography (Galileo) | Battle (Constantinople) | Pirate (Queen Anne) |
|---|---|---|---|
| **Total size** | 65K (25 sections) | 57K (16 sections) | 42K (~12 sections) |
| **Largest section** | `life_phases` 15K (6 phases × events) | `commanders` 9.3K (7 commanders) | `key_facts` ~10K |
| **Section overlap** | HIGH — person name appears in all sections | LOW — distinct topics | LOW — distinct lifecycle |
| **Event nesting** | DEEP — `life_phases.Phase.key_events[]` | FLAT — `battle_phases[].events[]` | MEDIUM — `combat_events[]` |
| **Fuzzy search risk** | HIGH — keywords match 30%+ of blueprint | LOW — military terms unique | LOW-MED |
| **Current ch blueprint size** | ~~38%~~ → 7% (with source_map) | ~15-20% (fuzzy) | ~12% (phase-section dict) |

## Risk Analysis

### Risk 1: AI Fails to Generate Good `_source_map` for Battle/Pirate
**Severity: MEDIUM** | **Probability: LOW**

Battle/pirate blueprints have simpler, flatter structure. Path format is straightforward:
```
"commanders.Constantine XI Palaiologos"      → exact commander name
"battle_phases.Naval Engagement Phase"        → exact phase name
"turning_points.Fall of the Kerkoporta Gate"  → exact moment name
```
Biography paths are MORE complex (nested: `life_phases.The Reluctant Medical Student.key_events`) and AI handled them fine (44/44 entries validated).

> [!NOTE]
> **Mitigated by**: AI validation already exists in `generate_narrative_phase_plan()`. If AI fails → pipeline stops. No silent degradation.

### Risk 2: Losing Pirate `_PHASE_SECTIONS` Determinism
**Severity: LOW** | **Probability: N/A (design choice)**

Current pirate mapping is 100% deterministic (hardcoded dict):
```python
"Bản Vẽ & Nguồn Gốc": ["ship_birth"]
"Đột Biến":           ["capture_and_mutation"]
```

Source_map would move this from hardcoded → AI-generated.

**BUT**: This is actually BETTER because:
- Hardcoded names break when framework or language changes
- Source_map is self-documenting — shows exactly which data feeds which key_data
- AI already classifies events correctly in phase plan (proven)

### Risk 3: Regression in Battle/Pirate Output Quality
**Severity: HIGH** | **Probability: LOW**

Removing fuzzy search means chapters only get data that source_map explicitly references. If AI omits a section → chapter misses data entirely.

**Mitigated by**:
- Always-include texture sections (per-niche)
- Niche section matching stays (commanders_featured, battle_phases_covered)
- COVERAGE CHECKLIST in prompt forces AI to check all sections
- Cross-check script catches gaps before deployment

### Risk 4: Breaking Existing Pipeline Runs
**Severity: LOW** | **Probability: CERTAIN**

All saved `_phase_plan_final.json` files lack `_source_map`. Strict mode → must re-run phase plan.

**Mitigated by**: Pipeline already has checkpoint resume. Only phase_plan → writing needs re-run (blueprint preserved).

### Risk 5: Prompt Engineering Effort
**Severity: LOW** | **Probability: CERTAIN**

Need to adapt SOURCE TRACING rule + COVERAGE CHECKLIST for each niche. Battle paths differ from biography paths.

**Effort**: ~30 lines per prompt × 2 niches = ~60 lines of prompt engineering.

---

## Gain Assessment — Is It Worth the Effort?

| Metric | Current (3 strategies) | Proposed (source_map) |
|---|---|---|
| Code lines in `_extract_chapter_blueprint` | ~270 | ~80 (-70%) |
| Niche-specific branches | 3 (bio/battle/pirate) | 1 (universal) + config dict |
| Adding new niche | ~40 lines code + matching logic | ~5 lines config + prompt |
| Data traceability | None for battle/pirate | Full — `_phase_plan.json` shows exactly what goes where |
| Cross-check capability | Only for biography | Universal — same `cross_check.py` for all |
| Fuzzy search false positives | Possible for battle | Eliminated |

---

## Recommendation

### ✅ Proceed — low risk, high maintainability gain

**Rationale:**
1. AI source_map output is already validated (fail-fast). Low risk of silent failure.
2. Battle/pirate blueprints are SIMPLER than biography → AI will handle paths more easily.
3. Code reduction -70% eliminates maintenance burden for 3 separate extraction strategies.
4. Cross-check becomes universal — every niche gets the same coverage audit.
5. New niche onboarding becomes trivial: add 5 lines to config + copy prompt template.

**Execution order (safe rollout):**
1. Battle v2 first (simpler, more tested, lower risk)
2. Test with Constantinople → verify output quality
3. Pirate second (after battle proves the pattern)
4. Remove fuzzy search code LAST (only after both niches pass)

> [!CAUTION]
> If battle source_map quality is bad after first test → abort pirate, keep battle on fuzzy. The architecture supports mixed modes (source_map for bio, fuzzy for battle).
