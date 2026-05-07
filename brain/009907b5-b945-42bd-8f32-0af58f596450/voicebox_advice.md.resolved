# Voicebox — Tư Vấn Cho Máy Bạn

## 📊 Cấu Hình Máy Bạn

| Thông số | Giá trị |
|----------|---------|
| **GPU** | NVIDIA GeForce RTX 2070 — **8 GB VRAM** |
| **RAM** | 32 GB (đang dùng ~16 GB, còn ~17 GB free) |
| **OS** | Windows 11 Pro |
| **CUDA Compute** | 7.5 (Turing) |
| **Voicebox** | v0.4+ cài tại `%LOCALAPPDATA%\Voicebox` |

---

## 🚨 VẤN ĐỀ NGHIÊM TRỌNG: GPU CHƯA ĐƯỢC BẬT!

> [!CAUTION]
> **Voicebox đang chạy trên CPU, KHÔNG dùng GPU!**
>
> Health check trả về:
> ```json
> {
>   "gpu_available": false,
>   "backend_variant": "cpu",
>   "backend_type": "pytorch"
> }
> ```
> Bạn có RTX 2070 nhưng Voicebox đang chạy ở mode CPU = **chậm 5-50x** so với GPU!

### ✅ Cách sửa — Cài CUDA Backend:
1. Mở Voicebox app
2. Vào **Settings → GPU**
3. Tìm nút **"Install CUDA Backend"** → nhấn vào
4. Chờ download 2 phần:
   - Server core: ~200-400 MB
   - CUDA libs: ~4 GB (PyTorch + CUDA DLLs)
5. App sẽ **restart** tự động
6. Kiểm tra lại: Settings → GPU phải hiện **"CUDA (NVIDIA GeForce RTX 2070)"**

Sau khi cài CUDA backend, tốc độ generate sẽ **nhanh hơn 5-10x**.

---

## 1. Nên Dùng Engine Nào?

### Cho ngôn ngữ English + Spanish, chất lượng tốt nhất:

| Engine | Chất lượng | Tự nhiên | English | Spanish | Fit với RTX 2070? |
|--------|-----------|----------|---------|---------|-------------------|
| **Qwen3-TTS 1.7B** ⭐ | ★★★★★ | ★★★★★ | ✅ | ✅ | ✅ (~3.5GB VRAM) |
| **Chatterbox Multilingual** | ★★★★☆ | ★★★★☆ | ✅ | ✅ | ⚠️ (model lớn, sát 8GB) |
| **TADA 3B** | ★★★★★ | ★★★★★ | ✅ | ✅ | ❌ (8GB VRAM, quá sát!) |
| **Chatterbox Turbo** | ★★★★☆ | ★★★★★ | ✅ | ❌ | ✅ (~350MB) |
| **LuxTTS** | ★★★☆☆ | ★★★★☆ | ✅ | ❌ | ✅ (cực nhẹ) |
| **Kokoro** | ★★★☆☆ | ★★★☆☆ | ✅ | ❌ | ✅ (82MB) |

### 🏆 Khuyến nghị: **Qwen3-TTS 1.7B — ĐÚNG LỰA CHỌN!**

> [!TIP]
> **Qwen3-TTS 1.7B là lựa chọn tối ưu nhất cho máy bạn.**
> - ✅ Chất lượng **tốt nhất** trong tầm giá VRAM 8GB
> - ✅ Hỗ trợ cả **English + Spanish** (10 ngôn ngữ)
> - ✅ Ngắt nghỉ **tự nhiên**, intonation tốt
> - ✅ Model ~3.5 GB VRAM = vừa vặn với RTX 2070 8GB
> - ✅ Clone giọng zero-shot

### Về "Turbo" trong tên "Qwen3 1.7B - turbo":
- Đó có thể là **Qwen3-TTS** (model chính, 1.7B params) — đây là engine tốt nhất
- Hoặc là **Chatterbox Turbo** — engine riêng biệt, chỉ English, nhưng hỗ trợ `[laugh]`, `[sigh]`
- Bạn cần mở app kiểm tra: **Settings → xem đang chọn engine gì**

### Khi nào dùng engine nào:

| Tình huống | Engine nên dùng |
|------------|----------------|
| **Voiceover narrative tiếng Anh** (chất lượng max) | Qwen3-TTS 1.7B |
| **Voiceover tiếng Tây Ban Nha** | Qwen3-TTS 1.7B |
| **Cần biểu cảm ([laugh], [sigh])** | Chatterbox Turbo (chỉ English) |
| **Test nhanh, draft** | LuxTTS (cực nhanh) hoặc Kokoro |
| **Cần nhiều ngôn ngữ lạ (Ả Rập, Hindi...)** | Chatterbox Multilingual |

---

## 2. Voice Personalities Là Gì?

### Giải thích đơn giản:
Voice Personalities là tính năng **gắn "tính cách" vào giọng nói**, sử dụng LLM local (Qwen3) để:

### 2 Chức năng:

#### A. Compose (Sáng tác)
- Nhấn nút → LLM **tự tạo câu nói mới** theo đúng phong cách nhân vật
- Ví dụ: Bạn mô tả "Morgan Freeman style - deep, calm, wise" → LLM tạo ra câu kiểu Morgan Freeman
- Dùng để: Brainstorm, tạo nhanh script

#### B. Speak in Character (Nói theo nhân vật)
- Bạn viết text bình thường → LLM **rewrite lại** theo phong cách nhân vật → rồi mới TTS đọc
- Ví dụ:
  - Input: "The war started in 1190"
  - Personality: "Gruff medieval warrior, speaks in short bursts"
  - Output: "That cursed year. 1190. Blood on every field."
- Dùng để: Biến script narrative thành giọng nhân vật cụ thể

### Có cần dùng không?
> [!NOTE]
> **Với pipeline content creation của bạn**: Voice Personalities **không cần thiết ngay**.
> - Pipeline của bạn đã có AI rewriter tạo script sẵn
> - Voice Personalities phù hợp hơn cho game dialogue, interactive content
> - Nếu muốn thử: Tạo personality "narrator" kiểu Morgan Freeman / David Attenborough

---

## 3. Thời Gian Tạo File & Sử Dụng Máy

### Ước tính thời gian (RTX 2070 + CUDA):

| Độ dài text | Qwen3-TTS 1.7B (GPU) | Qwen3-TTS 1.7B (CPU) ⚠️ hiện tại |
|-------------|----------------------|----------------------------------|
| 1 câu ngắn (5-10 từ) | ~2-5 giây | ~20-60 giây |
| 1 đoạn (50-100 từ) | ~10-20 giây | ~2-5 phút |
| 1 trang (200-300 từ) | ~30-60 giây | ~10-20 phút |
| Script 1 chapter (~500 từ) | ~1-2 phút | ~20-40 phút |

> [!WARNING]
> **Hiện tại bạn đang chạy CPU** = chậm gấp 10-20 lần so với bảng GPU bên trái!
> Hãy cài CUDA backend trước (xem phần trên).

### Có dùng máy được khi đang generate không?

> [!IMPORTANT]
> **CÓ, bạn vẫn dùng máy bình thường được!**
> 
> - Voicebox chạy backend riêng (FastAPI server), không block UI
> - Khi generate: GPU utilization tăng lên ~80-100% **TẠM THỜI**
> - Các app thường (trình duyệt, VS Code, Word...) vẫn chạy bình thường
> - **Tránh chạy đồng thời**: Game nặng, render video, training AI khác → tranh GPU

### Với hoạt động máy hiện tại:
- GPU đang dùng: 2175 MB / 8192 MB (27%) — **còn ~5.8 GB VRAM free**
- RAM đang dùng: ~16 GB / 32 GB (50%) — **rất thoải mái**
- GPU utilization: 23%

**→ Qwen3-TTS 1.7B cần ~3.5 GB VRAM → VỪA VẶN với 5.8 GB free hiện tại.**

Nhưng nếu bạn đang dùng app nào ngốn VRAM (CapCut preview, game, Premiere...) thì cần đóng trước khi generate.

---

## 4. Tối Ưu Chất Lượng Tốt Nhất

### Checklist tối ưu:

#### A. Cài CUDA Backend (QUAN TRỌNG NHẤT)
- [ ] Settings → GPU → Install CUDA Backend
- [ ] Verify: `gpu_available: true`, `backend_variant: cuda`
- Sau bước này mọi thứ nhanh hơn 5-10x

#### B. Voice Clone chất lượng cao
- [ ] Audio sample: **10-30 giây**, giọng rõ, **không background noise**
- [ ] Format: WAV hoặc MP3, sample rate ≥ 16kHz
- [ ] Nội dung: Nói tự nhiên, nhịp đều, không ậm ừ
- [ ] **Nhiều sample** (3-5 clips) từ cùng 1 người → clone chính xác hơn
- [ ] Mỗi sample nên khác style: vui, nghiêm túc, casual

#### C. Text input tối ưu
- [ ] **Dấu câu đầy đủ** — câu hỏi `?`, cảm thán `!`, dấu chấm `.`
- [ ] **Câu ngắn-trung bình** — 10-25 từ/câu tốt nhất cho TTS
- [ ] Dấu phẩy `,` và dấu gạch ngang `—` tạo ngắt nghỉ tự nhiên
- [ ] Tránh viết tắt lạ: viết "Doctor" thay vì "Dr."
- [ ] `ALL CAPS` cho từ cần nhấn mạnh: "That was INCREDIBLE!"
- [ ] Số nên viết thành chữ: "nineteen ninety" thay vì "1990"

#### D. Engine settings
- [ ] Engine: **Qwen3-TTS 1.7B** (cho cả English và Spanish)
- [ ] Bật **Voice Prompt Caching** (nhanh hơn khi generate nhiều lần cùng voice)
- [ ] Nếu output bị silence ở cuối → engine tự trim

#### E. Quy trình batch tối ưu cho nhiều file
1. Tạo voice profile 1 lần → dùng lại
2. Chia script thành chunks 100-200 từ
3. Generate từng chunk → tránh auto-chunking kém tự nhiên
4. Ghép lại bằng Stories Editor hoặc tool riêng (CapCut)

---

## 5. Tóm Tắt Hành Động Ngay

| # | Việc cần làm | Ưu tiên |
|---|-------------|---------|
| 1 | **Cài CUDA Backend** trong Settings → GPU | 🔴 NGAY |
| 2 | Restart Voicebox, verify GPU = CUDA | 🔴 NGAY |
| 3 | Test generate 1 câu ngắn với Qwen3-TTS 1.7B | 🟡 SAU |
| 4 | Tạo voice profile chất lượng (10-30s audio sạch) | 🟡 SAU |
| 5 | Test batch generate cho 1 chapter | 🟢 KHI SẴN SÀNG |
