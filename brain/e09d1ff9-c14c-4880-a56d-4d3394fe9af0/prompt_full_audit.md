# POV Prompt — Full Audit (Prompt + Style JSON)

Analyzed from actual prompt sent to AI: `ch01_prompt_debug.txt` (991 lines)

## A. REDUNDANCIES — Rules nói 2-3 lần

| # | Rule | Style JSON | Prompt | Lãng phí |
|---|---|---|---|---|
| 1 | POV second person | `pov_rules` (line 46) | Section 1 (759-765) | ~10 lines |
| 2 | No narrator voice | `zero_narrator_rule` (line 52) | FORBIDDEN VOICES (767-774) | ~8 lines |
| 3 | Sentence rhythm 4 patterns | `sentence_rhythm` (line 42) | Lines 869-874 | ~6 lines |
| 4 | Sentence length | `sentence_style` (line 88) | Line 876 | ~1 line |
| 5 | Action verbs / body-not-emotion | `vocabulary` (line 43) | Lines 852-867 | ~16 lines |
| 6 | Opening styles | `body_chapter_opening` (line 96) | Section 2 (777-801) | ~25 lines |
| 7 | Closing types | `chapter_ending_protocol` (line 51) | Section 4B (912-934) | ~23 lines |
| 8 | No context paragraphs | `tone` (line 41) | Lines 860-863 | ~4 lines |
| 9 | Anti-framework leak | `anti_framework_leak` (line 49) | Lines 970-976 | ~7 lines |
| 10 | Spoken rhythm | `voice_over_clarity` (line 44) | Lines 878-882 | ~5 lines |

**Total waste: ~105 lines** trùng lặp hoàn toàn.

## B. CONFLICTS — Rules mâu thuẫn nhau

| # | Rule | Style JSON nói | Prompt/User nói | Hậu quả |
|---|---|---|---|---|
| 1 | Word count | "100-200" (5 chỗ: lines 61,148,169,190,211) | User: "150 to 650" (line 990) | AI viết ~100 từ, ignore user |
| 2 | Opening styles | 5 styles kể cả COLD OPEN (line 96) | 4 styles, xóa COLD OPEN (777-801) | AI không biết COLD OPEN có hay không |
| 3 | Sentence max | "NEVER exceed 25 words" (line 88) | Kịch bản tham khảo có câu 29 từ | AI bị ép cắt câu |
| 4 | Closing types | 4 types (line 51) | 5 types, thêm ECHO (912-934) | AI không biết ECHO có trong menu không |
| 5 | Prompt line 827 | — | "The chapter is 100-200 words" (đã sửa → "Chapters are short") | Cũ: xung đột user word count |

## C. STRUCTURAL ISSUES

| # | Vấn đề | Ảnh hưởng |
|---|---|---|
| 1 | Prompt gửi AI = **991 dòng** | Quá dài, AI ưu tiên đầu/cuối, bỏ giữa |
| 2 | Style JSON = ~135 dòng JSON dense | AI phải parse 2 format khác nhau (JSON + prose) |
| 3 | Outline lặp 2 lần | 1 lần ở FULL OUTLINE (413-731), 1 lần ở YOUR CHAPTER (733-744) |
| 4 | Blueprint 12K chars | Nhiều field không liên quan đến chapter đang viết |

## D. FIX PLAN

### Nguyên tắc phân chia trách nhiệm:

```
STYLE JSON   → owns ALL style rules (rhythm, length, verbs, opening types, closing types, pacing)
PROMPT       → owns ONLY content rules that style JSON DOESN'T have
USER MESSAGE → owns word count
```

### Style JSON — CẦN SỬA:

1. **Xóa tất cả hardcoded word count** (5 chỗ):
   - Line 61: `"Body is 100-200 words of ACTION"` → `"Body is ACTION — no context paragraphs, no analysis"`
   - Line 148: `"NEVER exceed 200 words per chapter (body)"` → XÓA
   - Line 169: `"NEVER exceed 200 words per body chapter."` → XÓA
   - Line 190: `"Every chapter MUST be 100-200 words"` → XÓA
   - Line 211: duplicate → XÓA

2. **COLD OPEN**: Giữ hoặc xóa — nhưng phải THỐNG NHẤT giữa style JSON và prompt.
   Kịch bản tham khảo không dùng COLD OPEN → khuyến nghị xóa khỏi style JSON.

3. **Sentence max 25 words**: Nâng lên 30 hoặc xóa rule cứng (kịch bản tham khảo có câu 29 từ).

### Prompt — CẦN SỬA:

Giữ LẠI (unique, style JSON không có):
- ✅ Section 1: IDENTITY + POV CONTRACT (với ví dụ cụ thể)
- ✅ Section 3: CONTENT DEVELOPMENT (4 principles)
- ✅ Section 4A: CLOSING CONTENT RULE (change/lesson/cost)
- ✅ Section 5: SPECIAL CHAPTERS (Level 1 birth, End chapter echo)
- ✅ Section 6: CONSTRAINTS (foreign language, prohibitions)
- ✅ Section 7: OUTPUT

XÓA (trùng style JSON):
- ❌ Section 2: OPENING — 4 STYLES (đã có trong `body_chapter_opening`)
- ❌ WRITING STYLE RULES: body-not-emotion, numbers, context, action verbs (đã có trong `vocabulary`, `tone`)
- ❌ SENTENCE RHYTHM (đã có trong `sentence_rhythm`)
- ❌ SENTENCE LENGTH (đã có trong `sentence_style`)
- ❌ SPOKEN RHYTHM (đã có trong `voice_over_clarity`)
- ❌ Section 4B: CLOSING TYPES details (đã có trong `chapter_ending_protocol`)

### Kết quả dự kiến:

| Metric | Hiện tại | Sau fix |
|---|---|---|
| Prompt lines | ~230 | ~100 |
| Redundancies | 10 | 0 |
| Conflicts | 5 | 0 |
| Total sent to AI | ~991 lines | ~750 lines |
| Word count conflict | 6x "100-200" vs 1x user | 0x hardcode, chỉ user |
