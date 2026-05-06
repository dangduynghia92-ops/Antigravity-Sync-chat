# Fix: Data lặp across chapters (Deep Dive)

## Root Cause

**Prompt nói dối code.**

- Prompt line 1: `"You receive a FILTERED BLUEPRINT containing ONLY the data fields relevant to this specific chapter"`
- Prompt line 37: `"FILTERED BLUEPRINT (only your chapter's data)"`
- **Code thực tế** (rewriter.py line 7573): gửi `blueprint_json = json.dumps(_bp_sanitized)` — **FULL blueprint**, không filter gì.

→ AI thấy toàn bộ 22 field groups mỗi chapter → pick data "hay" bất kể thuộc chapter nào → "0.004 inch", "fuerza centrífuga", "5 fallos/1000" lặp ở ch2, ch6, ch7, ch8.

**Bằng chứng**:

| Data point | Xuất hiện ở |
|-----------|-------------|
| 0.004 inch (borde de latón) | ch2, ch6, ch8 |
| fuerza centrífuga | ch2, ch3, ch6, ch7 |
| 5 fallos/1000 | ch2, ch6, ch7, ch8 |

Trong khi outline phân chia data_focus rõ ràng:
- ch2: `casing, origin_history` — đúng chỗ cho "0.004 inch"
- ch6: `real_world_performance, compatible_platforms` — **không** nên nhắc lại "0.004 inch"

## Proposed Fix

### [MODIFY] [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

**Line ~7573**: Thêm logic filter blueprint theo `data_focus` trước khi gửi cho writer.

```python
# ── Filter blueprint by data_focus for body/topic_block chapters ──
ch_data_focus = chapter_outline.get("data_focus", [])
if ch_data_focus and chapter_type in ("body", "topic_block", "criterion"):
    _filtered_products = []
    for product in _bp_sanitized.get("product_evaluation", []):
        filtered_product = {}
        # Always keep identity fields
        for key in ("product_name", "product_type", "category", "key_specs"):
            if key in product:
                filtered_product[key] = product[key]
        # Only include field groups matching data_focus
        for field_group in ch_data_focus:
            fg_lower = field_group.lower().strip()
            for key, value in product.items():
                if fg_lower in key.lower():
                    filtered_product[key] = value
        _filtered_products.append(filtered_product)
    _filtered_bp = {**_bp_sanitized, "product_evaluation": _filtered_products}
    blueprint_json = json.dumps(_filtered_bp, ensure_ascii=False, indent=2)
```

**Logic**: 
- `data_focus: ["casing", "origin_history"]` → blueprint chỉ chứa `casing` + `origin_history` fields
- AI không thấy `real_world_performance` hay `internal_ballistics` → không lặp data từ field khác
- Giữ `product_name`, `key_specs` để AI biết context cơ bản

> [!IMPORTANT]  
> **Chỉ filter cho body/topic_block/criterion** — hook đã có slim riêng, end chapter cần full data để tổng kết.

## Verification Plan

- Chạy lại video .22 LR với code mới
- Search "0.004" / "centrífuga" / "fallos" trong output → chỉ xuất hiện ở chapter có data_focus tương ứng
