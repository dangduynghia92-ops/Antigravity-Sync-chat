# Thống nhất Character & Crowd xuyên suốt Pipeline

## Vấn đề
Crowd character được đối xử như phần phụ — thiếu costume, action, interaction trong các bước dựng cảnh và viết prompt. Character có đầy đủ thông tin LOCKED qua từng step, Crowd thì không.

## Hiện trạng từng Step

### Data gốc (Step 2b + 2d) — ✅ Đã đủ
Cả Character và Crowd đều có `visual_description` chi tiết (BODY, FACE, COSTUME, Acc, default_stance).
**→ Không cần sửa.**

---

### Step 3.1: Visual Interpreter (Dựng cảnh từ câu)
**Hiện tại**:
- Character: `character_labels`, `character_interaction` ✅
- Crowd: `crowd_labels` ✅, nhưng **không yêu cầu LLM mô tả crowd action** ❌

**Sửa**: Thêm field `crowd_action` vào output schema

```diff
  "scenes": [
    {
      "visual": "...",
-     "duration": 2.54
+     "duration": 2.54,
+     "crowd_action": "what the crowd extras are physically doing in this moment"
    }
  ]
```

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)
- `STEP3_1_SYSTEM_PROMPT` (~L637-660): Thêm field `crowd_action` vào JSON output schema
- Thêm Rule: "If crowd_labels is not empty, describe what the crowd is physically doing"

---

### Step 3.2: Camera Director (Cắt cảnh)
**Hiện tại**:
- Character: `character_labels`, `physical_action`, `character_interaction` ✅
- Crowd: `crowd_labels`, `has_crowd` ✅, nhưng **không có `crowd_action`** ❌

**Sửa**: Thêm field `crowd_action` vào output schema

```diff
  "scenes": [
    {
      "global_scene_id": "SEQ_01_SCN_01",
      ...
      "physical_action": "...",
+     "crowd_action": "what crowd extras are physically doing — visible pose/movement",
      "has_crowd": true
    }
  ]
```

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)
- `STEP3_SYSTEM_PROMPT` (~L742-764): Thêm `crowd_action` vào JSON output schema
- Rule 6 (~L710-715): Thêm yêu cầu: "When has_crowd = true, also fill `crowd_action` describing what the crowd extras are physically doing"

---

### Step 4: Prompt Writing — ĐÂY LÀ CHỖ CHÊNH LỆCH LỚN NHẤT

**Hiện tại** (code dòng 2758-2800):

| Input gửi cho LLM | Character | Crowd |
|---|---|---|
| Label | ✅ `Characters: Ayyubid-Commander-A` | ✅ chỉ label `Crowd: yes — EXT-*` |
| Costume LOCKED | ✅ `costume_lookup` chi tiết | ❌ **KHÔNG GỬI** |
| Action | ✅ `physical_action` | ❌ **KHÔNG GỬI** |
| Interaction | ✅ `character_interaction` | — |

**Sửa 3 chỗ**:

#### 4A. Build `crowd_costume_lookup` (giống `costume_lookup`)

```python
# Build crowd costume lookup (SAME logic as character)
crowd_costume_lookup = {}
for c in self.crowd_data.get("characters", []):
    label = c.get("label", "")
    desc = c.get("visual_description", "")
    costume_parts = []
    for line in desc.split("."):
        line_s = line.strip()
        ul = line_s.upper()
        if any(kw in ul for kw in ["COSTUME:", "CLOTHING:", "ACCESSORIES:", "ARMOR:"]):
            for prefix in ["COSTUME:", "CLOTHING:", "ACCESSORIES:", "ARMOR:"]:
                if ul.startswith(prefix):
                    line_s = line_s[len(prefix):].strip()
                    break
            costume_parts.append(line_s)
    if costume_parts:
        crowd_costume_lookup[label] = ". ".join(costume_parts)
```

#### 4B. Thêm crowd costume + crowd action vào `scenes_text_parts`

```diff
  f"  Costume (LOCKED — copy exactly):\n{costume_block}\n"
  f"  Action: {scene.get('physical_action', '')}\n"
  f"  Interaction: {scene.get('character_interaction', 'none')}\n"
- f"  Crowd: {'yes' if scene.get('has_crowd') else 'no'}"
- f"{'— ' + ', '.join(crowd_labels) if crowd_labels else ''}"
+ f"  Crowd: {'yes' if scene.get('has_crowd') else 'no'}\n"
+ f"  Crowd Labels: {', '.join(crowd_labels) if crowd_labels else 'none'}\n"
+ f"  Crowd Action: {scene.get('crowd_action', 'none')}\n"
+ f"  Crowd Costume (LOCKED — copy exactly):\n{crowd_costume_block}"
```

#### 4C. Step 4 output schema — thêm `crowd_detail` (đối xứng với `characters_detail`)

Hiện tại Step 4 output có:
```json
{
  "characters_detail": [{"label": "...", "costume": "...", "action": "..."}],
  "extras": "brief text about crowd"
}
```

Đổi thành:
```json
{
  "characters_detail": [{"label": "...", "costume": "...", "action": "...", "blocking": "...", "emotion": "..."}],
  "crowd_detail": [{"label": "[EXT-*]", "costume": "LOCKED from input", "action": "...", "blocking": "..."}],
  "extras": "brief summary for quick reference"
}
```

> [!IMPORTANT]
> `extras` field vẫn giữ (backward compatible) nhưng `crowd_detail` là nguồn chính cho flat_prompt.

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)
- `_process_sequence_step4` (~L2758-2800): Build crowd_costume_lookup + thêm vào scenes_text_parts
- `STEP4_USER_TEMPLATE` + `STEP4_USER_TEMPLATE_INLINE` (~L772-894): Thêm `crowd_detail` vào output schema, update rules
- Result builder (~L2849-2867): Lưu `crowd_detail` field

---

### Step 5: Excel Export — ✅ Đã sửa
Sheet 1 có `Crowd` column, Sheet 2 có crowd entries. Không cần thay đổi thêm.

---

## Tóm tắt thay đổi

| Bước | Thay đổi | Files |
|---|---|---|
| **Step 3.1** | Thêm `crowd_action` vào output schema | `STEP3_1_SYSTEM_PROMPT` |
| **Step 3.2** | Thêm `crowd_action` vào output schema | `STEP3_SYSTEM_PROMPT` |
| **Step 4 input** | Build `crowd_costume_lookup`, gửi LOCKED cho LLM | `_process_sequence_step4` |
| **Step 4 template** | Thêm `crowd_detail` output schema, update rules | `STEP4_USER_TEMPLATE`, `STEP4_USER_TEMPLATE_INLINE` |
| **Step 4 output** | Lưu `crowd_detail` field | `_process_sequence_step4` result builder |

> [!WARNING]
> Thay đổi này ảnh hưởng Step 3 + Step 4, cần **xóa checkpoint** Step 3 + 4 để chạy lại. Checkpoint Step 0-2 giữ nguyên.

## Verification Plan
1. Xóa checkpoint Step 3 + 4
2. Chạy lại pipeline trên Test 3
3. Kiểm tra:
   - `_step3_scenes.json`: mỗi scene có `crowd_action`
   - `_step4_prompts.json`: mỗi prompt có `crowd_detail` với costume LOCKED
   - `flat_prompt`: crowd mô tả đầy đủ costume + action
   - Excel: không thay đổi format
