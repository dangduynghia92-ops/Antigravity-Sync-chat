# Workflow: SRT to Visual Prompt Generation

This specialized pipeline transforms raw subtitle data into visually rich descriptive prompts.

## 1. Multi-Stage Pipeline
1. **Parsing**: SRT data is parsed into `SRTSegment` objects (Index, Start/End times, Text).
2. **Interval Grouping**: Rather than line-by-line generation, segments are grouped into fixed intervals (e.g., every 5 seconds) to create coherent scene descriptions.
3. **Consistency Check (Global)**: If Historical mode is active, the Visual Bible step is performed **automatically** (see `hierarchical_narrative_generation.md`).
4. **Generation**: Grouped segments are sent to the AI, ensuring English-only output and rich visual detail.

## 2. Local Narrative Coherence (`context_seconds`)

While the Visual Bible provides *global* consistency, `context_seconds` provides *local* consistency between adjacent scenes.
- **Mechanism**: The system fetches subtitle text from a configurable window (e.g., 10 seconds) before and after the current segment.
- **Prompt Structure**:
  ```
  === SURROUNDING CONTEXT ===
  BEFORE: [Previous lines]
  >>> CURRENT SEGMENT [Target line] <<<
  AFTER: [Next lines]
  ```
- **Result**: The AI understands the narrative flow (e.g., a character entering a door in the previous line determines their position in the current line).

## 3. Math and Formatting
- **Time Conversion**: Precise handling of SRT timestamps (`HH:MM:SS,mmm`) converted to floating-point seconds.
- **Formatting**: Final prompt results must include the exact `[Start - End]` time range for easy synchronization in video editing software.

## 4. Implementation Artifacts and Policies
- **CSV-Only Policy**: For structured review, results are saved only in CSV format. TXT exports are deprecated.
- **Output**: `{project_name}_prompts.csv`
- **Reference**: `{project_name}_visual_bible.txt` (stored in the output directory if Historical ✓)
- **Merging**: The system can merge multiple results into a single `_MERGED_xxx.csv` for bulk narrative review.
