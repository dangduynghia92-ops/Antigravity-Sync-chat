# Nâng cấp Step 2: World Bible → Characters → Locations

## Vấn đề hiện tại

Reference images ra kết quả không nhất quán vì thiếu historical context:
- **Characters**: "flashy crusader armor" → AI tự chọn màu/biểu tượng → 2 ảnh khác nhau hoàn toàn
- **Locations**: Không biết era → Japanese temple vs Medieval European village
- **World Bible**: Output sơ sài, `era` trống, không phân theo faction

### So sánh với Product Tab (SRT Prompt)

| Tiêu chí | Product Tab | Video Pipeline |
|---|---|---|
| Historical context | ✅ `character_scan_prompt.txt` có "HISTORICAL CONTEXT: Time Period, Geography, Factions" | ❌ Không có |
| Location detail | ✅ `location_prompt.txt` có Architecture, Environment, Key Props, Atmosphere | ❌ Chỉ có `bible_description` 2-3 câu |
| World Bible → Character | ✅ Context truyền từ scan → character description | ❌ Step 2c chạy SAU 2a → không dùng được |

## Proposed Changes

### 1. Đảo thứ tự Step 2

```
TRƯỚC: Step 2a (Characters) → Step 2b (Locations) → Step 2c (World Bible)
SAU:   Step 2c (World Bible) → Step 2a (Characters) → Step 2b (Locations)
```

---

### 2. Nâng cấp Step 2c — World Bible Prompt

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

Sửa `STEP2_WORLD_BIBLE_PROMPT` — output phải bao gồm:

```json
{
  "era": "Crusader States Period, 1174-1185 AD",
  "geography": "Kingdom of Jerusalem, Levant",
  "factions": [
    {
      "name": "Kingdom of Jerusalem (Crusaders)",
      "heraldry": "Gold Jerusalem cross on white/silver field",
      "primary_colors": ["white", "gold", "red"],
      "armor": "Chain mail hauberk with coif, flat-top great helm or nasal helm, white surcoat with gold Jerusalem cross, kite shield",
      "civilian_clothing": "Linen tunics, woolen mantles, leather sandals",
      "weapons": ["broadsword", "kite shield", "lance", "crossbow"]
    },
    {
      "name": "Ayyubid Sultanate (Saracens)",
      "heraldry": "Eagle of Saladin on yellow field",
      "primary_colors": ["yellow", "green", "black"],
      "armor": "Lamellar armor over mail, spiked helm with aventail, round shield",
      "civilian_clothing": "Flowing robes, turbans, embroidered sashes",
      "weapons": ["curved scimitar", "round shield", "composite bow"]
    }
  ],
  "architecture": {
    "crusader": "Romanesque limestone fortresses, pointed arches, crenellated walls, cross-shaped windows",
    "islamic": "Horseshoe arches, geometric tilework, muqarnas vaults, minarets",
    "mixed_jerusalem": "Blend of Romanesque and Islamic elements, golden limestone, domed roofs"
  },
  "props": {
    "military": "banners with faction heraldry, siege engines, war drums",
    "civilian": "oil lamps, clay pots, woven carpets, market stalls",
    "royal": "golden throne, velvet cushions, jeweled crown, silk banners"
  }
}
```

---

### 3. Nâng cấp Step 2a — Characters Prompt

Sửa `STEP2_CHARACTERS_SYSTEM_PROMPT`:

**Thêm vào visual_description requirement:**
```
- **visual_description**: MUST include ALL of the following:
  1. BODY: height, build, skin tone, hair style + color
  2. FACE: distinguishing features (scar, beard, expression)
  3. COSTUME (MAIN): primary garment with EXACT colors and emblems from World Bible faction data
  4. COSTUME (DETAIL): belt, boots, gloves, cape, accessories
  5. SIGNATURE ITEM: one unique prop/weapon that identifies this character
  
  BAD: "A mature man in crusader armor"
  GOOD: "A tall, broad-shouldered man (~5 heads tall) with short brown hair 
         and a thick handlebar mustache. Wears a white surcoat with a gold 
         Jerusalem cross over chain mail, brown leather belt with lion-head 
         buckle, tall brown riding boots. Carries a broadsword on left hip."
```

**Inject World Bible context:**
```python
# In _run_step2a():
if self.world_bible_data:
    sys_prompt += f"\n\n=== WORLD BIBLE REFERENCE ===\n{json.dumps(self.world_bible_data)}"
    sys_prompt += "\nUse faction colors, heraldry, and armor types from this reference."
```

---

### 4. Nâng cấp Step 2b — Locations Prompt

Sửa `STEP2_LOCATIONS_SYSTEM_PROMPT`:

**Thêm chi tiết giống Product Tab:**
```
For each unique location:
- **label**: Location name
- **bible_description**: MUST include ALL of:
  1. ARCHITECTURE: building style, materials, structural elements matching the era
  2. ENVIRONMENT: landscape, terrain, vegetation, indoor/outdoor
  3. KEY PROPS: furniture, decorations, objects in this setting
  4. ATMOSPHERE: typical weather, lighting, time of day, mood
- **default_lighting**: Specific lighting (e.g., "warm torchlight from iron sconces")
- **camera_angle**: FIXED camera angle for reference image — always "wide establishing shot, 
  eye-level, slightly low angle to show full space, 16:9 aspect ratio"
```

**Inject World Bible context:**
```python
# In _run_step2b():
if self.world_bible_data:
    arch_ref = json.dumps(self.world_bible_data.get("architecture", {}))
    sys_prompt += f"\n\n=== ARCHITECTURE REFERENCE ===\n{arch_ref}"
    sys_prompt += "\nAll locations MUST use architecture styles from this reference."
```

> [!IMPORTANT]
> **Camera angle thống nhất**: Tất cả location reference images phải dùng cùng 1 góc nhìn cố định (wide establishing shot, eye-level) để đảm bảo consistency khi tạo ảnh.

---

### 5. Code Changes — `_run_step` ordering

```python
# Current order in run():
("step2a", self._run_step2a),  # Characters
("step2b", self._run_step2b),  # Locations  
("step2c", self._run_step2c),  # World Bible

# New order:
("step2c", self._run_step2c),  # World Bible FIRST
("step2a", self._run_step2a),  # Characters (with World Bible context)
("step2b", self._run_step2b),  # Locations (with World Bible context)
```

---

## Open Questions

> [!IMPORTANT]
> 1. **Camera angle cho location ref**: Nên dùng góc nào cố định? Đề xuất: "wide establishing shot, eye-level, slightly low angle" — nhưng bạn có muốn khác không?
> 2. **field `original_name` ở Step 2a**: Hiện tại là `real_name` trong prompt nhưng code đọc `original_name`. Cần thống nhất tên field?

## Verification Plan

### Test
1. Xóa checkpoints Step 2a/2b/2c
2. Chạy lại pipeline cho Baldwin IV
3. Kiểm tra:
   - World Bible có đủ faction + heraldry + architecture
   - Character visual_description có màu sắc cụ thể từ faction
   - Location bible_description có 4 mục (Architecture, Environment, Props, Atmosphere)
4. Tạo ảnh reference từ Excel → kiểm tra consistency
