# Phân tích chất lượng Blueprint Extraction — Battle of Lepanto 1571

## Tổng quan

- **Script gốc**: 10 chapters, tiếng Anh, ~47KB
- **Blueprint output**: 209 dòng JSON, **tiếng Tây Ban Nha** (vì `lang=es`)
- **Prompt file**: [system_extract_blueprint.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_extract_blueprint.txt)

---

## Đánh giá theo từng Section

### ✅ Tốt — `key_facts` (19 items)
- Bao quát đầy đủ: ngày tháng, địa điểm, quân số, thương vong, kích thước đội hình
- Có chi tiết cụ thể: "40.000 muertos en 4 horas", "12.000 esclavos liberados"
- ✓ Không copy nguyên câu từ script — đã paraphrase đúng cách

### ✅ Tốt — `key_characters` (5 nhân vật)
- 5 nhân vật chính đều được trích: Don Juan, Bragadin, Pope Pius V, Ali Pasha, Cervantes
- Mỗi nhân vật có: role, personality traits, key_decisions, fate
- Personality có chiều sâu: "hijo bastardo del emperador" (Don Juan), "su confianza raya en la arrogancia" (Ali Pasha)

### ✅ Tốt — `technical_details` (4 items)
- Galley, Galeaza, Corte de espolones, Arcabuz vs Arco — đều có `mechanism` + `tactical_impact`
- Giải thích cơ chế rõ: "permitía que los cañones de proa bajaran su ángulo de tiro"

### ✅ Tốt — `arguments` (3 luận điểm)
- Có cả claim + evidence + counter evidence
- Bao gồm 3 góc nhìn: biểu tượng vs chiến lược, tâm lý, công nghệ

### ✅ Tốt — `narrative_moments` (4 scenes)
Vivid details rất chi tiết, giữ đúng hình ảnh cảm giác:
- "pelarle la piel metódicamente desde el cuello" (lột da)
- "cubiertas tan resbaladizas de sangre que los hombres deben esparcir arena" (boong trơn máu rải cát)
- "Cervantes, temblando de fiebre, se niega a obedecer" (run sốt từ chối ở dưới boong)

---

## ⚠️ Gaps — Nội dung bị thiếu/yếu

### 1. ❌ Missing key_event: **Trận đánh cánh Bắc (Barbaro vs Siroco)**
Script Ch.7 mô tả chi tiết:
- Siroco chui qua khe hẹp giữa bờ đá và đội hình Venice → flanking
- Barbaro bị bắn vào mắt → lính Venice bùng nổ phản công → đẩy Siroco vào bờ đá
- Đây là 1 trong 3 mặt trận quan trọng nhất nhưng **hoàn toàn vắng mặt** trong blueprint

### 2. ❌ Missing key_character: **Agostino Barbarigo** + **Mehmed Siroco**
- 2 chỉ huy cánh Bắc — Barbarigo (Venice) bị mũi tên xuyên mắt, Siroco (Ottoman) bị đẩy vào bờ đá
- Không có trong `key_characters` lẫn `key_events`

### 3. ⚠️ Yếu — `geography_and_conditions`
- Chỉ là 1 chuỗi text duy nhất, không structured
- Thiếu chi tiết: khoảng cách bờ đá cánh Bắc, mô tả vùng nước nông mà Siroco exploit
- Script gốc mô tả rất cụ thể terrain cánh Bắc ảnh hưởng trực tiếp đến chiến thuật

### 4. ⚠️ Yếu — `narrative_moments` thiếu scene cánh Bắc
- 4 scenes hiện tại: Famagusta, Galeaza, Flagship duel, Cervantes
- Thiếu: **Barbaro bị bắn vào mắt** (chi tiết visual cực mạnh: "lifted visor → arrow in eye → carried below deck screaming")
- Thiếu: **"Floating continent"** (mô tả cảm giác: boong nối boong tạo continent, trơn máu, rải cát)

### 5. ⚠️ Missing — `must_include` thiếu chi tiết về **lưới phòng thủ (netting)**
- Script Ch.7: Christians strung heavy nets over decks để bắt boarding parties và chặn mũi tên
- Đây là chi tiết kỹ thuật quan trọng nhưng không xuất hiện ở `technical_details` hay `must_include`

### 6. ⚠️ `product_evaluation` / `ranking_criteria` — **không cần nhưng vẫn có**
- Blueprint vẫn xuất hiện trường `ranking_criteria`, `original_order`, `thesis_angle`
- Đây là fields cho niche **product review**, không liên quan đến battle narrative
- Prompt yêu cầu return `"product_evaluation": []` nếu không phải product review → ✓ đã return `[]`
- Nhưng `ranking_criteria`, `original_order`, `thesis_angle` vẫn tồn tại → gây nhiễu

---

## Root Cause & Đề xuất cải thiện

### Vấn đề gốc: Prompt quá chung chung cho battle niche

`system_extract_blueprint.txt` hiện tại là **1 prompt dùng cho mọi niche**: history, mystery, product review. Kết quả:

| Vấn đề | Nguyên nhân |
|---------|-------------|
| Thiếu trận đánh cánh Bắc | Prompt chỉ yêu cầu "major events" — AI tự quyết cái nào "major" |
| Thiếu Barbarigo/Siroco | Prompt yêu cầu "major figures" — AI chỉ chọn 5 nhân vật chính nhất |
| `geography` quá sơ sài | Chỉ 1 trường text, không structured → AI viết lướt |
| Thừa fields product review | Prompt luôn yêu cầu `ranking_criteria`, `original_order` cho mọi niche |

### Đề xuất: Tạo `system_extract_blueprint_battle.txt`

Tương tự cách đã có `_mystery.txt` và `_review.txt`, tạo prompt riêng cho **battle/military niche** với:

1. **Structured `battles` field** thay vì chỉ `key_events`:
   - Mỗi trận/mặt trận: commanders, forces, terrain, tactics, outcome, turning_point
   - Bắt buộc cover **tất cả mặt trận** (left flank, center, right flank)

2. **Structured `geography`** — dict thay vì string:
   - `terrain_features`: danh sách các yếu tố địa hình ảnh hưởng chiến thuật
   - `weather_events`: thời tiết, gió, tầm nhìn
   - `strategic_positions`: các vị trí chiến lược

3. **Bỏ fields product review**: `ranking_criteria`, `original_order`, `thesis_angle`, `product_evaluation`

4. **Tăng quota `narrative_moments`**: Yêu cầu cover ≥1 scene per major battle phase

5. **Thêm `tactical_evolution` field**: Theo dõi chiến thuật thay đổi trong trận (pre-battle → opening → turning point → collapse)

### Code change cần thiết

Trong [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py#L1004-L1044):

```diff
 def extract_blueprint(full_text, api_client, lang="en", log_callback=None):
+    # Detect niche to choose appropriate prompt
+    # For now: use generic prompt for all niches
     system_template = _load_prompt("system_extract_blueprint.txt")
```

→ Thêm niche detection giống `extract_blueprint_review()` đã làm cho mystery vs review.
