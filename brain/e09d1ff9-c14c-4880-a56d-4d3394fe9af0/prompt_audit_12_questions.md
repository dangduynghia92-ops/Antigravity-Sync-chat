# Phân Tích 12 Vấn Đề Trong Write Prompt POV

## 1. Level Anchor bị hiểu nhầm thành tiêu đề chapter

**Phát hiện đúng.** Trong `PREVIOUS CHAPTERS`:
```
Level one, the dead flesh. You are 9 years old.
The Jerusalem sun bakes the courtyard stone...
```
Nhưng file output ch01 thực tế KHÔNG có câu "Level one, the dead flesh. You are 9 years old."

**Nguyên nhân**: Code tạo `PREVIOUS CHAPTERS` bằng cách ghép `chapter_title` + nội dung:
- Code lấy title "Level 1: The Dead Flesh" → format thành "Level one, the dead flesh. You are 9 years old."
- Dòng này KHÔNG phải là output gốc của writer AI — nó là code inject.
- Writer AI ch01 SKIP level anchor → output không có → nhưng code vẫn thêm vào previous context.
- AI ch03 đọc previous context → thấy "Level one..." → nghĩ output nên bắt đầu bằng Level anchor → **may mắn** ch03 có Level anchor.

**Kết luận**: Code inject fake Level anchor vào previous context dù output gốc không có. Nếu writer AI skip → previous context vẫn giả vờ có. **Không đáng tin cậy.**

---

## 2. PART 2 yêu cầu "1-3 sentences" — không nên giới hạn

**Đúng.** Prompt hiện tại:
```
PART 2 — CONTEXT (1-3 sentences, the CAUSE)
```

Giới hạn 1-3 câu cho context/cause là tùy ý. Một số sự kiện cần nhiều context hơn (ví dụ: Baldwin IV coronation cần context về cha chết, regency, leprosy). Một số chỉ cần 1 câu.

**Sửa**: Bỏ giới hạn số câu, chỉ giữ hướng dẫn "ngắn gọn, đủ để giải thích WHY".

---

## 3. `physical_state` là gì? Prompt viết cho Baldwin hay cho chung?

**Phát hiện đúng.** Prompt ghi:
```
Weave sub_key_data and physical_state INTO the action
```

`physical_state` là field trong outline, ví dụ:
```json
"physical_state": "Permanent claw hand deformity; physical exhaustion accelerating the disease."
```

Field này **CHUNG** — mọi nhân vật POV đều có (mỗi chapter outline đều generate `physical_state`). KHÔNG phải hardcode cho Baldwin.

**NHƯNG** ví dụ minh họa trong prompt:
```
✓ "Your clawed hands cannot grip the reins to remount."
```
→ Ví dụ này **ĐÚNG LÀ** viết cho Baldwin → **vi phạm nguyên tắc prompt chung**.

**Sửa**: Ví dụ cần generic, không reference Baldwin cụ thể. VÀ cần giải thích `physical_state` là field outline chứa body state cho chapter đó.

---

## 4. `scene_close` vs `PART 4 — WEIGHT LINE` khác nhau gì?

**Phát hiện mâu thuẫn đúng.** So sánh:

| | scene_close | WEIGHT LINE |
|---|---|---|
| Vị trí | Trong outline JSON, field `scene_close` | Trong write prompt, PART 4 |
| Mục đích | "CONSEQUENCE — what changed immediately" | "Close the event. State what CHANGED, what was LOST" |
| Ví dụ | "The enemy line shatters, Saladin barely escapes" | "Every Templar in the garrison is dead" |

**Chúng gần như GIỐNG NHAU.** AI đọc scene_close → viết consequence → rồi lại phải viết WEIGHT LINE = lặp lại.

Thực tế output ch03:
```
You save Jerusalem. The desert is painted in Ayyubid blood. But the extreme exertion burns through...
You have achieved immortal glory... But your greatest triumph only guarantees you will survive...
```
→ 2 đoạn close = scene_close + weight line — trùng nội dung.

**Sửa**: `scene_close` nên định nghĩa là consequence tức thì (kết quả trận đánh). `WEIGHT LINE` là reflection/cost sau consequence. HOẶC gộp thành 1.

Và PART 4 đang giới hạn "1-2 sentences, LAST" → không cần giới hạn.

---

## 5. Đoạn summary + opening styles mục đích gì?

```
A chapter with only SCENE = observation report (feels cut short)
A chapter with ANCHOR + CONTEXT + SCENE + WEIGHT LINE = complete event (lived and closed)

OPENING STYLES (assigned per chapter in outline):
  STANDARD (~60%)...
  THESIS (~20%)...
  ATMOSPHERE (~20%)...
```

**Mục đích**: Reinforcement — nhắc lại 4-part là bắt buộc, và opening styles là menu.

**Vấn đề**: **THỪA.** Đã nói ở PART 1-4 rồi, lại nhắc lại. Và opening styles ĐÃ có trong style JSON (line 70 `body_chapter_opening`). 
→ AI đọc 3 lần cùng 1 thông tin: style JSON + PART 1-4 + đoạn summary này → confused.

**Sửa**: XÓA đoạn này hoàn toàn. Đã có PART 1-4.

---

## 6. Lại `physical_state` ở PRINCIPLE 2

```
PRINCIPLE 2: WEAVE sub_key_data AND physical_state INTO ACTION.
```

**Giống câu 3**: `physical_state` là field outline — không phải hardcode. Nhưng ví dụ:
```
✓ "Your mother was taken from another man on his wedding day"
```
→ Ví dụ này là từ **Genghis Khan** biography, không phải Baldwin → cũng vi phạm nguyên tắc prompt chung, nhưng ít nhất không specific.

**Sửa**: Giải thích `physical_state` = body state field từ outline. Ví dụ dùng generic.

---

## 7. `CLOSING — CONTENT RULE` mục đích gì?

Prompt giải thích:
```
The STYLE GUIDE defines closing TYPES (cold_fact, paradox, etc.) — HOW to phrase it.
This section defines closing CONTENT — WHAT must be expressed.
```

**Ý đồ**: Style JSON nói closing TYPE (cold_fact, paradox...) = format. Phần này nói CONTENT (what changed, what cost...) = nội dung.

**Vấn đề**: **THỪA + MÂU THUẪN** với PART 4. PART 4 đã nói:
> "Close the event. State what CHANGED, what was LOST, or what this COST."

Section 3 lại nói lại + thêm 4 lựa chọn content. **2 chỗ nói cùng 1 việc = AI confused.**

**Sửa**: GỘP vào PART 4. Không cần section riêng.

---

## 8. `SPECIAL CHAPTERS` mục đích gì?

```
─── LEVEL 1 (OPENING CHAPTER) ───
─── END CHAPTER (LAST CHAPTER) ───
```

**Mục đích**: Hướng dẫn đặc biệt cho chapter đầu và cuối (birth scene, death scene, legacy, callback).

**Vấn đề**: Outline ĐÃ có `chapter_structure: "legacy_close"`, `closing_type: "echo"`. Style JSON ĐÃ có `first_chapter`, `last_chapter` rules. **Lặp 3 lần.**

**Sửa**: XÓA hoặc gộp vào 1 nơi duy nhất.

---

## 9. Mâu thuẫn closing rule — "WHAT IS COMING?"

**Phát hiện mâu thuẫn nghiêm trọng.**

PART 4 nói:
> "do NOT hint at the next chapter or create a cliffhanger"

`chapter_ending_protocol` nói:
> "Do NOT hint at the next chapter — each event is self-contained"

NHƯNG Section 3 `CLOSING — CONTENT RULE` lại có:
> "4. WHAT IS COMING? — Forward tension: a threat, a clock, an inevitability"
> Ví dụ: "He has something better. Time. And you're running out of it."

**TRỰC TIẾP MÂU THUẪN.** 2 chỗ nói "NEVER forward tension" + 1 chỗ nói "forward tension là 1 trong 4 lựa chọn".

**Sửa**: XÓA "WHAT IS COMING?" khỏi closing content. Chỉ giữ 3 lựa chọn: WHAT CHANGED, WHAT LEARNED, WHAT IS THE COST.

---

## 10. Gửi FULL OUTLINE cho AI để làm gì?

Trong file debug:
```
FULL OUTLINE (all chapters — for context, you are writing ONE chapter from this):
{...toàn bộ 10 chapters...}
```

**Mục đích**: Để writer AI biết tổng thể narrative arc, biết chapter mình viết nằm ở đâu trong câu chuyện.

**Vấn đề**: 
- Full outline = ~4000+ chars → chiếm token
- Writer đã có: previous chapters, event_cause, scene fields → đủ context
- Full outline chứa future chapters → AI có thể bị ảnh hưởng → tạo forward tension (vốn bị cấm)
- Style JSON đã có framework arc → không cần outline

**Sửa**: CÂN NHẮC bỏ full outline, chỉ giữ chapter outline riêng + previous context.

---

## 11. `─── SYSTEM PROMPT (sent to AI) ───` nghĩa là gì?

File debug format:
```
─── SYSTEM (70,894 chars) ───
[...style JSON + blueprint + outline + write prompt...]

─── USER (772 chars) ───
[...chapter instruction...]

─── AI RESPONSE (2,385 chars) ───
[...output...]
```

**Giải thích**: Đây là **API debug log** — ghi lại CHÍNH XÁC những gì gửi cho AI:
- **SYSTEM** = system prompt (hướng dẫn + data) → 70,894 chars
- **USER** = user message (lệnh viết chapter cụ thể) → 772 chars  
- **AI RESPONSE** = output AI trả về

**TẤT CẢ** nội dung trong section SYSTEM được gửi cho AI. Không chọn lọc. Đó là lý do **70,894 chars = quá nhiều**. Style JSON + blueprint + full outline + write rules = quá tải.

---

## 12. Mâu thuẫn opening styles trong `body_chapter_opening`

```json
"body_chapter_opening": "3 OPENING STYLES (menu, not formula):
  (1) STANDARD: 'Level N, [label]. You are [age].' → context/cause → scene.
  (2) THESIS: Bold statement about significance, THEN Level anchor + context.
  (3) ATMOSPHERE: Physical environment/body state, THEN Level anchor + context.
  RULE: Level anchor + age MUST appear within first 2 sentences regardless of style."
```

**Mâu thuẫn**:
- STANDARD: Level anchor FIRST → context → scene ✓
- THESIS: Bold statement FIRST, THEN Level anchor → Level anchor = sentence 2
- ATMOSPHERE: Physical environment FIRST, THEN Level anchor → Level anchor = sentence 2
- RULE: "within first 2 sentences" → cho phép Level anchor ở sentence 2

**NHƯNG** PART 1 trong write prompt nói:
> "The FIRST SENTENCE of every chapter MUST contain the Level label and age."

→ **Conflict**: Style JSON cho phép Level anchor ở sentence 2 (THESIS/ATMOSPHERE), write prompt bắt buộc sentence 1.

**Thêm nữa**: `hook.anchor` trong style JSON:
> "FIRST SENTENCE must be Level anchor: 'Level one, [label]. You are [age].'"

→ Cũng bắt buộc sentence 1.

**Kết quả**: AI confused → skip Level anchor hoàn toàn.

**Sửa**: 1 rule duy nhất, 1 chỗ duy nhất. Level anchor LUÔN ở sentence 1 cho mọi opening style.

---

## Tổng Kết

| # | Vấn đề | Loại | Mức độ |
|---|---|---|---|
| 1 | Level anchor inject fake vào previous | Bug code | 🔴 |
| 2 | Giới hạn 1-3 câu context | Tùy ý | 🟡 |
| 3 | physical_state không giải thích | Thiếu context | 🟡 |
| 4 | scene_close ≈ weight line trùng | Redundant | 🔴 |
| 5 | Summary + opening styles thừa | Redundant | 🟡 |
| 6 | physical_state lặp lại | Redundant | 🟡 |
| 7 | CLOSING CONTENT RULE trùng PART 4 | Redundant | 🔴 |
| 8 | SPECIAL CHAPTERS lặp 3 lần | Redundant | 🟡 |
| 9 | "WHAT IS COMING?" mâu thuẫn closing | **Conflict** | 🔴 |
| 10 | Full outline gửi thừa | Waste tokens | 🟡 |
| 11 | System = tất cả gửi cho AI, 70K chars | Quá tải | 🔴 |
| 12 | Opening style mâu thuẫn Level anchor | **Conflict** | 🔴 |

> [!CAUTION]
> **Root cause**: Write prompt có **quá nhiều sections nói cùng 1 việc** (closing rules x3, opening styles x3, Level anchor x4) → AI đọc conflicting instructions → output không ổn định. Cần viết lại prompt từ đầu, mỗi rule chỉ xuất hiện 1 lần, 1 chỗ.
