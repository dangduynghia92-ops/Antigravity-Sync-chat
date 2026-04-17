# Battle V2 & Biography Pipeline Refinement

## Completed
- [x] Eliminate `additional_findings` data leak (prompts + code safety net)
- [x] Separate end phase from last narrative phase (battle, pirate)
- [x] Fix phase plan logging (honest `node_count`)
- [x] Implement combined hook strategy for battle v2 (opening_scene + outcome)
- [x] Update new-niche workflow with lessons learned

## In Progress
- [/] Add DEMOTE logic to validate sub-key step (all niches)
  - [ ] Update `system_validate_sub_key_biography.txt` — add DEMOTE rules + Connective Protection
  - [ ] Update `system_validate_sub_key_battle.txt` — add DEMOTE rules
  - [ ] Update `system_validate_sub_key_pirate.txt` — add DEMOTE rules (if exists)
  - [ ] Update `rewriter.py` — parse `demoted` items, move main→sub
  - [ ] Add `iconic_details` to biography research Section A
