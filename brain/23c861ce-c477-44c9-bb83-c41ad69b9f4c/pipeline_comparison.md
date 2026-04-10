# So sánh Pipeline: Narrative vs Top/List Review (Mystery History)

## Bảng so sánh tổng quan

| Yếu tố | Narrative (8 steps) | Top/List Review (12 steps) |
|---|---|---|
| **Mục đích** | Kể lại 1 câu chuyện/sự kiện liền mạch | Liệt kê & phân tích N bí ẩn/item riêng biệt |
| **Cấu trúc nội dung** | Linear: mở → diễn biến → kết | Modular: 1 chapter = 1 item/mystery |
| **Framework examples** | "The Investigative Deep-Dive" | "Bí Ẩn Lịch Sử" (+ 7 structures) |
| **Output** | `v1_FrameworkName/`, `v2_FrameworkName/` | `style_rewrite/` |

---

## Chi tiết từng Step

### GIAI ĐOẠN 1: THU THẬP DỮ LIỆU

| Step | Narrative | Top/List Review | **Giống?** |
|---|---|---|---|
| **Concat text** | Step 1/8 | Step 1/12 | ✅ Giống |
| **Detect framework** | Step 2/8: `detect_framework()` | Step 2/12: `detect_framework()` | ✅ Giống |
| **Extract blueprint** | Step 3/8: `extract_blueprint()` | Step 3/12: `extract_blueprint_review()` | ❌ **KHÁC** |

> [!IMPORTANT]
> **Khác biệt lớn nhất**: Blueprint structure hoàn toàn khác nhau.
> - **Narrative** dùng `system_extract_blueprint_battle.txt` → `{key_facts, key_events, battle_phases, arguments}`
> - **Review** dùng `system_extract_blueprint_mystery.txt` → `{product_evaluation[], key_figures, geography, technology_and_artifacts, scholarly_debate}`
>
> Narrative **KHÔNG CÓ** prompt extract blueprint riêng cho mystery history. Nó fallback sang `battle` niche!

---

### GIAI ĐOẠN 2: LÀM GIÀU DỮ LIỆU

| Step | Narrative | Top/List Review | **Giống?** |
|---|---|---|---|
| **Enrich** | Step 3.5: `enrich_blueprint_google()` | Step 5c: `enrich_blueprint_google()` | ✅ Giống hàm |
| **Reality check** | ❌ KHÔNG CÓ | Step 5/12: `reality_check_blueprint()` | ❌ Chỉ Review |
| **Check completeness** | ❌ KHÔNG CÓ | Step 6/12: `check_blueprint()` | ❌ Chỉ Review |
| **Convert units** | ❌ KHÔNG CÓ | Step 7/12: `convert_units()` | ❌ Chỉ Review |

> [!WARNING]
> Narrative pipeline **bỏ qua 3 bước quan trọng** (reality check, completeness, unit conversion).
> Với mystery history, reality check rất quan trọng vì AI có thể ghi sai năm, sai tên, hoặc tạo myth.

---

### GIAI ĐOẠN 3: TẠO OUTLINE

| Step | Narrative | Top/List Review | **Giống?** |
|---|---|---|---|
| **Framework selection** | Step 4/8 (auto-rank or user) | Step 4/12 (auto-select single) | ⚠️ Tương tự logic |
| **Generate outline** | Step 5: `generate_renew_outline_v2()` | Step 8: `create_review_outline()` | ❌ **KHÁC** |
| **Audit outline** | Step 6: `audit_outline()` | Step 9: `audit_outline_review()` | ❌ KHÁC hàm |

> [!NOTE]
> - **Narrative** outline: `{narrative_arc, chapters: [{title, summary, key_points, emotional_beat}]}`
> - **Review** outline: `{chapters: [{title, products_covered, chapter_structure, tone_category, closing_type, ends_with, ...}]}`
>
> Review outline **chi tiết hơn rất nhiều** — có `chapter_structure` (mythbuster, detective_trail...), `closing_type`, `tone_category`, `debate_seed`.
> 
> Narrative outline chỉ có `title, summary, key_points`.

---

### GIAI ĐOẠN 4: VIẾT KỊCH BẢN

| Step | Narrative | Top/List Review | **Giống?** |
|---|---|---|---|
| **Write chapters** | Step 7: `write_from_blueprint()` | Step 10: `write_review_chapter()` | ❌ **KHÁC** |
| **Cross-chapter review** | Step 8: `review_narrative_full()` | Step 11: `review_cross_chapter()` | ❌ KHÁC |
| **Merge** | ❌ KHÔNG CÓ | Step 12: merge to `FULL_SCRIPT.txt` | ❌ Chỉ Review |

> [!IMPORTANT]
> **Writer prompt khác hoàn toàn**:
> - **Narrative** dùng `system_write_from_blueprint.txt` — prompt generic, không có mystery structures
> - **Review** dùng `base_mystery_writer.txt` + `mystery_structures/structure_*.txt` — modular, có 7 narrative structures riêng (mythbuster, detective_trail, ticking_clock...), có Adrenaline Test, có POV rules, có closing types, có vocabulary control

---

## Prompts được dùng

| Bước | Narrative | Review |
|---|---|---|
| Extract blueprint | `system_extract_blueprint_battle.txt` ⚠️ | `system_extract_blueprint_mystery.txt` ✅ |
| Reality check | ❌ | `system_reality_check_mystery.txt` |
| Check completeness | ❌ | `system_check_blueprint_mystery.txt` |
| Outline | `system_renew_outline.txt` (generic) | `system_mystery_outline.txt` ✅ |
| Audit outline | `system_audit_outline.txt` (generic) | `system_audit_outline_mystery.txt` ✅ |
| Write chapter | `system_write_from_blueprint.txt` (generic) | `base_mystery_writer.txt` + `structure_*.txt` ✅ |
| Cross-chapter review | generic review | `system_review_cross_chapter_mystery.txt` ✅ |

---

## Đánh giá: Narrative có tham khảo được Review không?

### ❌ KHÔNG tham khảo được trực tiếp

Lý do:

1. **Blueprint structure khác nhau**: Narrative dùng `key_facts/key_events` (flat), Review dùng `product_evaluation[]` (per-item). Các bước sau (outline, write) đều phụ thuộc vào structure này → không thể swap.

2. **Outline format khác nhau**: Narrative outline thiếu `chapter_structure`, `tone_category`, `closing_type` → writer prompt của Review sẽ thiếu input.

3. **Writer prompt khác nhau**: `write_from_blueprint` nhận `key_points`, `write_review_chapter` nhận `products_covered`, `evaluation_criteria`, etc.

### ✅ CÓ THỂ tham khảo CONCEPT

Những gì nên port sang Narrative mystery:

| Feature từ Review | Có thể port? | Cách port |
|---|---|---|
| 7 mystery structures | ✅ | Thêm `chapter_structure` vào narrative outline + inject structure prompts |
| Adrenaline Test POV | ✅ | Copy POV rules vào `system_write_from_blueprint.txt` |
| Reality check | ✅ | Thêm step giữa extract ↔ outline |
| Blueprint completeness | ✅ | Thêm step giữa extract ↔ outline |
| Closing types (6 loại) | ✅ | Thêm `closing_type` vào outline format |
| Per-chapter tone arc | ✅ | Thêm `tone_category` vào outline |
| Vocabulary control (Feynman) | ✅ | Copy section vào writer prompt |
| Cross-chapter mystery review | ✅ | Thay `review_narrative_full` bằng `review_cross_chapter` |

### ⚠️ Nhưng cần refactor lớn

Nếu muốn Narrative mystery tham khảo đầy đủ Review pipeline, cần:

1. **Tạo `system_extract_blueprint_mystery_narrative.txt`** — không dạng `product_evaluation[]` mà dạng `narrative_segments[]` nhưng có đủ structured fields (key_figures, geography, etc.)
2. **Tạo outline prompt riêng cho mystery narrative** — inject `chapter_structure`, `tone_category`, `closing_type`
3. **Sửa `write_from_blueprint` cho mystery narrative** — inject mystery structures, hoặc refactor để mystery narrative cũng dùng `write_review_chapter` (đổi tên thành `write_mystery_chapter`)
4. **Thêm reality check + completeness check vào narrative pipeline**

> [!CAUTION]
> Đây là refactor lớn (ước tính 3-5 new prompt files + sửa pipeline code). Cần plan riêng.

---

## Kết luận

**Narrative mode cho mystery history hiện tại đang dùng toàn bộ generic prompts** — không tận dụng được bất kỳ mystery-specific prompt nào từ Review mode. 

Blueprint dùng prompt `battle` (sai niche), outline và writer đều generic. Chất lượng kịch bản sẽ thấp hơn đáng kể so với Review mode vì thiếu:
- Mystery structures (7 loại framework)
- POV rules (Adrenaline Test)
- Reality check (kiểm tra sự thật)
- Structured data (key_figures, geography, scholarly_debate)
- Vocabulary control
- Diverse closing types
