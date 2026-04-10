# Audit: Hướng dẫn viết Chapter Intro (Hook) — Tất cả Niches & Frameworks

## 1. Tổng quan 3 lớp hướng dẫn

Hook chapter được hướng dẫn qua **3 lớp** — nhưng chúng KHÔNG nhất quán giữa các niches:

| Lớp | Biography | Battle | Mystery |
|---|:---:|:---:|:---:|
| **Style JSON** (`hook` field trong framework) | ✅ 5/5 fw có | ✅ (via `structure.hook`) | ✅ (via `hook` field) |
| **Writer Prompt** (HOOK CHAPTER section) | ✅ Chi tiết (lines 208-255) | ⚠️ Tối thiểu (lines 150-161) | ⚠️ Tối thiểu (lines 236-245) |
| **Outline Prompt** (hook rules) | ❌ Không có | ❌ Không có | ❌ Không có |

---

## 2. BIOGRAPHY — Writer Prompt (chi tiết nhất)

### Cấu trúc 3 phần:
```
1. COLD OPEN (1-3 câu): Drop into tension/paradox/mystery.
   "No context. No introduction."
   
2. NARRATIVE PROMISE (2-4 câu): WHO + WHY matters NOW.

3. CURIOSITY GAP (1-2 câu): Tease journey ahead.
```

### 5 Hook Types trong writer prompt:
| Type | Cách mở | Example |
|---|---|---|
| PARADOX | 2 sự thật mâu thuẫn | "He fought for peace. His signature created the bomb." |
| IN MEDIA RES | Drop vào crisis scene | "1939. A physicist pounds on his door." |
| COUNTER-INTUITIVE | Thách thức giả định | "Greatest genius couldn't get a job." |
| DARK SECRET | Mặt tối ít ai biết | "A pathologist stole his brain." |
| STAKES DECLARATION | Tuyên bố mức rủi ro | "One letter. One signature. 200,000 lives." |

### Anti-patterns:
- ✗ Giải thích kỹ thuật
- ✗ Khen chung chung ("He was one of the greatest...")
- ✗ Bắt đầu bằng ngày sinh
- ✗ Liệt kê thành tựu
- ✗ "Imagine a world where..." / "What if I told you..."

---

## 3. BIOGRAPHY — Style JSON (framework-level hook)

Mỗi framework có `hook` field riêng với `method`, `tone`, `example_approach`:

### Framework: Hai Mặt
```json
{
  "method": "Open with the MOST CONTRADICTORY fact. Impossible to categorize.",
  "tone": "Provocative question — 'Genius or monster?'",
  "example": "He saved millions. Then designed the gas that killed thousands."
}
```

### Framework: Bước Ngoặt
```json
{
  "method": "Open at THE MOMENT — vivid sensory detail. FREEZE. Then rewind.",
  "tone": "Cinematic, tense, almost real-time — then sudden stop.",
  "example": "July 16, 1945. 5:29 AM. The desert is silent. Oppenheimer stares..."
}
```

### Framework: Sử Thi
```json
{
  "method": "Open with MODERN IMPACT — a fact about TODAY. 'To understand why...'",
  "tone": "Awe-inspiring, grand scale — 'This person shaped your world.'",
  "example": "Every time you use a compass... 500 years ago, his ships carried 170 men."
}
```

### Framework: Bản Án
```json
{
  "method": "Open with the CONTRIBUTION — something audience uses every day. Then: destroyed.",
  "tone": "Warm admiration → sudden cold fact about their fate.",
  "example": "Every surgeon washes hands. His protocol. 3M lives/year. Reward? Asylum."
}
```

### Framework: Kẻ Xét Lại
```json
{
  "method": "Open with WORST thing people believe. Confidently. Then: 'what if propaganda?'",
  "tone": "Confident villain narrative → sharp pivot.",
  "example": "Nero burned Rome. Murdered his mother. Insane. Problem: none of it is true."
}
```

> [!WARNING]
> ### XUNG ĐỘT: Writer Prompt vs Style JSON
> 
> Writer prompt nói **"COLD OPEN — No context. No introduction."**
> Nhưng style JSON cho Sử Thi và Bản Án lại nói **"Open with MODERN IMPACT"** / **"Open with the CONTRIBUTION"** — tức là CÓ giới thiệu, CÓ context.
> 
> **Chỉ Bước Ngoặt thực sự dùng "No context"** (in media res). Còn lại 4/5 frameworks CẦN context/giới thiệu ở câu đầu.
> 
> ⇒ Quy tắc "No context" trong writer prompt **ĐANG GÂY HẠI** cho 4/5 frameworks.

---

## 4. BATTLE — Writer Prompt (tối thiểu)

```
HOOK CHAPTER RULES (lines 150-161):
- PRIORITY: follow style guide's hook_methods
- If no hook_methods, follow framework's structure.hook
- Set up STAKES: Why does this battle matter?
- Be SPECIFIC — cite real places, dates, forces
- Do NOT analyze any battle phase yet
- Hook with vivid moment, shocking statistic, or impossible outcome
```

> [!CAUTION]
> **KHÔNG CÓ** cấu trúc COLD OPEN / NARRATIVE PROMISE / CURIOSITY GAP.
> **KHÔNG CÓ** hook types (PARADOX, IN MEDIA RES, etc.).
> **KHÔNG CÓ** anti-patterns.
> 
> AI viết hook cho battle hoàn toàn PHỤ THUỘC vào style JSON framework.

---

## 5. MYSTERY — Writer Prompt (tối thiểu)

```
HOOK CHAPTER RULES (lines 236-245):
- Follow framework's hook method (Paradox Drop, Crime Scene, Timeline Break)
- Establish CENTRAL PARADOX / IMPOSSIBLE FACT in first 60 seconds
- NO deep analysis — just shocking/impossible fact
- Be SPECIFIC — cite real evidence
- Plant MASTER OPEN LOOP
- If flash-forward framework: show CONSEQUENCE first, then rewind
```

> [!NOTE]
> Mystery prompt **ủy thác hoàn toàn cho style JSON** — chỉ nói "follow framework's hook method". Không có cấu trúc riêng.

---

## 6. Ma trận tổng hợp: Hook Type × Framework

| Framework | Hook Method | Cần Context? | Writer Prompt Coverage |
|---|---|:---:|---|
| **Hai Mặt** | Contradictory fact | ✅ CẦN (establish legend first) | ⚠️ Writer nói "no context" |
| **Bước Ngoặt** | In media res → freeze → rewind | ❌ KHÔNG (drop vào scene) | ✅ Phù hợp |
| **Sử Thi** | Modern impact → rewind | ✅ CẦN (di sản hiện đại) | ⚠️ Writer nói "no context" |
| **Bản Án** | Contribution → fate twist | ✅ CẦN (giới thiệu đóng góp) | ⚠️ Writer nói "no context" |
| **Kẻ Xét Lại** | Villain narrative → pivot | ✅ CẦN (present what people believe) | ⚠️ Writer nói "no context" |

---

## 7. Vấn đề phát hiện

### A. XUNG ĐỘT "No Context" (Nghiêm trọng)

Writer prompt biography áp quy tắc "No context. No introduction." cho TẤT CẢ hook types. Nhưng chỉ **Bước Ngoặt** thực sự dùng kiểu "no context" (in media res). Các framework khác CẦN context:

- **Sử Thi**: Cần nói "ngày nay, mỗi khi bạn dùng GPS..." → context
- **Bản Án**: Cần nói "mỗi khi bác sĩ rửa tay..." → context  
- **Kẻ Xét Lại**: Cần nói "Nero đốt Rome, giết mẹ..." → context (villain narrative)
- **Hai Mặt**: Cần nói "Ông cứu triệu người..." → context (legend version)

**Hậu quả**: AI đọc "no context" → viết kiểu Van Gogh: ném vào scene nhà vàng mà khán giả không biết gì.

### B. Battle & Mystery thiếu hướng dẫn hook (Trung bình)

Cả 2 chỉ có ~10 dòng hook rules, so với biography có ~50 dòng. AI phải tự suy luận từ style JSON.

### C. Không có giới hạn độ dài cho scene IN MEDIA RES (Nghiêm trọng)

Writer prompt nói "COLD OPEN = 1-3 sentences" nhưng khi AI chọn IN MEDIA RES, nó viết cả **cảnh tiểu thuyết 15+ câu** vì không có giới hạn cụ thể cho scene length.

### D. "NARRATIVE PROMISE" nghe giảng bài

Block 2 ("Briefly establish WHO + WHY their story matters NOW") thường tạo ra đoạn giới thiệu formal kiểu Wikipedia, vì tên "NARRATIVE PROMISE" ám chỉ cần bày tỏ promise. Competitor channels dùng **TWIST** (lật ngược) thay vì "promise" (hứa hẹn).

---

## 8. Đề xuất: Cấu trúc Hook thống nhất (tham khảo)

Dựa trên competitor (kênh channel doi thu/4) và phân tích framework:

```
HOOK CHAPTER STRUCTURE (thay thế cái cũ):

1. ANCHOR (2-4 câu): 
   Bắt đầu bằng thứ khán giả ĐÃ BIẾT hoặc CÓ THỂ HÌNH DUNG.
   → Hai Mặt: fact nổi tiếng nhất (legend)
   → Bước Ngoặt: scene crisis (in media res)
   → Sử Thi: di sản hiện đại
   → Bản Án: đóng góp hàng ngày
   → Kẻ Xét Lại: villain narrative
   
2. TWIST (2-4 câu):
   Lật ngược ANCHOR bằng fact bất ngờ / mâu thuẫn.
   → Hai Mặt: "But this same person..."
   → Bước Ngoặt: FREEZE → "To understand this moment..."
   → Sử Thi: "But 500 years ago, nobody knew his name."
   → Bản Án: "His reward? They destroyed him."
   → Kẻ Xét Lại: "But what if none of this is true?"

3. QUESTION (1-2 câu):
   Câu hỏi trung tâm cho toàn video.

4. ROADMAP (2-3 câu, TÙY CHỌN):
   Tease 2-3 milestones — KHÔNG spoil.
```

**Khác biệt chính so với hiện tại:**
- **ANCHOR thay COLD OPEN**: Bỏ "no context" → mỗi framework có opening type riêng
- **TWIST thay NARRATIVE PROMISE**: Lật ngược thay vì giới thiệu
- **Mỗi framework mapping rõ ràng**: AI biết chính xác ANCHOR type nào cho framework nào
- **Áp dụng cho TẤT CẢ niches**: Không chỉ biography

