# New Feature Checklist

MANDATORY: When adding ANY new feature/step to the pipeline, MUST verify ALL of the following BEFORE delivering:

## Data Flow
- [ ] Input: Does every downstream step receive the new data in its LLM input?
- [ ] Output: Does every downstream step's LLM prompt instruct how to handle the new data?
- [ ] Propagation: Is there fallback logic if LLM returns empty for the new field?

## Checkpoint
- [ ] Does the new step have its own checkpoint file?
- [ ] Does it skip correctly on re-run?
- [ ] Does it load data into the correct `self.*` attribute when loading from checkpoint?

## Export (ALL outputs the user actually uses)
- [ ] Excel Sheet 1 (Video Prompts): new column added?
- [ ] Excel Sheet 2 (Reference Images): new entries added?
- [ ] Assembly JSON: relevant data included?
- [ ] Any other export format?

## Consistency
- [ ] Same format/template as existing similar features (e.g., sheet_prompt must match named characters)
- [ ] Same field naming convention across all steps
- [ ] Same LLM prompt style (rules, output format examples)

## Verification
- [ ] Run pipeline end-to-end on real data
- [ ] Check ACTUAL output files (open Excel, check JSON), not just grep code
- [ ] Verify data values are non-empty at every step boundary
