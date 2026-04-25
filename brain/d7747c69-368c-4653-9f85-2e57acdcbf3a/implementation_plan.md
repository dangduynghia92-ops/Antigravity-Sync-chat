# Fix: Lặp Vocabulary + Transition Sai Topic

## Bối cảnh

Hai bug trong Head-to-Head pipeline:
1. **Lặp metaphor**: "atleta de contacto" xuất hiện 3 chapter (1/3/4) vì `alternative_rhetoric` gắn theo product, không theo chapter
2. **Transition sai**: 3/6 transition nhắc topic đã cover (Ch5/6/7) vì writer không biết chapter tiếp theo

---

## Fix 1: Alternative Rhetoric — Lọc theo `data_focus`

### Nguyên nhân
`alternative_rhetoric` nằm ở cấp product. Trong H2H, mọi chapter cover cả 2 products → mọi chapter nhận **toàn bộ** alternatives → writer copy y nguyên.

### Phương án

**Code change** trong `write_review_chapter()` ở [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py) (line 6912-6928):

Thay vì broadcast tất cả alternatives, **lọc** chỉ alternatives có `data_source` liên quan đến `data_focus` của chapter hiện tại.

```diff
 # ── Build alternative_rhetoric block for writer ──
 alt_rhetoric_lines = []
+ch_data_focus = set(chapter_outline.get("data_focus", []))
 for prod_name in (products if products else []):
-    for prod in _bp_sanitized.get("product_evaluation", []):
+    for prod in blueprint.get("product_evaluation", []):
         if prod.get("product_name") == prod_name:
             alts = prod.get("alternative_rhetoric", [])
             if alts:
-                alt_rhetoric_lines.append(f"[{prod_name}]")
+                relevant_alts = []
                 for alt in alts:
                     if isinstance(alt, dict):
-                        alt_type = alt.get("type", "")
-                        alt_text = alt.get("alternative", "")
-                        if alt_text:
-                            alt_rhetoric_lines.append(f"  - ({alt_type}) USE: {alt_text}")
+                        ds = (alt.get("data_source") or "").lower()
+                        # Match if any data_focus field appears in data_source
+                        if ch_data_focus and not any(f in ds for f in ch_data_focus):
+                            continue  # Skip — not relevant to this chapter
+                        alt_type = alt.get("type", "")
+                        alt_text = alt.get("alternative", "")
+                        if alt_text:
+                            relevant_alts.append(f"  - ({alt_type}) DIRECTION: {alt_text}")
+                if relevant_alts:
+                    alt_rhetoric_lines.append(f"[{prod_name}]")
+                    alt_rhetoric_lines.extend(relevant_alts)
             break
```

**Logic**: Mỗi `alternative_rhetoric` entry có `data_source` (vd: `"energía_boca (300-400 ft-lb)"`). Mỗi chapter có `data_focus` (vd: `["cost_economics"]`). Chỉ show alternatives có `data_source` match `data_focus`.

> [!IMPORTANT]
> Cần dùng **blueprint gốc** (chưa sanitize) để đọc `data_source`, vì `_bp_sanitized` đã xóa `data_source` ở line 6823.

**Prompt change** trong [system_write_review_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_write_review_firearms_v2.txt) (line 45):

```diff
-You MUST NOT replicate these angles. Use ALTERNATIVE angles instead.
+You MUST NOT replicate these angles. Use the DIRECTION hints below to create your OWN ORIGINAL phrasing.
+NEVER copy these directions verbatim — they are STARTING POINTS, not scripts.
```

Và đổi label từ `USE:` → `DIRECTION:` trong code (đã thể hiện ở diff trên).

---

## Fix 2: Transition — Truyền `next_chapter_topic`

### Nguyên nhân
Writer prompt nói "tease next criterion" nhưng writer không biết chapter tiếp theo cover topic gì → đoán mò.

### Phương án

**Code change** trong `write_review_chapter()` ở [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py):

Hàm đã nhận `full_outline` (JSON string). Parse nó, tìm chapter `chapter_number + 1`, lấy `title` + `primary_criterion`:

```python
# ── Extract next chapter topic for transition accuracy ──
next_topic = "N/A"
try:
    _outline_data = json.loads(full_outline) if isinstance(full_outline, str) else (full_outline or {})
    _chapters_list = _outline_data.get("chapters", [])
    for _ch in _chapters_list:
        if _ch.get("chapter_number") == chapter_number + 1:
            _next_title = _ch.get("title", "")
            _next_crit = _ch.get("primary_criterion", "")
            next_topic = f"{_next_title} ({_next_crit})" if _next_crit else _next_title
            break
except Exception:
    pass
system_prompt = system_prompt.replace("{next_chapter_topic}", next_topic)
```

**Prompt change** — thêm placeholder vào [system_write_review_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_write_review_firearms_v2.txt):

Sau `{previous_context}`, thêm:

```
NEXT CHAPTER: {next_chapter_topic}
```

Và update H2H transition rule (line 172):

```diff
-H. COMEBACK TRANSITION: "But can [loser] take it back on [next criterion]?"
-   Build suspense. If the loser has been losing multiple rounds, acknowledge it
+H. COMEBACK TRANSITION: Reference the NEXT CHAPTER topic shown above.
+   "But can [loser] take it back on [next criterion from NEXT CHAPTER]?"
+   RULE: ONLY reference the topic listed in {next_chapter_topic}. Do NOT reference topics from earlier chapters.
+   If next chapter is "end"/verdict, build toward a final reckoning instead.
```

---

## Tổng hợp thay đổi

| File | Thay đổi |
|------|----------|
| `rewriter.py` line 6912-6928 | Lọc `alternative_rhetoric` theo `data_focus` match; đổi label `USE:` → `DIRECTION:` |
| `rewriter.py` (sau line 6910) | Thêm block parse `full_outline` → extract `next_chapter_topic` |
| `system_write_review_firearms_v2.txt` line 45 | Đổi instruction "Use ALTERNATIVE" → "Use DIRECTION hints, NEVER copy" |
| `system_write_review_firearms_v2.txt` line 58 | Thêm `NEXT CHAPTER: {next_chapter_topic}` |
| `system_write_review_firearms_v2.txt` line 172 | Update H2H transition rule reference `{next_chapter_topic}` |

## Verification Plan

### Manual Test
Chạy lại pipeline cho video `.22 LR vs 9mm` (Head-to-Head framework):
1. Kiểm tra `_prompts_dump` — mỗi chapter phải có `DIRECTION:` thay vì `USE:` với alternatives khác nhau
2. Grep "atleta" trong output → phải xuất hiện **tối đa 1 lần**
3. Kiểm tra transition cuối mỗi chapter → phải match topic của chapter tiếp theo
