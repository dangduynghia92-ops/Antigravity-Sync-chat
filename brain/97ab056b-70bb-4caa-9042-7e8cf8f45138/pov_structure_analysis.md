# POV Structure Analysis: Baldwin IV vs Reference

## Data

| Metric | Baldwin IV (output) | Genghis Khan (reference) |
|--------|:---:|:---:|
| Life span | 15 years (9→24) | 65 years (0→65) |
| Chapters | **19** | **13** |
| Avg years/chapter | 0.8 | 5.4 |
| Same-age clusters | Age 16: 4 ch, Age 22: 4 ch, Age 23: 4 ch | Age 15-16: 2 ch (max) |
| Main without "Age N." prefix | **9/19** (47%) | 0/13 (0%) |

## 4 Vấn đề gốc

### 1. `validate_sub_key` promote quá hung hăng
Phase plan ban đầu cho ra ~10 main. Nhưng bước validate_sub_key **promote thêm 9 items** từ sub → main (items không có "Age N." prefix). Đây là nguồn chính tạo ra 19 chapters.

**Reference pattern:** Genghis Khan KHÔNG có bước promote. Mỗi Level được chọn 1 lần, dứt khoát.

> [!IMPORTANT]
> **Đề xuất:** Với POV niche, **tắt validate_sub_key** hoặc chỉ cho phép promote nếu item đã có "Age N." prefix. Items không có age = KHÔNG BAO GIỜ là Level.

---

### 2. Thiếu bước gộp "cùng tuổi"
Sau khi promote, có 4 chapters ở age 16, 4 chapters ở age 22, 4 chapters ở age 23. Reference chỉ cho phép tối đa 2 chapters cùng tuổi (ages 15-16 liền kề).

**Reference pattern:** Mỗi tuổi = tối đa 1 chapter. Nếu 2 events cùng tuổi → gộp vào 1 chapter hoặc demote 1 xuống sub.

> [!IMPORTANT]
> **Đề xuất:** Sau split, thêm bước **merge cùng tuổi** — nếu >1 chapter cùng age_anchor → gộp main thành 1 chapter, chuyển events phụ thành sub_key_data.

---

### 3. Phase plan cho quá nhiều main ngay từ đầu
Level Gate yêu cầu "permanent change" nhưng AI vẫn cho ra:
- "Claw hand deformity begins" → đúng là permanent, nhưng CÙNG TUỔI với Montgisard (age 16)
- "Total loss of mobility" → permanent, nhưng CÙNG TUỔI với Kerak (age 22)
- "Saladin's army routed" → đây là KẾT QUẢ của Montgisard, không phải moment riêng

**Reference pattern:** Genghis Khan gộp "bị bắt + bị nhốt" thành 1 Level (The Cage), "thoát + đánh lính" thành 1 Level (The Escape). Mỗi Level = 1 SCENE duy nhất, không phải 1 sự kiện đơn lẻ.

> [!IMPORTANT]  
> **Đề xuất:** Sửa lại khái niệm main_key_data: mỗi item là 1 **SCENE** (có thể gồm nhiều sự kiện liên tiếp cùng tuổi), không phải 1 sự kiện đơn lẻ.
> Enforce: "Nếu 2 events xảy ra cùng ngày/cùng tuần → chúng là 1 scene, 1 main_key_data."

---

### 4. Thiếu logic liên kết giữa lifespan và chapter count
Baldwin IV sống 15 năm → 19 chapters = phi logic.
Genghis Khan sống 65 năm → 13 chapters = hợp lý.

**Reference pattern:** Số chapters phụ thuộc vào **số TURNING POINTS thực sự**, không phải số sự kiện.

> [!IMPORTANT]
> **Đề xuất:** Thêm ngưỡng cứng trong phase plan: `max chapters = min(lifespan_years, user_max_chapters)`. Ví dụ Baldwin IV sống 15 năm → tối đa 10-12 chapters (gần 1 chapter/1-2 năm).

---

## Phương án hành động (đề xuất)

| # | Fix | Vị trí | Mô tả |
|---|-----|--------|-------|
| A | Tắt/siết validate_sub_key cho POV | `script_creation_tab.py` | POV: skip validate hoặc chỉ promote items có "Age N." prefix |
| B | Siết phase plan prompt | `system_narrative_phase_plan_pov.txt` | "Events cùng tuổi = 1 main_key_data (1 SCENE)" |
| C | Cap total main | `system_narrative_phase_plan_pov.txt` | Enforce: total main ≤ user_max_chapters |
| D | Merge cùng tuổi sau split | `apply_chapter_splits()` | Nếu >1 chapter cùng age → merge |

**Thứ tự ưu tiên:** B → A → C → D (B giải quyết gốc, A chặn promote lạm, C cap cứng, D safety net)
