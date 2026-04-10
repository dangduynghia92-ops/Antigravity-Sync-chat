# Pre-compute Scoring — Phân tích rủi ro & Khả thi

## 🔴 PHÁT HIỆN NGHIÊM TRỌNG: Tier values trong blueprint KHÔNG MATCH style JSON

Tested trên 3 blueprint thật (Einstein, Barbarossa, Van Gogh). Kết quả:

### Einstein
| Framework | Tier field | Blueprint value | Expected value | Match? |
|---|---|---|---|---|
| Sử Thi | `impact_radius` | `"global"` | `"Civilizational_Level"` | ❌ |
| Bản Án | `opposition_severity` | `"extreme"`, `"high"`, `"medium"` | `"Lethal_Eradication"`, etc. | ❌ |
| Kẻ Xét Lại | `historical_distortion_level` | `"moderate"` | `"Oversimplification"` | ❌ |
| Hai Mặt | `dark_side_severity` | *(missing entirely)* | `"Personal_Flaws"` | ❌ |

### Barbarossa
| Framework | Blueprint value | Expected | Match? |
|---|---|---|---|
| Sử Thi | `"Intercontinental (Europe, Africa, Asia)"` | `"Civilizational_Level"` | ❌ |
| Bản Án | `"Extreme"`, `"High"` | `"Lethal_Eradication"` | ❌ |
| Kẻ Xét Lại | `"High (due to 16th-century..."` *(full sentence!)* | `"Demonization_Framing"` | ❌ |

### Van Gogh  
| Framework | Blueprint value | Expected | Match? |
|---|---|---|---|
| Sử Thi | `"Global"` | `"Domain_Level"` | ❌ |
| Bản Án | `"high"`, `"extreme"` | enum values | ❌ |

> [!CAUTION]
> ## Kết luận: 100% blueprint hiện tại KHÔNG dùng enum values
> 
> Blueprint extraction prompt **ĐANG** yêu cầu enum values (e.g., `"Civilizational_Level"`).
> Nhưng AI **THỰC TẾ** viết free-text (e.g., `"global"`, `"extreme"`, hoặc cả câu dài).
> 
> **Hậu quả**: Pre-compute scoring bằng Python sẽ **FAIL trên 100% blueprints hiện có**.
> AI recommend_framework "vẫn chạy" vì AI đọc ngôn ngữ tự nhiên được, nhưng code thì không.

---

## Phân tích chi tiết theo framework

### 1. Hai Mặt (`dual_nature.dark_side[].dark_side_severity`)
```
Expected: "Personal_Flaws" | "Professional_Unethical" | "Crimes_Against_Humanity"
Reality:  Field MISSING entirely in all 3 blueprints
```
**Nguyên nhân**: Blueprint extraction prompt (line 100-103) YÊU CẦU tag `dark_side_severity`, nhưng AI bỏ qua hoặc không tag.

### 2. Sử Thi (`paradigm_shift[].impact_radius`)
```
Expected: "Domain_Level" | "Societal_Level" | "Civilizational_Level"
Reality:  "global", "Global", "Regional (Mediterranean Basin)", "Continental (Europe)"
```
**Nguyên nhân**: AI viết theo cách hiểu tự nhiên thay vì dùng enum.

### 3. Bản Án (`systemic_opposition[].opposition_severity`)
```
Expected: "Censorship_Reputation" | "Exile_Imprisonment" | "Lethal_Eradication"
Reality:  "extreme", "high", "medium", "Extreme", "High", "Medium"
```
**Nguyên nhân**: AI dùng generic severity thay vì enum cụ thể.

### 4. Kẻ Xét Lại (`historiography.historical_distortion_level`)
```
Expected: "None" | "Oversimplification" | "Erasure_Stolen_Legacy" | "Demonization_Framing"
Reality:  "moderate", hoặc cả đoạn text dài giải thích
```
**Nguyên nhân**: AI không biết/không tuân thủ enum values.

### 5. Sự Lụi Tàn (`downfall_pattern[].severity`)
```
Expected: "Poor_Judgment" | "Systematic_Corruption" | "Megalomaniac_Collapse"
Reality:  Field chưa tồn tại (mới thêm)
```

---

## Hai hướng giải quyết

### Hướng A: Sửa extraction prompt (upstream fix)
**THÊM** ví dụ cứng và constraint nghiêm ngặt hơn vào extraction prompt để AI buộc phải dùng enum values.

| Ưu | Nhược |
|---|---|
| Sửa tận gốc | Blueprint cũ vẫn sai |
| Tương lai sẽ đúng | Cần re-extract blueprint cho projects cũ |
| Code pre-compute đơn giản | AI vẫn CÓ THỂ viết sai |

### Hướng B: Fuzzy tier mapping trong Python (downstream fix)
**THÊM** bảng mapping linh hoạt trong code:
```python
TIER_ALIASES = {
    "Civilizational_Level": ["global", "civilizational", "world-changing"],
    "Societal_Level": ["continental", "societal", "national"],
    "Domain_Level": ["regional", "domain", "field-level"],
    "Lethal_Eradication": ["extreme", "lethal", "death", "execution"],
    "Exile_Imprisonment": ["high", "exile", "imprisonment", "prison"],
    ...
}
```

| Ưu | Nhược |
|---|---|
| Hoạt động với blueprint cũ | Bảng alias có thể miss edge cases |
| Không cần re-extract | Thêm một lớp mapping phải maintain |
| Chấp nhận AI viết tự do | Khi thêm framework mới phải update alias |

### Hướng C: KẾT HỢP A + B (Khuyến nghị)
1. Sửa extraction prompt → blueprint mới sẽ dùng đúng enum
2. Thêm fuzzy mapping → blueprint cũ vẫn score được
3. Log WARNING khi fuzzy match → biết blueprint nào cần re-extract

---

## Rủi ro cụ thể nếu triển khai NGAY mà không fix

| Rủi ro | Xác suất | Ảnh hưởng |
|---|---|---|
| Pre-compute scoring = 0 cho mọi framework | 100% | AI nhận toàn điểm 0, chọn random |
| Blueprint cũ không tương thích | 100% | Phải re-extract HOẶC add fuzzy mapping |
| AI vẫn viết sai enum sau khi sửa prompt | ~30% | Cần fuzzy mapping làm safety net |
| Thêm framework mới quên update alias table | ~20% | Scoring sai cho framework mới |

---

## Kiến nghị thứ tự triển khai

1. **Sửa extraction prompt TRƯỚC** — thêm STRICT constraints cho tier values
2. **Test bằng cách re-extract 1 blueprint** (Einstein) — xem AI có tuân thủ enum không
3. **NẾU AI tuân thủ** → triển khai pre-compute đơn giản (exact match only)
4. **NẾU AI vẫn viết sai** → thêm fuzzy mapping table
5. **Log mọi thứ** — in tier values tìm thấy, matched/unmatched, final score
