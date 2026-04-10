# Per-Niche Config Auto-Save

- [x] Research current config save/load mechanism
- [x] Research `_on_mode_changed` and checkbox defaults
- [/] Write implementation plan
- [x] Get user approval
- [x] Add `save_niche_config` / `load_niche_config` to `config_manager.py`
- [x] Modify `_save_config` in `rewrite_style_tab.py` to also save per-niche
- [x] Modify `_load_saved_config` to load per-niche on mode+style change
- [x] Modify `_on_mode_changed` to trigger niche config load
- [/] Test with switching modes and styles
