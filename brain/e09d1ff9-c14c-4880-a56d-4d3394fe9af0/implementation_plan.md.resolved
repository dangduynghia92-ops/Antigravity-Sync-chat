# Upgrade Coverage Checklist — Generic Cross-Reference

## Problem

Coverage checklist hiện chỉ check 4 fields cụ thể:
```
a. key_relationships
b. death_and_funeral
c. turning_points
d. physical_state_arc
```

Hậu quả: Blueprint có data quan trọng (Jacob's Ford trong `military_campaigns`) nhưng AI bỏ sót hoàn toàn vì checklist không scan field đó.

## Proposed Fix

### [MODIFY] [phase_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pov.txt)

**Lines 170-175** — Thay coverage checklist cũ:

```
COVERAGE CHECKLIST:
10. Before finalizing, verify:
   a. key_relationships: every relationship with conflict/betrayal/sacrifice → at least one event
   b. death_and_funeral: covered in last event(s)
   c. turning_points: each appears as an event in chronologically appropriate position
   d. physical_state_arc: body changes distributed as sub_key_data showing progression
```

Thành:

```
COVERAGE CHECKLIST:
10. Before finalizing, cross-reference event_timeline against EVERY section
    of the blueprint (life_phases, turning_points, conflicts, achievements,
    military_campaigns, key_relationships, dark_impact, and any other section).

    For each significant data point NOT yet represented:
      - Apply Scene Test → PASS → add as standalone event
      - Apply Scene Test → FAIL → add to sub_key_data of nearest related event

    Mandatory checks:
      a. death_and_funeral → must be covered in last event(s)
      b. physical_state_arc → body changes distributed as sub_key_data showing progression
```

**Logic**:
- Dòng chính: scan TẤT CẢ sections, dùng Scene Test để quyết event vs sub_key_data
- `death_and_funeral`: giữ mandatory vì bắt buộc phải có ending
- `physical_state_arc`: giữ mandatory vì POV cần body-as-clock
- `turning_points`, `key_relationships`, `military_campaigns`, `conflicts`, `achievements`: đều được cover bởi dòng cross-reference chung — không cần liệt kê riêng

---

### [MODIFY] [validate_sub_key_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_validate_sub_key_pov.txt)

**CHECK 3 (lines 22-30)** — hiện tại chỉ check 3 fields:

```
CHECK 3: MISSING MILESTONES
  Cross-reference event_timeline against:
    a. blueprint.turning_points → each must appear as an event
    b. blueprint.key_relationships (with conflict/betrayal) → must have an event
    c. blueprint.death_and_funeral → must be covered
```

Thành:

```
CHECK 3: MISSING MILESTONES
  Cross-reference event_timeline against EVERY section of the blueprint.
  For each significant data point NOT yet in the timeline:
    - Apply Scene Test (PLACE + ACTION + CONSEQUENCE) → PASS → add as event
    - Apply Scene Test → FAIL → add to sub_key_data of nearest related event
  Mandatory: death_and_funeral must be covered in last event(s).
```

> [!IMPORTANT]
> Validate prompt cũng cần cùng logic, vì validate là bước kiểm tra SAU phase_plan. Nếu phase_plan bỏ sót, validate phải bắt được.

---

## Scope

| File | Thay đổi | Lines |
|---|---|---|
| `phase_plan_pov.txt` | Coverage checklist → generic cross-ref | 170-175 |
| `validate_sub_key_pov.txt` | CHECK 3 → generic cross-ref | 22-30 |

## Không sửa

- Scene Test: giữ nguyên (đã có PLACE + ACTION + CONSEQUENCE + Nguồn Gốc exception + DRAMATIC TENSION)
- Chapter plan: không liên quan (nhận events đã chọn)
- Style JSON: không cần thay đổi `excerpt_fields`
- Code: không thay đổi

## Verification

Chạy lại Saladin, verify:
- Jacob's Ford (1179) xuất hiện trong event_timeline hoặc sub_key_data
- Không có event nào bị bỏ sót hoàn toàn khỏi blueprint
