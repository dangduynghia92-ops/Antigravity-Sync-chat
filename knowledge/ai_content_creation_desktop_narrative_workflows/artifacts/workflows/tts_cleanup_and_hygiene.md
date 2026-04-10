# Workflow: TTS Cleanup and Script Hygiene

This workflow describes the process of preparing AI-generated scripts for Text-to-Speech (TTS) engines, ensuring neutrality, readability, and correct pronunciation.

## 1. Script Hygiene & Cleanup
AI models often include "residue" in their outputs (Markdown formatting, character names, descriptive tags) that can break TTS flow.

### Key Operations:
- **Markdown Removal**: Stripping `**bold**`, `# headers`, and `*italics*`.
- **Text Normalization**: Removing AI-added meta-comments (e.g., "[Scene: Forest]", "Scriptwriter Note:").
- **Acronym Handling**: Identifying acronyms (e.g., "FBI", "UN") and expanding or formatting them for natural voicing.
- **Visual Metadata Cleanup**: Removing specific prefixes like `tts_` or `final_` that might be auto-appended to filenames during the generation pipeline.

## 2. File Discovery & Scan Patterns
Handling large projects requires robust file discovery that avoids cluttering the UI with intermediate system files.

### Path & Scan Logic:
- **Recursive Scan**: Deep search into sub-directories to find scripts belonging to different projects or "versions."
- **Tree-Type Display**: Presenting files in a hierarchical tree (Folder > Subfolders > Files) to maintain project context.
- **Skip Patterns**: Systematically ignoring auxiliary files such as:
  - `_SUMMARY.txt`, `_VERIFY.json`, `_STATUS.json`
  - `FULL_SCRIPT.txt`, `_PREVIEW.csv`
  - Previously processed files (e.g., files starting with `tts_`).

## 3. Output Management
To simplify user workflow, the system defaults to "In-Place Hygiene":
- **Default Pathing**: Results are saved directly within the source folder or in a sibling `tts_` folder.
- **Source Folder Fallback**: If no specific output directory is provided, the system automatically saves cleaned files alongside the original source files, prepending a prefix (e.g., `tts_`).
- **Batch Processing**: Multiple folders can be processed in parallel using a thread-pool. If an output directory is specified, the system can preserve the subfolder structure (e.g., `output/tts_001/`, `output/tts_002/`).
