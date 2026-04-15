# Bộ Quy Tắc: Phân Bổ Key_Data & Viết Nội Dung (Pirate Ship Framework)

*Rút ra từ case study Queen Anne's Revenge. Áp dụng cho tất cả ship topics.*

---

## I. PHÂN LOẠI KEY_DATA

Mọi data từ blueprint thuộc 1 trong 3 loại:

### Loại 1: EVENT (Sự kiện có ngày, có hành động)
Có timeline cụ thể. Ai, làm gì, khi nào, kết quả gì.

> **Ví dụ QAR**: "Nov 28, 1717: Cướp La Concorde", "May 1718: Phong tỏa Charleston", "June 10, 1718: Mắc cạn Beaufort"

**Quy tắc phân bổ EVENT:**
- Mỗi EVENT = **1 main_key_data** tại phase phù hợp nhất theo lifecycle
- EVENT luôn đi kèm: setup + execution + aftermath = 1 cluster
- KHÔNG tách micro-steps thành nhiều main items

### Loại 2: CONDITION (Trạng thái liên tục, không có ngày)
Diễn ra liên tục trong suốt giai đoạn, không có start/end rõ ràng.

> **Ví dụ QAR**: "Bệnh syphilis hoành hành", "Ăn hardtack mốc", "Draft 12.5ft gây nguy hiểm ở vùng nước nông", "Pirate Code: bỏ phiếu, chia phần"

**Quy tắc phân bổ CONDITION:**
- Condition thuộc Bánh Răng (freeze-frame phase)
- Là **main_key_data** nếu tạo ra scene (Pirate Medicine, Pirate Code drama)
- Là **sub_key_data** nếu chỉ là background (ăn uống, thời tiết)
- **KHÔNG gán ngày** cho condition — nó là trạng thái, không phải sự kiện

### Loại 3: SEED (Nhân → Quả xuyên phase)
Một observation ở phase này **trực tiếp gây ra** event ở phase sau.

> **Ví dụ QAR**: "Bệnh dịch hoành hành" (Bánh Răng) → "Cướp thuốc ở Charleston" (Thử Lửa). "Draft sâu" (Bánh Răng) → "Mắc cạn" (Cái Chết).

**Quy tắc phân bổ SEED:**

| Phần | Ở đâu | Cách viết |
|------|-------|-----------|
| **Plant** (gieo) | Ở phase sớm hơn (thường Bánh Răng) | Nêu observation thuần túy, KHÔNG spoil kết quả. "Con tàu 300 tấn có draft 12.5ft — quá sâu cho vùng nước nông ven bờ." |
| **Harvest** (thu hoạch) | Ở phase EVENT xảy ra | Recall seed trong setup, rồi show kết quả. "Draft 12.5ft đã biến Beaufort Inlet thành nấm mồ." |

> [!IMPORTANT]
> **Quy tắc vàng**: SEED chỉ **GIEo** ở phase sớm (as observation). **MOTIVATION** (lý do hành động) thuộc về EVENT phase, KHÔNG tách riêng.
> - ✗ BAD: Bánh Răng main = "Bệnh nặng khiến họ quyết định cướp thuốc"  (motivation + spoiler)
> - ✓ GOOD: Bánh Răng main = "Hơn nửa thủy thủ đoàn nhiễm syphilis. Thợ mộc trở thành bác sĩ." (observation)
> - ✓ GOOD: Thử Lửa main = "Đoàn cướp biển không cướp vàng — họ phong tỏa Charleston cho một rương thuốc." (event + motivation bundled)

---

## II. SẮP XẾP CHAPTERS

### Quy tắc 1: LIFECYCLE PROGRESSION
Chapters tiến theo vòng đời con tàu: Sinh → Biến đổi → Vận hành → Đỉnh cao → Chết → Di sản.

Đây là trình tự **tự nhiên** mà audience hiểu — giống kể chuyện về 1 "nhân vật". Audience không cần biết framework, họ chỉ cần biết "con tàu sinh ra → lớn lên → chiến đấu → chết".

### Quy tắc 2: FREEZE-FRAME PLACEMENT
Phase Bánh Răng = **freeze-frame** — đóng băng thời gian, đưa audience vào bên trong tàu.

**Vị trí đặt**: SAU biến đổi (tàu đã hoàn chỉnh) và TRƯỚC trận đánh đầu tiên.

```
Mutation (tàu thành cỗ máy) 
  → FREEZE-FRAME (bên trong cỗ máy) 
    → First battle (cỗ máy ra trận)
```

**Tại sao vị trí này?**
- Audience vừa xem tàu được build xong → tò mò "bên trong nó thế nào?"
- Sau freeze-frame → audience đã biết bệnh tật, draft sâu → sẵn sàng hiểu WHY khi events xảy ra
- Seeds được gieo trước → harvest tự nhiên ở chapters sau

### Quy tắc 3: EVENT ESCALATION (cho Thử Lửa)
Khi có 2-3 events ở Thử Lửa, sắp xếp theo **LEO THANG**:

```
Event nhỏ → Event lớn → Event vĩ đại nhất
```

| Thứ tự | Vai trò | Transition |
|--------|---------|------------|
| Event 1 | Chứng minh sức mạnh (1 tàu vs 1 tàu) | Kết: "Nhưng hắn không dừng lại..." |
| Event 2 | Escalation (1 tàu vs 1 thành phố) | Kết: "Chiến thắng lớn nhất gieo mầm diệt vong..." |

**Nếu có event thứ 3 nhỏ** (vd: Great Allen) → **gom vào chapter của event 1** như brief mention hoặc sub_key_data. KHÔNG tạo chapter riêng cho event nhỏ.

**Quy tắc chọn event:**
- **Iconic event**: Sự kiện tạo dấu ấn kinh hoàng, rúng động (vd: đánh bại tàu chiến Hải quân)
- **Greatest event**: Sự kiện vĩ đại nhất, đỉnh cao khả năng (vd: phong tỏa cả thành phố)
- **Pyrrhic event**: Sự kiện chiến thắng nhưng trả giá (vd: cướp thuốc thay vì vàng = tàu đang chết)

Nếu event vừa iconic vừa pyrrhic → tốt nhất — tạo dramatic irony tự nhiên.

### Quy tắc 4: CAUSAL PROXIMITY (Nhân-Quả Gần Nhau)
Seed và harvest PHẢI nằm trong khoảng cách hợp lý.

| Khoảng cách | Đánh giá |
|-------------|----------|
| Cùng chapter hoặc chapter liền kề | ✅ Tốt nhất |
| Cách 2 chapters | ⚠️ Cần micro-callback nhắc lại |
| Cách 3+ chapters | ❌ Audience quên — mất hiệu quả |

**Áp dụng**: Nếu có quá nhiều chapters giữa seed và harvest → rút seed xuống gần hơn, hoặc thêm micro-callback ở chapters trung gian.

### Quy tắc 5: PHASE TRANSITION BRIDGE
Khi chuyển giữa 2 phases có tính chất khác nhau (freeze-frame → action, action → tragic):

```
Chapter cuối phase cũ: ends_with PHẢI tease MOTIVATION hoặc CONSEQUENCE
                       dẫn sang phase mới.
Chapter đầu phase mới: Scene Anchor PHẢI integrate callback_to 
                       (nhắc lại context) trong 1-2 câu đầu.
```

**Ví dụ generic:**
- Freeze → Action: "Cỗ máy đã sẵn sàng. Nhưng thứ [subject] cần không phải chiến thắng — mà là [real motive]."
- Action → Collapse: "[Subject] có tất cả. Nhưng cái giá nuôi cỗ máy... đang ăn mòn chính nó."
- Collapse → Archaeology: "Rồi tất cả biến mất. [X] năm sau, một [discoverer] tìm thấy..."

---

## III. QUY TẮC VIẾT NỘI DUNG

### Quy tắc W1: SCENE ANCHOR BẮT BUỘC
Mọi chapter body phải mở bằng 1-3 câu neo: **THỜI GIAN + ĐỊA ĐIỂM + CHỦ THỂ**.

- EVENT chapter: Ngày cụ thể + địa điểm + tàu/nhân vật
- FREEZE-FRAME chapter: Địa điểm mô tả + cảm giác (không cần ngày)
- ARCHAEOLOGY chapter: Năm hiện đại + người phát hiện

### Quy tắc W2: CALLBACK INTEGRATION
Nếu chapter có `callback_to` field trong outline → writer PHẢI integrate callback vào SCENE ANCHOR hoặc 3 câu đầu tiên.

```
✗ BAD:  "May 1718. Charleston Harbor." (chỉ có anchor, không recall)
✓ GOOD: "Hơn nửa thủy thủ đoàn đang gục vì syphilis. Tháng 5, 1718, 
         [subject] không nhắm tới vàng — hắn phong tỏa Charleston 
         cho một rương thuốc."
```

Callback KHÔNG phải recap — nó là 1 câu context giúp audience hiểu WHY ngay lập tức.

### Quy tắc W3: MOTIVATION-FIRST (Lý do trước, hành động sau)
Với mọi event có cause, nêu CAUSE trong 1-2 câu → rồi mới vào action.

```
✗ BAD:  "Hắn phong tỏa Charleston. Vì thủy thủ đoàn bị bệnh." 
        (action trước, lý do sau → audience confused)
✓ GOOD: "Thủy thủ đoàn đang chết dần vì syphilis. Hắn cần 
         thuốc — và Charleston có." (cause → action)
```

### Quy tắc W4: ESCALATION TRANSITION (giữa các events cùng phase)
Khi 2 events cùng thuộc 1 phase (vd: 2 trận đánh ở Thử Lửa):

```
Event 1 kết: Nêu consequence → tease sự leo thang
  "Hải quân Anh đã phải rút lui. Nhưng [subject] không dừng lại ở một con tàu."
  
Event 2 mở: New scene anchor → action ngay
  "Tháng 5, 1718. [Subject] đặt cả hạm đội chặn ngang cửa cảng Charleston."
```

Transition giữa events cùng phase = **escalation** (từ nhỏ → lớn), KHÔNG phải recap.

### Quy tắc W5: MICRO-CALLBACK (nhắc lại xuyên chapters)
Khi harvest một seed đã plant 2+ chapters trước:

- Tối đa 1-2 câu nhắc lại
- Nêu OBSERVATION, không recap chapter
- Tích hợp vào flow, không đứng riêng

```
✗ BAD:  "Như đã nói ở chương trước, con tàu có draft 12.5ft." (recap)
✓ GOOD: "Con tàu 300 tấn với draft 12.5ft đang tiến vào vùng 
         nước chỉ sâu 15ft." (observation tích hợp vào scene)
```

---

## IV. TÓM TẮT QUY TẮC VÀO 1 BẢNG

| # | Quy tắc | Áp dụng vào prompt nào |
|---|---------|----------------------|
| D1 | EVENT = main, gom setup+action+aftermath = 1 cluster | Phase Plan |
| D2 | CONDITION = main (nếu có scene) hoặc sub (nếu background) | Phase Plan |
| D3 | SEED: plant = observation ở phase sớm, harvest = event ở phase sau | Phase Plan |
| D4 | MOTIVATION thuộc về EVENT, không tách riêng | Phase Plan |
| O1 | Lifecycle progression: Sinh → Biến đổi → [Freeze] → Đỉnh → Chết → Di sản | Outline |
| O2 | Freeze-frame đặt SAU mutation, TRƯỚC first battle | Outline |
| O3 | Thử Lửa events: sắp theo ESCALATION (nhỏ → lớn) | Outline |
| O4 | Causal proximity: seed-harvest ≤ 2 chapters | Outline |
| O5 | Phase transition bridge: ends_with tease + callback_to recall | Outline + Write |
| W1 | Scene Anchor mở đầu mọi chapter | Write |
| W2 | Callback Integration trong 3 câu đầu | Write |
| W3 | Motivation-First: cause trước, action sau | Write |
| W4 | Escalation Transition giữa events cùng phase | Write |
| W5 | Micro-callback ≤ 2 câu, tích hợp vào flow | Write |
