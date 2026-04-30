# Nghiên cứu: Nguyên tắc Storyboard Chuyên nghiệp vs Pipeline Hiện tại

## Nguồn tham khảo
- StudioBinder, MasterClass, Adobe, Boords, LearnAboutFilm, PixFlow, Adorama

---

## 1. Nguyên tắc từ ngành phim

### A. Shot Size Progression (Wide → Close)
> "Scenes SHOULD progress from wide to close as emotion escalates"

| Giai đoạn | Shot | Mục đích |
|---|---|---|
| Mở đầu | Wide Shot | Thiết lập không gian, bối cảnh |
| Giữa | Medium Shot | Cầu nối — nhân vật trong context |
| Cao trào | Close-up | Cảm xúc, chi tiết quyết định |

**Pipeline hiện tại:** ✅ Đã có Rule 8 (Camera Motion) khuyến khích Wide mở đầu. **Nhưng CHƯA ép** tiến trình Wide→Medium→Close.

### B. 30-Degree Rule
> "Khi cắt giữa 2 shot cùng chủ thể, camera phải dịch ≥30°, nếu không sẽ bị 'jump cut'"

**Áp dụng thực tế:** Nếu 2 scenes liên tiếp đều Medium Shot cùng nhân vật → phải khác góc hoặc khác shot size.

**Pipeline hiện tại:** ❌ **Chưa có** — có thể xảy ra 3 Medium Shot liên tiếp.

### C. 180-Degree Rule
> "Camera phải giữ cùng 1 bên trục hành động giữa 2 nhân vật"

**Pipeline hiện tại:** ❌ Không áp dụng được — AI image gen mỗi frame độc lập, không có spatial continuity giữa frames. **Bỏ qua.**

### D. Match on Action
> "Cắt giữa 2 góc khác nhau của CÙNG 1 hành động"

**Pipeline hiện tại:** ✅ Đã có trong Anti 1:1 Rule — "Scenes must be DIFFERENT CAMERA ANGLES of the same event"

### E. Purposeful Cutting
> "Mỗi lần cắt phải phục vụ mục đích narrative — reveal thông tin mới, reaction, power shift"

**Pipeline hiện tại:** ⚠️ Có ngầm định nhưng chưa explicit.

---

## 2. So sánh: Pipeline vs Nguyên tắc

| Nguyên tắc | Pipeline | Status | Hành động |
|---|---|---|---|
| Shot progression (W→M→CU) | Có Rule 8 mở đầu Wide | ⚠️ Partial | **Thêm rule** |
| 30-degree / No duplicate shots | Chưa có | ❌ Missing | **Thêm rule** |
| 180-degree | Không áp dụng (AI gen) | N/A | Bỏ qua |
| Match on Action | Anti 1:1 Rule | ✅ Có | Giữ nguyên |
| Purposeful cutting | Ngầm định | ⚠️ Weak | Có thể thêm |
| Shot type whitelist | Rule 4 (3 types) | ✅ Mới thêm | Giữ nguyên |

---

## 3. Đề xuất bổ sung vào Step 3

### Rule mới 1: Shot Size Progression
```
Scenes SHOULD follow Wide → Medium → Close-up progression.
- Scene 1: MUST be Wide Shot (establishing)
- Middle scenes: Medium Shot preferred  
- Final scene: Close-up allowed for emotional climax
- FORBIDDEN: Close-up → Wide Shot (reverse jump)
```

### Rule mới 2: No Duplicate Adjacent Shots
```
Two CONSECUTIVE scenes MUST NOT have the same shot_type.
BAD:  Medium Shot → Medium Shot → Medium Shot
GOOD: Wide Shot → Medium Shot → Close-up → Medium Shot
```

> [!IMPORTANT]
> Cả 2 rules này đều **dễ validate bằng code** sau khi LLM trả kết quả — không cần phụ thuộc LLM tuân thủ 100%.

---

## 4. Rules KHÔNG nên thêm

| Rule | Lý do bỏ |
|---|---|
| 180-degree | AI gen frames độc lập, không có camera vị trí liên tục |
| Shot/Reverse Shot | Yêu cầu 2 nhân vật đối diện — quá cụ thể cho pipeline chung |
| Rule of Thirds | Thuộc về image generation prompt, không phải storyboard |
| Eyeline Match | Không kiểm soát được trong AI gen |
