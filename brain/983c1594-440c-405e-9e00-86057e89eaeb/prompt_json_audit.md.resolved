# Audit: JSON ↔ Prompt Text Consistency

## ✅ Đã đồng bộ (không xung đột)

| Khía cạnh | Prompt text | JSON | Status |
|---|---|---|---|
| Hook flow | ANCHOR→TWIST→SCORECARD→QUESTION | `hook.anchor/twist/scorecard/question` per-fw | ✅ Khớp |
| POV SHIFT | "Read your framework's you_role" | `pov_strategy.you_role` per-fw | ✅ Khớp |
| END CHAPTER | "Read last step's lens" | `steps[last].lens` per-fw | ✅ Khớp |
| Closing types | 6 types listed (L252-269) | `closing_types[]` 5 types | ⚠️ Xem bên dưới |
| Chapter structures | 8 structures (L425-464) | `chapter_structures[]` 8 items | ✅ Khớp |
| ANTI-RECAP body (L273-278) | Rule in prompt | Không cần ở JSON | ✅ OK |
| ANTI-RECAP end (L406-410) | Rule in prompt | Không cần ở JSON | ✅ OK |
| Framework names | Không còn tên fw nào | Tên nằm trong JSON | ✅ Clean |

---

## ⚠️ Vấn đề tìm thấy

### 1. ECHO closing chỉ có trong Prompt, không có trong JSON `closing_types`

**Prompt text** (L269):
```
ECHO (end chapter only): Callback to the hook's opening image/fact. Full circle.
```

**JSON** `closing_types` (L869-889) chỉ có 5:
- `contrast_cliff`, `foreshadow_doom`, `moral_question`, `cold_fact`, `witness_testimony`

❌ **Thiếu `echo`** trong JSON. Nếu outline assign `echo` → JSON không có description.

> **Fix**: Thêm `echo` vào JSON `closing_types`.

---

### 2. JSON `openings` section (L891-921) — KHÔNG ĐƯỢC SỬ DỤNG

JSON có `openings[]` array với 5 opening types:
- `Contradiction Drop`, `Myth Destroyer`, `Frozen Moment`, `Legacy Hook`, `Contribution Contrast`, `Countdown Hook`

Nhưng prompt text **KHÔNG bao giờ reference** array này. Hook chapter section chỉ dùng flow 4 bước ANCHOR→TWIST→SCORECARD→QUESTION.

Mỗi framework có `opening_closing_fit.best_openings` trỏ vào array này (ví dụ Hai Mặt: best_openings = ["Contradiction Drop", "Myth Destroyer"]) — nhưng **không ai gọi đến field này trong prompt writer**.

> **Rủi ro**: Nếu AI đọc `openings[]` + `best_openings` → nó có thể follow THOSE rules thay vì ANCHOR→TWIST→SCORECARD→QUESTION → xung đột.
>
> **Fix options**:
> - A) Bỏ `openings[]` array và `opening_closing_fit.best_openings` khỏi JSON — hook flow nằm hoàn toàn ở `hook.anchor/twist/scorecard/question` rồi.
> - B) Map openings vào anchor content — nhưng phức tạp không cần thiết.

---

### 3. JSON `closings` array (L923-948) — CÓ THỂ CONFLICT với `closing_types`

JSON có 2 sections:
- `closing_types[]` (L869-889): 5 types dùng cho body chapter endings
- `closings[]` (L923-948): 5 closings với technique descriptions

Hai array này **overlap nhưng khác tên**:

| `closing_types` | `closings` | Giống? |
|---|---|---|
| `contrast_cliff` | — | ❌ Không có |
| `foreshadow_doom` | — | ❌ Không có |
| `moral_question` | `Moral Mirror` | 🟡 Tương tự |
| `cold_fact` | `Cold Fact` (missing) | ❌ Không có |
| `witness_testimony` | — | ❌ Không có |
| — | `Echo Callback` | End-only |
| — | `Trao Quyền Cho Khán Giả` | Riêng |
| — | `Legacy Question` | Riêng |
| — | `Debt Unpaid` | Riêng |

> **Rủi ro**: AI thấy 2 arrays khác tên cho cùng 1 việc (chapter endings) → không biết follow cái nào.
>
> **Fix**: Merge `closings` vào `closing_types` hoặc bỏ `closings` array.

---

### 4. Prompt Example vẫn dùng framework name (L349, L358)

```
Example (Bản Án — Semmelweis):
Example (Sự Lụi Tàn — Napoleon):
```

**Không phải xung đột** — chỉ là label cho example. Nhưng nếu muốn 100% clean, có thể đổi thành:
```
Example (Semmelweis):
Example (Napoleon):
```

> **Severity**: Thấp — không ảnh hưởng logic.

---

### 5. Prompt `DUAL NATURE` section (L478-486) — Nằm ngoài framework control

```
If `dual_nature_aspect` is "light": emphasize achievements — but hint at shadows
If `dual_nature_aspect` is "dark": emphasize flaws — but acknowledge strengths
If `dual_nature_aspect` is "both": present both sides
```

Đây là logic chung, áp dụng cho mọi framework. Nhưng `dual_nature_aspect` field **chủ yếu relevant cho Hai Mặt** framework. Với Sử Thi hay Bản Án, field này thường null.

> **Severity**: Thấp — prompt xử lý OK (nếu null thì bỏ qua).

---

### 6. Prompt `HOW TO CHOOSE CONTENT` (L295-304) — Có thể conflict với JSON `hook.anchor`

Prompt nói:
```
Do NOT pick the "correct" fact — pick the MOST EXTREME version of it.
Use: extreme NUMBERS, absurd IRONY, specific PHYSICAL DETAILS.
```

JSON `hook.anchor` cho Sử Thi nói:
```
"The subject's NAME or a modern fact directly tied to them"
```

**Nhẹ conflict**: Prompt nói "most extreme" nhưng JSON cho Sử Thi nói "NAME or modern fact" — có thể tên không phải extreme. 

> **Severity**: Thấp — "HOW TO CHOOSE" section là kỹ thuật bổ trợ, không ngược hướng.

---

## 🔴 Tổng kết — 3 vấn đề cần fix ngay

| # | Vấn đề | Severity | Fix |
|---|---|---|---|
| 1 | Thiếu `echo` trong JSON `closing_types` | 🔴 High | Thêm |
| 2 | JSON `openings[]` + `best_openings` conflict với hook 4-step | 🔴 High | Bỏ `openings[]` và `best_openings` |
| 3 | JSON `closings[]` overlap với `closing_types[]` | 🟡 Medium | Merge hoặc bỏ |
| 4 | Example labels dùng tên fw | 🟢 Low | Optional |
| 5 | `dual_nature` section scope | 🟢 Low | OK |
| 6 | "Most extreme" vs specific anchor guide | 🟢 Low | OK |
