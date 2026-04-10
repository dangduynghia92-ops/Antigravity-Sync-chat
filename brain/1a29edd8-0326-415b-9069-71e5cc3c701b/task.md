# Transition Toggle Feature

- [x] Research codebase: writer pipeline, UI, prompt assembly
- [x] Create implementation plan
- [x] Add checkbox to UI (rewrite_style_tab.py)
  - [x] Add `_chk_transitions` widget
  - [x] Visibility toggle in `_on_mode_changed`
  - [x] Save/Load config
  - [x] Pass flag to writer at both call sites
- [x] Add `use_transitions` param to `write_review_chapter` (rewriter.py)
- [x] Strip/replace TRANSITIONS section conditionally
- [x] Verify syntax
