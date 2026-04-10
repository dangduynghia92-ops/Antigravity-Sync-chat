# Danh Sách Yêu Cầu Đầy Đủ — Ứng Dụng Desktop PyQt6

> Tổng hợp từ toàn bộ quá trình xây dựng, sửa đổi và cải tiến SRT Prompt Generator.
> Dùng làm template khi tạo ứng dụng mới tương tự.

---

## 1. Kiến Trúc & Mã Nguồn

- Viết code bằng **PyQt6** (không dùng customtkinter hay Tkinter)
- **Tách source code** từng chức năng riêng file — sửa file nào chỉ ảnh hưởng file đó, không rối code
- Chia chức năng lớn thành **từng tab riêng biệt** (Tab SRT Prompt, Tab Product Prompt, ...)
- **Tách biệt backend (`core/`) và UI (`ui/`)** — core logic không import bất kỳ module UI nào
- Cấu trúc thư mục rõ ràng:
  - `core/` — API client, process controller, prompt generator, SRT parser
  - `ui/` — main window, settings dialog, config section, projects section, actions section, log section, ...
  - `ui/icons/` — SVG icons cho arrows, buttons
  - `styles/` — style prompt files (`.txt`)
  - `logs/` — API call history
- File entry point `main.py` riêng biệt, chỉ khởi tạo app + window

---

## 2. Giao Diện UI/UX

- Giao diện **dark theme** hiện đại, chuyên nghiệp
- Hỗ trợ **chuyển đổi theme** Dark / Light trong Settings
- Theme styling **tập trung 1 file** (`theme.py`) — dùng hàm `_build_stylesheet()` nhận color tokens
- Mũi tên ComboBox/SpinBox dùng **file SVG** + `image: url()` (cách duy nhất đáng tin cậy trong Qt QSS)
- Nút bấm dùng **text thuần** (Refresh, Open, Preview) — KHÔNG dùng emoji icon
- Nút xóa/đóng dạng **✕ trắng nền tròn đỏ** (`border-radius: 50%`)
- Kích thước nút **compact, cân đối** giữa các tab — dùng `setFixedSize()` cho nút nhỏ
- **Searchable ComboBox** — combo có ô tìm kiếm lọc nhanh cho danh sách dài
- **Header bar** trên cùng với tên app, version, nút Settings và Restart
- Layout responsive dùng **QSplitter** chia panel trái/phải với tỷ lệ tùy chỉnh
- **ScrollArea** cho dialog/panel có nội dung dài

---

## 3. Chức Năng API — Multi-Endpoint Router

- Gọi **model AI xử lý tác vụ** thông qua API (Gemini, OpenAI compatible endpoints)
- Hỗ trợ **nhiều endpoint dự phòng** (Endpoint #1, #2, #3, ...)
- Khi endpoint bị **rate limit (HTTP 429)**, **tự động chuyển** sang endpoint tiếp theo
- Mỗi endpoint cấu hình riêng biệt:
  - Base URL
  - API Key (hiển thị dạng `●●●●●●`, lưu riêng trong `api_keys.json`)
  - Flash Model (nhanh, rẻ)
  - Pro Model (chất lượng cao)
  - Toggle **Bật/Tắt** từng endpoint
- Chọn **tier xử lý**: Flash (nhanh) hoặc Pro (chất lượng)
- **Test Connection** — kiểm tra endpoint có hoạt động không
- **Log API** toggle — ghi request/response vào `logs/api_history.jsonl` để debug
- URL tự động build: nếu base URL chưa kết thúc `/chat/completions` thì tự thêm

---

## 4. Xử Lý Lỗi & Recovery

- Khi **tất cả endpoint đều fail** → hiện **popup recovery** trên main thread:
  - **Retry** — thử lại tất cả endpoints
  - **Skip** — bỏ qua item hiện tại, tiếp tục item tiếp theo
  - **Stop** — dừng toàn bộ tiến trình
  - **Add Endpoint** — thêm endpoint mới ngay trong popup, rồi retry
- Hiển thị **countdown timer** chờ trước khi retry tự động
- **Retry Failed** — nút riêng để chỉ xử lý lại các items bị lỗi
- Log chi tiết lỗi từng endpoint (HTTP status, error message)

---

## 5. Quản Lý Tiến Trình

- **Start** — bắt đầu xử lý (Process Selected / Process ALL)
- **Pause** — tạm dừng tiến trình (dùng `threading.Event`)
- **Resume** — tiếp tục sau pause
- **Stop** — dừng hẳn tiến trình (set flag `_stop_flag`)
- Hiển thị **progress** cho từng item (thanh tiến trình %, status text)
- **State machine**: IDLE → RUNNING ↔ PAUSED → STOPPED → IDLE
- Xử lý **đa luồng** (`ThreadPoolExecutor`) — tùy chỉnh số threads
- **Thread safety**: mọi UI update qua `QTimer.singleShot(0, ...)`
- Nút bị **disable/enable** tự động theo trạng thái (đang xử lý thì disable Start, enable Stop)

---

## 6. Quản Lý Project & File

- **Scan Folder** — quét thư mục tìm tất cả file SRT
- **Add Files** — thêm file SRT đơn lẻ
- **Tree view** hiển thị projects, **nhóm theo thư mục** (folder grouping)
- **Chống trùng lặp** — không thêm file đã có trong danh sách
- **Remove Selected** / **Clear All** — xóa project khỏi danh sách
- Cột hiển thị: Name, Style, Status, Progress
- Chọn **style riêng** cho từng project (Set Style Selected / Set Style ALL)
- **Style Selector Dialog** riêng — popup chọn style từ danh sách
- **Mở thư mục output** trực tiếp từ app (`os.startfile`)
- **Merge Results** — gộp tất cả kết quả thành 1 file CSV

---

## 7. Style Management

- Load style từ **thư mục `styles/`** (mỗi style = 1 file `.txt`)
- **Refresh** styles — cập nhật danh sách khi thêm/sửa file style
- **Open** — mở thư mục styles trong file explorer
- **Preview** — xem trước nội dung style prompt (2 dòng đầu)
- **Hint text** hiển thị bên dưới combo: 2 dòng đầu tiên của style đang chọn
- Searchable ComboBox cho danh sách style dài

---

## 8. Cấu Hình & Settings

- **Dialog Settings** riêng biệt — popup cấu hình:
  - API Endpoints (thêm/xóa/sửa động)
  - Theme selection (Dark/Light)
  - Language selection
  - Dependencies check/update
- Nút **Reset Defaults** — khôi phục cấu hình mặc định
- Nút **Restart / Reset App** — restart ứng dụng khi cập nhật code mới (`os.execv`)
- Cấu hình **lưu/load tự động**: 
  - `api_keys.json` — API keys và endpoints
  - `srt_config.json` — config tab SRT (style, output, tier, threads, ...)
  - `product_config.json` — config tab Product
  - `settings.json` — theme, language
- **Check Dependencies** — kiểm tra packages đã cài (pip list)
- **Update Dependencies** — cài packages từ requirements.txt

---

## 9. Đa Ngôn Ngữ

- **Lựa chọn ngôn ngữ** output khi tạo prompt (Vietnamese, English, ...)
- Ngôn ngữ lưu trong config, tự load khi khởi động

---

## 10. Tab SRT Prompt — Chức Năng Chuyên Biệt

- **Parse file SRT** — đọc subtitle, group theo interval (giây)
- **SRT Preview** — xem trước nội dung SRT đã parse
- **Context Duration** (giây) — số giây context xung quanh mỗi segment
- **Gen SRT count** — số prompt tạo cho mỗi segment
- **Constraints** — hệ thống bộ lọc:
  - Safety (nội dung an toàn)
  - Quality (chất lượng prompt)
  - Historical (chính xác lịch sử)
  - Format (định dạng đầu ra)
- Kết quả lưu ra **CSV** (filename, segment, prompt, ...)
- **Merge** tất cả CSV trong output thành 1 file tổng hợp

---

## 11. Tab Product Prompt — Chức Năng Chuyên Biệt

- **Paste danh sách objects** (1 object per line) — bulk paste
- **Clear** danh sách objects
- Chọn **Style, Count (số prompt), Tier, Threads** cho batch
- **Generate Selected** / **Generate ALL** / **Retry Failed** / **Stop**
- **Auto-save** kết quả cho từng object ngay khi hoàn thành (file `.txt`)
- **Merge All** — gộp tất cả kết quả vào 1 file CSV
- **Copy All** — copy toàn bộ kết quả vào clipboard
- **Open Output** folder
- Panel **Generated Prompts** hiển thị kết quả realtime
- Progress tracking: Status + Progress cho từng object trong TreeWidget
- **System prompt** chuyên biệt cho product photography (nhiều góc chụp, ánh sáng, composition)

---

## 12. Kỹ Thuật UI/UX Đã Áp Dụng

- `addStretch()` sau nhóm widgets để không bị kéo giãn
- `setFixedSize()` cho nút nhỏ, kích thước biết trước
- `setContentsMargins()` và `setSpacing()` cho layout chặt chẽ
- Icon SVG path dùng **forward-slash** trên Windows (`os.path.replace("\\", "/")`)
- QSS `image: url()` cho arrows — KHÔNG dùng CSS border-triangle
- Inline `setStyleSheet()` chỉ cho nút có màu đặc biệt (nút xanh, đỏ, tím)
- `QTimer.singleShot(0, ...)` cho thread-safe UI updates
- `setWindowFlags` để ẩn nút `?` trên dialog
- Password/API key hiển thị dạng `QLineEdit.EchoMode.Password`
