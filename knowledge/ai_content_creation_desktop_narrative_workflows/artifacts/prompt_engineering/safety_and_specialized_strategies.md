# Safety Constraints and Visual Substitution Strategies

When generating content that involves celebrities, trademarked characters, or sensitive topics, standard AI requests often hit safety filters (Blocked Content). These strategies provide structured workarounds that maintain narrative intent while staying compliant.

## The Name Substitution Pattern (Celebrity Replacement)

Instead of instructing the AI to "avoid" a person (which often results in their complete removal), it is more effective to use the **Physical Substitution** pattern.

### 1. Mandatory Name Stripping
The AI is explicitly forbidden from using real names of celebrities, politicians, athletes, or copyrighted characters in its final generated prompt.

### 2. Physical Descriptors (Likeness Retention)
The AI is instructed to replace the prohibited name with a detailed physical description that captures iconic traits. 

**Examples:**
- **Elon Musk** → "A tall man in his 50s with short-cropped dark hair, an angular face, and a slight smirk, wearing a dark navy blazer."
- **Taylor Swift** → "A young woman with long blonde hair, red lipstick, tall and slender, wearing a sparkling sequined dress."
- **Son Goku** → "A muscular young man with wild spiky black hair pointing upward, wearing an orange and blue martial arts gi with a blue belt."

### Content-Free Style Synthesis

When instructing an AI to analyze and replicate a writing style, the prompts must be engineered to prevent the "leakage" of source content.

1. **The Methodology Filter**: The prompt must explicitly state: *"Extract the strategic GOAL of each choice, not the words."*
2. **Generic Implementation Hints**: Instead of quoting a source script, the synthesis prompt should require **Generic Scenarios**.
    - *Bad*: "Reference the way Script A describes the ghost." (Allows copying)
    - *Good*: "Provide a sensory implementation hint for creating dread, e.g., 'Describe the sound of fingernails dragging across a wooden door in a silent house'." (Provides a methodology that works for any topic).
3. **Instructional Voice**: The final Style Guide should be written in the **Imperative Mood** ("Use this...", "Never say...") rather than Descriptive Mood ("The writer used..."). This shifts the AI from "Historical Analyst" mode to "Professional Mentor" mode.
4. **Frequency over Probability**: Style guides should provide **concrete ranges** (e.g., "Use 2-3 metaphors per chapter") rather than vague probabilities ("Use metaphors frequently"). This is made possible by the Step 3 Python-based statistical analysis described in the Style Analysis Pipeline workflow.

## Handling Ambiguity and Case-Specific Fallbacks

AI knowledge may be incomplete for lesser-known or regional figures. To ensure stability:
- **Fallback Rule**: "If the person is not well-known or you are unsure of their appearance, describe them based on their **role, profession, and context** within the story scenario (e.g., 'a middle-aged politician in a formal suit' or 'a young athlete in a jersey')."
- **PG-13 Guardrail**: To prevent the AI from generating questionable content when describing physical traits, a mandatory "PG-13" constraint is applied alongside the substitution instructions.

## Thematic Storytelling Methods (Style Constraints)

For narrative scripts, consistency is further enhanced by selecting a singular **Mood/Method** constraint (e.g., `inquiry_arc`, `relic_anchor`, `descending_spiral`). 
- **The "Invisible Character" System**: In unsettling genres, prompts can use "ghostly voices" or "internalized counters" to build tension without explicit character dialogue.
- **Emotional Anchors**: Focusing on a specific relic or object to ground a historical scene.
