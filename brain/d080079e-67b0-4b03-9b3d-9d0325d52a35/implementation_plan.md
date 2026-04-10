# Price Enrichment via Google Search

Thêm bước **tra cứu giá thực tế mới nhất** (US street price) vào pipeline Top/List Review, sử dụng Google Search Grounding.

## Vị trí trong pipeline

```
Step 3: extract_blueprint_review()     ← Lấy product data từ script
Step 5: reality_check_blueprint()      ← Kiểm tra/enrich data bằng AI knowledge
  ↓
★ NEW STEP: enrich_prices_google()     ← Tra giá thực tế qua Google Search
  ↓
Step 6: check_blueprint()              ← Kiểm tra completeness
```

## Proposed Changes

### [NEW] `enrich_prices_google()` trong [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

Hàm mới nhận `blueprint` → duyệt qua `product_evaluation` → gửi prompt kèm `google_search=True` cho từng sản phẩm (hoặc batch) → trả về blueprint đã cập nhật giá.

**Logic:**
1. Lấy danh sách product từ `blueprint["product_evaluation"]`
2. Gửi 1 request duy nhất (batch tất cả products) với `google_search=True`:
   - *"Look up current US street price (March 2026) for these firearms: [list]. Return one estimated price each."*
3. So sánh giá search được vs giá trong `key_claims` / blueprint
4. Cập nhật trường `street_price_usd` + `price_source` + `price_date` vào mỗi product
5. Trả về blueprint đã enriched

### [MODIFY] [rewrite_style_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_style_tab.py)

- Chèn step mới **sau Step 5** (reality check, dòng ~2906) và **trước Step 6**
- Cần Gemini API key → đọc từ config hoặc chat_tab
- Tổng pipeline chuyển từ 12 → 13 steps
- Lưu kết quả vào `_price_enrichment.json` trong `_pipeline/`

### [MODIFY] Config / Settings

- Thêm ô **Gemini API Key** vào Settings dialog hoặc lưu riêng
- Thêm checkbox **💰 Price Check** trên thanh action của Style Rewrite tab (bật/tắt)

## Verification Plan

1. Chạy pipeline Top/List Review với 1 folder có niche súng đạn
2. Kiểm tra `_pipeline/_price_enrichment.json` có giá cập nhật
3. So sánh giá trong blueprint trước/sau enrichment
