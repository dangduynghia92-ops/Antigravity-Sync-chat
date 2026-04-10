# Phân Tích Tính Năng Resume — Auto Pipeline

## Kết Luận Tổng Quát

Auto Pipeline **CÓ tính năng Resume**, nhưng nó hoạt động **KHÔNG GIỐNG NHAU** giữa 2 mode (Top/List Review vs Narrative), và còn tồn tại một số **lỗ hổng nghiêm trọng** khiến resume tuy có nhưng lại không phải lúc nào cũng resume được đúng bước bị fail.

---

## 1. Cơ Chế Resume Hiện Tại

### Nút Resume trên Auto Pipeline Tab
- Nút `🔄 Resume` **ẩn mặc định**, chỉ hiện khi có item bị lỗi (error) trong queue.
- Khi nhấn Resume:
  1. Reset tất cả item `error` → `pending`
  2. Set `_resume_mode = True`
  3. Chạy lại queue loop bình thường

### Dữ liệu được cache giữa các lần resume

File: [auto_pipeline_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py#L1414-L1478) — `_preload_resume_cache()`

| Dữ liệu | Cache được? | Ghi chú |
|---|---|---|
| Transcript | ✅ | Phase 1 tự skip nếu đã download |
| Video download | ✅ | Tự skip nếu file `.mp4` đã tồn tại |
| Thumbnail | ✅ | Tự skip nếu file `_thumb.jpg` đã tồn tại |
| Chapter split | ✅ | Phase 2 tự skip nếu ≥2 chapter files đã tồn tại |
| Blueprint (`_blueprint_raw.json`) | ✅ | Pre-load từ `_pipeline/` folder |
| Full text (from chapters) | ✅ | Được reconstruct từ chapter dicts |

---

## 2. Phân Tích Theo Mode

### Mode: Top/List Review (Rewrite pipeline)

**Pipeline flow:** Step 1→12 trong `_do_renew_review()`

| Step | Mô tả | Resume skip? | Chi tiết |
|---|---|---|---|
| **Phase 1-2** | Download + Split | ✅ | Auto skip nếu file đã tồn tại |
| **Step 1** | Concatenate text | ✅ | Dùng `_cached_full_text` |
| **Step 2** | Detect framework | ✅ | Dùng `_cached_blueprint` (skip Steps 2-3) |
| **Step 3** | Extract blueprint | ✅ | Dùng `_cached_blueprint` |
| **Step 4** | Rank frameworks | ❌ **KHÔNG** | Luôn gọi API lại |
| **Step 5** | Reality check | ❌ **KHÔNG** | Luôn gọi API lại |
| **Step 5a-d** | Google Search / Enrich | ❌ **KHÔNG** | Luôn gọi API lại |
| **Step 6** | Check completeness | ❌ **KHÔNG** | Luôn gọi API lại |
| **Step 7** | Convert units | ✅ | Pure Python, tức thì |
| **Step 8** | Create outline | ⚠️ **CÓ ĐIỀU KIỆN** | Chỉ skip nếu `_review_outline_audited.json` tồn tại |
| **Step 9** | Audit outline | ⚠️ **CÓ ĐIỀU KIỆN** | Chỉ skip nếu `_review_outline_audited.json` tồn tại |
| **Step 10** | Write chapters | ❌ **KHÔNG** | Luôn viết lại từ đầu |
| **Step 11** | Cross-chapter review | ❌ **KHÔNG** | Luôn gọi API lại |
| **Step 12** | Merge | ❌ **KHÔNG** | Luôn chạy lại |

> [!WARNING]
> **Lỗ hổng lớn nhất của Review mode:** Nếu pipeline fail ở Step 9 (Audit — chính là trường hợp đã gặp trong log trước), resume sẽ **VẪN PHẢI CHẠY LẠI Step 4, 5, 5a-d, 6** vì không có cache. Điều này lãng phí 5-10 phút gọi API.

> [!WARNING]
> **Step 10 (Write chapters) KHÔNG có resume:** Nếu đang viết Chapter 8/11 thì fail, resume sẽ phải viết lại từ Chapter 1. Mỗi chapter tốn ~2-3 phút API call → mất ~25 phút thừa.

### Mode: Narrative (Script Creation pipeline)

**Pipeline flow:** `_run_shared_fw_pipeline()` với `resume=True`

| Step | Mô tả | Resume skip? | Chi tiết |
|---|---|---|---|
| **Step A** | Phase Plan | ✅ | Check `_phase_plan_final.json`, `_validated.json`, `_phase_plan.json` — resume từ checkpoint gần nhất |
| **Step B** | Outline | ✅ | Check `_renew_outline_audited.json` hoặc `_renew_outline.json` |
| **Step C** | Audit | ✅ | Skip nếu audited outline đã tồn tại |
| **Write chapters** | Viết từng chapter | ✅ ✅ ✅ | **RESUME TỪNG CHAPTER:** check file `ch_XX_*.txt` đã tồn tại → load từ disk, bỏ qua |
| **Review + Patch** | Cross-chapter review | ❌ | Luôn chạy lại |

> [!TIP]
> Narrative mode **vượt trội hơn hẳn** Review mode về resume: nó skip được phase plan, outline, audit, VÀ từng chapter đã viết xong. Nếu fail giữa chừng khi đang viết chapter 8/15, resume sẽ chỉ viết lại từ chapter 9.

---

## 3. So Sánh Resume: Review vs Narrative

| Tiêu chí | Top/List Review | Narrative |
|---|---|---|
| Resume Steps 1-3 (blueprint) | ✅ | ✅ |
| Resume Steps 4-6 (rank/reality/check) | ❌ | N/A (khác flow) |
| Resume Outline + Audit | ⚠️ Có điều kiện | ✅ |
| **Resume từng chapter đã viết** | ❌ **KHÔNG** | ✅ **CÓ** |
| File `_resume.json` metadata | ❌ Không tạo | ✅ Có tạo |
| Nút Resume trên Script Creation | N/A | ✅ Có nút riêng |

---

## 4. Kết Luận & Vấn Đề Cần Sửa

### Đánh giá hiện trạng
- **Narrative mode:** Resume hoạt động tốt, thiết kế checkpoint-based, tiết kiệm thời gian.
- **Review mode (Auto Pipeline):** Resume **rất yếu** — chỉ skip được Steps 1-3. Phần tốn API nhất (Steps 4-6, 8-12) sẽ bị chạy lại hoàn toàn.

### Vấn đề cụ thể với log lỗi trước
Lần chạy trước fail ở Step 9 (Audit Outline timeout). Khi resume:
- Steps 1-3: ⏭ Skip (có cache) — tiết kiệm ~8 phút
- Steps 4-6: 🔄 Chạy lại — tốn ~5 phút
- Step 8: 🔄 Chạy lại outline — tốn ~3 phút
- Step 9: 🔄 **Chạy lại audit** — đây là bước đã fail, hy vọng lần này không timeout
- **Tổng: mất ~8 phút thừa do Steps 4-6 không được cache**

### Đề xuất cải thiện
1. **Cache Steps 4-6 cho Review mode:** Lưu `_rankings.json`, `_reality_check.json`, `_completeness_check.json` và kiểm tra khi resume.
2. **Resume từng chapter cho Review mode:** Áp dụng cùng logic Narrative mode — check file `ch_XX_*.txt` tồn tại thì skip.
3. **Tạo `_resume.json` cho Review mode** giống như Narrative mode đã làm.
