# Narrative Rewrite Pipeline — Walkthrough

## What was implemented

Thêm chế độ **Narrative** cho thẻ Rewrite, cho phép rewrite kịch bản dạng narrative (các chapter liên kết flow).

## New Files

| File | Purpose |
|------|---------|
| [system_narrative_outline.txt](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline.txt) | Tạo outline tổng: content map, shared details, flow |
| [system_narrative_rewrite.txt](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_rewrite.txt) | Rewrite kèm context (outline + previous chapters) |
| [system_narrative_review.txt](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_review.txt) | Review full script: overlap, flow, callbacks |

## Modified Files

### [rewriter.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)
5 new functions:
- `generate_narrative_outline()` — tạo bản đồ nội dung
- `rewrite_chapter_narrative()` — rewrite tuần tự kèm context
- `review_narrative_full()` — review cross-chapter
- `patch_chapter_overlap()` — sửa cục bộ trùng lặp
- `merge_to_version()` — gộp file theo version (`v1/`, `v2/`, `final/`)

### [rewrite_tab.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_tab.py)
- Mode ComboBox: `Top/List` | `Narrative`
- `_do_narrative_rewrite()` — 6-step auto pipeline
- `_show_narrative_review_dialog()` — interactive dialog (issues + Fix/Finalize)
- `_fix_narrative_chapter()` — targeted patch + re-review cycle
- `_open_version_folder()` — mở folder version

## Flow

```
Bấm "2. Rewrite" (Narrative mode)
    │
    ├─ 🤖 Step 1: Outline tổng
    ├─ 🤖 Step 2: Rewrite tuần tự (analyze + rewrite per chapter)
    ├─ 🤖 Step 3: Verify từng chapter
    ├─ 🤖 Step 4: Cross-chapter review + auto patch
    ├─ 🤖 Step 5: Merge → v1/
    ├─ 🤖 Step 6: Final review
    │
    ⏸️ Dialog hiện: Flow Score + Issues
    │
    ├─ 📂 Open v1 → đọc FULL_SCRIPT.txt
    ├─ 🔧 Fix Ch.X → patch → v2/ → re-review → dialog
    └─ ✅ Finalize → final/
```

## Verification
- ✅ Import check passed
- ⏳ Manual test with sample chapters (requires API keys)
