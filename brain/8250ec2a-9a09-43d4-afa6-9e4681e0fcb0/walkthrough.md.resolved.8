# Audit: Step 4 (Prompt Writer) — Output Quality

## Tổng quan
- 26 scenes, flat_prompt avg 769 chars (min 619, max 1029)
- Style prefix ✅ — tất cả đều bắt đầu bằng "A stylized historical animation..."
- Style denial suffix ✅ — "NOT photorealistic, NOT anime..." (đây là **ĐÚNG**, không phải lỗi)

---

## Phân loại Issues

### ✅ FALSE POSITIVES (không phải lỗi)
**STYLE BAN: "anime", "stick figure", "3d cgi", "photorealistic"** — 88 hits

Đây là **style denial suffix** theo yêu cầu của style file (line 40):
```
"...NOT photorealistic, NOT anime, NOT stick figures, NOT 3D CGI."
```
→ Đây là tính năng, **KHÔNG PHẢI lỗi**. LLM đang tuân thủ style file.

---

### ⚠️ REAL ISSUES (cần fix)

#### Issue 1: "tanned" vẫn leak vào flat_prompt (2 scenes)
```
SEQ_01_SCN_06: "Kurdish-Leader-A's tanned, mitten-shaped hand..."
SEQ_03_SCN_04: "Kurdish-Leader-A's tanned, mitten-shaped hands..."
```
**Nguyên nhân**: Character sheet cũ có "tanned skin on hands" → Step 4 copy vào flat_prompt.
**Fix**: Đã fix ở Step 2b (bỏ skin tone). Chạy lại sẽ hết.

#### Issue 2: "identical" trong crowd descriptions (2 scenes)
```
SEQ_02_SCN_01: "rows of identical stylized guards"
SEQ_04_SCN_01: "a row of identical Seljuk guards"
```
**Nguyên nhân**: Style file line 11 nói "identical or near-identical stylized figures". LLM copy từ style.
**Fix**: Đã discuss trước — bỏ "identical" khỏi style file. Thay bằng "uniformed" hoặc "matching".

#### Issue 3: B-Roll mô tả guards nhưng append "NO characters"
```
SEQ_04_SCN_01 flat_prompt: "...guards with round white faces stand watch..."
                          + "NO characters, NO people, NO figures — empty scene only."
```
**Xung đột nghiêm trọng**: Prompt vừa mô tả guards vừa nói "NO people" → AI sẽ bối rối.

**Root cause**: Code line 2186 check `if not p.get("characters", "").strip()` — crowd scenes có `characters=""` (vì guards không phải named characters) → code auto-append "NO characters" → sai!

**Fix cần**: Khi `has_crowd=true`, KHÔNG append "NO characters" suffix.

#### Issue 4: Label `[Seljuk-Guard-Generic]` tạo nhưng không có trong flat_prompt
```
SEQ_04_SCN_03: characters_detail có [Seljuk-Guard-Generic] nhưng flat_prompt không mention label
```
**Nguyên nhân**: LLM tự tạo label "Seljuk-Guard-Generic" cho crowd → không nằm trong AVAILABLE LABELS list. Label này sẽ không match character sheet nào.

---

## Đề xuất Fix

| # | Fix | Mức độ | File |
|---|---|---|---|
| 1 | "tanned" — đã fix ở Step 2b prompt | ✅ Done | pipeline |
| 2 | "identical" → thay bằng "uniformed" trong style file | Minor | style file |
| 3 | Code: khi `has_crowd=true`, không append "NO characters" | **Critical** | pipeline code |
| 4 | Label validation: warn nếu LLM tạo label ngoài AVAILABLE LABELS | Low | pipeline code |
