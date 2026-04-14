# Conflict Audit: `system_narrative_write_pirate.txt`

Phân tích 552 dòng – tìm mâu thuẫn, xung đột, trùng lặp giữa các rules.

---

## 🔴 XUNG ĐỘT THỰC SỰ (cần sửa)

### Conflict 1: LOCALIZATION vs REQUIRED ELEMENTS example
**Lines:** L368-370 vs L514-517

L368 example:
> "Đại bác 18 pound bắn viên sắt **nặng 8 kg** ở tốc độ **400m/s**. Ở cự ly **50 yard**..."

L514 rule:
> "DYNAMIC CONVERSION: Convert general measurements to standard system of {lang}"

**Conflict**: Example dùng **hỗn hợp** metric ("8 kg", "400m/s") + imperial ("50 yard") + proper noun ("18 pound"). Nếu `{lang}` = Vietnamese thì "50 yard" phải convert → "45 mét". Nhưng "18 pound" giữ nguyên vì PROPER NOUN.

**Severity**: ⚠️ Medium — example cũ gây confused cho AI
**Fix**: Sửa example thành: `"Ở cự ly khoảng 45 mét, viên đạn xuyên qua gỗ sồi..."` (metric) nhưng giữ "18 pound" (proper noun)

---

### Conflict 2: FOREIGN LANGUAGE "Maritime terms → translate" vs LOCALIZATION "NAUTICAL TERMS: Keep original"
**Lines:** L502 vs L525-527

L502:
> "Maritime terms → translate or describe by action/result"

L525:
> "NAUTICAL TERMS: Keep original + explain ONCE on first use"

**Conflict**: L502 says **translate** maritime terms. L525 says **keep original** + explain. Which wins for "knot", "fathom", "broadside"?

**Severity**: 🔴 High — directly contradictory
**Fix**: L502 cần clarify: "Maritime terms → translate or **keep original + explain** (see LOCALIZATION section)". Hoặc remove L502 vì LOCALIZATION rule đã cover.

---

### Conflict 3: PHASE WRITING STYLE "Longer sentences for context" vs SPOKEN RHYTHM "ONE IDEA PER SENTENCE"
**Lines:** L150 vs L443

L150 (Bối Cảnh phase):
> "Longer sentences for context, explanation of world state"

L443 (Spoken Rhythm):
> "ONE IDEA PER SENTENCE. Never pack 2 facts into 1 sentence."

**Conflict**: Bối Cảnh encourages longer, multi-layered sentences. Spoken Rhythm demands 1 idea per sentence. A "longer sentence explaining world state" almost always packs 2+ ideas.

**Severity**: ⚠️ Medium — PRIORITY ORDER (L534-535) resolves this (#2 Spoken Rhythm > phase style) but the AI may still feel confused
**Fix**: Clarify L150: "Longer sentences for ATMOSPHERE and EXPLANATION — but still follow ONE IDEA PER SENTENCE. Long = richer sensory/contextual details, NOT multiple facts packed together."

---

## 🟡 MƠ HỒ (không mâu thuẫn nhưng có thể gây hiểu nhầm)

### Ambiguity 1: ENDS_WITH vs MICRO-HOOK — Same thing or different?
**Lines:** L103-109 vs L342-348

- **ENDS_WITH** (L103): "The `ends_with` idea is the FINAL thought. Hard cut."
- **MICRO-HOOK** (L342): "End of EVERY chapter via `ends_with` field. Tease NEXT chapter's content."

**Issue**: Both reference `ends_with` nhưng ENDS_WITH says "hard cut" (no extra teasers) while MICRO-HOOK says "tease NEXT chapter". These are conceptually the same thing — `ends_with` IS the micro-hook — but phrasing could confuse AI into thinking they're separate tasks.

**Fix**: Add 1 line to MICRO-HOOK: "The `ends_with` field IS the micro-hook. Write it, then STOP. No additional teaser after."

---

### Ambiguity 2: SCENE HIERARCHY vs STRUCTURE descriptions overlap
**Lines:** L44-75 vs L205-267

- SCENE HIERARCHY says: "main_key_data → FULL SCENE, sub_key_data → BRIDGE"
- Each STRUCTURE also defines its own flow (HEIST_SEQUENCE, MECHANICAL_AUTOPSY, etc.)

**Issue**: HEIST_SEQUENCE (L205-212) has its own mini-flow that doesn't explicitly map to main_key/sub_key. AI might follow the structure flow and ignore scene hierarchy, or vice versa.

**Not a conflict** — structures define WHAT to tell, scene hierarchy defines HOW MUCH to expand/compress. But could benefit from a clarifying line:
> "The chapter_structure defines the NARRATIVE FLOW. Scene hierarchy defines which data points get EXPANDED (main_key → scene) vs COMPRESSED (sub_key → bridge) within that flow."

---

### Ambiguity 3: HOOK "No technical specs" vs HOOK "SHOCKING FACT must be specific"
**Lines:** L407 vs L392

L407:
> "✗ Listing technical specs in the hook"

L392:
> "MUST be specific — numbers, dates, names. '40 khẩu đại bác và số vàng tương đương 400 triệu đô la'"

**Issue**: The SHOCKING FACT example literally uses a technical spec ("40 khẩu đại bác"). The anti-pattern bans "listing" specs — but the example uses ONE spec as a hook element.

**Not a real conflict** — the distinction is "listing specs" (multiple) vs "one shocking spec" (hook). But AI might over-apply the ban. Consider changing L407 to: "✗ Listing multiple technical specs in the hook (save anatomy details for body chapters)"

---

## 🟢 TRÙNG LẶP (có thể giảm tải)

### Redundancy 1: ANTI-REPETITION stated 3 times
- **MONEY ANGLE** (L316-319): "If a dollar figure was already stated... do NOT restate it"
- **ANTI-HERO ENGINE** (L334): "Later chapters do NOT re-explain"
- **UNIVERSAL RULES #15** (L487-493): Full ANTI-REPETITION section

These 3 all say the same thing: don't repeat. UNIVERSAL #15 is the comprehensive version; the other two are niche-specific reminders that overlap.

**Severity**: 🟢 Low — redundancy doesn't hurt, just adds prompt length
**Not urgent** — but could simplify if prompt token count becomes an issue.

---

### Redundancy 2: "Listener cannot rewind" stated 3 times
- L100: "The listener has no memory of the previous chapter's last word"
- L115: "The listener cannot rewind"
- L430: "Every sentence will be heard ONCE. The listener cannot rewind"

**Severity**: 🟢 Low — actually useful as reinforcement

---

## ✅ KHÔNG CÓ XUNG ĐỘT

Các cặp rule sau đã được xác nhận **KHÔNG conflict**:

| Rule A | Rule B | Tại sao OK |
|--------|--------|-----------|
| SURVIVAL_LENS limit (1 chapter) | PIRATE MEDICINE scope (Góc Khuất only) | Cùng nói 1 việc — consistent |
| QUESTION ENGINE (answer + open) | ENDS_WITH (hard cut) | question_opened lives INSIDE ends_with |
| CONJUNCTION BAN (no "But" opening) | MICRO-HOOK examples ("Nhưng...") | Micro-hook is at END, conjunction ban is at START |
| BEFORE/AFTER CONTRAST (L372) | TIMELINE FLOW cause→effect (L117) | Different purposes — contrast is dramatic, timeline is clarity |
| BALANCE RULE (L486) | ANTI-HERO ENGINE (L330) | Both about balance — UNIVERSAL #14 is the general, ANTI-HERO is specific scoping |

---

## 📋 TÓM TẮT & ĐỀ XUẤT

| # | Issue | Severity | Fix |
|---|-------|----------|-----|
| 1 | Example L368 mixes units | ⚠️ Medium | Update example to use consistent metric |
| 2 | L502 "translate maritime" vs L525 "keep nautical" | 🔴 **High** | Align L502 with LOCALIZATION section |
| 3 | L150 "longer sentences" vs L443 "one idea" | ⚠️ Medium | Clarify L150 meaning |
| 4 | ENDS_WITH vs MICRO-HOOK ambiguity | 🟡 Low | Add clarifying line |
| 5 | HOOK "no specs" vs "specific numbers" | 🟡 Low | Change "listing" to "listing multiple" |
