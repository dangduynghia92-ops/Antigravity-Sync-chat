# POV Biography Niche — Task List

## Phase A: Files to Create

- [x] A1. `niches/pov_tiểu_sử.txt` — niche categories
- [x] A2. `styles/narrative_pov_tiểu_sử.json` — style JSON (NEW)
- [x] A3. `prompts/system_research_blueprint_pov.txt` — research blueprint (clone+cut)
- [x] A4. `prompts/system_narrative_phase_plan_pov.txt` — phase plan (clone+adapt)
- [x] A5. `prompts/system_validate_sub_key_pov.txt` — validate sub-key (clone+adapt)
- [x] A6. `prompts/system_narrative_outline_pov.txt` — outline (clone+cut)
- [x] A7. `prompts/system_narrative_audit_pov.txt` — audit outline (clone+simplify)
- [x] A8. `prompts/system_narrative_write_pov.txt` — writer prompt (NEW)
- [x] A9. `prompts/system_narrative_review_pov.txt` — review (clone+adapt)
- [x] A10. `prompts/system_enrich_blueprint_pov.txt` — enrich (NEW, light)
- [x] A11. `prompts/system_extract_blueprint_pov.txt` — extract (clone+adapt)
- [x] A12. `prompts/system_audit_pov_blueprint.txt` — audit blueprint
- [x] A13. `prompts/system_crossref_pov_blueprint.txt` — crossref blueprint

## Phase B: Code Wiring

- [x] B1. Research sections in rewriter.py (3 POV sections + _NICHE_RESEARCH_MAP)
- [x] B2. Dispatch maps (7 narrative + extract + enrich + audit + crossref)
- [x] B3. Niche detection branching (_is_pov at 2 locations)
- [x] B4. Body structures (3 POV structures + alias)
- [x] B5. Always-include keys (age_timeline, physical_state_arc)

## Phase C: Verification

- [ ] C1. JSON validation
- [ ] C2. Dispatch coverage test
- [ ] C3. Biography regression test
- [ ] C4. Git commit
