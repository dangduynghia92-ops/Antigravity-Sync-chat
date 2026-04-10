# Hierarchical Narrative Generation: Global Analysis and Consistency

One of the most effective patterns for ensuring coherence in AI-generated series (episodes, chapters, or prompt sequences) is a **hierarchical two-pass strategy**.

## Strategy 1: The "Visual Bible" (Consistent Prompting)

For visual projects (e.g., historical videos from SRT), a preliminary "Global Review" generates a source of truth for the entire project.

### Visual Bible Components:
- **Era & Architecture**: Defines the structural and cultural setting (e.g., "Dai Viet 15th-century pagoda style").
- **Character Reference List**: Creates a canonical description for every recurring character (Age, Build, Iconic Props).
- **Group Standardization**: Defines standard uniforms or visual traits for recurring groups (e.g., armies, villagers).

### Workflow and Configuration:
1. **Trigger**: Triggered automatically when specific constraints (e.g., **Historical**) are enabled.
2. **Analysis Pass**: The AI (Pro tier) analyzes the full SRT or script text once per project. It generates a comprehensive "bible" covering context, characters, groups, and architecture.
3. **Persistence and Cache**:
   - The Bible is saved as a project-specific artifact (e.g., `{project}_visual_bible.txt`) in the output directory.
   - **Caching**: If a project is re-run, the system first checks for an existing Bible file to avoid redundant high-token API calls.
4. **Interactive vs. Automatic Flow**:
   - **Automatic**: Processing can skip user review and proceed directly to segment generation for speed.
   - **Interactive**: Optionally, a review popup allows users to edit the Bible text before saving and applying it.
5. **Resilience and Performance**:
   - **Input Management**: For extremely long source texts, the input should be capped or summarized to prevent token overflow.
   - **Cancellation (check_stopped)**: The generation process must check for user stop requests (cancellation) before and after the heavy AI call to ensure immediate responsiveness.
6. **Application**: The Visual Bible is injected as a "Reference" block in EVERY subsequent segment request.

## Strategy 2: Narrative Review Scoring (Quality Control)

For scriptwriting, a hierarchical review pass ensures that rewrites maintain thematic depth and logical consistency.

### Review Mechanisms:
- **Thematic Clustering**: Chapters are logically grouped to find thematic arcs.
- **Score-Based Guardrails**: Every chapter or segment is scored (e.g., 0-10). A threshold (typically **< 8.0**) is used to trigger mandatory reviews or rewrites.
- **Actionable Feedback**: The review stage identifies specific cross-chapter issues (e.g., character behavior shifts or logic holes) and produces a structured CSV report.

## Shared Pattern: The Role of the "Reference Section"

In both strategies, the core segment-level generation prompt is structured to treat the Global Analysis as "Ground Truth":
> "=== [REFERENCE SECTION: BIBLE/REVIEW] ===\n[Analysis text]\n=== END REFERENCE ===\n\nTask: Use the context above to generate [Segment/Chapter] N."

This drastically reduces "hallucinations" where the AI forgets character traits or atmospheric settings midway through a long document.
