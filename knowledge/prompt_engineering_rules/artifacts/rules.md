# Prompt Engineering — Mandatory Rules

## BEFORE creating or editing ANY prompt/style JSON, CHECK ALL of these:

### Rule 1: NEVER hardcode word counts
- Word count is ALWAYS set by the user via UI, passed as `{word_count_rule}` variable
- NEVER write "100-200 words", "NEVER exceed 200 words", or any specific number
- If a prompt needs to reference word count, use: "follow the word count specified by the user" or reference `{word_count_rule}`
- This applies to ALL prompts in the pipeline: write, outline, audit, review, style JSON

### Rule 2: NEVER hardcode numerical limits that should be configurable
- No fixed sentence length caps ("NEVER exceed 25 words")
- No fixed chapter count targets ("aim for 10-13 chapters")
- No minimum event counts ("must have at least X events")
- If guidance is needed, use soft language: "aim for brevity" not "NEVER exceed N"

### Rule 3: NEVER create contradicting rules
- Before adding ANY rule, check if it contradicts an existing rule in the SAME file or OTHER files in the pipeline
- If two rules say opposite things (e.g., "merge same-age events" AND "do NOT merge"), the AI will behave unpredictably
- Each rule must have a unique number — no duplicate numbering

### Rule 4: NEVER duplicate rules across prompt + style JSON
- Style JSON owns ALL style rules (sentence rhythm, opening styles, closing types, vocabulary, etc.)
- Prompts own ONLY content/structural rules that style JSON doesn't cover
- If a rule exists in style JSON, the prompt should NOT repeat it — just reference "follow the STYLE GUIDE"
- Duplication wastes tokens AND creates conflict risk when one copy is updated but the other isn't

### Rule 5: Cross-audit ALL files when changing any rule
- The POV pipeline has 11 prompts + 1 style JSON
- Changing a rule in ONE file requires checking ALL other files for:
  - Contradictions (same topic, different instruction)
  - Stale references (removed option still referenced elsewhere)
  - Hardcoded values that should match the changed rule
- NEVER report "audit complete" after checking only 1-2 files

### Rule 6: NEVER propose solutions that impose fixed quantities
- User has explicitly banned: minimum chapter counts, minimum event counts, target ranges
- The pipeline should let the AI pick based on data quality, not arbitrary numbers
- If output seems too few/many, fix the CLASSIFICATION RULES, not add quantity targets

## Files to check (POV pipeline):
1. `system_research_blueprint_pov.txt`
2. `system_extract_blueprint_pov.txt`
3. `system_enrich_blueprint_pov.txt`
4. `system_audit_pov_blueprint.txt`
5. `system_crossref_pov_blueprint.txt`
6. `system_narrative_phase_plan_pov.txt`
7. `system_validate_sub_key_pov.txt`
8. `system_narrative_outline_pov.txt`
9. `system_narrative_audit_pov.txt`
10. `system_narrative_write_pov.txt`
11. `system_narrative_review_pov.txt`
12. `narrative_pov_tiểu_sử.json` (style)

## Also applies to biography pipeline:
- Same rules apply when editing biography prompts/styles
- Check biography protection rule KI before modifying shared code
