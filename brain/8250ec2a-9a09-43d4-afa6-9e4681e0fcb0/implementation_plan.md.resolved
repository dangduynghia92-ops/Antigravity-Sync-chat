# Location Reference Toggle — Inline Environment Mode

## Background

Hiện tại pipeline tạo location reference file (Step 2c) rồi dùng `[Location-Label]` bracket trong prompt. Cách này gây prompt bị gò bó — mọi scene trong 1 sequence đều nhét cùng label `[Tigris River - Mid-Stream]` bất kể shot type (Wide hay Close-up), khiến AI image gen render không tự nhiên.

**Giải pháp**: Thêm checkbox "Location Ref" trên UI. Khi **tắt** → bỏ Step 2c, Step 3 mô tả environment inline, Step 4 weave environment vào prompt thay vì dùng label.

## User Review Required

> [!IMPORTANT]
> Khi tắt Location Ref, file Excel Sheet 2 (Reference Images) sẽ **không còn location rows** — chỉ còn character reference. Cột "Location" ở Sheet 1 sẽ hiển thị `location_anchor` (mô tả ngắn) thay vì label.

## Proposed Changes

### UI — video_prompt_tab.py

#### [MODIFY] [video_prompt_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py)

**Thêm checkbox `Location Ref`** vào config area (cạnh Safety/Quality/Historical):
```python
self.location_ref_var = QCheckBox("Location Ref")
self.location_ref_var.setChecked(True)  # default = ON (hiện tại)
r2.addWidget(self.location_ref_var)
```

**Truyền vào constraints dict:**
```python
constraints = {
    "safety": self.safety_var.isChecked(),
    "quality": self.quality_var.isChecked(),
    "historical": self.historical_var.isChecked(),
    "location_ref": self.location_ref_var.isChecked(),  # NEW
}
```

Không cần thay đổi gì ở pipeline constructor — constraints đã được pass sẵn.

---

### Pipeline — video_pipeline.py

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

**6 điểm sửa:**

##### 1. `run()` — Skip Step 2c khi `location_ref=False`

```python
# Trong run(), thay step chain:
use_loc_ref = self.constraints.get("location_ref", True)

steps = [
    ("step0", self._run_step0),
    ("step1", self._run_step1),
    ("step2a", self._run_step2a),
    ("step2b", self._run_step2b),
]
if use_loc_ref:
    steps.append(("step2c", self._run_step2c))
else:
    # Mark step2c as skipped in UI
    steps.append(("_skip_2c", lambda: (
        self._update_step("step2c", "done", "Skipped (inline mode)"),
        self._log("[Step 2c] ⏭ Skipped — inline location mode"),
        True
    )[-1]))

steps.extend([
    ("_labels", lambda: (self._extract_valid_labels(), True)[1]),
    ("step3", self._run_step3),
    ("step4", self._run_step4),
    ("step5", self._run_step5),
])
```

##### 2. `_extract_valid_labels()` — Không extract location labels khi inline

Giữ nguyên logic, nhưng khi `location_ref=False`, `valid_labels["locations"]` sẽ tự động rỗng (vì `locations_data` rỗng).

→ **Không cần sửa** — tự hoạt động.

##### 3. `_build_labels_block()` — Bỏ location labels

Giữ nguyên logic — khi `valid_labels["locations"]` rỗng, block tự không in location.

→ **Không cần sửa**.

##### 4. Step 3: `STEP3_SYSTEM_PROMPT` + `_build_visual_reference()` + `_process_sequence_step3()`

**Rule 1 (Label Lock)** — thay đổi khi inline mode:

Hiện tại:
```
### Rule 1: Label Lock (CRITICAL)
`locked_location` must match a location label.
```

Inline mode thêm:
```
### Rule 1: Label Lock (CRITICAL)
`character_labels` must match character labels.
IF location labels are provided in === AVAILABLE LABELS ===, `locked_location` must match.
IF NO location labels provided, write `location_anchor` — a one-sentence description 
of the PHYSICAL PLACE where this sequence happens (era-specific, filmable).
```

**Output format** — thêm `location_anchor`:
```json
{
  "sequence_id": "SEQ_01",
  "locked_location": "",              // empty khi inline mode
  "location_anchor": "Makeshift timber raft crossing the Tigris River at night, 1138 AD",
  "visual_event": "...",
  "scenes": [...]
}
```

**`_build_visual_reference()`** — khi inline mode, bỏ VISUAL REFERENCE: LOCATIONS section (vì `locations_data` rỗng, tự bỏ).

→ **Không cần sửa** — đã handle `self.locations_data` rỗng.

**`_validate_scene_labels()`** — khi `valid_labels["locations"]` rỗng, bỏ qua location validation.

→ **Không cần sửa** — code hiện tại kiểm tra `loc not in valid_labels["locations"]`, nếu list rỗng thì skip.

##### 5. Step 4: `STEP4_USER_TEMPLATE` + `_build_mini_bible()` + `_process_sequence_step4()`

**`STEP4_USER_TEMPLATE`** — thay đổi rule cho location:

Hiện tại:
```
Location: [{location}]
...
- flat_prompt MUST contain the [Location-Label] from the sequence — NEVER omit it
```

Inline mode:
```
Location Context: {location}
...
- flat_prompt MUST describe the environment naturally based on the scene's 
  background_and_extras and lighting_and_atmosphere fields.
  For Wide/Medium shots: describe the full environment.
  For Close-ups: describe only what the camera sees (surface texture, object detail) 
  with subtle environmental hints.
- Do NOT use [bracket] notation for locations.
```

→ Cần **2 template**: `STEP4_USER_TEMPLATE` (hiện tại) và `STEP4_USER_TEMPLATE_INLINE`.

**`_build_mini_bible()`** — khi inline mode:
- Bỏ phần location reference
- Giữ character reference + World Bible compact

**`_process_sequence_step4()`**:
- Chọn template dựa trên `location_ref` flag
- `location` field trong output = `location_anchor` (descriptive) thay vì label

##### 6. Step 5: `_export_excel()` — Sheet 2 bỏ location rows

Khi `location_ref=False`:
- Sheet 1 cột "Location" hiển thị `location_anchor`
- Sheet 2 **không output location reference images** (vì không có `locations_data`)

→ **Không cần sửa** — code hiện tại loop `self.locations_data.get("locations", [])`, rỗng thì skip.

---

## Tóm tắt Files Changed

| File | Thay đổi |
|---|---|
| `video_prompt_tab.py` | +1 checkbox, +1 constraint |
| `video_pipeline.py` | Skip Step 2c, Step 3 prompt alt rule, Step 4 new template + mini_bible branch |

## Chi tiết impact per step

| Step | `location_ref=True` (mặc định) | `location_ref=False` (inline) |
|---|---|---|
| 2a | Không đổi | Không đổi |
| 2b | Không đổi | Không đổi |
| 2c | Chạy bình thường | **Skip** (done + skipped message) |
| Labels | Chars + Locations | Chars only |
| 3 | `locked_location` = label | `location_anchor` = description, `locked_location` = "" |
| 4 | `[Label]` bracket + location ref | Inline environment weave, no brackets |
| 5 | Location rows in Sheet 2 | No location rows |

## Verification Plan

### Automated Tests
1. Syntax check 3 files
2. Run pipeline với `location_ref=False` trên ch_01 test data
3. So sánh output prompt: kiểm tra không còn `[Location-Label]` bracket

### Manual Verification
- So sánh 2 bản Excel output (ref vs inline) trên cùng chapter
- Kiểm tra prompt tự nhiên hơn, environment mô tả phù hợp shot type
