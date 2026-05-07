# Audit: Character Sheet (Step 2b) — So sánh với chuẩn ngành

## Character Sheet là gì?

Theo chuẩn animation, **character model sheet** (turnaround) là **bản thiết kế kỹ thuật** để đảm bảo nhân vật nhất quán qua mọi frame. Nó PHẢI:

| ✅ Phải có | ❌ Không được có |
|---|---|
| Nhiều góc nhìn (front, 3/4, side) | Biểu cảm/cảm xúc |
| Neutral pose (đứng thẳng, tay buông) | Dynamic/action poses |
| Tỷ lệ cơ thể rõ ràng | Backstory, tính cách |
| Trang phục chi tiết | Skin tone (khi art style quyết định) |
| Đặc điểm nhận dạng cố định (râu, sẹo, tóc) | Shading/rendering phức tạp |
| Nền trắng sạch | Bối cảnh/background |

---

## 6 Lỗi trong output hiện tại

### Lỗi 1: Biểu cảm trong visual_description
```
Seljuk-Official-A: "Surprised expression with wide eyebrows"
Seljuk-Governor-A: "high-arched angry eyebrows"
Kurdish-Warrior-A: "fierce and determined eyebrows"
Kurdish-Prince-A: "Eyes closed in a peaceful expression"
```
❌ Sheet phải NEUTRAL — biểu cảm thuộc về scene prompt

### Lỗi 2: "tanned skin on hands"
```
Kurdish-Leader-A: "Pure white mask-like face, tanned skin on hands"
```
❌ Xung đột: mặt trắng nhưng tay rám nắng? Art style cartoon = tất cả trắng

### Lỗi 3: body_language mô tả tâm trạng
```
"Aggressive and alert, moving with heavy steps of a soldier"
"Protective and strained posture, muscles tensed"
"depicted in a state of shock or collapse"
```
❌ body_language trong sheet chỉ nên là posture mặc định (đứng thẳng, vai mở, v.v.) — không nên mô tả trạng thái cảm xúc

### Lỗi 4: "Not visible" cho HAIR
```
Seljuk-Governor-A HAIR: "Not visible"
Seljuk-Official-A HAIR: "Not visible"
```
❌ Nếu tóc bị turban che, nên viết "covered by turban" — "Not visible" không cung cấp thông tin gì

### Lỗi 5: sheet_prompt dump raw text
```
"...Not visible. Surprised expression with wide eyebrows, small dot eyes..."
```
❌ Sheet prompt chỉ copy/paste visual_description nguyên xi — bao gồm cả lỗi emotion

### Lỗi 6: SKIN section thừa
```
Kurdish-Prince-A: "SKIN: Pure white face, mitten-shaped hands"
```
❌ Prompt yêu cầu 4 mục (BODY, FACE, COSTUME MAIN, COSTUME DETAIL) nhưng LLM tự thêm "SKIN" — field không tồn tại trong schema

---

## Đề xuất sửa Step 2b prompt

Cần rewrite `visual_description` để:
1. **Bỏ emotion/expression** — chỉ permanent features
2. **Bỏ skin tone** — để style file quyết định  
3. **Tách rõ 4 section** với label bắt buộc
4. **body_language** → rename thành **default_stance** — chỉ posture trung tính
5. **sheet_prompt** → template cứng, không copy raw visual_description

### Proposed structure:
```
visual_description phải có ĐÚNG 4 section:
  BODY: [chiều cao (heads), build, tóc (style + màu)]
  FACE: [đặc điểm nhận dạng cố định: râu, sẹo, hình dạng mắt — KHÔNG biểu cảm]
  COSTUME: [trang phục chính + chi tiết, màu sắc cụ thể]
  ACCESSORIES: [headwear, belt, boots, weapons, trang sức]
```
