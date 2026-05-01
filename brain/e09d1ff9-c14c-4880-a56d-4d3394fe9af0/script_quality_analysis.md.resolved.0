# King Baldwin IV — Script Quality Analysis

## Phân tích toàn diện: Outline → Phase Plan → Nội dung

---

## 🔴 Vấn đề 1: Chapter mở đầu THIẾU bối cảnh thời gian/không gian

### Hiện trạng
Outline có `age_anchor` (ví dụ "You are 15") nhưng **nhiều chapter KHÔNG dùng nó** trong câu mở đầu. Người đọc không biết đang ở giai đoạn nào.

### Ví dụ cụ thể

| Chapter | age_anchor | Câu mở đầu thực tế | Vấn đề |
|---|---|---|---|
| Ch 3 | "You are 15" | "Your right hand curls inward..." | ❌ Không nhắc tuổi, không biết đã bao lâu kể từ ch2 |
| Ch 4 | "You are 16" | "The numbness climbs past your right elbow..." | ❌ Không nhắc tuổi |
| Ch 5 | "You are 16" | "You stand before a polished silver mirror..." | ❌ Không nhắc tuổi, cùng tuổi ch4 nhưng không phân biệt |
| Ch 7 | "You are 18" | (cần kiểm tra) | ❌ Nhảy 2 năm không giải thích |
| Ch 10 | "You are 19" | "You sit in the high council chamber..." | ❌ Không nhắc tuổi |

### Chapter mở đầu TỐT (so sánh)

| Chapter | Câu mở đầu | Tại sao tốt |
|---|---|---|
| Ch 1 | "You sit in the sunlit courtyard of Jerusalem" | ✅ Có location, có bối cảnh |
| Ch 2 | "Your father is dead" | ✅ Có event trigger rõ |
| Ch 6 | "Saladin marches on Jerusalem with 26,000 soldiers" | ✅ Có bối cảnh quân sự |

### Nguyên nhân gốc
Outline có `opening_style` (standard/callback/atmosphere/thesis/cold_open) nhưng **KHÔNG có rule bắt buộc** phải chèn:
- **Tuổi hiện tại** (đặc biệt khi nhảy tuổi)
- **Năm** (1176, 1177...)
- **Khoảng cách thời gian** so với chapter trước ("Two years pass...")

---

## 🔴 Vấn đề 2: Chapter kết thúc CỤT LỦN

### Hiện trạng
Outline có `closing_type` (cold_fact/weight/forward_pull/paradox/echo) nhưng nhiều chapter kết **bằng 1 câu đơn** mà không:
- Chốt ý nghĩa sự kiện
- Tạo link sang chapter sau
- Để lại dư vị

### Ví dụ cụ thể

| Chapter | closing_type | Câu kết thực tế | Vấn đề |
|---|---|---|---|
| Ch 1 | cold_fact | "You cannot feel the right side of your body." | ⚠️ OK nhưng hơi ngắn |
| Ch 3 | forward_pull | "You have already decided where to march them next." | ⚠️ Vague — march ĐI ĐÂU? |
| Ch 4 | paradox | "Half of your body is already dead, yet your grip on the living has never been tighter." | ✅ TỐT |
| Ch 8 | cold_fact | "You are a king who must be carried." | ✅ TỐT — ngắn nhưng đủ nặng |
| Ch 9 | forward_pull | "You know what the ring means... but you have no idea what the man behind it will cost." | ❓ Cần kiểm tra |

### Chapter kết TỐT

| Chapter | Câu kết | Tại sao tốt |
|---|---|---|
| Ch 6 | "The blood dripping from your steel belongs to the enemy. The blood soaking your tied reins is your own." | ✅ Paradox + imagery tuyệt vời |
| Ch 10 | "You have bought twenty-four months for the realm, but you cannot negotiate with the rot in your own blood." | ✅ Weight + forward pull |
| Ch 14 | "...bowing to a dying ghost and a frightened child, bound by a whispered command you will never live to see them break." | ✅ Hoàn hảo |

### Nguyên nhân gốc
Writing prompt có `closing_type` nhưng **không có hướng dẫn cụ thể** về:
- Độ dài tối thiểu cho closing (2+ câu)
- Phải liên kết với chapter tiếp theo
- Phải chốt emotional_beat của chapter

---

## 🟡 Vấn đề 3: Outline gán sub_key_data yếu thành chapter riêng

### Hiện trạng
Phase "Thử Lửa" có 4 main_key_data nhưng 2 cái thực ra **quá yếu** cho standalone chapter:

```
✅ STRONG: "At Montgisard, you charge 500 knights..."  → Ch 6 (1385 bytes - dày)
✅ STRONG: "You strip Raymond of his regency..."       → Ch 3 (1089 bytes - OK)
⚠️ WEAK:  "Skin lesions begin to appear"               → Ch 5 (1237 bytes - phải kéo dãn)
⚠️ WEAK:  "Refuses to cede power to Philip of Flanders" → Ch 4 (1154 bytes - phải bịa thêm)
```

"Skin lesions begin to appear" không phải event — nó là **state change**. Nó nên là sub_key_data ghép vào chapter khác.

### Hệ quả
- Ch 4 và Ch 5 phải **bịa thêm chi tiết** để đủ content
- Pacing bị chậm — 4 chapter liên tiếp cùng tuổi 15-16

---

## 📊 Tổng quan chất lượng theo chapter

| Ch | Tuổi | Mở đầu | Kết thúc | Nội dung | Tổng |
|---|---|---|---|---|---|
| 1 | 9 | ✅ | ⚠️ | ✅ | 🟢 |
| 2 | 13 | ✅ | ⚠️ | ✅ | 🟢 |
| 3 | 15 | ❌ thiếu tuổi | ⚠️ vague | ✅ | 🟡 |
| 4 | 16 | ❌ thiếu tuổi | ✅ | ⚠️ kéo dãn | 🟡 |
| 5 | 16 | ❌ thiếu tuổi | ✅ | ⚠️ kéo dãn | 🟡 |
| 6 | 16 | ✅ | ✅ | ✅✅ | 🟢🟢 |
| 7 | 18 | ❌ thiếu tuổi | ? | ⚠️ | 🟡 |
| 8 | 18 | ⚠️ | ✅ | ✅ | 🟢 |
| 9 | 19 | ❌ thiếu tuổi | ? | ✅ | 🟡 |
| 10 | 19 | ❌ thiếu tuổi | ✅✅ | ✅ | 🟢 |
| 11 | 22 | ❌ thiếu tuổi | ? | ✅ | 🟡 |
| 12 | 22 | ? | ? | ✅ | ? |
| 13 | 22 | ? | ? | ✅ | ? |
| 14 | 23 | ✅ | ✅✅ | ✅✅ | 🟢🟢 |
| 15 | 23 | ✅ | ✅✅ | ✅ | 🟢 |

---

## 🛠 Đề xuất sửa

### Fix 1: Bắt buộc context mở đầu
Thêm vào writing prompt rule:
```
OPENING RULE: Khi age_anchor thay đổi so với chapter trước, 
câu đầu tiên PHẢI chứa thời gian ("Two years later", "You are now 18")
hoặc event trigger ("The treaty expires", "The riders return with news").
```

### Fix 2: Nâng chuẩn kết chapter
Thêm vào writing prompt rule:
```
CLOSING RULE: Đoạn kết PHẢI có ≥2 câu. 
Câu cuối PHẢI chốt emotional_beat hoặc tạo tension cho chapter tiếp.
KHÔNG được kết bằng 1 câu mô tả đơn giản.
```

### Fix 3: Lọc main_key_data chặt hơn ở outline stage
State changes ("skin lesions appear", "truce with Saladin") nên là **sub_key_data** ghép vào chapter có event mạnh hơn, KHÔNG tạo chapter riêng.

> [!IMPORTANT]
> Fix 1 và Fix 2 cần sửa trong **writing system prompt** (rewriter.py).
> Fix 3 cần sửa trong **outline prompt** (phase_plan hoặc outline audit).
> 
> Bạn muốn tôi triển khai fix nào?
