# Battle V2 & Biography Pipeline Refinement

## Completed
- [x] Eliminate `additional_findings` data leak (prompts + code safety net)
- [x] Separate end phase from last narrative phase (battle, pirate)
- [x] Fix phase plan logging (honest `node_count`)
- [x] Implement combined hook strategy for battle v2 (opening_scene + outcome)
- [x] Update new-niche workflow with lessons learned
- [x] Add DEMOTE logic to validate sub-key step (all niches)
  - [x] Update `system_validate_sub_key_biography.txt` — DEMOTE + Connective Protection
  - [x] Update `system_validate_sub_key_battle.txt` — DEMOTE + Connective Protection
  - [x] Update `system_validate_sub_key_pirate.txt` — DEMOTE + Connective Protection
  - [x] Update `rewriter.py` — parse `demoted` items, move main→sub (backward compat)
  - [x] Add `iconic_details` to biography research Section A
