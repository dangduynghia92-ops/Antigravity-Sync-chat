# Walkthrough: Pirate Ship Framework — Lifecycle + Cause-Effect Rules

## Tóm Tắt Thay Đổi

**Mục tiêu**: Chuyển pipeline từ THEMATIC mapping (nhóm theo chủ đề) sang LIFECYCLE mapping (theo vòng đời tàu), đảm bảo nội dung dễ hiểu, logic cho YTB.

**4 files sửa, 0 code changes.**

---

## 1. Phase Plan — [system_narrative_phase_plan_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pirate.txt)

**Giảm từ 258 → 193 dòng** (bỏ trùng lặp, gom rules).

| Thay đổi | Chi tiết |
|----------|---------|
| Section-based classification | Blueprint section names = tags tự nhiên. `combat_events` = EVENT, `ship_life_and_crew` = CONDITION |
| General cause-effect rule | Thay COLLAPSE SEEDS (chỉ cover "chết") bằng CAUSE-EFFECT ACROSS PHASES (cover mọi kiểu nhân-quả) |
| Plant/Harvest pattern | Bánh Răng PLANT observation → phase sau HARVEST event+motivation |
| Freeze-frame | Bánh Răng = dừng timeline, bước vào bên trong tàu |
| Escalation | Thử Lửa events sắp theo leo thang (nhỏ → lớn) |

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pirate.txt)

---

## 2. Outline — [system_narrative_outline_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pirate.txt)

| Thay đổi | Chi tiết |
|----------|---------|
| Bánh Răng | FREEZE-FRAME label + "plant seeds as observations" |
| Thử Lửa | MOTIVATION RECALL + escalation order |
| Question Engine | Updated examples for lifecycle flow |
| Critical rule #5 | LIFECYCLE ORDER IS MANDATORY (was THEMATIC) |

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pirate.txt)

---

## 3. Write — [system_narrative_write_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pirate.txt)

| Thay đổi | Chi tiết |
|----------|---------|
| CALLBACK INTEGRATION | Nếu chapter có `callback_to`, tích hợp vào scene anchor trong 3 câu đầu |
| ESCALATION TRANSITION | Giữa 2 chapters cùng phase: chapter 1 kết bằng escalation tease, chapter 2 mở scene anchor mới |

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pirate.txt)

---

## 4. JSON — [narrative_lịch_sử_hải_tặc.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_lịch_sử_hải_tặc.json)

| Thay đổi | Chi tiết |
|----------|---------|
| `chapter_design` | THEMATIC → LIFECYCLE + freeze-frame + bundle motivations |
| `middle_chapters` | THEMATIC → LIFECYCLE + observations only + bundle motivations |
| Bánh Răng `lens` | FREEZE-FRAME + "CHỈ nêu HIỆN TRẠNG, không spoil kết quả" |

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_lịch_sử_hải_tặc.json)

---

## Verification
- ✅ "THEMATIC" removed from all 4 files
- ✅ "COLLAPSE SEEDS" replaced with general cause-effect in phase plan
- ✅ No biography/battle impact (all pirate-specific files)
- ✅ No code changes needed
- ✅ Prompt size reduced (phase plan: 258→193 lines)

## Next Steps
- Run pipeline on QAR or new ship topic from phase_plan step
- Verify chapters flow lifecycle + cause-effect pairs stay close
- Check Bánh Răng is observation-only, Thử Lửa recalls motivations
