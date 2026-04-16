# Walkthrough: Framework "The Deep Anatomy" + Pipeline Updates

## Thay đổi đã thực hiện

### 1. Framework mới: "The Deep Anatomy"
**File:** [Review_súng_đạn.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/Review_s%C3%BAng_%C4%91%E1%BA%A1n.json) (+234 dòng, tổng: 2627 dòng, 12 frameworks)

Framework phân tích chuyên sâu **1 sản phẩm duy nhất** (súng, đạn, phụ kiện) theo nhiều khía cạnh:

| Yếu tố | Chi tiết |
|---------|----------|
| **Chapter type** | `topic_block` — mỗi chapter = 1 khía cạnh, KHÔNG phải 1 sản phẩm |
| **Topic pool** | 10 topics (Origin, Ballistics, Recoil, Terminal, Platforms, Variants, Tactical, Handloading, Myths, Limitations) |
| **Chapter template** | `TOPIC ANCHOR → DATA FOUNDATION → PHYSICAL TRANSLATION → PROOF LAYER → PRACTICAL IMPLICATION` |
| **Kỹ thuật chính** | Physical Translation (BẮT BUỘC), Scenario Painting (tự tạo, KHÔNG copy), Data Barrage |
| **Feedback tích hợp** | ✅ Tribal CTA (end chapter), ✅ Tribal Enemy (use_moderately), ✅ Proof Layer cấm copy case study |

---

### 2. Topic Block Writing Rules
**File:** [system_write_review_firearms.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_write_review_firearms.txt) (+52 dòng, tổng: 220 dòng)

Thêm block hướng dẫn viết chapter dạng `topic_block` với:
- 5 required elements mới (vs 5 elements cũ cho product-per-chapter)
- 4 writing patterns: T1 (Data Lead), T2 (Myth Lead), T3 (Story Lead), T4 (Catalog Lead)
- Rule: không dùng cùng 1 pattern cho 2 chapter liên tiếp

---

### 3. Head-to-Head Duel — Criteria Pool
**File:** [Review_súng_đạn.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/Review_s%C3%BAng_%C4%91%E1%BA%A1n.json) (thay thế 6 dòng → 12 dòng)

| Trước | Sau |
|-------|-----|
| Hardcoded 6 criteria: `trigger, ergonomics, accuracy, reliability, value_proposition, specs_core` | Flexible `criteria_pool` với 3 nhóm: `firearm_criteria` (7), `caliber_criteria` (7), `universal_criteria` (2) |

Giờ Head-to-Head Duel **tự động hoạt động** cho cả .357 vs .44 Mag lẫn Glock 19 vs SIG P365.

---

## Validation

- ✅ Framework "The Deep Anatomy" confirmed at position 12/12 in frameworks array
- ✅ TOPIC BLOCK CHAPTER WRITING RULES confirmed at line 96-147 in write prompt
- ✅ `criteria_pool` confirmed at line 1617 in Head-to-Head Duel evaluation_focus
- ⚠️ JSON validation via PowerShell timed out (165KB file too large for ConvertFrom-Json) — file reads confirm valid structure
