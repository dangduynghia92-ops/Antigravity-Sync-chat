# Walkthrough — POV Biography Pipeline Hardening

## Changes Made

### 1. event_cause: TRIGGER → BACKGROUND CONTEXT

| File | Change |
|---|---|
| [chapter_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_chapter_plan_pov.txt) | Redefined from \"EXTERNAL TRIGGER\" to \"BACKGROUND CONTEXT\" + new examples |
| [outline_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pov.txt) | event_cause desc updated |
| [write_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pov.txt) | Label + PART 2 examples updated |

---

### 2. physical_state: Xóa mandatory, flow qua sub_key_data

| File | Change |
|---|---|
| [write_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pov.txt) | Xóa `Physical state: {physical_state}` line + weave mention |
| [outline_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pov.txt) | Xóa field, ownership, mandatory rule |
| [audit_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_audit_pov.txt) | Xóa scope, checklist, output type |
| [validate_sub_key_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_validate_sub_key_pov.txt) | Xóa từ output format |
| [chapter_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_chapter_plan_pov.txt) | Xóa từ output format |
| [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py) | Xóa `{physical_state}` từ `_NICHE_OUTLINE_FIELDS` |

---

### 3. Level anchor: Giữ age, AI cũng weave age tự nhiên

| File | Change |
|---|---|
| [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py) | `_inject_level_anchor()` inject đầy đủ \"Level N, label. You are X years old.\" |
| [write_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pov.txt) | Rule: \"opening paragraph MUST also naturally mention age\" |

---

### 4. Metaphor reduction

| File | Change |
|---|---|
| [Style JSON](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_pov_tiểu_sử.json) | `identity`: bỏ \"memory recalled under pressure\" |
| Style JSON | `tone`: \"Spoken-word thriller\" → \"Action thriller\" |
| Style JSON | `metaphor_family`: bỏ \"Weather as mood\", \"Architecture as power\" → \"Describe what body DOES\" |
| [write_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pov.txt) | weight example: bỏ \"crown sits on skull\" → \"They carry you off the field\" |

---

### 5. echo → reflection (end chapter closing)

| File | Change |
|---|---|
| [write_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pov.txt) | `reflection` closing type with 5 tones (pride/release/irony/cost/regret) |
| [outline_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pov.txt) | ECHO → REFLECTION, `callback_theme` → `reflection_tone` |
| [audit_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_audit_pov.txt) | Check #9 updated |

---

### 6. Scene Test: Nguồn Gốc exception

| File | Change |
|---|---|
| [phase_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pov.txt) | Nguồn Gốc: only PLACE + CONSEQUENCE required (no ACTION) |
| [chapter_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_chapter_plan_pov.txt) | Nguồn Gốc: only CONFLICT + SCENE POTENTIAL required (no AGENCY) |

---

### 7. Gap > 10 years rule: Xóa

| File | Change |
|---|---|
| [validate_sub_key_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_validate_sub_key_pov.txt) | Xóa CHECK 3d: gap > 10 years |
| [phase_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pov.txt) | Xóa coverage checklist d: gap > 10 years |

---

### 8. Log \"?\" title fix

| File | Change |
|---|---|
| [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py) | Line 4728: Lookup event_title từ validated timeline thay vì fix dict |

## Verification

- ✅ `rewriter.py` syntax check: PASS
- ✅ `script_creation_tab.py` syntax check: PASS
- ✅ `narrative_pov_tiểu_sử.json` JSON parse: PASS
- ⏳ Pipeline re-run: cần chạy lại Saladin để verify
