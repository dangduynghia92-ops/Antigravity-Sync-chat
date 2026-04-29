# Đánh giá Step 1: Sequence Chunking — Chapter 1 Baldwin IV

## Tổng quan
- **Tổng sequences:** 29 (SEQ_01 → SEQ_29)
- **Tổng sentences đầu vào:** 244 (từ 10+ chapters merged)
- **Sentence #1 (title "Level one, the numb arm")** → đã bị SKIP ✅
- **Sentence #47 (title "Level two, the final verdict")** → đã bị SKIP ✅
- **Sentence #73 (title "Level three, the boy king")** → đã bị SKIP ✅

## ✅ Điểm mạnh

### 1. Skip Rule hoạt động tốt
Các câu tiêu đề chapter như "Level one, the numb arm", "Level two...", "Level three..." đều bị loại đúng. Không sentence nào bị assign vào sequence.

### 2. Location/Time shift nhìn chung hợp lý
| SEQ | Location | Đánh giá |
|-----|----------|----------|
| 01 | Palace courtyard | ✅ Wrestling match ngoài sân |
| 02 | Inside the palace | ✅ Tutor gọi vào → đổi location |
| 03 | Jerusalem stone palace | ✅ Giới thiệu tổng quan |
| 07 | Dark examination room | ✅ Bác sĩ khám bệnh |
| 08 | Leper colonies outside walls | ✅ Mô tả bệnh phong |
| 10 | Great Hall | ✅ Coronation |
| 13 | Palace war room | ✅ Báo tin Saladin |
| 14 | Road to Montgisard | ✅ Hành quân |
| 15 | Battlefield of Montgisard | ✅ Trận chiến |
| 16 | Jerusalem streets | ✅ Khải hoàn |
| 23 | Sea of Galilee fortress | ✅ Siege |
| 26 | Dark bedchamber | ✅ Mù lòa |

### 3. Duration tuân thủ tốt (≤25s rule)
| SEQ | Duration | Status |
|-----|----------|--------|
| 01 | 21.95s | ✅ |
| 02 | 13.07s | ✅ |
| 03 | 13.56s | ✅ |
| 04 | 22.76s | ✅ |
| 05 | 18.71s | ✅ |
| 06 | 22.62s | ✅ |
| 07 | 21.34s | ✅ |
| 08 | 20.30s | ✅ |
| 09 | 5.95s | ✅ (ngắn, nhưng rule cho phép no minimum) |
| 15 | **24.51s** | ⚠️ Gần sát 25s nhưng OK |
| 27 | **24.84s** | ⚠️ Gần sát 25s nhưng OK |

Tất cả 29 sequences đều ≤25s → **PASS 100%**

## ⚠️ Vấn đề phát hiện

### 1. BUG NGHIÊM TRỌNG: Timing nhảy bất thường (Cross-Chapter)

> [!CAUTION]
> SEQ_03 end_time = **609.0s** nhưng SEQ_04 start_time = **609.115s**
> Sentence #27 end_time = 51.0s nhưng Sentence #28 start_time = **607.846s**
> 
> → Khoảng cách **~557s** giữa 2 câu liền kề trong cùng 1 sequence!

Nguyên nhân: **Step 0 merge** đang offset timing theo chapter, nhưng LLM ở Step 1 vẫn gom sentence #27 (Chapter 1) và #28 (Chapter 10) vào cùng SEQ_03. LLM không biết chúng thuộc chapter khác nhau.

**Các điểm nhảy timing tương tự:**
| Transition | Gap | Giải thích |
|---|---|---|
| SEQ_03 → SEQ_04 | 51s → 609s | Chapter 1 → Chapter 10 |
| SEQ_06 → SEQ_07 | 1277s → 1333s | Chapter 11 → Chapter 2 |
| SEQ_09 → SEQ_10 | 1382s → 1492s | Chapter 2 → Chapter 3 |
| SEQ_12 → SEQ_13 | 1549s → 1720s | Chapter 3 → Chapter 5 |
| SEQ_16 → SEQ_17 | 1797s → 2051s | Chapter 5 → Chapter 6 |
| SEQ_19 → SEQ_20 | 2120s → 2445s | Chapter 6 → Chapter 7 |
| SEQ_22 → SEQ_23 | 2504s → 2892s | Chapter 7 → Chapter 8 |
| SEQ_25 → SEQ_26 | 2957s → 3413s | Chapter 8 → Chapter 9 |
| SEQ_27 → SEQ_28 | 3462s → 3973s | Chapter 9 → Chapter 10 |

### 2. SEQ_03 trộn câu từ Chapter 1 và Chapter 10

SEQ_03 chứa sentence_ids [22-28]:
- Sentences 22-27: Chapter 1 (end_time ~51s)
- **Sentence 28**: Chapter 10 "The price." (start_time 607s)

LLM gom "The price." vào SEQ_03 vì nó là câu kết thúc ngữ nghĩa ("Something that will eat you alive. **The price.**"). Đúng về mặt narrative, **sai về mặt timing** vì câu này thuộc chapter hoàn toàn khác.

### 3. Một số location bị trùng lặp không cần thiết

| SEQ_19 | Throne room |
| SEQ_20 | Throne room |
| SEQ_21 | Throne room |
| SEQ_22 | Throne room |

4 sequence liên tiếp cùng 1 location. SEQ_20-22 có thể gộp thành 2 sequences nếu xét thuần về location rule, nhưng subject shift (Masked King → Stripping power → Appointing regent) hợp lý nên CÓ THỂ chấp nhận.

## 📊 Sentence Coverage

Sentences đã SKIP đúng: 1, 47, 73 (chapter titles) ✅

Sentences đã gán: 2-46, 48-72, 74-244 → tổng **241/244 sentences** được gán.

Không có sentence nào bị bỏ sót ngoài titles → **Coverage: 100%** ✅

## 🔧 Khuyến nghị sửa

### Fix #1: Thêm chapter boundary marker vào Step 1 input
Hiện tại Step 1 chỉ nhận `sentence_id + text + duration`. LLM không biết chapter boundary.

**Giải pháp:** Thêm `chapter_id` vào mỗi sentence khi gửi Step 1 + thêm rule: "NEVER merge sentences from different chapters into the same sequence."

### Fix #2: Validate timing gap
Sau khi LLM trả sequences, validate: nếu max_gap giữa 2 sentences liên tiếp trong 1 sequence > 10s → tách ra.

## Verdict

| Tiêu chí | Kết quả |
|---|---|
| Skip Rule | ✅ 100% |
| Duration ≤25s | ✅ 100% |
| Location logic | ✅ 90% (tốt) |
| Subject shift | ✅ 85% (hợp lý) |
| Coverage | ✅ 100% |
| **Cross-chapter merge** | **❌ BUG** |
| Timing continuity | ⚠️ Nhảy bất thường |

> [!IMPORTANT]
> **Ưu tiên #1:** Fix cross-chapter merge bug — thêm `chapter_id` vào Step 1 input và rule "never merge across chapters".
