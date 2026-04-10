# Mystery History Pipeline v2 — Walkthrough

## Tổng quan
Nâng cấp chất lượng viết dựa trên feedback thực tế từ kịch bản "10 Terrifying Ancient Weapons."

## Files đã sửa

### 1. [system_mystery_outline.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_mystery_outline.txt)
- **Macro Tone Arc**: Xếp mystery theo sóng hình sin (Banger → Fascinator → Creep → Epic → Philosophical → Echo)
- **3 fields mới**: `tone_slot`, `chapter_structure`, `closing_type` — outline assign sẵn, writer follow
- **7 chapter structures** mô tả chi tiết khi nào dùng
- **4 closing types** + constraint: không 2 chương liên tiếp cùng structure/closing
- CTA `callback_theme` thay `cumulative_callback_items` (callback by theme, không liệt kê tên)

### 2. [system_write_review_mystery.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_write_review_mystery.txt)
- **7 Structures** thay Pattern A/B/C/D — mỗi structure có flow + best-for khác nhau
- **4 Closing types** thay "luôn 3 câu hỏi tu từ"
- **2nd-person POV** dựa trên nội dung (không theo tỷ lệ cố định)
- **Pivot Blacklist**: cấm "This/That explanation, however" lặp, 6 alternatives cụ thể
- **Feynman Vocabulary Control**: analogy ngay sau thuật ngữ khó
- **Echo Outro**: callback by theme, kéo về hiện tại

### 3. [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)
- 3 `.replace()` mới: `{tone_slot}`, `{chapter_structure}`, `{closing_type}`

### 4. [system_extract_blueprint_mystery.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_extract_blueprint_mystery.txt)
- Cấm extract analogies/metaphors/rhetorical comparisons
- `comparisons` field chỉ ghi factual comparison, không copy câu so sánh

### 5. [system_review_cross_chapter_mystery.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_review_cross_chapter_mystery.txt)
- 4 checks mới: pivot diversity, closing variety, 2nd-person context, vocabulary density

### 6. [Review_bí_ẩn_lịch_sử.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/Review_bí_ẩn_lịch_sử.json)
- `transitions`: cập nhật cho 4 closing types + Echo outro
- `checklist`: bỏ "luôn kết bằng câu hỏi tu từ", thay bằng luân phiên 4 loại

## Verification
- ✅ Compile check: `rewriter.py` + `rewrite_style_tab.py` OK
- ✅ JSON validity: `Review_bí_ẩn_lịch_sử.json` parsed OK
- ⏳ Test thủ công: cần chạy pipeline lại để so sánh output v1 vs v2
