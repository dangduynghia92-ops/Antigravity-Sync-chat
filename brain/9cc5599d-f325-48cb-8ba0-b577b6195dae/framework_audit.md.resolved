# 🔍 Full Audit — cinematic_military_v2.json

## 1. TERMINOLOGY LEAK (đã phát hiện trước)

> [!CAUTION]
> Framework jargon vẫn rải rác ở `steps`, `outline_rules`, `transitions`, `cliffhanger_types`, `act_breakdown`, `chapter_rhythm`, `forbidden`. Cần fix toàn bộ.

---

## 2. POV STRATEGY — Sai loại

**Trial (L409-414)**: Dùng "Prosecution voice" và "Defense voice" — đây là **tone**, không phải POV.
**Pendulum (L542-547)**: Dùng "Admiring third-person" và "Cold, clinical third-person" — cũng là **tone**.

`core_rules.pov_rules` chỉ định nghĩa 4 POV: 3rd omniscient, 2nd person, 1st plural, 1st singular.

> [!WARNING]
> AI có thể viết literal: *"The prosecution argues that..."* hoặc *"From a cold, clinical perspective..."* — lộ framework.

**Fix**: Đổi thành POV thật (3rd omniscient) + ghi tone riêng trong miêu tả, ví dụ: `"to": "Third-person omniscient (confident, assertive tone)"`.

---

## 3. FRAMEWORK APPLICABILITY — Trial quá hẹp

| Framework | Áp dụng được cho | Phạm vi |
|-----------|------------------|---------|
| Deep-Dive | Mọi kết quả gây shock | ✅ Rộng |
| Domino | Chuỗi nguyên nhân-hệ quả | ✅ Rộng |
| Zoom Lens | Sự kiện trong bối cảnh lớn | ✅ Rộng |
| **Trial** | **Chỉ sự kiện có tranh cãi thật sự** | ⚠️ **Hẹp** |
| Pendulum | Chiến thắng + cái giá | ✅ Rộng |

**Vấn đề**: Nhiều trận đánh lịch sử **không có tranh cãi thực sự** (ví dụ: trận Stalingrad rõ ràng ai thắng ai thua). Nếu AI bị chọn Trial → phải **bịa ra tranh cãi** → mất tự nhiên.

**Đề xuất**: Mở rộng `use_when` của Trial: *"Cho sự kiện có NHIỀU GÓC NHÌN khác nhau"* (không nhất thiết phải có tranh cãi).

---

## 4. XUNG ĐỘT GIỮA CORE RULES

| Rule A | Rule B | Xung đột |
|--------|--------|----------|
| `vocabulary`: "Personifies abstract concepts like geography, fear" | `analogy_strategy`: "NEVER use abstract philosophical metaphors" | ⚠️ AI khó phân biệt "personification" vs "abstract metaphor" |
| `anti_copy`: "translate abstract concepts into analogies" | `analogy_strategy`: chi tiết hơn, cùng nội dung | 🟡 Trùng lặp (không sai nhưng thừa) |

**Fix**: Thêm clarification vào `vocabulary`: *"Personification means giving human actions to non-human things ('the empire gasped', 'fear whispered'). This is NOT the same as abstract metaphors."*

---

## 5. THIẾU QUY TẮC QUAN TRỌNG

| Thiếu | Tại sao cần |
|-------|-------------|
| **Step names = internal only** | Không có rule nào nói rõ tên bước ("The Shocking Outcome", "The Cascade") là **hướng dẫn nội bộ**, không phải tiêu đề chapter trong output. AI có thể dùng làm heading. |
| **Analogy density** | `analogy_strategy` nói "what types" nhưng không nói "how many". Bao nhiêu ẩn dụ/chapter là phù hợp? Quá nhiều → mệt. Quá ít → nhạt. |
| **Blueprint integration** | Không có hướng dẫn cách sử dụng `key_characters`, `technical_details`, `geography_and_conditions` từ blueprint vào từng framework. |

---

## 6. `diversity_rules.framework_rule` CONFLICT

L760: `"When rewriting, ALWAYS choose a different framework than the original."`

Nhưng chúng ta vừa thêm checkbox "Exclude Original" cho phép user bỏ tích → AI có thể dùng lại framework gốc.

**Fix**: Đổi thành: *"By default, choose a different framework. This can be overridden by user preference."*

---

## 7. `checklist.never` CONFLICT

L779: `"Reuse the same framework as the original script."`

Cùng vấn đề với #6 — mâu thuẫn với checkbox mới.

---

## 8. STRUCTURAL CHECKS ✅

| Kiểm tra | Kết quả |
|----------|---------|
| Act percentages sum to 100% | ✅ Tất cả 5 framework |
| All `opening_closing_fit` references exist in shared sections | ✅ |
| `technique_emphasis` references match `techniques` names | ✅ |
| Each framework has unique emotional_arc | ✅ |
| Each framework has unique pacing pattern | ✅ |
| Cliffhanger types: 3 per framework, no duplicates | ✅ |
| Anti-patterns: 3-5 per framework, actionable | ✅ |

---

## 9. Zoom Lens `anti_patterns` — quá cứng

L387: `"Do NOT let microscope focus on a famous leader — choose someone unexpected"`

**Vấn đề**: Blueprint có thể chỉ chứa famous leaders (e.g. Don Juan, Ali Pasha). Nếu không có "unexpected person" trong data thì AI sẽ **bịa ra nhân vật**.

**Fix**: Đổi thành: *"PREFER focusing on a lesser-known figure if available in the content. If not, focus on a specific MOMENT of a famous leader, not their entire biography."*

---

## TÓM TẮT — Mức ưu tiên fix

| Priority | Issue | Effort |
|----------|-------|--------|
| 🔴 P0 | Terminology leak (steps, outline_rules, etc.) | Trung bình |
| 🔴 P0 | POV strategy sai loại (Trial, Pendulum) | Nhỏ |
| 🟡 P1 | diversity_rules + checklist conflict với checkbox | Nhỏ |
| 🟡 P1 | Thêm rule "step names = internal" | Nhỏ |
| 🟡 P1 | Zoom Lens anti_pattern quá cứng | Nhỏ |
| 🟢 P2 | Vocabulary vs analogy_strategy clarification | Nhỏ |
| 🟢 P2 | Trial use_when mở rộng | Nhỏ |
| 🟢 P2 | Thêm analogy density rule | Nhỏ |
| 🟢 P2 | anti_copy trùng analogy_strategy | Nhỏ |
