# Coverage Checklist Backup — Before Generic Cross-Reference

## phase_plan_pov.txt (lines 170-175)

```
COVERAGE CHECKLIST:
10. Before finalizing, verify:
   a. key_relationships: every relationship with conflict/betrayal/sacrifice → at least one event
   b. death_and_funeral: covered in last event(s)
   c. turning_points: each appears as an event in chronologically appropriate position
   d. physical_state_arc: body changes distributed as sub_key_data showing progression
```

## validate_sub_key_pov.txt (lines 22-30)

```
CHECK 3: MISSING MILESTONES
  Cross-reference event_timeline against:
    a. blueprint.turning_points → each must appear as an event
    b. blueprint.key_relationships (with conflict/betrayal) → must have an event
    c. blueprint.death_and_funeral → must be covered
  If a milestone is missing → create a new event entry (with event_id, age, event_description) and insert at correct chronological position.
  IMPORTANT: After adding a new event, if it shares the same age as an existing event,
  you MUST run CHECK 6 (independence test) on those same-age events immediately.
  If the new event and existing event are CONTINUOUS → merge them into 1 event instead of adding separately.
```

## Rollback Instructions

To revert, replace the new generic cross-reference with the above content at the same line positions.
