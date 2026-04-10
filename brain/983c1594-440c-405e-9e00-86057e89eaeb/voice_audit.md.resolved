# Audit: Văn Phong — "Write for Ear" vs Output Thực Tế

## Kết Luận Trước

> [!WARNING]
> Output hiện tại viết **rất tốt cho đọc** nhưng **chưa tối ưu cho nghe**. Tone giữa "literary essay" và "documentary narration" — hơi nghiêng về essay. Prompt hiện tại KHÔNG có hướng dẫn nào về "write for ear".

---

## 1. Những Gì ĐÃ TỐT (Phù Hợp YTB)

| Kỹ thuật | Ví dụ từ output | Đánh giá |
|---|---|---|
| Câu ngắn impact | "He failed." (ch2 dòng 21) | ✅ Rất tốt |
| Show don't tell | Compass scene, Mileva list scene | ✅ Xuất sắc |
| Rhetorical question | "How could they?" (ch2) | ✅ Có nhưng ít |
| Direct address | "Imagine it. You are fifteen." (ch2 dòng 15) | ✅ Rất hiệu quả |
| Cold fact closing | "the FBI amassed a file...1,427 pages long" | ✅ Gọn, impact |

---

## 2. Những Gì CÓ VẤN ĐỀ

### 2.1 Câu quá dài cho tai nghe

> [!CAUTION]
> Nhiều câu 40-60 từ — reader có thể đọc lại, listener KHÔNG THỂ.

**Ví dụ xấu (ch5 dòng 1):**
> "The quest began not with an equation, but with a daydream. It was 1907, and he was still at the patent office in Bern. He imagined a man falling from the roof of a house. In that terrifying freefall, the man would not feel his own weight. If he were to empty his pockets, the keys and coins would float beside him, weightless."

→ OK ở đoạn đầu. Nhưng sau đó:

> "This was his principle of equivalence, the cornerstone of his new theory. But turning this beautiful thought into a rigorous mathematical theory would become an eight-year odyssey, a descent into an intellectual hell that would push him to the brink of madness and break his body."

→ **68 từ 1 câu!** Tai nghe bị overload. Nên tách:
> "This was his principle of equivalence. The cornerstone of his new theory. But turning this beautiful thought into mathematics? That would take eight years. Eight years that nearly broke him."

### 2.2 Từ vựng hàn lâm — không phù hợp tai nghe

| Từ/Cụm | Xuất hiện | Vấn đề | Thay thế |
|---|---|---|---|
| "indistinguishable" | ch5 | Khó nghe | "the same thing" |
| "axioms" | ch2 | Thuật ngữ | cắt hoặc giải thích |
| "arcane discipline of tensor calculus" | ch5 | Academic | "a math so complex..." |
| "deterministic reality" | ch7 | Academic | "a universe that follows rules" |
| "precession" | ch5 | Jargon | "a tiny wobble" (đã có) |
| "abdication of science's highest purpose" | ch7 | Literary | quá trang trọng |
| "gilded cage" | ch7 | Literary metaphor | OK nếu giải thích |

### 2.3 Đoạn quá dài — không có "breath points"

**ch5 dòng 21** = 1 đoạn duy nhất mô tả cả quá trình General Relativity: 
- November 1915 sprint → race with Hilbert → 4 lectures → Mercury orbit → "heart palpitate"
- **160 từ liền 1 paragraph!** → listener mất theo dõi

**Rule cho YTB**: Mỗi đoạn nên **≤ 80 từ** (khoảng 30s đọc). Nếu dài hơn = tách.

### 2.4 Thiếu "conversational markers"

Prompt hiện tại KHÔNG có hướng dẫn về:
- **Breath pauses**: "..." hoặc câu 1-2 từ giữa đoạn dài
- **Listener anchoring**: "Here's the thing.", "Think about that.", "And that's the key."
- **Recap/orientation**: Khi jump thời gian, listener cần "So now it's 1914..."
- **Spoken rhythm**: viết để ĐỌC THÀNH TIẾNG, không phải để in trên giấy

---

## 3. Phân Tích Prompt: Thiếu Gì?

### Prompt hiện tại có:
```
- "Speak directly to the listener — as if sharing a secret"
- "Use SHORT sentences for impact"
- "Anti-pattern: Wikipedia vs documentary voiceover"
```

### Prompt hiện tại THIẾU:

| Rule cần thêm | Lý do |
|---|---|
| **MAX SENTENCE LENGTH** | Không rule → AI viết câu 60+ từ |
| **PARAGRAPH LENGTH** | Không rule → đoạn 150+ từ |
| **SPOKEN LANGUAGE** | Không distinction "written" vs "spoken" |
| **BREATH POINTS** | Không yêu cầu pauses |
| **JARGON BAN** | Không cấm thuật ngữ chuyên ngành |
| **TIME ORIENTATION** | Không hướng dẫn khi jump thời gian |

---

## 4. Đề Xuất Thêm Vào Prompt

Thêm section **"WRITE FOR EAR"** ngay sau VOICE AND EMOTIONAL REGISTER:

```
═══════════════════════════════════════
WRITE FOR EAR (THIS IS A SPOKEN SCRIPT)
═══════════════════════════════════════

This text will be READ ALOUD. Every sentence must sound natural 
when spoken. Apply these rules without exception:

1. SENTENCE LENGTH: Max 25 words per sentence. If longer, split it. 
   The audience cannot rewind. They hear it once.
   BAD: "The principle of equivalence, which states that gravitational 
   and inertial mass are indistinguishable, became the cornerstone 
   of his general theory."
   GOOD: "He had one simple idea. Gravity and acceleration — they're 
   the same thing. That one idea changed everything."

2. PARAGRAPH LENGTH: Max 80 words per paragraph (≈30 seconds of 
   speech). Break long passages with a line break.

3. NO ACADEMIC JARGON: If a term requires a dictionary, replace it 
   or explain it immediately in the SAME sentence.
   BAD: "the arcane discipline of tensor calculus"
   GOOD: "a kind of math so complex it could describe curved space"

4. BREATH POINTS: After a dense or emotional passage, insert a 
   short "landing" sentence (1-5 words) before moving on.
   Examples: "That was the end.", "He was alone.", 
   "Nobody knew.", "And then — silence."

5. TIME ANCHORING: When jumping between years, orient the listener 
   with a clear time marker at the start.
   BAD: "His star was rising. The papers had finally broken through."
   GOOD: "By 1909, his star was rising."

6. READ ALOUD TEST: After writing, imagine reading every sentence 
   out loud in one breath. If you run out of breath, the sentence 
   is too long. Split it.
```

---

## 5. Tóm Tắt

| Hạng mục | Hiện tại | Sau khi fix |
|---|---|---|
| Sentence length | ❌ nhiều câu 40-60 từ | ✅ max 25 từ |
| Paragraph length | ❌ nhiều đoạn 120-160 từ | ✅ max 80 từ |
| Jargon | ⚠️ Có thuật ngữ academic | ✅ Cấm hoặc giải thích ngay |
| Breath points | ❌ Không có | ✅ Bắt buộc |
| Time anchoring | ⚠️ Thiếu nhất quán | ✅ Rule rõ ràng |
| Conversational tone | ⚠️ Giữa essay/narration | ✅ Spoken script |
