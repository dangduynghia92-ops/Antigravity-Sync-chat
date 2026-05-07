# Deep Quality Analysis — Pipeline Run (ch_01)

## Issue 1: B-Roll prompts không có nhân vật → AI image vẫn tạo người

### Dữ liệu
- Total prompts: **27**
- Có nhân vật: **20** (74%)  
- Không nhân vật (B-Roll): **7** (26%)

### 7/7 prompts B-Roll đều bị WARNING "mentions people"

Các B-Roll prompt tuy không có `character_labels` nhưng flat_prompt vẫn nhắc đến người gián tiếp:

| Scene | Vấn đề trong flat_prompt |
|---|---|
| SEQ_04_SCN_02 | "guards searching" — có Seljuk-Commander-A + has_crowd=True nhưng bị classify B-Roll sai |
| SEQ_04_SCN_01 | "fortress walls" — AI suy ra có lính trên tường |
| SEQ_05_SCN_04 | flat_prompt ghi rõ "empty scene" nhưng AI image gen vẫn thêm người |

> [!IMPORTANT]
> **Root cause kép**: 
> 1. **Prompt thiếu "NO characters"**: Khi B-Roll không có nhân vật, flat_prompt cần ghi rõ "NO characters, NO people, NO figures — empty scene only" → một số prompt đã có, một số chưa.
> 2. **AI image gen tự thêm người**: Ngay cả khi ghi "NO characters", model image gen (Wan/Kling) vẫn thường thêm người vào cảnh có raft/fortress. Đây là limitation của model, không phải lỗi prompt pipeline.

### Vấn đề dựng cảnh B-Roll

26% prompt là B-Roll (không nhân vật) — **quá nhiều** cho 1 chapter 90 giây. Script chỉ có 2 đoạn text không nhắc nhân vật (SEQ_04), còn SEQ_01/SEQ_03/SEQ_05 đều có nhân vật nhưng Step 3 vẫn tạo B-Roll opening Wide Shot không người.

> [!WARNING]
> **Pattern lặp**: Mỗi sequence đều bắt đầu bằng 1 cảnh B-Roll Wide Shot Pan rồng (raft trên sông), giống nhau. Đây là do Step 3 Rule "OPENING scene = Wide + Slow Pan" — LLM diễn giải quá máy móc, mọi sequence đều bắt đầu bằng establishing shot trống.

---

## Issue 2: Đánh giá phân đoạn & dựng cảnh

### 2A. Phân đoạn (Step 1)

| SEQ | Dur | Location | Subject | Nhận xét |
|---|---|---|---|---|
| 01 | 20.2s | Raft, Tigris | Baby trên raft | OK — POV em bé |
| 02 | 13.9s | Tikrit walls | Shirkuh assassination | OK — flashback |
| 03 | 21.3s | Raft, Tigris | Father shielding baby | OK — action tiếp |
| 04 | 13.4s | Fortress/banks | Guards searching | OK — đối kháng |
| 05 | 19.6s | Raft, far bank | Reaching far bank | OK — resolution |

**Đánh giá**: Phân đoạn hợp lý — mỗi sequence có 1 event rõ ràng, location shift đúng.

### 2B. Dựng cảnh (Step 3)

#### SEQ_01 (20.2s, 6 scenes) ✅
- Camera progression tốt: Wide → Medium → Close-up → Wide → Medium → Close-up zoom
- Visual_event factual
- **Vấn đề**: SCN_01 là B-Roll trống dù script nói "your fragile frame" (baby đang trên raft) → cảnh này nên có baby

#### SEQ_03 (21.3s, 6 scenes) ✅  
- Action progression tốt: raft pitching → father kneeling → holding baby → water splash → shifting weight → swept downstream
- **Vấn đề**: SCN_01 lại là B-Roll trống (y hệt SEQ_01_SCN_01)

#### SEQ_04 (13.4s, 4 scenes) ⚠️
- **A-Roll chỉ 1/4 scenes (25%)** — script nói "guards sweep the riverbanks" nhưng chỉ 1 cảnh có guards, 3 cảnh B-Roll
- SEQ_04_SCN_02 có `has_crowd: True` + Seljuk-Commander-A → đúng
- SEQ_04_SCN_04 mô tả raft bobbing — **trùng** với opening shots của SEQ_01/03/05 → lặp visual

---

## Issue 3: Character count — 5 vs 3

### final2/Test: **5 characters**
1. Ayyubid-Noble-A-Child (Yusuf)
2. Ayyubid-Commander-A (Najm ad-Din) 
3. Ayyubid-Commander-B (Shirkuh)
4. **Seljuk-Noble-A** (victim)
5. **Seljuk-Commander-A** (governor)

### V4: **3 characters**  
1. Kurdish-Noble-A (Yusuf)
2. Kurdish-Noble-B (Najm ad-Din)
3. Kurdish-Commander-A (Shirkuh)

### Nguyên nhân

**Step 1 khác nhau**: 
- final2/Test Step 1 nhận diện 5 nhân vật, bao gồm "Shirkuh's victim" và "Tikrit's governor"
- V4 Step 1 chỉ nhận diện 3 nhân vật — bỏ sót victim và governor

> [!IMPORTANT]
> **Root cause**: Step 1 (segmentation) là non-deterministic — cùng input nhưng LLM có thể list khác nhau tùy lần chạy. Nhân vật "victim" và "governor" chỉ được nhắc 1 lần trong text ("drove a blade into a high-ranking Seljuk official", "The local governor demands"), LLM có thể bỏ qua nếu coi họ không quan trọng.
>
> final2/Test đúng hơn (5 chars) vì tạo character sheet cho tất cả nhân vật được nhắc → prompt đầy đủ hơn.

---

## Tổng hợp vấn đề cần xử lý

| # | Vấn đề | Mức độ | Giải pháp |
|---|---|---|---|
| 1 | B-Roll opening shot lặp lại ở mỗi sequence | ⚠️ Trung bình | Sửa Step 3 rule: opening scene nên có nhân vật nếu script nhắc nhân vật |
| 2 | B-Roll prompt thiếu "NO characters" | ⚠️ Trung bình | Thêm rule Step 4: B-Roll + no character_labels → bắt buộc ghi "NO characters" |
| 3 | Character count non-deterministic | ⚠️ Trung bình | Step 1 cần rule chặt hơn: phải list TẤT CẢ nhân vật/thực thể được nhắc đến |
| 4 | SEQ_04 B-Roll quá nhiều (75%) | Minor | Step 3 anti-pattern: nếu script mô tả hành động người → nên A-Roll |
