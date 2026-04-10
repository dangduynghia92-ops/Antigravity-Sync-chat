# Đánh giá toàn diện & Đề xuất cải tiến

## 🐛 Lỗi cần sửa

### 1. Chapter 9 & 10 cùng timecode → content sai
Trong log user gửi, Ch9 chỉ có **231 chars** và Ch10 có **40,134 chars** — cả hai cùng timecode `(86:58)`. Đây là do `_find_timecode_in_text` tìm thấy cùng vị trí cho 2 timestamps khác nhau (86:58 và 96:05 cùng ±10s).

**Sửa**: Khi 2 chapters cùng tìm ra 1 vị trí → log cảnh báo rõ ràng, và gộp/bỏ qua chapter trùng.

### 2. Retry thiếu `chapter_count`
Khi verify phát hiện lỗi → retry `split_chapters` nhưng **không truyền `chapter_count`** → retry có thể cho ra số chapters khác với yêu cầu.

```python
# Hiện tại (thiếu chapter_count):
retry_chapters = split_chapters(
    srt_text_lines=text_lines,
    script_type=script_type,
    api_client=api_client,
    chapter_guide=chapter_guide,
    verification_feedback=feedback,
    log_callback=log_cb,
)
```

### 3. `_summarize_results` — duplicate filter check
Sau khi sort chapter files numerically, inner loop vẫn có `if f.startswith("Chapter ")` check thừa (đã filter ở outer loop).

---

## ⚠️ Vấn đề tiềm ẩn

### 4. Timeout cho scripts lớn
`api_client.call_api` dùng `timeout=300` (5 phút). Scripts 130K+ chars + verify + retry = có thể vượt timeout, đặc biệt với Pro model.

### 5. Không retry khi API trả rỗng
Nếu AI trả response nhưng `chapters_data` rỗng (parse thất bại), code return `[]` mà không thử lại.

### 6. Memory với scripts cực dài
`verify_chapters` gửi **toàn bộ original text + tất cả chapters** trong 1 message. Scripts 130K+ chars → message ~260K+ chars → có thể vượt context window.

---

## 💡 Đề xuất cải tiến

### A. Progress bar cho từng bước (Ưu tiên: ⭐⭐)
Hiện tại progress chỉ theo file. Thêm sub-progress cho các bước:
- `Splitting... (1/3)` → `Verifying... (2/3)` → `Saving... (3/3)`

### B. Preview chapters trước khi save (Ưu tiên: ⭐⭐⭐)
Hiện phải chạy xong mới xem kết quả. Thêm bước **preview** để user xem trước danh sách chapters (title + vài dòng đầu) rồi quyết định save hay re-split.

### C. Chỉnh sửa chapter guide bằng UI (Ưu tiên: ⭐⭐)
Thêm text area ngay trong UI để paste timestamps/chapter guide thay vì phải vào Google Docs description copy.

### D. Export kết quả ra nhiều format (Ưu tiên: ⭐)
Hiện chỉ xuất `.txt`. Có thể thêm:
- **Markdown** (`.md`) — có heading, formatting
- **JSON** — để tích hợp với workflow khác
- **DOCX** — cho Google Docs upload lại

### E. So sánh trước/sau khi retry (Ưu tiên: ⭐)
Khi verify → retry, tạo diff report cho thấy cụ thể gì đã thay đổi giữa lần split 1 và lần 2.

### F. Rate limiting thông minh (Ưu tiên: ⭐⭐)
Khi dùng nhiều threads + verify + retry + summary = nhiều API calls liên tục. Thêm delay tự động giữa các calls để tránh rate limit 429.

### G. Batch summarize song song (Ưu tiên: ⭐)
Hiện `_summarize_results` xử lý tuần tự từng folder. Có thể song song hóa nếu có nhiều files.

---

## ✅ Những gì đã hoạt động tốt

| Tính năng | Trạng thái |
|---|---|
| Timestamp-based splitting | ✅ Ổn định |
| AI marker-based splitting | ✅ Hoạt động |
| Fuzzy timecode search (±10s) | ✅ Tốt |
| Sentence boundary adjustment | ✅ Đã fix |
| Auto-verify + retry (AI mode) | ✅ Mới thêm |
| Verify report cho timestamps | ✅ Mới thêm |
| Cleanup old files | ✅ Mới thêm |
| Chapter count constraint | ✅ Mới thêm |
| Multi-endpoint failover | ✅ Ổn định |
| Auto-save per item | ✅ Có sẵn |
