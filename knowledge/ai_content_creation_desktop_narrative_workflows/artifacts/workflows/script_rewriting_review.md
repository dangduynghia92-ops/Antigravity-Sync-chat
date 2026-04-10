# Workflow: Mystery Script Rewriting and Review

This pipeline is optimized for depth, thematic consistency, and unsettling tension in historical mystery narratives.

## 1. Thematic Chapter Clustering
To avoid disjointed storytelling, the system performs "Thematic Clustering" across chapters.
- **Analysis**: Groups chapters into narrative arcs (e.g., The Discovery, The Investigation, The Dark Turn).
- **Consistency**: Ensures that character motivations and mystery reveals carry over across cluster boundaries.

## 2. Specialized Storytelling Methods

The system enforces a selection of one primary method per rewrite to maintain a consistent "voice."

| Method | Primary Hook | Atmospheric Goal | Ending Type |
|---|---|---|---|
| `inquiry_arc` | Logical investigation | Intellectual curiosity | Reflective / Objective |
| `cognitive_arc` | Internal psychological shift | Intellectual tension | Internal Realization |
| `relic_anchor` | Material/Physical discovery | Reverent / Mysterious | Weighted Silence |
| `descending_spiral` | Dark, unsettling mystery | Creeping unease | Hollow Silence |

### The "Ghostly Voice" Mechanic (`descending_spiral`)
Especially effective for historical horror, this method utilizes an "invisible character" system (ghostly voices of historical figures) and internal counter-arguments to create psychological haunting without traditional jump scares.

## 3. The Narrative Review System

A structured quality-control layer that evaluates the script against a high standard.
- **Scoring Threshold**: Chapters are given a score from 0 to 10. Any score **below 8.0** is flagged as failing.
- **Automated "Fix & Rewrite"**:
  1. The Review stage generates a structured critique identifying cross-chapter issues (overlaps, flow breaks).
  2. The system allows batch selection of failed chapters or automatic identification of "Fix Chapters" from the critique.
  3. **Targeted Patching**: Instead of a full rewrite, the system applies a "Patch" (minimal edit) to the specific overlapping section while preserving the rest of the chapter.
- **Index Alignment Reliability**:
  - **The Problem**: When filtering for "ready to review" chapters, indices between the source list and the results list can diverge if empty or failed chapters are present.
  - **The Fix**: Use an explicit `rw_index_map` to track the relationship between the subset being reviewed and the original chapter list, ensuring patches are applied to the correct physical files.
- **Reporting & Merging**: 
  - Produces `review_vX.csv` with scores and reasoning.
  - Automatic creation of `FULL_SCRIPT.txt` upon successful patching/completion.
