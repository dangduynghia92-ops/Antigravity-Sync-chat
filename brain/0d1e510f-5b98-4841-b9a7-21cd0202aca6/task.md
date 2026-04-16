# Battle V2 Framework Enhancement

## Completed
- [x] Add "Bóng Tối" to `_GENERAL_FWS` in `script_creation_tab.py` (2 locations)
- [x] Remove HEAD/HEART labels from battle v2 JSON (14 references)
- [x] Add `breakthrough_weapons` to battle blueprint prompt + excerpt_fields
- [x] Revamp POV strategy (max 1 shift/chapter, any vivid scene)
- [x] Add 3-beat body chapter opening (bridge → context → content)
- [x] Fix CONTEXT beat (1-5 sentences, atmosphere/tension)
- [x] Implement Battle Blueprint Audit step
  - [x] Create prompt: `system_audit_battle_blueprint.txt`
  - [x] Create function: `audit_battle_blueprint()` in rewriter.py
  - [x] Hook into pipeline in script_creation_tab.py (battle niche only, step 1.5)
  - [x] Add `additional_findings` to excerpt_fields + phase plan prompt
