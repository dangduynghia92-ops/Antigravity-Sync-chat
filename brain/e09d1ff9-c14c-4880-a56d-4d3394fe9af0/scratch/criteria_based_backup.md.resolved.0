# Backup: Criteria-Based Approach (Before Questionnaire)
# Date: 2026-05-10
# Revert to this if Q1-Q4 questionnaire doesn't produce good results.

═══════════════════════════════════════════════════════
FILE 1: chapter_plan_pov.txt — SCENE TEST (lines 7-67)
═══════════════════════════════════════════════════════

═══════════════════════════════════════
SCENE TEST — EVALUATE EVERY EVENT
═══════════════════════════════════════

For EACH event, apply the Scene Test:

  CRITERION 1 — CHARACTER AGENCY:
    Does the character ACTIVELY DO something? Make a choice? Take action?
    ✓ "You refuse Philip's demand" → character acts
    ✓ "You charge into Saladin's army" → character acts
    ✗ "William dies of malaria" → something happens TO the situation, character doesn't act
    ✗ "You reach legal majority" → automatic, no action

  CRITERION 2 — DRAMATIC TENSION OR CAUSAL WEIGHT (pass EITHER):

    2a. DRAMATIC TENSION — Does the event have AT LEAST ONE of these:
      a. Opposition/Confrontation (violence, defiance, resistance)
      b. Obsession/Extreme sacrifice (locking himself in a room, destroying his own body for an ideal)
      c. Irreversible choice (burning ships, abandoning power, signing a death warrant)
      ✓ "Philip demands your army — you refuse" → opposition
      ✓ "You lock the door for 3 days and write the final equation" → obsession
      ✗ "You are crowned king" → ceremony, no tension

    2b. CAUSAL WEIGHT — Does this event DIRECTLY cause the next major event?
      Would removing it leave a logic gap in the story?
      ✓ "Caesar appointed governor of Gaul" → directly enables conquest campaigns
      ✓ "Temüjin's father poisoned" → directly causes clan exile
      ✓ "Entering Damascus after Nur ad-Din's death" → directly enables Syrian unification
      ✗ "Received honorary title" → ceremony, no causal link to next event

  CRITERION 3 — SCENE POTENTIAL:
    Can this fill a chapter with action, physical detail, and consequence?
    ✓ Battle, confrontation, betrayal, escape, breakthrough, collapse → rich scene
    ✓ Political seizure with physical stakes (entering a city, claiming a throne) → scene
    ✗ Death of someone else (reported news), legal formality → thin scene

DECISION:
  Nguồn Gốc phase → (TENSION or CAUSAL) + SCENE POTENTIAL pass → KEEP
    (Origin events are things that happen TO the character — agency not expected)
  All other phases → AGENCY + (TENSION or CAUSAL) + SCENE POTENTIAL pass → KEEP
  Otherwise → DEMOTE to sub_key_data of the nearest related event

═══════════════════════════════════════
DEMOTING EVENTS
═══════════════════════════════════════

When demoting an event:
  1. Choose the nearest event that is CAUSALLY RELATED (same political thread)
  2. Move the demoted event's key info into that event's sub_key_data
  3. If the demoted event provides CAUSE/CONTEXT for the next event, note this

EXAMPLES:
  ✗ DEMOTE: "The King's Majority" (age 15) — reaching legal age is automatic
    → Move to sub_key_data of "Defying Flanders" (the first ACTION after majority)

  ✗ DEMOTE: "The Widow's Crisis" (age 16) — William dies of disease, Baldwin doesn't act
    → Move to sub_key_data of "Defying Flanders" (Philip arrives BECAUSE of the power vacuum)

  ✓ KEEP: "The Fall of Jacob's Ford" — Baldwin force-marches an army (agency),
    faces Saladin's destruction (conflict), arrives too late (consequence)


═══════════════════════════════════════════════════════
FILE 2: validate_sub_key_pov.txt — CHECK 3 (lines 22-45)
═══════════════════════════════════════════════════════

CHECK 3: MISSING MILESTONES
  Scan EVERY item in EVERY section of the blueprint
  (life_phases, turning_points, conflicts, achievements, military_campaigns,
   key_relationships, dark_impact, and any other section).

  For EACH item, answer two questions:

    Q1: Does this item pass Scene Test?
        (Has specific PLACE + ACTION + CONSEQUENCE?)
        → NO → skip
        → YES → go to Q2

    Q2: Is this item already COVERED in the event_timeline?
        "Covered" = its specific place, action, AND outcome
        already appear in an existing event_description or sub_key_data.
        → YES → skip
        → NO → MUST add (as event or sub_key_data)

  Mandatory: death_and_funeral must be covered in last event(s).

  If a milestone is missing → create a new event entry (with event_id, age, event_description) and insert at correct chronological position.
  IMPORTANT: After adding a new event, if it shares the same age as an existing event,
  you MUST run CHECK 6 (independence test) on those same-age events immediately.
  If the new event and existing event are CONTINUOUS → merge them into 1 event instead of adding separately.


═══════════════════════════════════════════════════════
FILE 3: phase_plan_pov.txt — COVERAGE CHECKLIST (lines 176-196)
═══════════════════════════════════════════════════════

COVERAGE CHECKLIST:
10. Before finalizing, scan EVERY item in EVERY section of the blueprint
    (life_phases, turning_points, conflicts, achievements, military_campaigns,
    key_relationships, dark_impact, and any other section).

    For EACH item, answer two questions:

      Q1: Does this item pass Scene Test?
          (Has specific PLACE + ACTION + CONSEQUENCE?)
          → NO → skip
          → YES → go to Q2

      Q2: Is this item already COVERED in the event_timeline?
          "Covered" = its specific place, action, AND outcome
          already appear in an existing event_description or sub_key_data.
          → YES → skip (already represented)
          → NO → MUST add it (as standalone event or sub_key_data)

    Mandatory:
      a. death_and_funeral → must be covered in last event(s)
      b. physical_state_arc → body changes distributed as sub_key_data


═══════════════════════════════════════════════════════
ROLLBACK INSTRUCTIONS
═══════════════════════════════════════════════════════

To revert from Q1-Q4 questionnaire back to criteria-based approach:

1. chapter_plan_pov.txt: Replace lines 7~65 with FILE 1 content above
2. validate_sub_key_pov.txt: Replace lines 22~45 with FILE 2 content above
3. phase_plan_pov.txt: Replace lines 176~196 with FILE 3 content above
