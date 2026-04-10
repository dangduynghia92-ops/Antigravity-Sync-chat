# In-App User Manual (Tabbed HTML + Help Button)

Tạo User Manual dạng HTML với tab tương ứng các tab trong app. Thêm nút Help trên header bar để mở manual, tự nhảy đến tab đang mở.

## Proposed Changes

### User Manual HTML File

#### [NEW] [user_manual.html](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/user_manual.html)

File HTML tiếng Việt, styled đẹp, bao gồm **11 tab** tương ứng app:

| # | App Tab | Manual Tab ID | Nội dung chính |
|---|---------|---------------|----------------|
| 1 | 🚀 Auto Pipeline | `auto-pipeline` | Paste URL → Download → Split → Rewrite tự động. Mode, Style, Word count, Checkboxes |
| 2 | 📥 YouTube | `youtube` | Download sub-tab (add URL, batch, transcript) + Scanner sub-tab (playlist/channel, Excel export) |
| 3 | 📂 SRT Chapter | `srt-chapter` | Split SRT/TXT thành chapters. Script Type, Tier, Threads, Auto-Verify, AI Summary |
| 4 | 🔀 Regroup | `regroup` | Scan chapters → AI phân loại theo niche → Copy to group. Mode Chapter/Folder |
| 5 | ✍️ Rewrite | `rewrite` | Rewrite chapters: Analyze → Rewrite → Merge. Top/List và Narrative mode |
| 6 | ✦ Style Rewrite | `style-rewrite` | **Tab phức tạp nhất**: Mode (Review/Narrative), Style, Niche config, Framework, Word count, Checkboxes, Pipeline 12 bước |
| 7 | ✂ Video Cutter | `video-cutter` | Cắt video theo chapter timestamps |
| 8 | 🔊 TTS Cleanup | `tts-cleanup` | Làm sạch text cho TTS. Rules, diacritics, special terms |
| 9 | 🔍 Style Analyzer | `style-analyzer` | Phân tích phong cách viết, tạo style JSON |
| 10 | 🍪 Cookies | `cookies` | Quản lý cookies cho YouTube |
| 11 | 💬 Chat | `chat` | Chat test với Google Search |

**Design**: Dark theme, tab navigation bên trái (vertical sidebar), nội dung bên phải. Responsive.

---

### Header Bar — Help Button

#### [MODIFY] [header_bar.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/header_bar.py)

- Thêm signal `help_clicked = pyqtSignal()`
- Thêm nút `"❓ Help"` vào header bar (sau Gemini keys, trước Restart)

#### [MODIFY] [main_window.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/main_window.py)

- Connect `help_clicked` signal → `_open_help()`
- Method `_open_help()`: lấy index tab hiện tại → map sang tab ID trong manual → mở browser `user_manual.html#tab-id`

Tab index mapping:
```python
TAB_HELP_IDS = [
    "auto-pipeline", "youtube", "srt-chapter", "regroup",
    "rewrite", "style-rewrite", "video-cutter", "tts-cleanup",
    "style-analyzer", "cookies", "chat"
]
```

## Verification Plan

### Manual Verification
1. Khởi động app → kiểm tra nút **❓ Help** hiện trên header bar
2. Click Help khi đang ở **tab 1 (Auto Pipeline)** → trình duyệt mở manual, tab "Auto Pipeline" active
3. Chuyển sang **tab 6 (Style Rewrite)** → click Help → manual mở đúng tab "Style Rewrite"
4. Kiểm tra manual hiển thị đẹp trên trình duyệt, tất cả 11 tab hoạt động
5. Kiểm tra nội dung tiếng Việt đầy đủ, mô tả đúng chức năng
