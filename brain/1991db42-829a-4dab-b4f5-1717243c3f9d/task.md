# Narrative Rewrite Pipeline

## Prompts
- [x] Create `system_narrative_outline.txt`
- [x] Create `system_narrative_rewrite.txt`
- [x] Create `system_narrative_review.txt`

## Core Logic (`core/rewriter.py`)
- [x] `generate_narrative_outline()`
- [x] `rewrite_chapter_narrative()`
- [x] `review_narrative_full()`
- [x] `patch_chapter_overlap()`
- [x] `merge_to_version()`

## UI (`ui/rewrite_tab.py`)
- [x] Add Mode ComboBox (Top/List | Narrative)
- [x] `_do_narrative_rewrite()` — main flow (steps 1–6)
- [x] `_show_narrative_review_dialog()` — interactive dialog
- [x] `_fix_narrative_chapter()` — fix cycle
- [x] `_open_version_folder()` — open version in explorer
- [x] Finalize → copy to `final/`
- [x] Mode saved/loaded in config

## Testing
- [x] Import check
- [ ] Manual test with sample chapters
