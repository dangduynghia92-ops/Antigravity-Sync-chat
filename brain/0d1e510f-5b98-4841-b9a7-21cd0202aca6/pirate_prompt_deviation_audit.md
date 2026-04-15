# Audit: Pirate Prompt Deviations from Biography Template

So sánh kiến trúc (rules, constraints) giữa pirate prompts và biography prompts (bản mẫu ổn định).
Chỉ liệt kê các **quy tắc tôi tự thêm/bịa** mà biography KHÔNG có.

---

## 1. `system_narrative_phase_plan_pirate.txt` vs `_biography.txt`

| Rule | Biography | Pirate | Đánh giá |
|------|-----------|--------|----------|
| Main-key definition | "turning_points and conflicts" = 1 node | ~~"each modification is a separate milestone"~~ | ✅ **ĐÃ FIX** → Event Cluster |
| Anti-Merge example | main:["Bị bắt"], sub:["12 năm tù","Phát tán"] | ~~main:["captured"], main:["renamed"], main:["armed"]~~ | ✅ **ĐÃ FIX** → Cluster Rule |
| End phase main_key | `main_key_data = []` | ~~`main_key_data = []`~~ | ✅ **ĐÃ FIX** → có main (discovery + legacy) |
| File size | 4,089 bytes (compact) | **11,288 bytes** (gần 3x!) | ⚠️ Pirate prompt quá dài, có thể chứa quy tắc thừa |

> [!IMPORTANT]
> Phase plan pirate đã fix 3 vấn đề chính. Nhưng **kích thước 3x biography** gợi ý vẫn có quy tắc dư thừa.

---

## 2. `system_narrative_audit_pirate.txt` vs `_biography.txt`

| Rule | Biography | Pirate | Đánh giá |
|------|-----------|--------|----------|
| Chapter count | "LOCKED. DO NOT ADD, MERGE, or REMOVE" | ~~"You may REDUCE"~~ | ✅ **ĐÃ FIX** → LOCKED |
| remove_chapter action | Không tồn tại | ~~`remove_chapter`~~ | ✅ **ĐÃ FIX** → DISABLED |
| event_cramming check | Không có (bio không cần) | **CÓ** — rule #4 | ⚠️ Rule bịa thêm. Bio không có vì phase plan đã phân bổ đúng |
| Pirate-specific rules | N/A | Money Angle, Anti-Hero, Medicine, Dark Underbelly, Myth Check, Anatomy | ✅ OK — niche-specific, không phải deviation |

> [!WARNING]
> Rule `event_cramming` (#4) trong audit pirate cho phép AI đánh giá "quá nhiều events trong 1 chapter" → dẫn đến gộp. Biography KHÔNG có rule tương đương vì tin tưởng phase_plan phân bổ đúng.

---

## 3. `system_validate_sub_key_pirate.txt` vs `_biography.txt`

| Rule | Biography | Pirate | Đánh giá |
|------|-----------|--------|----------|
| Promote budget | Không có (ít sub nên không cần) | ~~Không có~~ | ✅ **ĐÃ FIX** → max 2/phase |
| UNLESS exceptions | **Không có** | 7 UNLESS gates (specs, daily life, trade, governance, weapons, disease, movement) | ⚠️ **PIRATE TỰ THÊM**. Bio validator không có UNLESS gate nào — chỉ dùng 3-test thuần túy |
| Calibration examples | 6 examples | 6 examples | ✅ OK — niche-specific |

> [!CAUTION]
> **7 UNLESS gates trong pirate validator là quy tắc tự bịa**. Biography validator chỉ dùng 3-test system (Scene/Turning/Causal) thuần túy, KHÔNG có cửa hậu UNLESS. Mỗi UNLESS gate = 1 lỗ hổng cho AI promote mass sub→main.

---

## 4. `system_narrative_review_pirate.txt` vs `_biography.txt`

| Rule | Biography | Pirate | Đánh giá |
|------|-----------|--------|----------|
| Compliance object | Không có | `pirate_compliance` (5 checks) | ⚠️ Tự thêm. Bio trả issues[] thuần, không có compliance block. Không gây hại nhưng thêm phức tạp. |
| Review checks count | 15 checks | 15 checks | ✅ Same count |
| Pirate-specific checks | N/A | Money Angle, Anti-Hero, Pirate Medicine, Mechanical Repetition | ✅ OK — content-specific |

---

## 5. `system_narrative_write_pirate.txt` vs `_biography.txt`

Cả 2 file đều ~34KB. Cần check:

| Rule | Biography | Pirate | Đánh giá |
|------|-----------|--------|----------|
| Chapter structures | 5 structures content-driven | 5 structures content-driven | ✅ Aligned (vừa fix xong) |
| Needs deep comparison | — | — | ⚠️ Chưa kiểm tra chi tiết vì file 34KB |

---

## 6. `system_narrative_outline_pirate.txt` vs `_biography.txt`

Cả 2 file đều ~17KB. Cần check structure selection logic.

---

## TÓM TẮT: CÁC QUY TẮC TỰ BỊA

| # | Quy tắc | File | Trạng thái |
|---|---------|------|-----------|
| 1 | "each modification = separate milestone" | phase_plan | ✅ ĐÃ FIX |
| 2 | Anti-Merge xé lẻ thay vì cluster | phase_plan | ✅ ĐÃ FIX |
| 3 | Bóng Ma main = [] | phase_plan | ✅ ĐÃ FIX |
| 4 | Audit cho phép REDUCE chapters | audit | ✅ ĐÃ FIX |
| 5 | Audit có `remove_chapter` action | audit | ✅ ĐÃ FIX |
| 6 | **7 UNLESS gates trong validator** | validate_sub_key | ❌ **CHƯA FIX** — là lỗ hổng chính gây promote hàng loạt |
| 7 | **`event_cramming` rule trong audit** | audit | ❌ **CHƯA FIX** — dẫn đến gộp chapter |
| 8 | `pirate_compliance` block trong review | review | ⚠️ Không gây hại, nhưng thêm phức tạp |
