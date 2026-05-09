# Kiểm tra cấu trúc Step 3 & Step 4

## Step 3 — Scenes (97 scenes / 17 sequences)

### Fields mỗi scene:
| Field | Mô tả | Ví dụ |
|---|---|---|
| `global_scene_id` | ID duy nhất | `SEQ_01_SCN_01` |
| `duration` | Thời lượng (s) | `4.0` |
| `character_labels` | Nhân vật chính | `['Ayyubid-Commander-A']` |
| `crowd_labels` | Nhân vật phụ | `['EXT-Ayyubid-Soldier-Infantry']` |
| `shot_type` | Kiểu shot | `Wide Shot`, `Medium Shot`, `Close-up` |
| `roll_type` | A-Roll/B-Roll | `A-Roll` |
| `camera_motion` | Camera | `Static`, `Slow Tracking` |
| `time_of_day` | Thời gian | `night` |
| `physical_action` | Hành động | "stands at the entrance looking toward the mountains" |
| `has_crowd` | Có quần chúng | `True`/`False` |
| `location_anchor` | Bối cảnh | "A sprawling Ayyubid siege camp at night..." |
| `audio_sync` | Câu thoại | "The mountain air is thin and freezing." |
| `character_interaction` | Tương tác | `none` hoặc mô tả |

> [!NOTE]
> Step 3 đầy đủ 14 fields. `crowd_labels` có mặt ở 72% scenes.

---

## Step 4 — Flat Prompts (97 prompts)

### Fields mỗi prompt:
| Field | Mô tả |
|---|---|
| `global_scene_id` | ID scene |
| `duration` | Thời lượng |
| `characters` | Labels nhân vật chính |
| `character_info` | Mô tả visual chi tiết (body, face, costume) |
| `characters_detail` | JSON chi tiết costume |
| `extras` | **Mô tả crowd** — bao gồm `[EXT-*]` label + costume detail |
| `lighting` | Ánh sáng chi tiết |
| `background` | Background painterly detail |
| `key_props` | Props quan trọng |
| `camera_angle` | Góc camera |
| `effects` | Hiệu ứng (smoke, dust...) |
| `crowd_labels` | Danh sách EXT-* labels |
| `flat_prompt` | **Prompt gen ảnh cuối cùng** |
| `negative_prompt` | Prompt loại trừ |
| `index` | STT |

### Mẫu flat_prompt:
```
(1_SEQ_01_SCN_01) Stylized historical animation illustration of [Ayyubid-Commander-A] 
standing at the entrance of a large fortified command tent at night. 
[Ayyubid-Commander-A] wears a yellow silk kaftan with gold thread embroidery over 
iron lamellar armor, red linen sirwal, and a gilded iron conical helmet wrapped in 
a yellow silk turban. He has a circular geometric head with a uniform flat white 
#FFFFFF fill, small oval dot eyes, and thick black eyebrows. In the background, 
a sprawling siege camp is filled with [EXT-Ayyubid-Soldier-Infantry] in yellow 
padded cotton kazaghand huddled near fires. The landscape features jagged black 
basalt mountain peaks under a pitch black sky with sharp starlight. The background 
is a detailed painterly environment. Thick uniform dark outlines on all characters. 
Professional animation quality, 16:9 aspect ratio.
```

### Thống kê coverage:

| Metric | Kết quả |
|---|---|
| Total prompts | 97 |
| `characters` empty | 13/97 (13%) — scenes chỉ có crowd, không có named char |
| `crowd_labels` present | **70/97 (72%)** |
| `EXT-` in flat_prompt | **64/97 (65%)** |
| `extras` empty | 32/97 (32%) |
| `effects` empty | 33/97 (34%) — nhiều scene đơn giản không có effect |
| `lighting`, `background`, `key_props` | ✅ 100% có |
| `camera_angle` | ✅ 100% có |

> [!IMPORTANT]  
> **Thành phần có trong flat_prompt:**  
> ✅ Style prefix (Stylized historical animation)  
> ✅ Character label `[Ayyubid-Commander-A]`  
> ✅ Costume chi tiết (color + material + specific garment)  
> ✅ Art style rules (circular head, flat white #FFFFFF, minimalist features)  
> ✅ Crowd `[EXT-*]` với costume  
> ✅ Background painterly detail  
> ✅ Lighting (scene-specific)  
> ✅ Camera (shot type embedded)  
> ✅ Index prefix `(1_SEQ_01_SCN_01)`
