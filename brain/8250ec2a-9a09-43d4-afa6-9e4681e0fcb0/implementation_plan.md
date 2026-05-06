# Refactor Step 3 & Step 4

## Step 3: chỉ giữ quyết định cấu trúc cảnh

**Bỏ** 3 field: `costume_note`, `lighting_and_atmosphere`, `background_and_extras`  
**Thêm**: `has_crowd` (boolean)

Output JSON mới:
```json
{
  "global_scene_id": "SEQ_01_SCN_01",
  "duration": 4.0,
  "audio_sync": "...",
  "character_labels": [],
  "shot_type": "Wide Shot",
  "roll_type": "B-Roll",
  "camera_motion": "Slow Pan",
  "time_of_day": "night",
  "physical_action": "...",
  "has_crowd": true
}
```

## Step 4: thêm thinking fields, tự tra reference data

Step 4 **tự viết** chi tiết visual từ reference:

| Thinking field | Nguồn |
|---|---|
| `costume` | Character sheet + action context |
| `lighting` | time_of_day + location data |
| `background` | Location bible_description + shot_type |
| `extras` | Crowd archetypes từ World Bible (chỉ khi `has_crowd = true`), mô tả hành động, không cần tả trang phục chi tiết |
| `character_blocking` | character_labels + shot_type |
| `emotion` | Nhân vật + context |
| `key_props` | Action context |
| `camera_angle` | Shot context |
| `effects` | Scene context |
| `flat_prompt` | Tổng hợp tất cả trên |

## Sửa code cụ thể

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

**1. `STEP3_SYSTEM_PROMPT`** (~line 438-570):
- Bỏ Rule 6 (Costume Note)
- Bỏ Rule 7 (Background & Extras) → thay: `has_crowd = true/false`
- Output schema: bỏ 3 field cũ, thêm `has_crowd`

**2. `STEP4_USER_TEMPLATE` + `STEP4_USER_TEMPLATE_INLINE`** (~line 575-688):
- Bỏ rules cũ (from costume_note, from background_and_extras, from lighting_and_atmosphere)
- Thêm thinking fields mới: `costume`, `lighting`, `background`, `extras`
- Rules mới: tra character reference cho costume, suy lighting từ time_of_day + location, viết background từ location data + shot_type, mô tả extras action khi has_crowd = true

**3. scenes_text_parts builder** (~line 1883-1896):
- Bỏ: `Costume:`, `Background:`, `Lighting:` 
- Thêm: `Crowd: yes/no`

**4. Final prompt dict** (~line 1946-1960):
- Thêm fields mới: `costume`, `lighting`, `background`, `extras`
- Bỏ: `crowd_description`

## Verification
1. Syntax check
2. Xóa checkpoint Step 3 + 4 → chạy lại chapter test
3. So sánh flat_prompt mới vs cũ
