# Nâng cấp Step 2a: World Bible — Implementation Plan

## Mục tiêu
Cải thiện chất lượng và độ chính xác lịch sử của Step 2a (World Bible) trong Video Pipeline bằng cách tối ưu input, chia nhỏ API call, và cấu trúc output cho việc inject downstream chính xác hơn.

---

## Proposed Changes

### Prompts (System Prompts trong video_pipeline.py)

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

**Thay đổi 1: Tách `STEP2_WORLD_BIBLE_PROMPT` thành 2 prompt**

- **`STEP2A_IDENTIFY_PROMPT`** (Call 1 — nhẹ, chính xác)
  - Input: `cleaned_text` (plain text narrative)
  - Task: Xác định era, exact date_range, geography, liệt kê tên tất cả factions
  - Output: JSON nhỏ ~500 tokens

- **`STEP2A_DESCRIBE_PROMPT`** (Call 2 — nặng, chi tiết)
  - Input: `cleaned_text` + kết quả Call 1 (era đã chốt)
  - Task: Mô tả chi tiết visual cho từng faction, architecture, props
  - Output: JSON đầy đủ ~2000-4000 tokens

**Thay đổi 2: Schema mới cho output**

Chia thành 3 domain:

```json
{
  "historical_context": {
    "era": "Late Roman Republic, 82-44 BC",
    "date_range": "82-44 BC",
    "geography": "Rome, Mediterranean"
  },
  "factions": [{
    "name": "...",
    "heraldry": "mô tả VẬT THỂ cụ thể, không dùng từ trừu tượng",
    "primary_colors": [],
    "armor": "chi tiết theo đúng date_range",
    "weapons": [],
    "role_variants": {
      "general": "trang phục cụ thể cho tướng",
      "noble/senator": "trang phục cụ thể cho quý tộc",
      "priest/clergy": "trang phục cụ thể cho giáo sĩ"
    },
    "crowd_archetypes": {
      "soldier": "...",
      "civilian_man": "...",
      "civilian_woman": "...",
      "child": "...",
      "noble": "...",
      "clergy": "..."
    }
  }],
  "architecture": [{
    "name": "...",
    "materials": [],
    "structural_elements": [],
    "interior": "...",
    "lighting": "..."
  }],
  "props": {
    "military": "...",
    "household": "...",
    "religious": "...",
    "marketplace": "..."
  }
}
```

- Bỏ `civilian_clothing` (đã có trong `crowd_archetypes`)
- Thêm `role_variants` vào faction
- `architecture` chuyển từ flat dict → structured array

---

**Thay đổi 3: Logic `_run_step2a()` — 2 calls + retry**

```
Flow mới:
1. Input = self.cleaned_text (thay vì sequences JSON)
2. Call 1: IDENTIFY (retry 2 lần)
   → Parse JSON → lấy era, factions list
3. Call 2: DESCRIBE (retry 2 lần)
   → Inject era + faction names từ Call 1
   → Parse JSON → lấy full details
4. Merge Call 1 + Call 2 → save checkpoint
```

---

**Thay đổi 4: Update downstream injection**

- `_run_step2b()` (line 953-955): Inject chỉ `historical_context` + `factions` (bỏ architecture/props)
- `_run_step2c()` (line 1004-1010): Inject chỉ `historical_context` + `architecture` + `props` (bỏ factions)
- `_build_visual_reference()` (line 1101-1129): Update field names cho schema mới
- `_build_mini_bible()` (line 1263-1294): Update field names cho schema mới

---

## Verification Plan

### Manual Verification
- Xem debug dump output từ 2 calls (system_prompt + raw_response)
- Kiểm tra JSON checkpoint `_step2_world_bible.json` có đúng schema mới
- Kiểm tra Step 2b/2c/3/4 có nhận đúng data từ World Bible mới
