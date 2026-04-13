# Task: Pirate History Narrative Pipeline

## Phase A: Files to Create
- [ ] A1. Style JSON (`narrative_lịch_sử_hải_tặc.json`)
- [ ] A2. Research Blueprint Prompt (`system_research_blueprint_pirate.txt`)
- [ ] A3. Phase Plan Prompt (`system_narrative_phase_plan_pirate.txt`)
- [ ] A4. Validate Sub-Key Prompt (`system_validate_sub_key_pirate.txt`)
- [ ] A5. Outline Prompt (`system_narrative_outline_pirate.txt`)
- [ ] A6. Audit Prompt (`system_narrative_audit_pirate.txt`)
- [ ] A7. Writer Prompt (`system_narrative_write_pirate.txt`)
- [ ] A8. Review Prompt (`system_narrative_review_pirate.txt`)

## Phase B: Code Wiring
- [ ] B1. Dispatch Maps (all 7 in `_NICHE_PROMPT_MAP`)
- [ ] B2. Research Sections (3 constants + `_NICHE_RESEARCH_MAP`)
- [ ] B3. `_RESEARCH_PROMPT_MAP` in `research_blueprint()`
- [ ] B4. Niche Detection (`_extract_chapter_blueprint`, `write_from_blueprint`, `validate_phase_plan_sub_keys`)
- [ ] B5. Outline Fields (`_NICHE_OUTLINE_FIELDS`)
- [ ] B6. Key Normalization (`_KEY_NORMALIZE`)
- [ ] B7. Research blueprint log update

## Phase C: Verification
- [ ] C1. Pre-flight check (JSON valid, prompts exist, dispatch maps correct)
- [ ] C2. Regression test (biography + battle dispatch still correct)
- [ ] C3. Git commit
