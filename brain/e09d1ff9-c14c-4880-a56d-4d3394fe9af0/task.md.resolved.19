# POV Pipeline Rebuild — Task Tracker

## Step 0: Backup
- [x] Backup all POV files → `_backup_v2_pov_rebuild/`

## Step 1: Style JSON — Strip to voice-only
- [x] Remove outline/structure rules (checklist, anti_patterns, chapter_rhythm, outline_rules, hook, weight_line_types, technique_emphasis, counter_argument, anti_copy)
- [x] Remove duplicates
- [x] Keep voice rules only (identity, tone, rhythm, vocab, POV, language, steps, pacing pattern)
- [x] JSON validates OK

## Step 2: Write Prompt — Clean rewrite
- [x] Rewrite to ~130 lines, 5 sections (from 234 lines, 6 sections)
- [x] Level anchor = "auto-injected by code, do NOT write it"
- [x] Merge closing rules into PART 4 (single source)
- [x] Remove {full_outline} variable
- [x] Add ownership header comment
- [x] Opening styles follow outline assignment (not duplicated)

## Step 3: Outline Prompt — Simplify
- [x] Remove writer-facing rules (BEAT references)
- [x] Simplify opening style (no Level anchor positioning — code handles)
- [x] Add ownership header comment
- [x] Add event_cause copy instruction

## Step 4: Audit Prompt — Restrict scope
- [x] Add metadata-only restriction ("NEVER rewrite content")
- [x] Remove vocabulary/word count checks
- [x] Remove blueprint_coverage check (no blueprint sent)
- [x] Simplify fix actions (only SET + SWAP, no REMOVE/ADD)
- [x] Add ownership header

## Step 5: Code — Data injection (rewriter.py)
- [x] Phase plan: remove Style Guide → send phase labels only (POV gated)
- [x] Outline: replace Style Guide → phase labels only (POV gated)
- [x] Audit: remove Style Guide + Blueprint (POV gated)
- [x] Write: remove {full_outline} replacement
- [x] Model tier: all hardcoded flash → user tier
  - [x] _validate_event_timeline_pov(): tier param added
  - [x] validate_phase_plan_sub_keys(): tier param added
  - [x] plan_chapters_pov(): tier param added
  - [x] Non-POV validate (closure): tier param used
  - [x] Audit in script_creation_tab.py: tier=tier
  - [x] Resume-path validate: tier=tier

## Step 6: Code — Level anchor inject (rewriter.py)
- [x] Add _extract_phase_labels() helper
- [x] Add _NUM_WORDS lookup table
- [x] Add _inject_level_anchor() helper
- [x] Call after write_from_blueprint output (POV gated)
- [x] Skip injection if AI already wrote Level anchor

## Step 7: Verify
- [x] Python syntax check: rewriter.py OK
- [x] Python syntax check: script_creation_tab.py OK
- [x] JSON syntax check: style JSON OK
- [ ] Cross-audit: verify no contradictions remain
- [ ] Runtime test on Baldwin IV blueprint
