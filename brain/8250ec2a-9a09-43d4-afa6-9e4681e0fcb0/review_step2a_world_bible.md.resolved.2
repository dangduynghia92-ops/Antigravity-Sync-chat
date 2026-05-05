# Phân tích chiến lược: Step 2a World Bible — 5 câu hỏi

---

## Câu 1: Step 2a nên chứa DATA gì?

### Hiện tại World Bible chứa:
```
era, geography, factions[](name, heraldry, primary_colors, armor, 
civilian_clothing, weapons, crowd_archetypes{}), architecture{}, props{}
```

### Bảng phân tích: Downstream cần gì từ World Bible?

| Field | Step 2b (Characters) | Step 2c (Locations) | Step 3 (Storyboard) | Step 4 (Prompt) |
|---|---|---|---|---|
| `era` + exact dates | ✅ Xác định trang phục đúng thời kỳ | ✅ Xác định kiến trúc | ❌ Không cần | ❌ Không cần |
| `geography` | ❌ | ✅ Landscape, terrain | ❌ | ❌ |
| `faction.heraldry` | ✅ Gắn biểu tượng lên áo | ❌ | ✅ Banner trong background | ✅ Mô tả cờ hiệu |
| `faction.primary_colors` | ✅ Tô màu trang phục | ❌ | ✅ Phân biệt phe | ✅ Ghi màu trong prompt |
| `faction.armor` | ✅ Tạo character visual_desc | ❌ | ✅ costume_note | ✅ Mô tả nhân vật |
| `faction.weapons` | ✅ Gắn vũ khí | ❌ | ✅ key_props | ✅ Mô tả đạo cụ |
| `faction.crowd_archetypes` | ❌ | ❌ | ✅ Rule 7: background | ✅ crowd_description |
| `architecture` | ❌ | ✅ Bible description | ❌ | ✅ Location trong prompt |
| `props` | ❌ | ✅ Key props of setting | ✅ key_props | ✅ Chi tiết cảnh |

### Data THIẾU mà nên thêm:

| Data thiếu | Tại sao cần | Ví dụ |
|---|---|---|
| **`date_range`** (exact years) | Phân biệt đầu kỳ/cuối kỳ — armor thay đổi trong cùng 1 era | `"82-44 BC"` thay vì `"Roman Republic"` |
| **`technology_constraints`** | Cảnh quay không có đồ vật chưa phát minh | `"No stirrups (not invented until ~6th century)"` |
| **`banner_rules`** | Cổ đại dùng standards, không dùng cờ vải | `"Roman legions use eagle aquila standards on poles, NOT cloth flags"` |
| **`faction.role_variants`** | Mô tả vai trò trung gian (vua, tướng, thầy tu) — hiện chỉ có generic crowd | `"general": "wears red cloak over standard armor, crested helmet"` |
| **`lighting_palette`** | Ánh sáng đặc trưng của era — torch/candle/oil lamp | `"Indoor: oil lamps and tallow candles, warm amber"` |

### Đề xuất cấu trúc data mới — Chia 3 DOMAIN:

```
Domain A: HISTORICAL CONTEXT (Nền tảng sự thật)
├── era (exact date range)
├── geography
├── technology_constraints
├── banner_rules

Domain B: FACTION VISUAL BIBLE (Trang phục & con người)
├── factions[]
│   ├── name, heraldry, primary_colors
│   ├── armor (chi tiết theo date_range)
│   ├── weapons[]
│   ├── role_variants{} (general, priest, noble, merchant)
│   └── crowd_archetypes{} (soldier, civilian_man/woman, child)

Domain C: ENVIRONMENTAL VISUAL BIBLE (Không gian & đồ vật)
├── architecture[] (structured, not flat dict)
├── props{} (by category)
└── lighting_palette
```

**Lợi ích:** Khi inject downstream, Python chỉ chọn domain cần thiết:
- Step 2b → inject Domain A + Domain B
- Step 2c → inject Domain A + Domain C
- Step 3 → inject Domain B (crowd_archetypes) + một phần Domain C
- Step 4 → inject compact summary từ cả 3

---

## Câu 2: Output format nên như nào?

### Vấn đề hiện tại

Step 2b inject World Bible bằng cách **DUMP TOÀN BỘ JSON** vào system prompt:

```python
# Line 954-955
sys_prompt += f"\n\n=== WORLD BIBLE REFERENCE ===\n{json.dumps(self.world_bible, ensure_ascii=False)}\n..."
```

Step 2c chỉ inject `architecture + era + geography` — đã lọc tốt hơn.

Step 3 `_build_visual_reference()` trích xuất từng field riêng lẻ — format rõ ràng.

Step 4 `_build_mini_bible()` compact nhất — chỉ lấy data liên quan đến sequence hiện tại.

### Đánh giá

| Bước | Cách inject hiện tại | Đánh giá |
|---|---|---|
| Step 2b | DUMP toàn bộ JSON | 🔴 Quá nhiều data. architecture, props không cần cho character |
| Step 2c | Lọc architecture + era + geo | ✅ Tốt |
| Step 3 | Trích xuất field-by-field | ✅ Tốt nhưng text format lộn xộn |
| Step 4 | Mini bible (chỉ chars/locs liên quan) | ✅ Tốt |

### Đề xuất format output

JSON nên giữ nguyên **1 file checkpoint** nhưng chia rõ 3 domain để code Python dễ lọc:

```json
{
  "historical_context": {
    "era": "Late Roman Republic, 82-44 BC",
    "date_range": "82 BC to 44 BC", 
    "geography": "Rome, Italy; Mediterranean coastlines; Spain; Egypt",
    "technology_constraints": [
      "No stirrups — cavalry mounts bareback or uses simple saddle",
      "Iron weapons, no steel — gladius is short thrusting sword",
      "Writing on wax tablets and papyrus scrolls, no codex books"
    ],
    "banner_rules": "Roman legions carry aquila (eagle standard) on a pole. Vexillum (small cloth square) used for sub-units only. NO large cloth national flags."
  },
  "factions": [
    {
      "name": "Sullan Loyalists (Optimates)",
      "heraldry": "Roman eagle (aquila) on red field",
      "primary_colors": ["crimson red", "bronze", "dark brown"],
      "armor": "Lorica hamata (iron chain mail shirt to mid-thigh), bronze Montefortino helmet with horsehair crest, rectangular scutum shield with red leather cover and bronze boss",
      "weapons": ["gladius hispaniensis (short sword)", "pilum (heavy javelin)", "pugio (dagger)"],
      "role_variants": {
        "general": "Red paludamentum cloak over polished bronze muscled cuirass, transverse red horsehair crest on helmet",
        "senator": "White toga with broad purple stripe (toga praetexta), leather sandals",
        "priest": "White toga with head covered (capite velato), no armor"
      },
      "crowd_archetypes": {
        "soldier": "Chain mail over red wool tunic, bronze helmet, rectangular shield, sandaled boots",
        "civilian_man": "Simple undyed wool tunic to knees, rope belt, leather sandals",
        "civilian_woman": "Long stola in muted earth tones over white tunica, palla (shawl) draped over head",
        "child": "Short undyed tunic, barefoot or simple sandals",
        "noble": "White toga with narrow purple stripe, leather shoes",
        "clergy": "White robes, laurel wreath headband for augurs"
      }
    }
  ],
  "architecture": [
    {
      "name": "Roman Republic Villa",
      "materials": ["travertine limestone", "terracotta roof tiles", "marble columns (imported)"],
      "structural_elements": ["atrium with impluvium pool", "peristyle garden with columns", "opus reticulatum wall pattern"],
      "interior": "Mosaic floors, painted frescoes on plastered walls, oil lamp niches",
      "lighting": "Oil lamps (lucernae) on bronze stands, natural light from atrium opening"
    }
  ],
  "props": {
    "military": "Pilum javelin, scutum shield, gladius in leather scabbard on right hip, military standard with eagle",
    "household": "Terracotta oil lamps, bronze mirrors, wooden writing tablets with iron stylus, ceramic amphorae",
    "religious": "Incense burner (turibulum), sacrificial knife, laurel branches, small household shrine (lararium)",
    "marketplace": "Wooden market stalls, ceramic pottery, woven baskets, bronze coins (denarii)"
  }
}
```

Code Python chỉ cần:
```python
# Step 2b: inject factions + historical context (NO architecture, NO props)
inject_for_2b = {
    "historical_context": self.world_bible["historical_context"],
    "factions": self.world_bible["factions"]
}

# Step 2c: inject architecture + props + historical context (NO factions)
inject_for_2c = {
    "historical_context": self.world_bible["historical_context"],
    "architecture": self.world_bible["architecture"],
    "props": self.world_bible["props"]
}
```

---

## Câu 3: Input hiện tại có hợp lý không?

### Hiện tại:

```python
seq_data = [{"sequence_id": s["sequence_id"],
             "full_text": s.get("full_text", "")}
            for s in self.sequences]
```

Gửi **mảng các sequences** (đã chunked) từ Step 1.

### Đánh giá: ⚠️ KHÔNG tối ưu

| Vấn đề | Giải thích |
|---|---|
| **Fragmented context** | Text đã bị chia thành 15-30 sequences. LLM phải tự ghép lại trong đầu để hiểu tổng thể |
| **Sequence IDs thừa** | World Bible không cần biết SEQ_01, SEQ_02... — nó cần TOÀN BỘ câu chuyện |
| **Token waste** | JSON formatting + sequence_id = ~15-20% tokens thừa |
| **Đã có sẵn `cleaned_text`** | Step 0 đã tạo ra `self.cleaned_text` — plain text liền mạch, SẠCH — nhưng Step 2a KHÔNG dùng |

### Đề xuất: Dùng `cleaned_text` thay vì sequences

```python
# Thay đổi input:
user_msg = self.cleaned_text  # Plain text narrative, no JSON, no sequence_ids
```

**Lý do:**
1. World Bible cần **ngữ cảnh TỔNG THỂ** (ai vs ai, ở đâu, thời nào) — plain text cho bức tranh toàn cảnh tốt nhất
2. Tiết kiệm tokens — không có JSON formatting overhead
3. LLM đọc văn xuôi tốt hơn JSON khi cần hiểu ngữ cảnh lịch sử
4. `cleaned_text` đã có sẵn từ Step 0, đã lọt bỏ timecode

> [!IMPORTANT]
> `cleaned_text` là input LÝ TƯỞNG cho World Bible vì nó giống như đọc một cuốn kịch bản — LLM có thể nắm bắt toàn bộ cốt truyện, nhân vật, bối cảnh trong một lần đọc.

---

## Câu 4: Trang phục nhân vật chính/phụ có ở bước này không?

### Hiện tại: KHÔNG có trang phục NHÂN VẬT CỤ THỂ

Step 2a chỉ có trang phục cấp **PHE PHÁI** (faction level):
- `faction.armor` = armor chung cho cả phe
- `faction.civilian_clothing` = quần áo dân thường chung
- `faction.crowd_archetypes` = 6 mẫu người generic

Step 2b mới tạo `visual_description` cho từng nhân vật cụ thể.

### Đánh giá: ✅ ĐÚNG thiết kế — nhưng có GAP

**Đúng:** Nhân vật CỤ THỂ (Caesar, Sulla) nên ở Step 2b vì cần:
- Khuôn mặt riêng, vóc dáng riêng
- Trang phục có thể khác biệt (Caesar mặc toga, Sulla mặc giáp)
- Age variants (Caesar trẻ vs già)

**GAP:** Giữa "faction generic" và "named character" có **khoảng trống**:

```
faction.armor = "lorica hamata, bronze helmet"  ← QUÁ CHUNG
                                                   ↕ GAP
step2b.character.visual_desc = "Caesar in white toga..."  ← QUÁ CỤ THỂ
```

Step 2b phải **tự đoán** trang phục cho vai trò trung gian:
- Tướng quân mặc gì khác lính thường?
- Quan chức mặc gì khác dân thường?
- Thầy tu mặc gì?

### Đề xuất: Thêm `role_variants` để lấp gap

```json
"role_variants": {
  "general": "Red cloak over polished muscled cuirass, transverse helmet crest",
  "senator": "White toga praetexta with purple stripe",
  "priest": "White toga, head covered, no armor",
  "merchant": "Shorter tunic, leather belt with coin pouch",
  "slave": "Simple rough linen tunic, no shoes, no belt"
}
```

**Tác dụng:** Step 2b sẽ có sẵn "nguyên liệu" để phối trang phục cho nhân vật dựa trên vai trò của họ, thay vì tự bịa.

---

## Câu 5: Có nên chia nhỏ API call không?

### Hiện tại: 1 CALL duy nhất

LLM phải làm TẤT CẢ trong 1 lần:
1. Đọc toàn bộ script
2. Xác định era + date range
3. Liệt kê tất cả factions
4. Mô tả chi tiết armor, weapons, heraldry cho MỖI faction
5. Mô tả 6 crowd archetypes cho MỖI faction
6. Mô tả tất cả architecture styles
7. Mô tả tất cả props categories

**Đây là 7 tasks trong 1 call.** Với script dài (5000+ từ), output dễ dàng 3000-5000 tokens.

### Đánh giá: 🔴 NÊN CHIA

Khi bắt LLM làm quá nhiều task cùng lúc:
- Chất lượng giảm ở các task cuối (attention suy yếu)
- Dễ bỏ sót faction/location
- Chi tiết lịch sử dễ bị "trộn" giữa các era nếu script có time jump

### Đề xuất: Chia thành 2 CALL

```
CALL 1: "IDENTIFY" — Nhẹ, nhanh, chính xác
├── Input: cleaned_text
├── Output: era, date_range, geography, faction names, technology_constraints, banner_rules
├── Tier: Pro (cần accuracy)
└── Tokens: ~500-800 output

CALL 2: "DESCRIBE" — Nặng, chi tiết, dùng output Call 1 làm context
├── Input: cleaned_text + kết quả Call 1 (era + factions list)
├── Output: chi tiết từng faction (armor, weapons, crowd_archetypes, role_variants) 
│           + architecture[] + props{}
├── Tier: Pro (cần accuracy)
└── Tokens: ~2000-4000 output
```

### Tại sao 2 call tốt hơn 1 call?

| Tiêu chí | 1 Call (hiện tại) | 2 Calls (đề xuất) |
|---|---|---|
| **Xác định era** | Đoán → viết luôn | Đoán → xác nhận → viết |
| **Chi tiết lịch sử** | Phải nhớ era trong khi viết 20+ mô tả | Era đã chốt, chỉ cần viết mô tả |
| **Trường hợp script mơ hồ** | LLM đoán sai era → toàn bộ sai | Call 1 sai → có thể kiểm tra trước khi Call 2 |
| **Token budget** | 1 prompt dài, attention bị phân tán | 2 prompt ngắn, focused |
| **Chi phí** | 1 API call | 2 API calls (tốn thêm ~30% nhưng chất lượng cao hơn nhiều) |

> [!TIP]
> Call 1 còn có thể dùng làm **checkpoint riêng** — nếu user thấy era sai, có thể sửa tay trước khi Call 2 chạy (future feature).

---

## Tổng kết các thay đổi đề xuất

| # | Thay đổi | Impact | Effort |
|---|---|---|---|
| 1 | Dùng `cleaned_text` thay sequences làm input | 🟢 Input tốt hơn, tiết kiệm tokens | Nhỏ |
| 2 | Chia thành 2 API calls (Identify → Describe) | 🔴 Cải thiện chất lượng lớn nhất | Trung bình |
| 3 | Thêm `role_variants` vào faction | 🟡 Lấp gap cho Step 2b | Nhỏ |
| 4 | Cấu trúc architecture[] thành array có fields | 🟡 Location descriptions chính xác hơn | Nhỏ |
| 5 | Chia JSON thành 3 domain để lọc selective | 🟡 Inject downstream chính xác, bớt token | Trung bình |
| 6 | Bỏ `civilian_clothing`, gộp vào crowd_archetypes | 🟢 Bỏ trùng lặp | Nhỏ |
| 7 | Thêm retry 2 lần | 🟡 Robustness | Nhỏ |
