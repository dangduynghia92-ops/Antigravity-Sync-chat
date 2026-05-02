# Chuyển Phase Plan sang Event Timeline — POV Biography (Final)

## Tóm tắt

Chuyển pipeline POV từ phase-based grouping sang flat event timeline. Mỗi event có mô tả đầy đủ (mở→đóng). Outline tách/gộp chapters. Validate kiểm tra completeness.

## Rollback Strategy

> [!IMPORTANT]
> Trước khi sửa bất kỳ file nào, backup toàn bộ version hiện tại.

```
prompts/_backup_v1_pov/
  ├── system_narrative_phase_plan_pov.txt     (bản gốc)
  ├── system_narrative_outline_pov.txt        (bản gốc)
  ├── system_validate_sub_key_pov.txt         (bản gốc)
  └── system_narrative_audit_pov.txt          (bản gốc)
```

- **Prompts**: Restore từ `_backup_v1_pov/`
- **Code**: Tất cả thay đổi nằm sau `if _is_pov:` → revert chỉ POV paths, các niche khác không ảnh hưởng
- **Write prompt**: KHÔNG sửa → không cần rollback

---

## Pipeline Flow

```
PHASE PLAN       → Liệt kê mốc tuổi + sự kiện tuyến tính (event_description 2-4 câu)
       ↓
VALIDATE         → Kiểm tra completeness + auto-fix (tuổi đúng? sót mốc? event đủ mở-đóng?)
       ↓
OUTLINE          → Map events → chapters. Dựng scene_open/action/close. Quyết tách/gộp.
       ↓
AUDIT            → Kiểm tra outline structure
       ↓
WRITE            → Viết chapter (nhận scene fields + 3 beats)
```

---

## Proposed Changes

---

### Step 0: Backup

#### [NEW] prompts/_backup_v1_pov/

Copy 4 files hiện tại vào backup folder trước khi sửa.

---

### Component 1: Phase Plan Prompt

#### [MODIFY] [system_narrative_phase_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pov.txt)

**Trách nhiệm**: Liệt kê sự kiện tuyến tính theo tuổi. KHÔNG quyết chapter count/split.

**Giữ nguyên:**
- Scene Test (Place + Action + Consequence)
- Body State Rule (body state = sub_key_data)
- Source tracing (_source_map)
- 6 phase labels (Nguồn Gốc → Kết Thúc) — chỉ làm tag

**Output format:**

```json
{
  "framework_used": "Cuộc Đời Bạn",
  "biography_subject": "...",
  "event_timeline": [
    {
      "event_id": 1,
      "age": 9,
      "phase_label": "Nguồn Gốc",
      "event_title": "The Numb Arm",
      "event_description": "In the courtyard of Jerusalem, noble boys play endurance games. A boy digs nails into your arm — blood beads but you feel nothing. Your tutor grabs your wrist, presses a candle to your skin. Nothing. His face goes white.",
      "sub_key_data": ["Born healthy, resembling father Amalric", "Mother Agnes banished from court"],
      "physical_state": "Healthy appearance, localized numbness in right arm"
    }
  ],
  "_source_map": { ... }
}
```

**event_description rules:**
- 2-4 câu, tổng hợp từ blueprint (life_phases, turning_points, conflicts...)
- Bắt đầu bằng WHERE → WHAT happens → CONSEQUENCE
- Mô tả event **từ mở đầu đến kết thúc** — không dừng giữa chừng

**Sự kiện cùng tuổi — 3 tiêu chí INDEPENDENCE:**

| Tiêu chí | Độc lập → tách | Liên tục → gộp |
|---|---|---|
| Nơi chốn | Khác place | Cùng place / chuyển tiếp tự nhiên |
| Nhân quả | A kết thúc KHÔNG gây ra B | A → trực tiếp dẫn đến B |
| Đối tượng | Khác actors chính | Cùng actors |

Cả 3 tiêu chí đều phải "độc lập" → mới tách. Bất kỳ 1 tiêu chí "liên tục" → gộp.

---

### Component 2: Validate Prompt

#### [MODIFY] [system_validate_sub_key_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_validate_sub_key_pov.txt)

**Trách nhiệm mới**: Kiểm tra tính đầy đủ + chính xác của event_timeline. **Auto-fix tất cả.**

**Checks + auto-fix:**

| Check | Phát hiện | Auto-fix |
|---|---|---|
| Sai tuổi | age ≠ blueprint `age_timeline` | Sửa age |
| Event thiếu consequence | event_description không có hậu quả | Bổ sung từ blueprint |
| Sót mốc tuổi quan trọng | `turning_points` / `key_relationships` (conflict) / `death_and_funeral` không có trong timeline | Tạo event mới, insert đúng vị trí |
| Body state là standalone event | event_description chỉ mô tả body state, không có action | Chuyển vào sub_key_data của event gần nhất, xóa event |
| Thứ tự tuổi sai | ages không tăng dần | Sắp xếp lại |
| Cùng tuổi gộp nhầm | 2 events độc lập bị gộp (3 tiêu chí) | Tách thành 2 events |
| Cùng tuổi tách nhầm | 2 events liên tục bị tách (nhân quả trực tiếp) | Gộp lại 1 event |

**Output**: event_timeline đã fix + validation log (ghi rõ từng fix).

---

### Component 3: Outline Prompt

#### [MODIFY] [system_narrative_outline_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pov.txt)

**Trách nhiệm**: Nhận event_timeline (đã validate) → tạo chapters + dựng scene fields.

**Mapping**: 1 event = 1 chapter (mặc định). Event_timeline đã xử lý tách/gộp ở validate.

**Thêm scene fields** — Outline tách `event_description` thành 3 fields cho writer:

```json
{
  "chapter_number": 1,
  "chapter_title": "Level 1: The Numb Arm",
  "scene_open": "In the courtyard of Jerusalem, noble boys play endurance games — digging nails into each other's skin.",
  "scene_action": "A boy digs his nails into your right arm. Blood beads. You feel nothing. You don't flinch.",
  "scene_close": "Your tutor grabs your wrist, presses a lit candle to your skin. Nothing. His face goes white.",
  "sub_key_data": ["Born healthy, resembling father Amalric", "Mother Agnes banished"],
  "physical_state": "Healthy appearance, localized numbness",
  "age_anchor": "You are 9 years old",
  "opening_style": "standard",
  "closing_type": "cold_fact",
  "chapter_structure": "action_scene",
  "emotional_beat": "dread"
}
```

**Scene fields rules:**
- `scene_open`: WHERE + setup (1-2 câu)
- `scene_action`: WHAT the character does/faces (1-2 câu) 
- `scene_close`: CONSEQUENCE — what changed (1-2 câu)
- Tổng 3 fields ≈ event_description nhưng structured rõ ràng hơn

**Giữ nguyên**: Level format, rotation rules (3 consecutive ≠ same style/closing), variety constraints.

---

### Component 4: Write Prompt

#### [NO CHANGE] [system_narrative_write_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pov.txt)

3-beat rule đã đủ. Writer nhận scene_open/action/close → viết chapter đầy đủ.

---

### Component 5: Code — rewriter.py

#### [MODIFY] [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

**5a. `apply_chapter_splits`** (line 4766) — POV path:
- Đọc `event_timeline[]` thay vì `phase_chapter_plan[]`
- Mỗi event = 1 chapter. Gán chapter numbers tuần tự.
- Last event → chapter_type "end"
- `phase_label` → `framework_step`
- Bỏ merge/split logic cho POV (đã xử lý ở validate)

**5b. `validate_phase_plan_sub_keys`** (line 4454) — POV path:
- Thêm branch `if _is_pov:` → gọi validate mới (completeness check)
- Nhận `event_timeline[]` + blueprint
- Auto-fix: sửa age, thêm missing events, bổ sung event description, chuyển body state
- Return: event_timeline đã fix + validation log
- Niche khác: giữ nguyên logic promote/demote hiện tại

**5c. `write_from_blueprint`** (line 5205+) — POV path:
- Chapter outline có `scene_open`, `scene_action`, `scene_close`
- Truyền 3 fields vào user prompt thay vì `main_key_data: ["1 dòng"]`

**5d. `_extract_chapter_blueprint`** (blueprint filter) — POV path:
- Sử dụng `event_description` + `sub_key_data` để filter blueprint data

---

### Component 6: Code — script_creation_tab.py

#### [MINOR] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

- Pipeline data flow: đọc `event_timeline` thay vì `phase_chapter_plan` cho POV
- Validate call: route POV → completeness check
- Save files: `_phase_plan.json` vẫn giữ tên (backward compat), content chứa `event_timeline`

---

### Component 7: Audit Prompt

#### [MINOR] [system_narrative_audit_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_audit_pov.txt)

- Nhận biết format mới (scene_open/action/close thay vì main_key_data)
- Logic audit giữ nguyên: check structure, variety, chronological order

---

## Execution Order

1. **Backup** → `prompts/_backup_v1_pov/`
2. **Phase plan prompt** → rewrite
3. **Validate prompt** → rewrite  
4. **Code validate** → thêm `_is_pov` branch
5. **Outline prompt** → rewrite (thêm scene fields)
6. **Code apply_chapter_splits** → thêm `_is_pov` branch
7. **Audit prompt** → minor update
8. **Code write_from_blueprint** → truyền scene fields
9. **Code script_creation_tab** → data flow
10. **Test** → chạy Baldwin IV, so sánh

## Verification Plan

### Automated Tests
- Chạy pipeline Baldwin IV
- Verify: event_timeline có đủ mốc tuổi (9, 13, 16, 18, 20, 21, 22, 23)
- Verify: validate phát hiện + fix issues
- Verify: mỗi chapter có scene_open/action/close + Level anchor + 3 beats
- So sánh word count vs reference (149-196 words/chapter)

### Manual Verification
- So sánh chapter 1 mới vs reference ch1
- Kiểm tra forward tension ở mỗi ending
- Kiểm tra body state woven, không standalone
