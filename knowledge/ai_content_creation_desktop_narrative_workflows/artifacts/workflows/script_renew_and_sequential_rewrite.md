# Workflow: Script Renew and Sequential Context Rewriting

This workflow introduces a deep restructuring method called "Renew" and a high-consistency "Sequential" rewrite mode.

## 1. The "Renew" Workflow (Full Re-outlining)

Unlike standard rewriting which preserves the original chapter structure, the "Renew" feature treats the entire script as a single narrative source and rebuilds it from the ground up.

### Process Steps:
1. **Source Concatenation**: All input text (from multiple files or a single large script) is joined into one block (the "Raw Script").
2. **Framework-Aware Outlining**:
   - The AI reads the full source text + a Style Guide JSON containing predefined narrative frameworks (e.g., "The Underdog's Gambit", "The Revenge Quest").
   - **User Constraints**: Users specify a desired chapter count range (e.g., "Ch: 5 ~ 20"). The system handles these via a helper that converts `0` (Min or Max) into "no limit" instructions for the LLM.
   - **Generation**: AI selects the best-fitting framework from the style guide and maps the raw story onto the framework's "steps" (e.g., Establishing dominance, The strategic gamble, The chaotic pivot) to produce a NEW chapter plan.
   - **Output**: Returns `{chosen_framework, narrative_arc, chapters: [{title, summary, key_points, emotional_beat, ends_with}]}`.
3. **Sequential Writing**: AI writes each chapter one-by-one following the plan, using a context window of the 2 previous chapters.
4. **Verification**: Individual chapters are verified against word count rules and quality metrics.
5. **Cross-Chapter Review & Auto-Patch**: The full script is reviewed for overlaps or flow breaks. AI-powered "Patching" applies minimal, targeted fixes to specific chapters to resolve issues without redundant rewriting.
6. **Final Review & Merging**: A final flow analysis is performed, and all chapters are concatenated into a `FULL_SCRIPT.txt`.

## 2. Sequential Rewriting with Sliding Context

To maintain narrative flow and avoid repetition, the system utilizes a "Forward Context" pattern during sequential generation.

### Context Pattern (N-2 Window):
- **Chapter 1**: Prompt + Outline info + Full Source.
- **Chapter 2**: Prompt + Outline info + Full Source + **Chapter 1 (rewritten)**.
- **Chapter 3**: Prompt + Outline info + Full Source + **Chapter 1 & 2 (rewritten)**.
- **Chapter N**: Prompt + Outline info + Full Source + **Chapter N-1 & N-2 (rewritten)**.

### Solving "Repetitive Openings"
A common issue in narrative series is the AI starting every chapter with the same pattern (e.g., "Imagine...", "Picture this...").

**The "Global Frequency" Trap**:
This often occurs during Style Synthesis. If the AI analyzes 10 scripts and finds that 8 of them use a second-person opening ("Imagine..."), it correctly identifies this as a dominant pattern. However, without specific instructions, the AI may summarize this as a global rule: *"Frequently use second-person address."*
- **The Failure**: When rewriting, the AI applies this "frequent" rule to *every* chapter. While the original scripts only used the technique once per script, the AI applies it multiple times per chapter, leading to extreme repetition.

**Mitigation Strategies**:
1. **Diverse Style Synthesis**: When generating a Style Guide, the AI must be forced to propose 4-5 *different* opening techniques (e.g., Sensory Immersion, Myth Rebuttal, In Medias Res), even if the source material is uniform.
2. **Actionable Hints over References**: Replace vague `example_reference` fields (e.g., "See Script 1") with concrete `example_hint` scenarios (e.g., "Describe the smell of gunpowder and the cold rain on a soldier's face"). This gives the AI a specific sensory target instead of a generic pattern.
3. **Rotating Assignments**: During the rewrite phase, the system assigns a specific opening technique (rotating by index) to each chapter in the system prompt.
4. **Negative Prompting**: The local generation prompt includes a list of openings used in the current context window and explicitly forbids their repetition.

## 3. Style Guide Refinement: Example Hints vs. References

Early versions of Style Guides used "Example References" (e.g., "See Script 1, Chapter 3"). However, when rewriting *new* scripts, the AI does not have those reference scripts in its context window, making the reference useless.

**The Refinement**: Transition to **`example_hint`**. 
Instead of a reference, the AI synthesizes a **concrete implementation scenario**:
- *Ineffective*: "Technique used in Script 1."
- *Effective*: "Place the viewer on a muddy battlefield at dawn, surrounded by the clang of swords and screams of the dying."

These descriptive hints provide the AI with actionable context it can carry forward into the task without needing the original source files.

A common UI pattern in these tools is the range selector (Min/Max).
- **Special Value**: Value `0` is treated as "No Limit" (displayed as "—").
- **Logic Mapping**:
  - `Min > 0, Max > 0` -> "N to M [units]"
  - `Min > 0, Max == 0` -> "At least N [units]"
  - `Min == 0, Max > 0` -> "At most M [units]"
  - `Min == 0, Max == 0` -> "No specific limit"

### Solving the "Copying vs. Re-imagining" Problem

A persistent challenge in AI rewriting is the tendency for models to produce **paraphrased copies** (changing words but keeping the exact same flow and sentence-by-sentence logic) rather than a fresh narrative.

#### 1. The "Source of Facts" Separation
The most effective mitigation is to instruct the AI to treat the original chapter *exclusively* as a **Fact Sheet** or **Data Source**. 
- **The Prompt**: "Extract the core events and data points from the source. Discard the original prose, structure, and tone. Use the attached Style Guide as the exclusive map for how to reconstruct these facts."

#### 2. Mandatory "New Perspective" (Angling)
Instead of asking for a "rewrite," the system demands a specific **Perspective Angle** for each scene. This forces the model to construct a new scene logically:
- **Example**: "Write this through the eyes of a cynical historian reviewing a dusty ledger" or "Describe the event as if it were a half-whispered rumor in a crowded marketplace."
- **Effect**: By changing the *perspective*, the AI is physically unable to copy the original structure, as the observational points and emotional priorities have shifted.

#### 3. Structured Style-Only Guides
By synthesizing Style Guides that contain **zero content references**, the system ensures the AI cannot accidentally "leak" metaphors or unique phrasing from the source scripts into the new output. The Style Guide acts as a **Methodology Teacher**, not a catalog of examples.

## 4. Output Merging and Flow Verification

Upon completion of any sequential flow (Narrative Rewrite or Renew), the system automatically performs a "Final Merge":
- **Final Merge**: All individual chapter files are read in order and consolidated into a `FULL_SCRIPT.txt`.
- **Flow Verification**: A final AI pass reviews the merged script for "Continuity Fatigue" (e.g., losing the primary mystery thread across a long series) and applies patches to restore the thematic arc.
