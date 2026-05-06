# Quality Review — Pipeline Run (ch_01)

## Step 1: Sequences ✅

| Seq | Dur | Location | Subject |
|---|---|---|---|
| SEQ_01 | 20.2s | Tigris River, raft | Newborn on a raft escaping |
| SEQ_02 | 13.9s | Inside walls of Tikrit | Shirkuh's assassination triggers flight |
| SEQ_03 | 21.3s | Tigris River, raft | Father straining to navigate raft |
| SEQ_04 | 13.4s | Tigris River banks | Guards with torches searching |
| SEQ_05 | 19.6s | Tigris River, far bank | Reaching the far bank, exile |

**Đánh giá**: Tốt — phân đoạn logic, subject factual, characters đúng.

---

## Step 3: Scene Director ✅

**Ưu điểm**:
- `has_crowd: false` đúng cho tất cả cảnh (chỉ có 2-3 nhân vật chính, không có quần chúng)
- `physical_action` chi tiết, cụ thể, visible: "Kurdish-Noble-B turns his shoulder to block the water from hitting the wool bundle"
- Camera progression hợp lý: Wide → Medium → Close-up → Wide (không stuck 1 angle)
- `visual_event` factual, không bịa: "Najm ad-Din Ayyub kneels on a violently rocking timber raft..."

**Vấn đề phát hiện**:

> [!WARNING]
> **SEQ_01 `locked_location` trống**: `loc=` — thiếu location label. Kiểm tra lại output JSON.

> [!WARNING]
> **SEQ_03_SCN_05**: `camera_motion: Extreme Slow Zoom In` trên `Close-up` — Rule 7 cấm Pan on Close-up, nhưng Zoom In trên Close-up có thể chấp nhận. Cần review nếu muốn strict.

---

## Step 4: Prompt Writer ✅

**Ưu điểm mới (so với phiên bản cũ)**:
1. **`characters_detail` per-character**: Mỗi nhân vật có costume/blocking/emotion/action riêng biệt ✅
   - SEQ_03_SCN_03: cả [Kurdish-Noble-B] (leaning forward, pulling bundle) VÀ [Kurdish-Noble-A] (wrapped, resting motionless) đều được mô tả riêng
   - SEQ_03_SCN_04: Father turning shoulder to block spray, infant tucked under chin — 2 nhân vật có 2 vị trí, 2 hành động khác nhau

2. **`lighting` tự suy**: Từ `time_of_day: night` + location → "Harsh orange torchlight from below", "flickering orange glow" — chính xác, phong phú

3. **`background` theo shot_type**: 
   - Wide Shot → "wide view of the violent Tigris River... dark muddy banks and dense reeds"
   - Close-up → "textured, damp surface of the charcoal wool blanket" — đúng logic camera

4. **Costume từ character sheet**: "crimson silk thobe, charcoal wool cloak (aba), black silk hijab" — phù hợp với character reference, không bịa

5. **Không còn `[civilian_man]` label bug** ✅

**Vấn đề phát hiện**:

> [!WARNING]
> **flat_prompt lặp style text**: Nhiều prompt có "In the style of a professional historical animation. This is NOT photorealistic, NOT anime, NOT stick figures, NOT 3D CGI." — đây là nội dung thuộc Mandatory Style, đáng ra LLM không nên repeat vì code đã append. **Token lãng phí**.

> [!NOTE]
> **SEQ_05_SCN_01 + SEQ_05_SCN_04**: B-Roll prompts thêm "NO characters, NO people, NO figures — empty scene only." — LLM tự thêm rule này, không xấu nhưng hơi dài.

> [!NOTE]
> **SEQ_05_SCN_07 camera_angle**: `"wide shot"` — đây phải là góc camera (eye-level/low-angle/high-angle), không phải shot type. LLM nhầm 2 field.

---

## Tóm tắt

| Hạng mục | Đánh giá |
|---|---|
| Step 3 schema mới (bỏ 3 field, thêm has_crowd) | ✅ Hoạt động đúng |
| Step 4 characters_detail per-character | ✅ Rất tốt, mô tả từng nhân vật riêng |
| Step 4 tự suy lighting/background/costume | ✅ Chính xác, phong phú |
| `[civilian_man]` bug | ✅ Đã sửa |
| flat_prompt lặp style text | ⚠️ Cần thêm rule cấm lặp |
| `locked_location` trống | ⚠️ Cần điều tra |
