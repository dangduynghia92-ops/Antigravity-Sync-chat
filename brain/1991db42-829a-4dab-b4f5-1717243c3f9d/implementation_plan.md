# Narrative Rewrite Pipeline — Implementation Plan

Thêm chế độ **Narrative** cho thẻ Rewrite. Kịch bản dạng narrative các chapter liên kết, cần flow mượt, tránh trùng lặp nội dung giữa các chapter.

## Proposed Changes

### 1. Prompts — 3 file mới

#### [NEW] [system_narrative_outline.txt](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline.txt)
- AI đọc tất cả chapter gốc → tạo **outline tổng**: mỗi chapter gồm nội dung chính, chi tiết độc quyền, vai trò trong flow
- Output JSON: `{chapters: [{number, title, main_content, unique_details, role_in_flow}]}`

#### [NEW] [system_narrative_rewrite.txt](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_rewrite.txt)
- Giống `system_rewrite.txt` nhưng thêm:
  - `{outline}` — outline tổng toàn bộ script
  - `{previous_chapters}` — full text các chapter đã rewrite trước
  - Rule: "Không lặp nội dung đã phân tích ở chapter trước. Tham chiếu ngắn gọn nếu cần callback"

#### [NEW] [system_narrative_review.txt](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_review.txt)
- Đọc toàn bộ bản rewrite → phát hiện:
  - Trùng lặp nội dung giữa chapter (xác định chapter trọng điểm vs chapter phụ)
  - Flow đứt giữa chapter liền kề
  - Callback thiếu/thừa
- Output JSON: `{issues: [{type, chapters_involved, main_chapter, detail, severity, suggested_fix}], flow_report: "..."}`

---

### 2. Core Logic — `core/rewriter.py`

#### [MODIFY] [rewriter.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

**Thêm 4 hàm mới:**

| Hàm | Mô tả |
|-----|--------|
| `generate_narrative_outline(chapters, api, log_cb)` | Gửi tất cả chapter → nhận outline JSON |
| `rewrite_chapter_narrative(chapter, outline, prev_rewritten, api, wc_rule, log_cb)` | Rewrite 1 chapter kèm outline + full text trước |
| `review_narrative_full(all_rewritten, api, log_cb)` | Review tổng thể → trả issues |
| `patch_chapter_overlap(chapter_text, issue, full_context, api, log_cb)` | Sửa cục bộ 1 đoạn trùng |
| `merge_to_version(output_dir, version, chapters)` | Gộp chapters → `v{N}/FULL_SCRIPT.txt` |

---

### 3. UI — `ui/rewrite_tab.py`

#### [MODIFY] [rewrite_tab.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_tab.py)

**Thay đổi UI:**
- Thêm ComboBox **Mode**: `Top/List` | `Narrative` (ở hàng top, cạnh "Từ:")
- Khi chọn Narrative, nút "2. Rewrite" chạy flow mới

**Thay đổi logic:**
- `_do_rewrite_all()` — kiểm tra mode, nếu Narrative → gọi `_do_narrative_rewrite()`
- `_do_narrative_rewrite()` — chạy bước 1→6 auto trong background thread:
  1. `generate_narrative_outline()`
  2. Rewrite tuần tự (for loop, không thread pool)
  3. Verify từng chapter
  4. `review_narrative_full()` → auto `patch_chapter_overlap()` nếu có trùng
  5. `merge_to_version(output_dir, 1)` → tạo `v1/`
  6. `review_narrative_full()` lần cuối → emit signal dừng

**Dialog review kết quả:**
- Hiện sau bước 6: báo cáo issues + nút cho từng chapter có vấn đề
- Bấm "Sửa Chapter X" → AI patch → `merge_to_version(v2)` → hiện lại dialog
- Bấm "Finalize" → copy sang `final/`

---

### 4. Output Structure

```
output_dir/
├── v1/
│   ├── Chapter_1_rewritten.txt
│   ├── Chapter_2_rewritten.txt
│   └── FULL_SCRIPT.txt
├── v2/
│   ├── Chapter_5_rewritten.txt  ← sửa
│   └── FULL_SCRIPT.txt
└── final/
    ├── Chapter_1_rewritten.txt
    ├── ...
    └── FULL_SCRIPT.txt
```

---

## Verification Plan

### Manual Verification
1. Load 1 folder có 5-6 chapter narrative
2. Chọn mode Narrative → bấm "2. Rewrite"
3. Kiểm tra: outline được tạo, rewrite tuần tự, review phát hiện trùng lặp
4. Kiểm tra thư mục `v1/` có đủ file + `FULL_SCRIPT.txt`
5. Kiểm tra dialog review hiện đúng issues
6. Test sửa 1 chapter → `v2/` được tạo
7. Bấm Finalize → `final/` được tạo
