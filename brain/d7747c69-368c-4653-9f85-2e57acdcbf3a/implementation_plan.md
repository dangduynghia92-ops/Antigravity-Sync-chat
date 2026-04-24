# Anti-Plagiarism Fix — Content Originality Pipeline

## Problem
Pipeline copies 3 types of content from original source:
1. **Ranking order** — Same 8 guns in same positions (8→1)
2. **Unique metaphors** — "fits in a briefcase" (Kel-Tec), NFA legal loophole angle (Mossberg)
3. **Subjective arguments** — "cheap so if stolen it's less loss" (PSA AR)

## Root Cause — 3 Contamination Points

### Point 1: Blueprint `author_rhetoric` field
Blueprint extraction captures original author's **subjective metaphors and conclusions** verbatim:
```json
"author_rhetoric": [
  {"type": "physical_translation", "content": "Se pliega a 16 pulgadas planas. Es más corto que la mayoría de las computadoras portátiles."}
]
```
This data flows directly to outline + writer → reproduced in output.

### Point 2: `myths_misconceptions` carries reasoning chains
```json
"myths_misconceptions": [
  {"myth": "La gente no quiere dejar un rifle de $1200 en un vehículo por miedo a robos.",
   "reality": "A $600, la pistola PSA AR reduce significativamente esa barrera económica."}
]
```
This is the **original author's argument**, not objective data. Writer reproduces it as if it's the channel's own insight.

### Point 3: Outline lacks ranking-independence rule
`system_review_outline_firearms_v2.txt` line 19: `"you MUST NOT replicate thesis"` ✅
But **NO rule** says: "Create your OWN ranking order based on criteria, not the source's order."

## Proposed Changes

---

### Blueprint Extraction

#### [MODIFY] [system_review_outline_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_review_outline_firearms_v2.txt)

Add **ANTI-COPY RULES** section:
1. **Ranking Independence**: "You MUST create your OWN ranking order. The source's ranking is CONTAMINATED DATA — using it is plagiarism. Re-rank based on the angle's primary evaluation criteria."
2. **Metaphor Prohibition**: "NEVER use metaphors/analogies from `author_rhetoric`. Create original analogies based on raw specs."
3. **Reasoning Independence**: "The `myths_misconceptions.reality` field contains the source author's reasoning. You may use the FACT but must construct your OWN argument chain."

---

### Writer Prompt

#### [MODIFY] [system_write_review_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_write_review_firearms_v2.txt)

Add **ORIGINALITY RULES**:
1. `author_rhetoric` data is READ-ONLY REFERENCE — do NOT paraphrase or translate it. Create original analogies from raw specs.
2. Every comparison/analogy must be ORIGINAL — if the blueprint mentions "briefcase", you must NOT use "briefcase" or any container analogy.
3. Ranking justification must come from YOUR analysis of data_focus fields, not from the blueprint's ranking_reason.

---

### Blueprint Extraction Prompt (upstream fix)

#### [MODIFY] Blueprint extraction prompt (in rewriter.py)

Add instruction: "For `author_rhetoric`, mark entries as `contaminated: true`. These are the source author's intellectual property and MUST NOT be reproduced."

> [!IMPORTANT]
> The `author_rhetoric` field should be kept for context (understanding the source's angle) but explicitly marked as contaminated to prevent downstream reproduction.

## Verification Plan

### Manual Check
1. Re-run pipeline on same "10 Truck Guns" video
2. Compare new output ranking order vs original — must be DIFFERENT
3. Check for Kel-Tec "briefcase" analogy — must NOT appear
4. Check for PSA "stolen gun" argument — must use different reasoning
5. Check for Mossberg NFA loophole angle — must frame differently
