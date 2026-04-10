# Workflow: AI Style Analysis and Synthesis Pipeline

A robust 4-step process for extracting the writing methodology of a script corpus and synthesizing it into a "Content-Free" Style Guide. This prevents the AI from generating repetitive paraphrases and enables it to apply the voice to entirely new subject matter.

## 1. Step 1: Voice DNA Extraction (Global Overview)
The first step analyzes the entire corpus (all provided scripts) to identify high-level writing principles.

- **Objective**: Extract patterns in Tone, Register, Sentence Rhythm, Vocabulary Strategy, and Narrative Perspective.
- **Rules**: 
    - Focus on **HOW** the writer communicates, not **WHAT** they say.
    - Explicitly forbidden from quoting or referencing specific content names or events.
    - Descriptions must be abstract and reusable (e.g., "Frequent use of second-person scenarios to establish immediate immersion" instead of "The writer often says 'Imagine you are...'").

## 2. Step 2: Method Analysis (Per-Chapter Detail)
Analyzes individual chapters in detail with context (preceding and following snippets).

- **Objective**: Identify the strategic "purpose" behind specific segments (Openings, Transitions, Closings).
- **Technique Deployment**: Tracks frequency and positioning of specific narrative tools (suspense, contrast, callbacks).
- **POV Shifts**: Records the exact triggers and purposes for shifting perspective (e.g., shifting from 3rd-person narrator to 2nd-person immersion during a climax).

## 3. Step 3: Cross-Chapter Statistical Analysis (Python-Based)
Crucially, this step uses **deterministic Python logic** rather than AI to aggregate the per-chapter analysis data. This prevents "pattern hallucination" and provides the AI with "hard numbers" to follow in the final synthesis.

- **Frequency Metrics**: Average occurrences of techniques per chapter.
- **Opening Diversity**: Calculates the uniqueness ratio of opening methods (e.g., 8 different opening principles used across 10 chapters).
- **Variation Patterns**: Identifies repetition risks (e.g., "Chapters 3 and 4 used identical opening patterns").
- **Typical Positions**: Statistically determines where certain techniques most commonly appear (e.g., "Analytic analogies typically occur in the first 20% of the body").

## 4. Step 4: Style Guide Synthesis (Instructional Prompt)
The final stage combines the Voice DNA, Per-Chapter logic, and Cross-Chapter statistics into a structured JSON Style Guide.

- **Content-Free Instruction**: The synthesized guide is written as a "Teaching Document." It tells the writer **HOW** to write, not what the source looked like.
- **Instructional Hierarchy**:
    - **Core Rules**: Persona, sentence length rules, mandatory vocabulary levels.
    - **Frameworks**: Generic narrative templates (e.g., "The Inquiry Arc") derived from the analyzed structures.
    - **Technique frequency**: Uses the exact numbers from Step 3 (e.g., "Use 1-2 second-person shifts per chapter, typically at the opening").
    - **Checklists**: Explicit "Always/Never" rules distilled from the analysis.

## Solving the "Copy Machine" Problem
The pipeline addresses the risk of AI simply paraphrasing source text by:
1. **Separating Extracted Facts from Voice**: Original scripts are treated *only* as sources of data/facts.
2. **Style-Only Guide**: The Style Guide contains ZERO references to the original names, places, or metaphors.
3. **New Angle Requirement**: The writing prompts explicitly demand a "New Perspective" or "Specific Angle" (e.g., "Describe this event through the eyes of an archivist reading a faded note") to force the AI to re-imagine the scene rather than copy it.
