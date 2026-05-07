# Tạo Tab "🎙 Audio → SRT" — Chuyển audio thành phụ đề SRT

## Mô tả
Thêm tab mới vào app PyQt cho phép chuyển file audio (MP3, WAV, etc.) thành file phụ đề SRT bằng **Faster-Whisper** (chạy local, miễn phí), kèm tính năng **AI verify** tự động so sánh SRT với text gốc.

---

## Trả lời câu hỏi

### 1. Các model Whisper — So sánh chi tiết

| Model | Tham số | Kích thước tải | RAM/VRAM cần | Độ chính xác (WER) | Tốc độ | Dùng khi nào |
|-------|---------|----------------|-------------|---------------------|--------|-------------|
| **tiny** | 39M | ~75 MB | < 1 GB | Thấp — sai nhiều từ | ⚡ Cực nhanh (32x) | Test nhanh, draft |
| **base** | 74M | ~140 MB | ~1 GB | Thấp–TB — vẫn sai nhiều | ⚡ Rất nhanh (16x) | Mobile, realtime |
| **small** | 244M | ~460 MB | 1.5–2 GB | Trung bình — OK cho audio rõ | 🚀 Nhanh (6x) | Cân bằng tốc độ/chất lượng |
| **medium** | 769M | ~1.5 GB | 3–4 GB | Cao — tốt cho đa số trường hợp | 🏃 TB (2x) | Chất lượng cao |
| **large-v3** | 1.5B | ~3 GB | 5–6 GB | Cao nhất — ít sai nhất | 🐢 Chậm (1x) | Yêu cầu chính xác tuyệt đối |
| **large-v3-turbo** | 809M | ~1.6 GB | ~3 GB | Rất cao (gần = large-v3) | 🚀 Nhanh (6x) | ⭐ **BEST — nên dùng mặc định** |

> [!TIP]
> **`large-v3-turbo`** là lựa chọn tốt nhất hiện tại. Nó có độ chính xác gần bằng `large-v3` nhưng nhanh gấp 6 lần và chỉ tốn ~3GB RAM. Đây sẽ là model mặc định.

**Tối ưu thêm:**
- Dùng `compute_type="int8"` giảm RAM 30-40% mà gần như không mất chất lượng
- Trên CPU: model `small` hoặc `large-v3-turbo` + `int8` chạy tốt
- Có GPU NVIDIA: bất kỳ model nào cũng nhanh

### 2. Auto-detect ngôn ngữ

✅ **Có!** Faster-Whisper hỗ trợ `language=None` → tự phát hiện ngôn ngữ. Sẽ có dropdown:
- **Auto Detect** (mặc định)
- Vietnamese, English, Spanish, Chinese, Japanese, Korean, ...

### 3. Output path

- Có ô nhập output path + nút Browse `...`
- **Để trống** = lưu file SRT cùng thư mục với file audio gốc
- **Có path** = lưu vào thư mục đó

### 4. AI Verify — So sánh SRT với text gốc

Tham khảo pattern từ `video_prompt_tab.py` (project Prompt_Image), thêm bước verify:

**Workflow:**
```
1. User thêm file audio + file text gốc (optional)
2. Whisper transcribe audio → SRT
3. Nếu có text gốc → AI Verify:
   - Gửi text SRT + text gốc lên Gemini
   - AI so sánh, tìm lỗi sai (tên riêng, số liệu, thuật ngữ)
   - Tự động sửa SRT (giữ nguyên timestamp, sửa text)
   - Xuất file SRT đã sửa
```

---

## Proposed Changes

### Dependencies

#### [MODIFY] [requirements.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/requirements.txt)
- Thêm `faster-whisper>=1.1.0`

---

### Core Module

#### [NEW] core/audio_to_srt.py

**Chức năng chính:**

1. **`transcribe_audio(audio_path, model_size, language, device, compute_type)`**
   - Load Whisper model (cache lần đầu)
   - Transcribe audio → segments (start, end, text)
   - Return list segments

2. **`segments_to_srt(segments, output_path)`**
   - Format segments thành SRT chuẩn
   - Ghi file `.srt`

3. **`verify_srt_with_original(srt_text, original_text, api_client, log_callback)`**
   - Gửi SRT text + original text lên Gemini API
   - Prompt: "So sánh 2 văn bản, tìm các lỗi sai tên riêng/số liệu/thuật ngữ trong SRT so với bản gốc, trả về bản sửa"
   - Parse response → cập nhật text trong SRT entries (giữ nguyên timestamps)
   - Return corrected SRT content + danh sách lỗi đã sửa

4. **`get_available_models()`** — trả về dict model info
5. **`detect_device()`** — auto detect CPU/CUDA

**Hỗ trợ format:** MP3, WAV, M4A, FLAC, OGG, WMA, AAC

---

### UI Tab

#### [NEW] ui/srt_generator_tab.py

Tab UI theo pattern `tts_tab.py`:

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│ 🎙 Audio → SRT                                      │
├─────────────────────────────────────────────────────┤
│ [Add Files] [Scan Folder] │ Model: [large-v3-turbo▼]│
│ Language: [Auto Detect ▼] │ Device: [CPU ▼]         │
│ Output: [________________________] [...]            │
│ ☑ AI Verify (so sánh với text gốc)                  │
├─────────────────────────────────────────────────────┤
│ 📁 Folder_01 (3 files)                              │
│   ├ chapter_01.mp3  │ 5:32  │ ✓ TXT │ ✓ 100%      │
│   ├ chapter_02.mp3  │ 4:18  │ ✓ TXT │ ⏳ 60%       │
│   └ chapter_03.mp3  │ 6:01  │ ✗ TXT │ —            │
│ voice_standalone.wav │ 2:45  │ ✗ TXT │ —            │
├─────────────────────────────────────────────────────┤
│ [All] [None] [Clear] [Remove]    [Generate] [Stop]  │
├─────────────────────────────────────────────────────┤
│ Log panel                                           │
└─────────────────────────────────────────────────────┘
```

**Tree columns:** Tên File | Duration | TXT Pair | Status

**Tính năng:**
- **Scan folder**: tìm `.mp3/.wav/.m4a/.flac` + auto match file `.txt` cùng tên (cho verify)
- **Add Files**: thêm file audio riêng lẻ
- **Model dropdown**: tiny, base, small, medium, large-v3, large-v3-turbo (mặc định)
- **Language dropdown**: Auto Detect, Vietnamese, English, Spanish, Chinese, Japanese, Korean
- **Device dropdown**: CPU, CUDA (auto-detect, disable CUDA nếu không có GPU)
- **AI Verify checkbox**: bật/tắt bước so sánh SRT với text gốc
- **Progress**: per-file status (Transcribing 40% → Verifying 80% → ✓ 100%)
- **Output**: SRT file cạnh audio hoặc vào folder riêng

**AI Verify flow (khi checkbox bật + có file .txt):**
1. Whisper transcribe → raw SRT
2. Đọc file .txt gốc
3. Gửi lên Gemini: so sánh raw SRT text vs original text
4. Gemini trả về corrected text + list changes
5. Apply changes vào SRT (giữ timestamps) → ghi file `_verified.srt`
6. Log ra các lỗi đã sửa

---

### Main Window

#### [MODIFY] [main_window.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/main_window.py)
- Import `SRTGeneratorTab`
- Thêm tab `"🎙 Audio → SRT"` sau tab "🔊 TTS Cleanup"
- Cập nhật `TAB_HELP_IDS`

---

## Verification Plan

### Automated Tests
- Chạy app → tab hiển thị đúng
- Test transcribe 1 file MP3 ngắn (~30s) → verify SRT format chuẩn
- Test AI verify với SRT + TXT → verify corrections applied

### Manual Verification  
- User test với audio TTS thật → kiểm tra SRT chính xác
- Test AI verify: cố tình cho text gốc khác → xem AI có phát hiện và sửa
