# Điều tra: Verify Loop lặp vô ích & Audit Outline fail JSON

## Bug 1: Verify Loop — 3 lần re-split cho kết quả giống hệt nhau

### Root Cause

Verify loop nằm ở [auto_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/auto_pipeline.py#L451-L490):

```python
for _verify_attempt in range(3):  # 0=first verify, 1-2=retries
    verify_result = verify_chapters(chapters, full_text, api, ...)
    issues = verify_result.get("issues", [])
    if not issues:
        break
    if _verify_attempt >= 2:
        break  # Max re-split attempts reached
    
    # Re-split with feedback
    chapters = split_chapters(lines, ..., verification_feedback=feedback, ...)
```

**Vấn đề 1: `verify_chapters()` gửi ~42,000 chars lên API**

[verify_chapters()](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/chapter_splitter.py#L737-L784) gửi **original_text + tất cả chapter contents** = text gốc 20,939 chars × 2 lần (1 lần nguyên bản + 1 lần chia ra). Mỗi lần verify mất **100-120 giây** cho tier `pro`.

**Vấn đề 2: Re-split trả kết quả giống hệt vì marker-based splitting là deterministic**

Khi re-split, hàm `split_chapters()` gửi verification feedback nhưng AI vẫn trả lại **cùng các `start_marker` giống hệt cũ**. Sau đó `_split_by_markers()` tìm marker trong full_text → cùng vị trí → cùng kết quả.

Điều này xảy ra vì:
- Script gốc **không thay đổi** — marker positions cố định trong text
- AI trả lại cùng markers vì đó thực sự là **ranh giới nội dung hợp lý nhất** trong text
- Issue mà verifier phát hiện (ngắt giữa câu ở Ch10/Ch11 boundary) **không thể sửa bằng cách chọn marker khác** — vì đoạn text gốc chứa `[music]` giữa 2 câu, tạo ranh giới "tự nhiên nhất" mà AI luôn chọn

**Vấn đề 3: Verify quá strict — nitpick những issue không ảnh hưởng rewrite**

Issues mà verifier tìm ra ("tiêu đề không khớp chính tả với bản gốc", "1 câu nằm sát ranh giới 2 chương") là cosmetic issues không ảnh hưởng đến pipeline rewrite — vì rewrite **không dùng chapter titles gốc**, mà tạo outline mới hoàn toàn.

### Tổng thiệt hại
- 3 lần verify × ~100s = ~300s (5 phút)
- 2 lần re-split × ~45s = ~90s (1.5 phút)
- **Tổng: ~6.5 phút lãng phí**. Lần verify đầu (tốn 100s) là cần thiết, nhưng 2 lần re-split + re-verify là vô ích.

---

## Bug 2: Audit Outline — JSON parse fail 100%

### Root Cause

[audit_outline_review()](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py#L1412-L1483) gửi input **rất lớn** cho `gemini-3-flash-preview`:

```python
user_content = (
    f"BLUEPRINT:\n{json.dumps(blueprint, indent=2)}\n\n"   # ~ 15-30 KB
    f"OUTLINE:\n{json.dumps(outline, indent=2)}\n\n"       # ~ 5-10 KB  
    f"FRAMEWORK:\n{json.dumps(framework, indent=2)}\n\n"   # ~ 2-5 KB
    f"STYLE GUIDE:\n{style_json}"                          # ~ 10-15 KB style JSON
)
```

Yêu cầu trả về:
```json
{
  "audit_issues": [...],
  "outline": { ... cả outline đầy đủ ... }
}
```

**Vấn đề: Yêu cầu AI "echo" lại toàn bộ outline (5-10 KB JSON) trong output**

Prompt yêu cầu trả lại **cả outline gốc** (dù có sửa hay không). Với 10 chapters, mỗi chapter có ~500 bytes metadata → outline output ~5-10KB. Khi kết hợp với audit_issues → output JSON rất lớn → **flash model sinh JSON dài bị truncated hoặc chứa lỗi cú pháp**.

Error cụ thể: `Expecting ',' delimiter: line 134 column 8 (char 8730)` — line 134 trong JSON output = AI đang viết một object rất dài và mắc lỗi cú pháp ở giữa.

**Tại sao mỗi audit mất ~5 phút?**
- Input: ~40-60 KB text
- Output yêu cầu: ~5-10 KB JSON (echo lại outline + audit issues)
- Model: `flash` — nhưng phải generate nhiều output tokens cho một task đơn giản
- timeout=500 (500s) → model dùng hết thời gian suy nghĩ

### Tổng thiệt hại
- 2 lần audit (v1 + v2) × ~5 phút = ~10 phút
- Cả 2 đều fail JSON → kết quả bị bỏ → **hoàn toàn lãng phí**

---

## Proposed Fixes

### Fix 1: Smart Verify Loop — phát hiện sớm khi re-split không thay đổi gì

> [!IMPORTANT]
> Sau mỗi re-split, so sánh marker positions mới vs cũ. Nếu giống → dừng ngay, không verify lại.

#### [MODIFY] [auto_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/auto_pipeline.py#L451-L490)

Thêm logic so sánh chapter positions trước khi verify lại:
```python
prev_positions = [(ch.start_index, ch.end_index) for ch in chapters]

# After re-split:
new_positions = [(ch.start_index, ch.end_index) for ch in chapters]
if new_positions == prev_positions:
    self._log("[Phase 2] Re-split produced identical results — skipping re-verify")
    break
```

**Tiết kiệm: ~5 phút** (loại bỏ 2 lần verify + 1 lần re-split vô ích)

### Fix 2: Audit Outline — không yêu cầu echo lại outline nếu no issues

Hai lựa chọn:

#### Option A: 2-pass audit (Recommended) ⭐
1. **Pass 1 (nhẹ)**: Chỉ yêu cầu `{"audit_issues": [...]}` — không echo outline
2. **Pass 2 (chỉ khi cần)**: Nếu có issues → gửi lại chỉ outline + issues → yêu cầu trả lại outline đã sửa

#### Option B: Sửa JSON parsing — thêm retry/repair
- Nếu JSON parse fail → thử `json_repair` library hoặc regex fallback
- Vẫn tốn thời gian generate, chỉ giải quyết phần parsing

#### [MODIFY] [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py#L1412-L1483)

Implement 2-pass:
```python
# Pass 1: detect issues only (small output)
pass1_prompt = "... Respond with ONLY audit_issues array, do NOT return the outline ..."
# → output nhỏ, flash xử lý nhanh + không fail JSON

# Pass 2: fix outline (only if issues found)
if audit_issues:
    pass2_prompt = "Fix these issues in the outline: ..."
    # → đợi outline sửa
```

**Tiết kiệm: ~8 phút** (2 × ~4 phút nếu no-issues path, hoặc không fail JSON nữa)

## Open Questions

> [!IMPORTANT]
> **Option A hay B cho audit fix?** Option A (2-pass) giải quyết triệt để cả tốc độ + JSON fail. Option B chỉ giải quyết JSON fail mà vẫn chậm.

## Verification Plan

### Automated Tests
- Chạy 1 pipeline và so sánh thời gian trước/sau fix
- Kiểm tra verify loop dừng sớm khi positions giống nhau
- Kiểm tra audit trả kết quả parseable

### Manual Verification
- So sánh output quality trước/sau (audit có ảnh hưởng gì không khi bị skip)
