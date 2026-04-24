# Audit: Angle ↔ Opening Pattern ↔ Body Element Compatibility

## Phương pháp

Với mỗi **body element** trong write prompt, xác định **data field** cần thiết → đối chiếu với **required_fields** và **preferred_fields** của 8 angle_presets → tìm **conflict** (element cần data mà angle không cung cấp).

---

## 1. Body Elements cần data gì?

| Element | Data field cần | Bắt buộc? |
|---------|---------------|:---------:|
| A. Countdown Anchor | — (chỉ cần `countdown_position` từ outline) | ✅ Luôn có |
| B. Opening Angle | **Tùy pattern** (xem bảng dưới) | ✅ |
| C. Spec Foundation | `key_specs` + `data_focus` fields | ✅ Luôn có |
| D. Mechanical Insight | `action_mechanism` hoặc `internal_ballistics` | ✅ |
| E. Physical Translation | Bất kỳ số liệu nào | ✅ Luôn có nếu có specs |
| F. Heritage Nugget | `origin_history` | ⚠️ Tùy chọn |
| G. Weakness | `cons_to_mention` (từ outline, dựa trên blueprint) | ✅ |
| H. User Verdict | `target_user` (từ outline) | ✅ |
| I. Cliffhanger | — (từ outline `ends_with`) | ✅ |

---

## 2. Opening Patterns cần data gì?

| Pattern | Data field thực sự cần | Không hoạt động nếu thiếu |
|---------|----------------------|--------------------------|
| R1 `myth_crusher` | `myths_misconceptions` | ❌ Myth để crush |
| R2 `heritage_authority` | `origin_history` | ❌ Lịch sử để kể |
| R3 `rd_endurance` | `reliability_durability` | ❌ Test data / round count |
| R4 `rule_breaker` | `unique_selling_point` (từ outline) | ⚠️ Outline phải có USP mạnh |
| R5 `hater_bait` | — (dựa vào controversy, không cần field cụ thể) | ✅ Luôn dùng được |
| R6 `category_disruptor` | — (dựa vào positioning, không cần field cụ thể) | ✅ Luôn dùng được |

---

## 3. MA TRẬN XUNG ĐỘT: 8 Angles × 6 Opening Patterns

> ✅ = Dùng được (angle CÓ data cho pattern)
> ⚠️ = Có thể dùng nhưng data ở preferred chứ không required
> ❌ = XUNG ĐỘT (angle KHÔNG có data cho pattern)

| Angle ↓ / Pattern → | R1 myth | R2 heritage | R3 rd_endure | R4 rule_break | R5 hater | R6 disrupt |
|---------------------|:---:|:---:|:---:|:---:|:---:|:---:|
| **combat_self_defense** | ❌ | ❌ | ✅ `reliability` | ⚠️ | ✅ | ✅ |
| **budget_value** | ❌ | ❌ | ✅ `reliability` | ⚠️ | ✅ | ✅ |
| **myth_busting** | ✅ `myths` | ⚠️ `origin` | ❌ | ⚠️ | ✅ | ✅ |
| **technical_deep_dive** | ❌ | ❌ | ❌ | ⚠️ | ✅ | ✅ |
| **heritage_evolution** | ⚠️ `myths` | ✅ `origin` | ❌ | ⚠️ | ✅ | ✅ |
| **contrarian_underrated** | ⚠️ `myths` | ❌ | ✅ `reliability` | ⚠️ | ✅ | ✅ |
| **durability_torture** | ❌ | ❌ | ✅ `reliability` | ⚠️ | ✅ | ✅ |
| **practical_duty** | ❌ | ❌ | ⚠️ `reliability` | ⚠️ | ✅ | ✅ |

### Tóm tắt xung đột:

| # | Xung đột | Mức nghiêm trọng | Chi tiết |
|---|----------|:-:|---------|
| 1 | `combat` + R1 `myth_crusher` | 🔴 | `myths_misconceptions` không nằm trong required NOR preferred |
| 2 | `combat` + R2 `heritage_authority` | 🔴 | `origin_history` không nằm trong required NOR preferred |
| 3 | `budget` + R1 `myth_crusher` | 🔴 | Không có myth data |
| 4 | `budget` + R2 `heritage_authority` | 🔴 | Không có heritage data |
| 5 | `technical` + R1 `myth_crusher` | 🔴 | Không có myth data |
| 6 | `technical` + R2 `heritage_authority` | 🔴 | Không có heritage data |
| 7 | `technical` + R3 `rd_endurance` | 🔴 | Không có reliability data |
| 8 | `heritage` + R3 `rd_endurance` | 🟡 | Reliability không required, không preferred |
| 9 | `durability` + R1 `myth_crusher` | 🔴 | Không có myth data |
| 10 | `durability` + R2 `heritage_authority` | 🔴 | Không có heritage data |
| 11 | `practical` + R1 `myth_crusher` | 🔴 | Không có myth data |
| 12 | `practical` + R2 `heritage_authority` | 🔴 | Không có heritage data |

---

## 4. Body Element "Mechanical Insight" — Ai KHÔNG có data?

| Angle | Có `action_mechanism`? | Có `internal_ballistics`? | Viết Mechanical Insight được? |
|-------|:---:|:---:|:---:|
| combat_self_defense | ❌ | ❌ | ❌ **Chỉ có terminal + recoil + reliability** |
| budget_value | ❌ | ❌ | ❌ **Chỉ có cost + reliability** |
| myth_busting | ❌ | ✅ | ✅ |
| technical_deep_dive | ✅ preferred | ✅ required | ✅ |
| heritage_evolution | ❌ | ⚠️ preferred | ⚠️ |
| contrarian | ❌ | ⚠️ preferred | ⚠️ |
| durability_torture | ✅ preferred | ❌ | ✅ |
| practical_duty | ❌ | ❌ | ❌ **Chỉ có use-case + ergonomics** |

> **Vấn đề:** 3 angles (combat, budget, practical) KHÔNG có bất kỳ mechanism data nào → element "Mechanical Insight" sẽ buộc AI bịa hoặc bỏ trống.

---

## 5. Body Element "Heritage Nugget" — Ai KHÔNG có data?

| Angle | Có `origin_history`? | Heritage Nugget khả thi? |
|-------|:---:|:---:|
| combat | ❌ | ❌ |
| budget | ❌ | ❌ |
| myth_busting | ⚠️ preferred | ⚠️ |
| technical | ❌ | ❌ |
| heritage | ✅ required | ✅ |
| contrarian | ❌ | ❌ |
| durability | ❌ | ❌ |
| practical | ❌ | ❌ |

> **Vấn đề:** 6/8 angles KHÔNG có `origin_history` → Heritage Nugget sẽ bị skip ở đa số scripts. Hoặc AI bịa.

---

## 6. Giải pháp đề xuất

### A. Thêm `compatible_patterns` cho mỗi angle

Thay vì để outline AI tự chọn bất kỳ pattern nào, mỗi angle preset nên khai báo patterns nào DÙNG ĐƯỢC:

```json
"combat_self_defense": {
    "compatible_patterns": ["rd_endurance", "rule_breaker", "hater_bait", "category_disruptor"],
    "incompatible_patterns": ["myth_crusher", "heritage_authority"]
}
```

### B. Sửa Heritage Nugget + Mechanical Insight thành conditional

Trong write prompt, thay vì bắt buộc:
```
F. HERITAGE NUGGET: If origin_history is empty, skip gracefully — do NOT invent.
   → ĐÃ CÓ rule này nhưng chưa rõ ràng.

D. MECHANICAL INSIGHT: If action_mechanism AND internal_ballistics are BOTH empty,
   replace with USE-CASE INSIGHT — how does this product perform in its intended scenario?
```

### C. Mở rộng required_fields cho một số angles

Thêm data sources phù hợp:
- `combat_self_defense`: thêm `action_mechanism` vào preferred (biết trigger type, safety matters for combat)
- `budget_value`: thêm `materials_finish` đã có, thêm `action_mechanism` vào preferred
- `practical_duty`: thêm `action_mechanism` vào preferred

### D. Thêm `origin_history` làm universal preferred

Vì Heritage Nugget là element đã chứng minh hiệu quả (competitor lúc nào cũng dùng), nên `origin_history` nên là **universal preferred** cho MỌI angle — không phải required, nhưng luôn được ưu tiên khi enrich.

---

## 7. Tương tự cho Deep Dive & H2H

### Deep Dive (topic_block)

| Pattern | Data cần | Xung đột? |
|---------|---------|-----------|
| T1 `myth_attack` | `myths_misconceptions` | ❌ nếu blueprint không có myth cho topic này |
| T2 `scenario_cold_open` | `practical_use_case` | ⚠️ Một số topics (casing, projectile) khó cold-open với scenario |
| T3 `comparative_anchor` | `comparisons` | ❌ Deep Dive = single product → comparison data có thể thiếu |
| T4 `historical_context` | `origin_history` | ⚠️ Chỉ 1-2 topics có historical context |

> **Vấn đề:** T3 `comparative_anchor` không hợp lý cho Deep Dive (single product). Comparisons data thường rất mỏng ở single-product blueprint.
>
> **Giải pháp:** Đổi T3 thành `cross_reference` — thay "so sánh 2 sản phẩm" thành "so sánh số liệu ĐÃ NÓI ở chapter trước vs chapter này" (ví dụ: "Chamber pressure was 21,000 PSI. Now look at what that means for recoil: 7.5 ft-lbs.")

### Head-to-Head (criterion)

| Pattern | Data cần | Xung đột? |
|---------|---------|-----------|
| H1 `standard_showdown` | Both products have data for this criterion | ✅ Outline đã yêu cầu |
| H2 `same_scenario` | Scenario context | ⚠️ Một số criteria (casing, projectile_construction) khó dựng scenario |
| H3 `myth_crusher` | Common belief about this criterion | ⚠️ Không phải criterion nào cũng có myth |

> **Vấn đề nhẹ:** H2 và H3 không phải lúc nào cũng dùng được. Nhưng vì outline chọn pattern, và chỉ có 4-6 criterion chapters → chọn H2/H3 cho 1-2 chapters phù hợp là đủ.
