# Phân tích: `chapter_rhythm` hint trong niche Tiểu Sử Nhân Vật

## Tổng hợp — TẤT CẢ 5 frameworks đều có vấn đề

| # | Framework | Steps | `chapter_rhythm` | Ch cụ thể? |
|---|---|---|---|---|
| 1 | **Hai Mặt** | 7 steps | `"Ch1: provocative hook. Ch2-3: build admiration (warm). Ch4-5: reveal darkness (cold). Ch6-7: escalating duality. Final: reflective."` | ⚠️ **Ch1-Ch7 + Final** |
| 2 | **Bước Ngoặt** | 8 steps | `"Ch1: flash-forward hook. Ch2-3: measured backstory. Ch4-5: accelerating toward moment. Ch6: THE moment (peak). Ch7-8: aftermath + legacy."` | ⚠️ **Ch1-Ch8** |
| 3 | **Sử Thi** | 7 steps | `"Ch1: grand legacy hook. Ch2: intimate childhood. Ch3: formative (building). Ch4-5: rise + achievement (energy up). Ch6: peak + first cracks. Ch7: fall/decline (energy down). Ch8: legacy callback (grand)."` | ⚠️ **Ch1-Ch8** |
| 4 | **Bản Án** | 7 steps | `"Ch1: contribution hook. Ch2-3: person + discovery (warm). Ch4: first opposition (unease). Ch5-6: escalating persecution (anger). Ch7: destruction (enraging). Ch8: too-late recognition (heavy)."` | ⚠️ **Ch1-Ch8** |
| 5 | **Kẻ Xét Lại** | 7 steps | `"Ch1: villain hook (confident). Ch2: era context (measured). Ch3: who wrote history (suspicious). Ch4-5: counter-evidence (revelatory). Ch6: accumulated reversal (momentum). Ch7-8: real person + who benefited."` | ⚠️ **Ch1-Ch8** |

## 2 Nguồn hint cứng

### Hint 1: `steps` array (7-8 items)
AI nhận được array `steps` khi tạo outline. AI có xu hướng map **1 step = 1 chapter**.

### Hint 2: `chapter_rhythm` trong `pacing` (Ch1-Ch8 cụ thể)
Liệt kê cụ thể "Ch1 làm gì, Ch2-3 làm gì..." → AI đọc = **fix cứng 7-8 chapters**.

## Ảnh hưởng

1. User chỉnh `chapter_range` (ví dụ: 5-6) → AI CÓ THỂ vẫn tạo 7-8 chapters vì `chapter_rhythm` hint mạnh hơn
2. Tất cả 5 frameworks đều hint 7-8 chapters → **không có framework nào tạo script ngắn hơn**
3. `steps` và `chapter_rhythm` cùng hướng → double hint → rất khó override bằng `chapter_range` alone

## Vị trí trong file

| Framework | `chapter_rhythm` line | `steps` lines |
|---|---|---|
| Hai Mặt | Line 72 | Lines 86-127 |
| Bước Ngoặt | Line 210 | Lines 224-269 |
| Sử Thi | Line 347 | Lines 361-397 |
| Bản Án | Line 485 | Lines 499-543 |
| Kẻ Xét Lại | Line 623 | Lines 637-681 |

> [!IMPORTANT]
> **Câu hỏi**: Bạn muốn xử lý vấn đề này không?
> 
> **Nếu có**, có 2 hướng:
> - **Hướng A**: Xóa `chapter_rhythm` (bỏ hint cứng, giữ `steps` làm gợi ý)
> - **Hướng B**: Đổi `chapter_rhythm` thành mô tả **tỷ lệ %** thay vì Ch cụ thể  
>   VD: `"Opening 15% → Build 30% → Twist 20% → Climax 20% → Resolution 15%"`
> 
> **Nếu không** (chấp nhận 7-8 chapters): giữ nguyên, đây là hành vi known.
