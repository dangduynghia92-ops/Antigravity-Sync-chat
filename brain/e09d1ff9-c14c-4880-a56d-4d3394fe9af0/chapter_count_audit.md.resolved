# Baldwin IV — Phase Plan Data Audit

## Blueprint Raw Data

| Source | Count |
|---|---|
| age_timeline events | **26** |
| military_campaigns | **8** |
| turning_points | **7** |
| life_phases | **5** (27 key_events total) |
| conflicts | **5** |

## Phase Plan Result: 9 main + 12 sub

| Phase | Main (→ chapters) | Sub (→ texture) |
|---|---|---|
| Nguồn Gốc | 1: Leprosy discovery (age 9) | Born in Jerusalem; Hostile politics |
| Thử Lửa | 2: Coronation (13), Seizes power (15) | Father dies; Skin lesions |
| Trỗi Dậy | 1: Montgisard (16) | Hand loses motor function |
| Đỉnh Cao | 2: Marj Ayyun (18), Sibylla marriage (19) | Claw hand; Blindness onset |
| Suy Tàn | 2: Kerak siege (22), Baldwin V coronation (23) | Total blindness; Voice whisper |
| Kết Thúc | 1: Death (23) | Buried; Hattin; Callback |
| **Total** | **9 main** | **12 sub** |

## Events in Blueprint that Phase Plan SKIPPED or DEMOTED

These are significant events from the age_timeline that are NOT in main OR sub:

| # | Age | Event | Potential Scene? |
|---|---|---|---|
| 1 | 13 | Miles of Plancy assassinated in Acre | ✅ Court intrigue, power vacuum |
| 2 | 16 | Refuses cousin Philip of Flanders' demands | ✅ Confrontation, asserting control |
| 3 | 17 | Jacob's Ford fortress construction | ❌ State action, no conflict |
| 4 | 18 | Jacob's Ford falls, Templars slaughtered | ✅ Loss, failure, cost |
| 5 | 19 | Negotiates truce with Saladin | ❌ Diplomacy, no visceral scene |
| 6 | 20 | Health declines sharply, loses eyesight/feet | Physical state → already sub |
| 7 | 21 | Battle of Belvoir Castle, commands from litter | ✅ Military, body-failing |
| 8 | 22 | Appoints Guy as regent | ✅ Political defeat, desperation |
| 9 | 22 | Strips Guy of regency (Pools of Goliath failure) | ✅ Confrontation, fury |
| 10 | 23 | Second Siege of Kerak | ✅ Final campaign |
| 11 | 23 | Tries to annul Sibylla's marriage, fails | ✅ Political failure, frustration |

## Analysis: Which Skipped Events Should Be Main?

Applying the Scene Test (place + actor intent + immediate consequence):

| Event | Scene Test | Verdict |
|---|---|---|
| **Jacob's Ford falls** (18) | ✅ Place: fortress. Intent: relieve garrison. Consequence: arrives too late, Templars dead. | **Should be MAIN** — concrete military failure, body failing |
| **Battle of Belvoir** (21) | ✅ Place: Belvoir Castle. Intent: repel Saladin. Consequence: commands from litter, succeeds. | **Should be MAIN** — first time commanding from litter |
| **Strips Guy of regency** (22) | ✅ Place: court. Intent: punish incompetence. Consequence: political chaos. | **Could be SUB** of Kerak chapter — events same year |
| **Second Kerak** (23) | ✅ Place: Kerak. Intent: relieve again. Consequence: Saladin retreats again. | **Could be SUB** — repeat of first Kerak, less dramatic |
| Annul Sibylla's marriage (23) | ✅ Place: court. Intent: remove Guy. Consequence: FAILS. | **Could be MAIN** — rare political defeat |
| Philip of Flanders (16) | Partial — confrontation, but no visceral consequence | SUB is fine |
| Miles of Plancy (13) | ❌ Baldwin is passive — assassination happens around him | SUB is fine |

## Conclusion

Phase Plan **skipped at least 2-3 events that qualify as main**:

> [!IMPORTANT]
> 1. **Jacob's Ford** (age 18) — major military failure, body-as-clock milestone
> 2. **Belvoir Castle** (age 21) — FIRST command from litter, transition from horseback to stretcher
> 3. **Annul attempt fails** (age 23) — rare moment where Baldwin's WILL is defeated

Adding these would give **11-12 chapters**, closer to the reference script's 13. Without them:
- **Age 20-21 is a complete gap** — nothing between age 19 (Sibylla marriage) and age 22 (Kerak)
- The **body-as-clock progression** loses a critical transition point (horseback → litter)
- Baldwin's **only political failure** (annulment blocked) is lost

## Root Cause

The phase plan prompt asks AI to pick events per framework phase. With only **6 phases** and a soft cap, AI tends to pick **1-2 events per phase**. This produces 9 main events.

Possible fixes:
1. **Increase phase plan prompt guidance** — tell AI to aim for 10-13 main events total
2. **Add a review step** — after phase plan, check for timeline gaps > 2 years
3. **Manual override** — let user adjust main/sub classification before outline generation
