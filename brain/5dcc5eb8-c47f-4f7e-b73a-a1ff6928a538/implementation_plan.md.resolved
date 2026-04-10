# Add Queue + Skip Feature to Auto Pipeline Tab

## Tính năng 1: Queue

### Hành vi
- Paste URL → ấn **"+ Add"** hoặc Enter → URL thêm vào queue list
- **"📋 Paste"** → paste clipboard, nếu nhiều dòng → thêm tất cả vào queue
- Ấn **"▶ Run Queue"** → chạy lần lượt từng item (mỗi video 1 kịch bản)
- **Có thể thêm URL mới ngay cả khi pipeline đang chạy** → item mới tự động được xử lý khi đến lượt
- **"⏹ Stop"** → dừng sau video hiện tại, các video chưa chạy vẫn ở trạng thái pending
- Queue không lưu khi đóng app

### Merge mode
- Giữ nguyên như cũ. Thêm nút **"▶ Run Merge"** riêng (chỉ enabled khi queue ≥ 2 items và mode = Top/List Review)
- Merge lấy **tất cả URL pending** trong queue → chạy merge giống hành vi cũ (không queue)

### UI Layout

```
┌─ YouTube URL ─────────────────────────────────────────────┐
│ [__URL input (1 dòng)__________]  [+ Add] [📋 Paste]     │
├───────────────────────────────────────────────────────────┤
│ Queue (3):                                  [Clear Queue] │
│  🔄 1. Best Scout Rifles in 2026...                  [×] │
│  ⏳ 2. https://youtu.be/def456                       [×] │
│  ⏳ 3. https://youtu.be/ghi789                       [×] │
├───────────────────────────────────────────────────────────┤
│ [Config: Mode, Style, Lang, Tier, ...]                    │
│ [▶ Run Queue] [▶ Run Merge] [⏹ Stop] [Save] [📂 Open]   │
└───────────────────────────────────────────────────────────┘
```

### Queue item states
| Icon | Status | Ý nghĩa |
|------|--------|---------|
| ⏳ | `pending` | Chờ xử lý, có thể xoá |
| 🔄 | `running` | Đang chạy, không xoá được |
| ✅ | `done` | Hoàn thành |
| ❌ | `error` | Lỗi |
| ⏭ | `skipped` | Bỏ qua (user xoá trước khi đến lượt) |

---

## Tính năng 2: Skip completed steps

### Logic skip cho `_run_single(url)`

Kiểm tra project folder `[videoID]_Title/` đã tồn tại hay chưa. Nếu tồn tại → kiểm tra từng step:

| Step | Điều kiện skip | File kiểm tra |
|------|---------------|---------------|
| Download transcript | `*_transcript.txt` tồn tại và > 500 bytes | `[vid]_*_transcript.txt` trong project dir |
| Download video | `*.mp4` tồn tại và > 1MB | Bất kỳ `.mp4` trong project dir |
| Download thumbnail | `*_thumb.jpg` tồn tại | `[vid]_thumb.jpg` trong project dir |
| Classify | Có chapter files trong `01_chapters/` | `.txt` files (không phải `_MERGED`, `_SUMMARY`) |
| Split chapters | Có chapter files trong `01_chapters/` | Giống trên |
| Cut video | Có `.mp4` files trong `02_video_chapters/` | Bất kỳ `.mp4` trong `02_video_chapters/` |
| **Rewrite** | **KHÔNG BAO GIỜ SKIP** | Luôn chạy lại từ đầu |

### Khi skip:
```
[Phase 1] ⏭ Transcript already exists — skipping download
[Phase 1] ⏭ Video already exists — skipping download  
[Phase 2] ⏭ 11 chapters already exist — skipping split
[Auto] ⏭ Video chapters already exist — skipping cut
[Auto] Phase 3: Rewriting 11 chapters...  ← LUÔN CHẠY
```

---

## Proposed Changes

### [MODIFY] [auto_pipeline_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/auto_pipeline_tab.py)

#### UI Changes (`_build_ui`)
- `_txt_urls` (QPlainTextEdit multi-line) → `_txt_url_input` (QLineEdit, 1 dòng) + Enter = add
- Add `_btn_add` (QPushButton, "+ Add")
- Add `_queue_list` (QListWidget) — hiển thị queue items
- Add `_btn_clear_queue` (QPushButton, "Clear Queue")
- Add `_lbl_queue_count` (QLabel)
- Rename `_btn_run` → "▶ Run Queue"
- Add `_btn_merge` (QPushButton, "▶ Run Merge") — chỉ enabled khi queue ≥ 2, mode = Top/List
- Chỉnh Run Merge enabled/disabled theo điều kiện

#### New data structures
```python
self._queue = []         # [{"url": str, "status": str, "title": str, "error": str}]
self._queue_lock = threading.Lock()
```

#### New methods
- `_add_to_queue(url)` — validate URL, thêm vào queue, refresh list
- `_add_from_paste()` — paste clipboard, nhiều URL → thêm tất cả
- `_remove_queue_item(index)` — xoá item pending khỏi queue
- `_clear_queue()` — xoá tất cả pending items
- `_refresh_queue_list()` — cập nhật QListWidget từ self._queue
- `_run_queue()` — loop: lấy item pending → chạy `_run_single` → update status → tiếp
- `_on_run_merge()` — lấy tất cả URL pending → gọi `_run_merge(urls)` → hoàn nguyên

#### Modified methods
- `_on_run()` → gọi `_run_queue()` thay vì đọc text area → luôn mode independent
- `_run_single()` → thêm logic skip (check existing files)
- `_on_stop()` → giữ nguyên, chỉ set `_stop_flag`
- `_on_pipeline_done()` → update trạng thái nếu dừng giữa chừng

### [MODIFY] [auto_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/auto_pipeline.py)

#### Skip logic trong `phase1_fetch_info_and_transcript`
- Kiểm tra transcript file đã tồn tại → skip, load text từ file
- Kiểm tra thumbnail đã tồn tại → skip
- Return `True` (đã có data)

#### Skip logic trong `start_video_download`
- Kiểm tra `.mp4` file đã tồn tại → skip, set `task.video_path`

#### Skip logic trong `phase2_split`
- Kiểm tra chapter files đã tồn tại trong `01_chapters/` → skip

#### New method: `check_existing_project(task)` 
- Tìm project dir theo video ID
- Set `task.project_dir`, `task.chapters_dir`, `task.rewrite_dir`, `task.title`, `task.transcript_path`, `task.video_path`
- Return `True` nếu project đã tồn tại

## Verification Plan

### Automated Tests
- `py_compile` — no syntax errors
- Module imports OK

### Manual Verification
- Thêm 3 URL vào queue → Run → chạy lần lượt ✓
- Thêm URL mới khi pipeline đang chạy → chạy tiếp ✓
- Ấn Stop → dừng đúng ✓
- Xoá item pending → không bị chạy ✓
- Chạy lại video đã có transcript/chapters → skip đúng ✓
- Rewrite vẫn chạy lại từ đầu ✓
- Merge: chọn 3 URL → Run Merge → gộp đúng ✓
