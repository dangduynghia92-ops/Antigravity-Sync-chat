# Review: Step 2a — World Bible (Đánh giá độ chính xác lịch sử)

## Mục tiêu

Step 2a phải tạo ra một "từ điển hình ảnh lịch sử" **chính xác** để các bước sau (2b Characters, 2c Locations, 3 Storyboard, 4 Prompt Writing) tham chiếu. Nếu bước này sai → toàn bộ pipeline sai theo.

---

## 1. Prompt hiện tại — Phân tích từng phần

### ✅ Những gì đang tốt

| Yếu tố | Đánh giá |
|---|---|
| Schema JSON rõ ràng | ✅ LLM biết chính xác cần trả về gì |
| `crowd_archetypes` (6 loại) | ✅ Giúp Step 3 mô tả nhân vật nền |
| `primary_colors` distinct per faction | ✅ Tránh nhầm phe |
| Flexible cho biography | ✅ "Use social groups if no military" |

### 🔴 Vấn đề nghiêm trọng

#### Vấn đề 1: LLM phải TỰ ĐOÁN thời kỳ lịch sử — không có cơ chế kiểm chứng

Prompt chỉ nói:
> *"Analyze the script to identify the historical era"*

LLM đọc script rồi tự đoán era. Nhưng:
- Script POV thường **không ghi năm cụ thể** ("You are 18..." → LLM phải tự biết đó là Caesar, 82 BC)
- Nếu LLM đoán sai era → toàn bộ armor, weapons, heraldry sẽ sai theo
- **Không có cơ chế double-check** era sau khi LLM trả về

> [!CAUTION]
> Ví dụ thực tế: Script nói "Roman soldiers" nhưng không nói năm. LLM có thể trả về:
> - Republic era (lorica hamata, gladius, scutum) ← đúng cho Caesar
> - Imperial era (lorica segmentata, spatha, clipeus) ← sai cho Caesar
> - Late Empire (lamellar armor, ridge helmet) ← sai hoàn toàn
> 
> Sai lệch 100 năm = trang phục hoàn toàn khác nhau.

#### Vấn đề 2: Prompt thiếu yêu cầu DẪN CHỨNG cụ thể

Prompt hiện tại chỉ nói:
> *"Historically accurate to the identified era"*

Quá chung chung. Không ép LLM phải:
- Nêu **nguồn tham chiếu** (tranh vẽ, tượng, tài liệu)
- Giải thích **tại sao** chọn chi tiết này
- Phân biệt giữa **đầu kỳ vs cuối kỳ** (ví dụ: French infantry mặc white trước 1806, blue sau 1806 — cùng Napoleonic Wars)

#### Vấn đề 3: `architecture` schema quá lỏng

```json
"architecture": {
    "style_name": "description"
}
```

Chỉ là 1 dict key-value. Không ép cấu trúc cụ thể. LLM có thể viết:
- ❌ `"Crusader architecture": "stone buildings"` (quá chung)
- ✅ Nên ép tách ra: materials, structural_elements, decorative_features, roof_type

#### Vấn đề 4: `props` schema quá lỏng — giống architecture

```json
"props": {
    "category": "description"
}
```

LLM không biết category nào cần viết. Có thể bỏ sót furniture, lighting, food, transport...

#### Vấn đề 5: Không retry khi fail

Step 1 retry 2 lần. Step 2a **chỉ 1 lần** — nếu JSON parse fail thì return False.

#### Vấn đề 6: `civilian_clothing` trùng với `crowd_archetypes.civilian_man/woman`

Hai field cùng mô tả quần áo dân thường. LLM dễ viết mâu thuẫn hoặc copy-paste.

---

## 2. Data flow — World Bible đi đâu?

```
World Bible JSON
├─→ Step 2b: TOÀN BỘ JSON inject vào system prompt
│   → LLM dùng faction colors, armor, weapons để tạo character visual_description
│   → ⚠ NẾU armor sai ở World Bible → character mặc sai
│
├─→ Step 2c: Chỉ inject architecture + era + geography
│   → LLM dùng để mô tả locations
│   → ⚠ NẾU architecture sai → location mô tả sai vật liệu/phong cách
│
├─→ Step 3: _build_visual_reference() → trích xuất:
│   - Era, Geography
│   - Faction name, heraldry, colors, armor, weapons
│   - Crowd archetypes (6 loại)
│   - Architecture styles
│   → Step 3 prompt Rule 7 yêu cầu dùng crowd_archetypes cho background_and_extras
│
└─→ Step 4: Inject vào STEP4_USER_TEMPLATE → {mini_bible}
    → LLM viết flat_prompt dựa trên visual reference này
```

> [!IMPORTANT]
> **World Bible là nền tảng cho TOÀN BỘ visual output.** Sai 1 chi tiết ở đây = sai ở mọi frame video.

---

## 3. Đề xuất cải thiện — Xếp theo mức độ ưu tiên

### 🔴 P0: Thêm yêu cầu DATE-SPECIFIC trong prompt

Hiện tại prompt chỉ nói "historically accurate". Cần ép LLM phải:

1. **Xác định EXACT date range** trước khi mô tả bất kỳ thứ gì
2. **Giải thích logic** cho các chi tiết nhạy cảm (armor, banner, weapons)
3. **Phân biệt đầu kỳ vs cuối kỳ** nếu era dài (e.g., Roman Republic 509-27 BC)

Đề xuất thêm vào prompt:
```
## CRITICAL RULES FOR HISTORICAL ACCURACY
- You MUST identify the EXACT date range (e.g., "82-44 BC", not just "Roman Republic")
- Armor, weapons, and banners CHANGE within the same era. Use the SPECIFIC date, not the general era.
- For EACH faction, add a "historical_note" field explaining WHY you chose these specific visual details
- Ancient armies (Rome, Greece, Persia, Egypt) did NOT have cloth national flags — they used standards, signa, aquilae, or vexillum
- Medieval armies used heraldic banners tied to specific lords/kingdoms, NOT national flags
```

### 🟡 P1: Cấu trúc `architecture` và `props` chặt hơn

Đề xuất thay đổi schema:

```json
"architecture": [
  {
    "name": "Crusader Fortress",
    "materials": ["limestone blocks", "cedar wood beams"],
    "structural_elements": ["pointed arches", "barrel vaults", "crenellated walls"],
    "decorative_features": ["carved Jerusalem crosses", "iron-studded doors"],
    "roof_type": "flat stone roof with battlements",
    "interior_lighting": "narrow arrow slits, iron torch sconces"
  }
],
"props": {
  "military": "description",
  "household": "description", 
  "religious": "description",
  "marketplace": "description",
  "lighting": "description (torches, candles, oil lamps)"
}
```

### 🟡 P2: Bỏ `civilian_clothing`, gộp vào `crowd_archetypes`

Loại bỏ trùng lặp. `crowd_archetypes` đã có `civilian_man` + `civilian_woman` → đủ rồi.

### 🟡 P3: Thêm retry (giống Step 1)

```python
for attempt in range(2):
    raw = self._send_llm(...)
    parsed = _try_parse_json(raw)
    if parsed and isinstance(parsed, dict) and parsed.get("factions"):
        break
```

### 🟢 P4 (Optional): Thêm field `historical_note` cho mỗi faction

Ép LLM giải thích tại sao chọn chi tiết đó. Không dùng cho downstream, chỉ để user/debug kiểm tra.

```json
{
  "name": "Roman Republic Forces",
  "historical_note": "82 BC — Sulla's army. Late Republic era uses lorica hamata (chain mail), NOT the later segmentata. Weapons: gladius hispaniensis (shorter than Imperial gladius).",
  "armor": "...",
  ...
}
```

---

## 4. Tóm tắt

| Vấn đề | Impact | Fix |
|---|---|---|
| LLM tự đoán era, không verify | 🔴 Cao | Ép exact date + historical_note |
| Prompt quá chung "historically accurate" | 🔴 Cao | Thêm specific rules (flags, armor changes) |
| Architecture/Props schema quá lỏng | 🟡 Trung bình | Ép cấu trúc chi tiết |
| civilian_clothing trùng crowd_archetypes | 🟡 Nhỏ | Bỏ civilian_clothing |
| Không retry | 🟡 Trung bình | Thêm retry 2 lần |
| Không có historical_note | 🟢 Nice-to-have | Thêm field giải thích |
