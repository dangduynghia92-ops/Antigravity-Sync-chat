# Product Tab Redesign

- [x] Create `core/file_reader.py` (read .txt, Google Docs public link)
- [x] Create `prompts/extract_objects.txt` (system prompt for extraction)
- [x] Rewrite `ui/product_tab.py`:
  - [x] Remove Generated Prompts panel (`_build_results_panel`, `_show_placeholder`, `result_text`)
  - [x] Add File Import panel (left): Add Files, Add URL, Extract tree, Export CSV, Send to Objects
  - [x] Modify Objects panel (right): tree format with grouping
  - [x] Separate Generate buttons per panel
  - [x] Redesign action buttons layout
  - [x] Wire up extraction logic (API call per file)
- [x] Test app launches without errors
