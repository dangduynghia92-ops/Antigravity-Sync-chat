# Nghiên cứu: Chuyển ngôn ngữ văn chương → điện ảnh cho AI pipeline

## Vấn đề hiện tại

Pipeline đang gửi **văn bản gốc** (POV narrative) thẳng vào Step 3 (Scene Director):

```
"Nỗi sợ hãi bao trùm lấy anh, bóng tối nuốt chửng linh hồn"
                    ↓ (Step 3 nhận trực tiếp)
        → LLM phải vừa hiểu metaphor vừa dựng scene
        → Dễ sai: vẽ "bóng tối nuốt người" theo nghĩa đen
```

Step 3 hiện cố giải quyết bằng Rule 8 (Visual Translation Strategy), nhưng LLM phải làm **2 việc cùng lúc**: hiểu ý nghĩa + dựng cảnh.

---

## 3 Phương án

### Phương án A: Giữ nguyên (embedded trong Step 3)
**Hiện tại**: `visual_event` field = LLM tóm tắt visual event trước khi dựng cảnh

- ✅ Không thêm API call
- ❌ LLM phải vừa dịch ngữ vừa dựng cảnh → cognitive load cao
- ❌ Không kiểm tra được bước dịch ngữ riêng

### Phương án B: Thêm Step riêng (Step 2.5)
Tạo bước trung gian: **Visual Scene Decomposition**

```
Step 1 output: "Nỗi sợ bao trùm, bóng tối nuốt chửng linh hồn"
    ↓
Step 2.5: Rewrite thành "filmable action lines"
    ↓
Output: "Nhân vật đứng run trong phòng tối. Tay nắm chặt thành ghế. 
         Ngọn nến cuối cùng chập chờn rồi tắt."
    ↓
Step 3: Scene Director nhận bản đã clean → dựng cảnh chính xác hơn
```

- ✅ Tách biệt rõ: 1 LLM dịch ngữ, 1 LLM dựng cảnh
- ✅ Debug dễ — xem bước nào sai
- ❌ Thêm 1 API call/sequence → tăng chi phí + thời gian
- ❌ Có thể mất context nếu rewrite quá xa bản gốc

### Phương án C: Prompt Chaining (nâng cấp Step 3)
Giữ nguyên Step 3 nhưng **buộc LLM viết bản dịch trước khi dựng cảnh**:

```json
{
  "visual_event": "tóm tắt sự kiện visual (đã có)",
  "filmable_actions": [          ← MỚI
    "Nhân vật đứng run trong phòng tối",
    "Tay nắm chặt thành ghế",
    "Ngọn nến tắt"
  ],
  "scenes": [...]                ← dựng cảnh từ filmable_actions
}
```

- ✅ Không thêm API call — cùng 1 request
- ✅ Buộc LLM "nghĩ trước khi làm" (chain-of-thought)
- ✅ Debug được: xem filmable_actions có đúng không
- ❌ Vẫn 1 LLM làm 2 việc, nhưng tách bước rõ hơn

---

## So sánh

| Tiêu chí | A (hiện tại) | B (Step riêng) | C (Prompt Chain) |
|---|---|---|---|
| Chi phí API | Không đổi | +1 call/seq | Không đổi |
| Độ chính xác | Trung bình | Cao nhất | Cao |
| Debug | Khó | Dễ nhất | Dễ |
| Tốc độ | Nhanh | Chậm hơn | Không đổi |
| Complexity | Đã có | Thêm step mới | Sửa prompt |

---

## Đề xuất: Phương án C (Prompt Chaining)

**Lý do**: Không tốn thêm API call, nhưng bắt LLM tách rõ 2 giai đoạn trong 1 request.

### Cách thực hiện

Trong Step 3, thêm field `filmable_actions` vào **Phase 1** (trước khi dựng scenes):

```
### Phase 1 — Visual Event Synthesis
1. Read full_text → write visual_event (đã có)
2. NEW: Break visual_event into filmable_actions:
   - Mỗi action = 1 hành động camera có thể quay được
   - Cấm metaphor/abstract → phải chuyển thành physical action
   - Mỗi action bắt đầu bằng "[Ai] [làm gì]"
   
   BAD: "Darkness consumed his soul"
   GOOD: "Character stands trembling in dark room, gripping chair edge"
   
   BAD: "His kingdom crumbled before his eyes"
   GOOD: "Character's hands drop the scroll, shoulders slump forward"

### Phase 2 — Camera Cuts
Based on filmable_actions (NOT full_text), create camera angles...
```

### Lợi ích
1. LLM buộc phải **viết lại** text thành filmable trước khi dựng
2. `filmable_actions` nằm trong JSON output → **kiểm tra được**
3. Step 4 (Prompt Writer) cũng nhận được filmable_actions → prompt chính xác hơn
4. Không tốn thêm tiền/thời gian
