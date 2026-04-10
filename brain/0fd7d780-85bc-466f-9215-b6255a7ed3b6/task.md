# TTS Language Cleanup

## Rename Folders
- [ ] Rename `prompts/en/` → `prompts/english/`
- [ ] Rename `prompts/es/` → `prompts/español/`
- [ ] Create `tts_niche_rules/english/`
- [ ] Create `tts_niche_rules/español/`

## Prompt Files
- [ ] Create `english/system_tts_verify.txt` (copy from base)
- [ ] Create `español/system_tts_verify.txt` (Spanish examples)
- [ ] Move `tts_niche_rules/firearms.txt` → `español/firearms.txt`
- [ ] Write `tts_niche_rules/english/firearms.txt` (English pronunciations)
- [ ] Move `tts_niche_rules/history.txt` → `english/history.txt`
- [ ] Research + write `tts_niche_rules/español/history.txt`
- [ ] Delete old root-level niche files

## Code Changes
- [ ] Update `_load_prompt` in `tts_cleanup.py`
- [ ] Update `load_niche_rules` — add `lang` param
- [ ] Update `_load_prompt` in `rewriter.py`
- [ ] Update UI dropdown in `tts_tab.py`: full names, wider
- [ ] Check other tabs using lang dropdown
- [ ] Update `_run_cleanup` to pass `lang` to `load_niche_rules`

## Verify
- [ ] py_compile all modified Python files
- [ ] Test by restarting tool
