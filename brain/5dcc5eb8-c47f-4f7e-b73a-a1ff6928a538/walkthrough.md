# Walkthrough: Queue + Skip Feature

## Files Changed

### [auto_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/auto_pipeline.py)

**Skip Logic** — Mỗi phase tự kiểm tra file tồn tại trước khi chạy:

| Method | Skip Condition | Log Message |
|--------|---------------|-------------|
| `phase1_fetch_info_and_transcript` | Project dir + transcript file > 500 bytes | `⏭ Transcript already exists` |
| `start_video_download` | `.mp4` file > 1MB | `⏭ Video already exists` |
| `phase2_split` | ≥ 2 chapter `.txt` files in `01_chapters/` | `⏭ N chapters already exist` |
| Rewrite | **KHÔNG BAO GIỜ SKIP** | Luôn chạy lại |

**New helper methods:**
- `find_existing_project(video_id)` — tìm project dir theo video ID
- `_find_transcript_file(project_dir)` — tìm transcript > 500 bytes
- `_find_video_file(project_dir)` — tìm video .mp4 > 1MB
- `_count_chapter_files(chapters_dir)` — đếm chapter files
- `has_cut_video_chapters(task)` — check `02_video_chapters/` (for future use)

---

### [auto_pipeline_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py)

**UI Changes:**
- `QPlainTextEdit` (multi-line URL) → `QLineEdit` (1 dòng) + **"+ Add"** button
- Thêm `QListWidget` hiển thị queue items với status icons
- Thêm nút **"▶ Run Merge"** (màu tím)
- Thêm nút **"🔄 Retry Failed"** (ẩn khi không có error)
- Bỏ nút **"Save Config"** (config tự lưu khi Run)

**Queue System:**
- `_queue` list + `_queue_lock` (thread-safe)
- Status: ⏳ pending → 🔄 running → ✅ done / ❌ error
- Add URL: Enter hoặc nút "+ Add" → validate → thêm vào queue
- Paste: nếu clipboard có nhiều URL → thêm tất cả
- Right-click context menu: Remove / Retry
- Double-click error item → retry
- **"Clear Queue"** — xoá tất cả non-running items
- **"🔄 Retry Failed"** — reset tất cả ❌ → ⏳

**Execution:**
- **"▶ Run Queue"** → `_run_queue_loop()`: lấy item pending → chạy → check tiếp
- Có thể thêm URL mới khi đang chạy → item mới tự động được xử lý
- **"▶ Run Merge"** → lấy tất cả pending URLs → gọi `_run_merge()` (logic cũ)
- `_run_single` raise `RuntimeError` khi lỗi → queue loop bắt → set status error

## Verification
- ✅ `py_compile` — no syntax errors
- ✅ Module imports OK
- ✅ Git committed
