# POV Writing Prompt — Full Audit

## Contradictions Found

### ❌ 1. COLD OPEN vs MANDATORY Level rule
```
Line 48: "Every chapter MUST begin with the Level label and age."
Line 66: "COLD OPEN: No 'Level' word."
Line 69: "Starting a chapter without 'Level [N]' = STRUCTURAL FAILURE."
```
**COLD OPEN literally violates its own MANDATORY rule AND triggers STRUCTURAL FAILURE.**
Kịch bản tham khảo: 0/13 chapters dùng COLD OPEN. Luôn có Level.

### ❌ 2. Level 1 birth — "age" rule bị vi phạm bởi ví dụ
```
Line 48: "MUST begin with Level label and age."
Line 53: "Level one, the blood clot. You are born with a clot..."
                                      ↑ "born" không phải age
```
**Ví dụ STANDARD đầu tiên vi phạm chính rule MANDATORY.**

### ❌ 3. STILLNESS example contradicts CLOSING CONTENT RULE
```
Line 93: STILLNESS example: "You look at the horizon. No satisfaction, only distance.
         The steppe ends somewhere out there. You have already decided where you are going next."
Line 171: VIOLATION: "You look at the horizon." (no change stated)
Line 172: VIOLATION: "You decide where to go next." (no closure)
```
**STILLNESS dùng chính 2 câu mà CLOSING CONTENT RULE gọi là VIOLATION.**

### ❌ 4. "echo" closing type — không có trong CLOSING TYPES section
```
Line 221: "closing_type = 'echo'" (END CHAPTER RULES)
Line 176-199: CLOSING TYPES chỉ có: cold_fact, paradox, forward_pull, weight
```
**END CHAPTER yêu cầu "echo" nhưng phần CLOSING TYPES không định nghĩa nó.**

### ❌ 5. POV RULES trùng lặp GOLDEN RULES
```
Line 100: "SECOND PERSON ABSOLUTE: 'You' is the ONLY subject" (GOLDEN RULES)
Line 249-254: "You = the historical figure. ALWAYS." (POV RULES)
```
**Cùng 1 rule viết 2 lần ở 2 nơi khác nhau. AI không biết cái nào ưu tiên.**

### ❌ 6. SENTENCE LENGTH contradicts reference script
```
Line 130: "NEVER exceed 25 words in a single sentence."
```
Kịch bản tham khảo Ch 10: *"A merchant convoy of 450 men, everyone traveling under your banner and your protection is massacred at a western border by a governor who wanted their goods."* — **29 words.**
Kịch bản tham khảo Ch 7: *"You were chosen by every winter your mother survived on bark, by every man who bet against you and lost, by every scar your body carries."* — **28 words.**

### ❌ 7. CHAPTER FLOW "WEIGHT LINE" vs CLOSING CONTENT RULE
```
Line 142: "WEIGHT LINE: 1-2 sentences closing (via closing_type)"
Line 155: "The last 1-3 sentences MUST answer ONE of these..."
```
**Không rõ closing là 1-2 hay 1-3 câu.**

---

## Redundancies

| Rule | Appears at | Also at | Notes |
|---|---|---|---|
| Second person POV | Line 100 (Golden Rules) | Line 249-254 (POV Rules) | Nói 2 lần |
| No narrator voice | Line 40 (Identity) | Line 117-124 (Golden Rule 5) | Nói 2 lần |
| Sentence rhythm | Line 72-94 (RHYTHM section) | Line 129-130 (Golden Rule 7) | Overlap sentence length |
| "Level" usage | Line 48-50 (Opening Discipline) | Line 263 (Universal Rules) | Overlap |

---

## Structure Issues

1. **13 sections** cho 1 prompt duy nhất — quá nhiều section, AI dễ bỏ qua phần cuối
2. **PRIORITY ORDER** ở cuối (line 267-278) — nhưng AI đọc từ trên xuống, khi gặp mâu thuẫn ở trên đã tự quyết rồi
3. **Không có CONTEXT/BRIDGE rule** — kịch bản tham khảo có bridge opening (Ch 7, 9, 10 đều mở bằng câu nối từ chapter trước) nhưng prompt không dạy
4. **CLOSING CONTENT RULE** (mới thêm) xung đột với ví dụ cũ trong STILLNESS

---

## Proposed Clean Structure

Viết lại prompt với cấu trúc rõ ràng, không chồng chéo:

```
1. IDENTITY + POV (gộp Golden Rule 1 + POV Rules)
2. OPENING (gộp Opening Discipline, bỏ COLD OPEN, thêm birth exception)
3. BODY (gộp Chapter Flow + Sentence Rhythm + Golden Rules 2-6)
4. CLOSING (gộp Closing Content Rule + Closing Types + echo)
5. SPECIAL CHAPTERS (Level 1 + End Chapter)
6. CONSTRAINTS (gộp Universal Rules + Foreign Language + Spoken Rhythm)
7. OUTPUT
```

7 sections thay vì 13. Không trùng lặp. Không mâu thuẫn.
