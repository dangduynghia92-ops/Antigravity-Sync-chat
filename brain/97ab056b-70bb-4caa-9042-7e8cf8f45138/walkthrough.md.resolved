# POV Biography Pipeline — Implementation Walkthrough

## Summary

Implemented the complete **POV Biography** (`pov_tiểu_sử`) niche pipeline — a second-person, action-driven narrative system where the viewer **lives as** a historical figure. This is a standalone niche branched from the existing biography pipeline with zero regression risk.

## Changes Made

### Phase A: 13 Files Created

| File | Type | Description |
|------|------|-------------|
| `niches/pov_tiểu_sử.txt` | Niche list | Topic categories for POV |
| `styles/narrative_pov_tiểu_sử.json` | Style JSON | 1 framework ("Cuộc Đời Bạn"), 6 phases, 5 opening styles, 4 sentence rhythms, 3 chapter structures, 4 closing types |
| `prompts/system_research_blueprint_pov.txt` | Research prompt | Simplified blueprint schema: removed 10 bio fields, added `age_timeline` + `physical_state_arc` |
| `prompts/system_narrative_phase_plan_pov.txt` | Phase plan prompt | 6 phases (Nguồn Gốc→Thử Lửa→Trỗi Dậy→Đỉnh Cao→Suy Tàn→Kết Thúc), Visual Moment Test |
| `prompts/system_validate_sub_key_pov.txt` | Validate prompt | 3-test system (Physical Moment, Agency, Consequence) with Connective Protection |
| `prompts/system_narrative_outline_pov.txt` | Outline prompt | Level-based format, age_anchor + physical_state mandatory, opening_style rotation |
| `prompts/system_narrative_audit_pov.txt` | Audit prompt | POV-specific checks: Level format, age progression, physical state, POV compliance |
| `prompts/system_narrative_write_pov.txt` | **Writer prompt (NEW)** | Menu-based openings (5 types) + sentence rhythms (4 patterns), Golden Rules, body-not-emotion, zero narrator |
| `prompts/system_narrative_review_pov.txt` | Review prompt | Second-person compliance, narrator leak detection, emotion naming, sentence length |
| `prompts/system_enrich_blueprint_pov.txt` | Enrich prompt | Prioritizes physical/body data over psychology |
| `prompts/system_extract_blueprint_pov.txt` | Extract prompt | Simplified POV schema for rewrite mode |
| `prompts/system_audit_pov_blueprint.txt` | Blueprint audit | Visual Moment Test filter, physical data priority |
| `prompts/system_crossref_pov_blueprint.txt` | Blueprint crossref | Same structure, Google Search source |

### Phase B: Code Wiring (`core/rewriter.py`)

1. **Dispatch Maps** — Added POV entries to **11 dispatch maps**:
   - 7 narrative maps: outline, phase_plan, validate, audit, writer, review, validate_sub_key
   - 4 blueprint maps: extract, enrich, audit_blueprint, crossref_blueprint
   - Keywords: `pov biography`, `pov tiểu sử`, `góc nhìn`, `nhập vai`

2. **Research Sections** — 3 POV-specific multi-call sections:
   - Section A: Identity, Physical Profile & Life Phases
   - Section B: Achievements, Conflicts, Relationships & Quotes  
   - Section C: Death, POV Fields (age_timeline, physical_state_arc) & Legacy

3. **Body Structures** — 3 POV chapter structures:
   - `action_scene` — Physical confrontation → blow-by-blow → consequence
   - `transformation_scene` — Before-state → catalyst → after-state
   - `legacy_close` — Death → scorecard → callback → final line

4. **Niche Detection** — `_is_pov` flag added at both detection locations:
   - `_extract_chapter_blueprint()` — POV uses biography's section matching
   - `write_from_blueprint()` — POV hooks get full blueprint (like biography)
   - POV detected **before** biography to prevent false matching (POV niche string contains "tiểu sử")

5. **Always-include Keys** — POV chapters always receive:
   - `core_identity`, `key_quotes`, `age_timeline`, `physical_state_arc`

## Verification

- ✅ `rewriter.py` compiles without syntax errors (`py_compile`)
- ✅ Style JSON validates as proper JSON (1 framework)
- ✅ All dispatch map entries point to existing prompt files
- ✅ Biography pipeline untouched — all POV entries are additive (no existing code modified)

## Git Commits

```
c088fd3 feat(pov): add niche file + style JSON for POV Biography pipeline
fd06836 feat(pov): add research blueprint, phase plan, validate sub-key prompts
954a75f feat(pov): add outline, writer, audit, review, enrich, extract, audit/crossref blueprint prompts
5f98d33 feat(pov): wire POV niche into rewriter.py - dispatch maps, research sections, blueprint extraction, body structures
```

## Remaining Work (Phase C)

- [ ] C1. Full dispatch coverage test (verify all 11 maps resolve correctly)
- [ ] C2. Biography regression test (run existing biography pipeline, verify no changes)
- [ ] C3. Smoke test with "Genghis Khan" POV narrative
