# Voicebox — Tổng Hợp Toàn Bộ Tài Liệu

> Nguồn: [docs.voicebox.sh](https://docs.voicebox.sh/)

---

## 1. Voicebox Là Gì?

Voicebox là **phần mềm AI voice studio mã nguồn mở, chạy hoàn toàn trên máy local** — thay thế miễn phí cho ElevenLabs (voice cloning + TTS) và WisprFlow (voice dictation).

> [!IMPORTANT]
> **100% local** — Không cloud, không account, không dữ liệu nào rời khỏi máy bạn. Model AI, audio, transcript, output LLM đều ở trên máy.

### Vòng lặp Voice I/O 2 chiều:
- **Chiều VÀO (Dictation)**: Bạn nói → Whisper chuyển thành text → paste vào bất kỳ ô text nào đang focus
- **Chiều RA (TTS)**: Text → AI sinh giọng nói → phát audio bằng giọng clone

---

## 2. Các Tính Năng Chính

### 🎙️ Voice Cloning (Clone giọng nói)
- **Zero-shot cloning** — Chỉ cần 10-30 giây audio rõ ràng
- 5 engine hỗ trợ clone: Qwen3-TTS, Chatterbox Multilingual, Chatterbox Turbo, LuxTTS, TADA
- Hỗ trợ **23 ngôn ngữ** (tiếng Anh, Trung, Nhật, Hàn, Đức, Pháp, Ả Rập, Hindi...)
- **Best practices**: Audio sạch, ít noise, nói tự nhiên, 10-30s. Nhiều sample = chất lượng tốt hơn

### 🗣️ 7 TTS Engines (Text-to-Speech)

| Engine | Đặc điểm | Ngôn ngữ |
|--------|----------|-----------|
| **Qwen3-TTS** | Chất lượng cao, Alibaba | 10 ngôn ngữ |
| **Qwen CustomVoice** | Preset voices, hướng dẫn giọng bằng text | Multi |
| **LuxTTS** | Cực nhanh (>150x realtime trên CPU!) | English |
| **Chatterbox Multilingual** | Đa ngôn ngữ nhất | 23 ngôn ngữ |
| **Chatterbox Turbo** | Hỗ trợ tag biểu cảm `[laugh]`, `[sigh]` | English |
| **HumeAI TADA** | Model lớn 3B, chất lượng cao | 10 ngôn ngữ |
| **Kokoro** | Nhẹ nhất (82MB), chạy realtime trên CPU | English |

### ✍️ Dictation (Đọc chính tả)
- **Push-to-talk**: Giữ phím tắt → nói → thả ra → text tự paste vào ô đang focus
- **Toggle mode**: Nhấn Space lần nữa để chuyển sang hands-free mode (nói dài)
- **Auto-refine**: LLM local (Qwen3) tự động dọn dẹp text — xóa "uh", "um", sửa câu lặp
- **Auto-paste**: Text tự paste vào đúng ô bạn đang focus lúc bắt đầu nói
- **Windows**: Phím mặc định `Ctrl+Shift`, tránh xung đột AltGr
- **Pill nổi**: Hiện overlay nhỏ trên màn hình khi đang Recording → Transcribing → Refining

### 🎭 Voice Personalities
- Gắn **personality prompt** vào voice profile (mô tả nhân vật, cách nói, phong cách)
- **Compose**: LLM tự tạo câu nói mới theo phong cách nhân vật
- **Speak in character**: Viết text bình thường → LLM rewrite theo giọng nhân vật → TTS đọc
- Dùng LLM **Qwen3** local (cùng model với Dictation refinement)
- 3 size model: nhỏ, trung bình, lớn

### 📚 Stories Editor
- **Timeline đa track** kiểu DAW (Digital Audio Workstation)
- Kéo thả audio từ History, tạo clip mới inline, upload file
- Trim, split, sắp xếp timing
- Export ra file audio hoàn chỉnh
- **Use cases**: Podcast, audiobook, game dialogue, video voiceover, audio drama

### 🔌 MCP Server (Model Context Protocol)
- Cho phép **AI agents** (Claude Code, Cursor, Cline...) gọi Voicebox để nói bằng giọng clone
- Endpoint: `http://127.0.0.1:17493/mcp` (Streamable HTTP)
- 4 tools:
  - `voicebox.speak` — Nói text bằng voice profile
  - `voicebox.transcribe` — Chuyển audio → text
  - `voicebox.list_captures` — Liệt kê captures
  - `voicebox.list_profiles` — Liệt kê voice profiles
- **Per-client bindings**: Pin mỗi agent vào voice profile riêng (Claude → Morgan, Cursor → Scarlett...)
- **Speaking pill**: Luôn hiển thị overlay khi agent đang nói — tránh TTS ngầm

### 📡 Remote Mode
- Chạy backend trên máy GPU mạnh, frontend trên máy local
- Connect qua HTTP: `http://<server-ip>:17493`
- Hỗ trợ deploy lên AWS EC2, Vast.ai, RunPod
- **Chưa có authentication** — nên dùng VPN/firewall

### 🎛️ Post-Processing Effects
- Pitch shift, reverb, delay, chorus, compression, filters
- Sử dụng **Spotify's Pedalboard** library

---

## 3. Cài Đặt Trên Windows (Liên Quan Đến Bạn)

### Yêu cầu hệ thống:
| | Tối thiểu | Khuyến nghị |
|---|---|---|
| OS | Windows 10+ | Windows 10+ |
| RAM | 8GB | 16GB+ |
| Storage | 5GB | 10GB+ |
| GPU | Không bắt buộc | NVIDIA CUDA (nhanh 5-10x) |

### Cài đặt:
1. Chạy file MSI hoặc Setup.exe
2. Mở app → Server tự khởi động
3. **Lần đầu dùng engine nào** → tự download model:
   - Kokoro: ~350 MB (nhẹ nhất)
   - Qwen 1.7B: ~3.5 GB (khuyên dùng đầu tiên)
   - TADA 3B: ~8 GB (nặng nhất)

### Thư mục dữ liệu:
```
%APPDATA%/sh.voicebox.app/
```

### GPU Acceleration (CUDA):
1. Voicebox **không bundle CUDA** vào installer (để giữ nhẹ)
2. Khi phát hiện NVIDIA GPU → hiện nút **"Install CUDA backend"** trong Settings → GPU
3. Download 2 phần:
   - Server core: ~200-400 MB (update mỗi version)
   - CUDA libs: ~4 GB (PyTorch + CUDA DLLs, ít update)
4. App restart để swap sang CUDA backend

### Kiểm tra hoạt động:
- Settings → GPU: Hiện tên GPU + backend (CUDA/DirectML/CPU)
- Server status: Đèn xanh ở góc trái dưới
- API health check: `curl http://localhost:17493/health`

---

## 4. Kiến Trúc Kỹ Thuật

```
┌─────────────────────────────────────────┐
│           Tauri Desktop App             │
│  ┌───────────────────────────────────┐  │
│  │    React 18 + TypeScript (UI)     │  │
│  │    Zustand (State) + TanStack     │  │
│  │    WaveSurfer.js (Audio)          │  │
│  └──────────────┬────────────────────┘  │
│                 │ HTTP localhost:17493   │
│  ┌──────────────▼────────────────────┐  │
│  │   Python FastAPI Backend          │  │
│  │   ├── routes/ (API endpoints)     │  │
│  │   ├── services/ (business logic)  │  │
│  │   ├── backends/ (7 TTS engines)   │  │
│  │   ├── mcp_server/ (MCP)           │  │
│  │   └── database/ (SQLite)          │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### Flow tạo giọng nói:
1. User nhập text + chọn engine + profile
2. React Query gửi `POST /generate`
3. Route validate → Service xử lý
4. Load/cache voice prompt từ engine backend
5. Task queue serializes (tránh GPU contention)
6. Engine chạy inference → trả audio + sample rate
7. Post-process (trim, effects)
8. Lưu file + metadata SQLite → trả về frontend

---

## 5. REST API (Dùng Để Tích Hợp)

### Endpoints chính:

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| `GET` | `/health` | Kiểm tra server + GPU status |
| `POST` | `/generate` | Sinh giọng nói từ text |
| `POST` | `/speak` | Giống generate nhưng thêm MCP context |
| `PUT` | `/profiles/{id}` | Cập nhật profile (bao gồm personality) |
| `POST` | `/profiles/{id}/compose` | LLM tạo câu nói in-character |
| `GET` | `/events/speak` | SSE stream cho speak events |

### Ví dụ gọi API:
```bash
# Tạo giọng nói
curl -X POST http://127.0.0.1:17493/speak \
  -H 'Content-Type: application/json' \
  -H 'X-Voicebox-Client-Id: my-script' \
  -d '{"text":"Xin chào!","profile":"Morgan"}'

# Kiểm tra health
curl http://localhost:17493/health
```

---

## 6. Tips Sử Dụng

### Tối ưu chất lượng giọng:
- Audio clone: **10-30 giây**, giọng rõ, ít noise, nhịp nói tự nhiên
- Nhiều sample khác nhau (vui, buồn, casual, formal) → clone chính xác hơn
- Dấu câu đúng → giọng tự nhiên hơn: `"Hello! How are you?"` thay vì `"Hello how are you"`
- `ALL CAPS` = nhấn mạnh, `*italic*` = nhấn nhẹ

### Engine nào phù hợp cho bạn:

> [!TIP]
> **Cho pipeline content creation (voiceover video)**:
> - **Qwen3-TTS 1.7B** — Chất lượng cao nhất, hỗ trợ đa ngôn ngữ, cần GPU
> - **LuxTTS** — Cực nhanh trên CPU, chỉ English
> - **Chatterbox Turbo** — Nếu cần biểu cảm `[laugh]`, `[sigh]`, chỉ English

### Paralinguistic tags (chỉ Chatterbox Turbo):
```
[laugh]  → tiếng cười
[sigh]   → tiếng thở dài
[gasp]   → tiếng hít hơi
```
Gõ `/` trong text input để mở tag inserter.

---

## 7. Liên Quan Đến Pipeline Của Bạn

> [!IMPORTANT]
> Voicebox có **REST API** chạy ở `localhost:17493`. Bạn có thể tích hợp trực tiếp vào pipeline Python hiện tại bằng cách gọi `POST /generate` hoặc `POST /speak` thay vì dùng API TTS cloud.

### Lợi ích cho workflow của bạn:
1. **Miễn phí hoàn toàn** — không chi phí API như ElevenLabs
2. **Local** — không cần internet, không rate limit
3. **Voice cloning** — clone giọng narrator riêng, dùng lại cho mọi video
4. **Auto-chunking** — text dài tự chia nhỏ + crossfade, phù hợp script narrative
5. **Stories Editor** — ghép multi-track cho video có nhiều giọng
6. **API-first** — REST endpoint dễ gọi từ Python script
