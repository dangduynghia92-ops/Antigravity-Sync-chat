# Tối ưu Pipeline Audio → SRT

## Vấn đề hiện tại

Pipeline chạy theo **batch steps** — TẤT CẢ file qua Step 0 → TẤT CẢ file qua Step 1 → TẤT CẢ file qua Step 2. Nếu Step 2 lỗi ở file thứ 3/10, phải chạy lại toàn bộ.

## Đề xuất: Per-file Pipeline + Implicit Checkpoints

### Luồng mới

```
Với MỖI file (tuần tự, từng file một):
  Step 0: Match & Rename  → checkpoint: file audio đã đúng tên
  Step 1: Transcribe       → checkpoint: file .srt tồn tại
  Step 2: Verify           → checkpoint: file .srt.verified marker
  
  Nếu bước nào lỗi → log lỗi, chuyển sang file tiếp theo
```

### Checkpoint bằng file existence (không cần database)

| Step | Checkpoint | Cách check |
|------|-----------|------------|
| Match & Rename | Audio đã đúng tên | `basename_audio == basename_txt` |
| Transcribe | File `.srt` đã tồn tại | `os.path.exists(srt_path)` |
| Verify | File `.srt` đã verified | `os.path.exists(srt_path + ".verified")` hoặc marker trong SRT comment |

> [!TIP]
> Khi nhấn Generate lại, pipeline tự skip các bước đã hoàn thành. Chỉ chạy bước còn thiếu.

### Xử lý lỗi

- **File lỗi** → log `❌`, đánh status trên tree, **tiếp tục file tiếp theo**
- **Stop** → dừng ngay, file đã xong giữ nguyên
- **Chạy lại** → tự skip file đã có SRT + đã verified

### Multi-file: Tuần tự (không song song)

> [!IMPORTANT]
> **Whisper chỉ chạy 1 instance** trên GPU (tải cả VRAM). Song song = crash. Verify cũng tuần tự vì dùng chung API rate limit.

Tuy nhiên, vì đã dùng subprocess cho Whisper, pipeline **không block UI**.

---

## Proposed Changes

### Pipeline Logic

#### [MODIFY] [srt_generator_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/srt_generator_tab.py)

Thay đổi `_do_generate` → `_run`:

**Trước:**
```
Step 0: rename ALL files
Step 1: transcribe ALL files  
Step 2: verify ALL files
```

**Sau:**
```python
for each file:
    # Skip nếu đã xong
    if srt_exists and verified:
        status = "⏭ Done"
        continue
    
    if not srt_exists:
        result = transcribe(file)
        if failed: 
            status = "❌ Transcribe failed"
            continue  # KHÔNG dừng, tiếp file sau
    
    if do_verify and srt_exists and not verified:
        ok = verify(srt, txt)
        if failed:
            status = "⚠️ Verify failed"
            continue  # SRT vẫn giữ, chỉ verify lỗi
    
    status = "✅ Done"
```

**Cụ thể:**
- Match & Rename chạy 1 lần đầu cho toàn bộ (vì cần natural sort order)
- Transcribe + Verify chạy per-file tuần tự
- File đã có `.srt` → skip transcribe
- File đã có `.srt.verified` → skip verify
- Lỗi ở file nào → chỉ đánh ❌ file đó, chạy tiếp file sau

#### [MODIFY] [audio_to_srt.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/audio_to_srt.py)

- Thêm function `is_verified(srt_path)` — check `.srt.verified` marker file
- Thêm function `mark_verified(srt_path)` — tạo marker file sau verify thành công

---

## Verification Plan

### Manual Verification
1. Chạy pipeline với 1 file → xong → chạy lại → phải skip hết
2. Xóa `.srt` → chạy lại → chỉ re-transcribe, không re-verify
3. Chạy 2+ files, file 1 OK, file 2 lỗi path → file 1 vẫn ✅, file 2 ❌, file 3 tiếp tục
