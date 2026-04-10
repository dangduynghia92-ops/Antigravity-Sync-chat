# Đánh giá 3 vấn đề: Auto-Patch, Blueprint Filter, Blueprint Schema

## A) Auto-Patch toggle trong New Content

### Kết luả: ⚠️ HARDCODED — Checkbox bị bỏ qua

| Pipeline | auto_patch | Nguồn |
|---|---|---|
| **New Content** (`_do_new_content`) | `auto_patch=True` | **Hardcoded** (line 2052) |
| **Rewrite** (`_run_fw_pipeline`) | `auto_patch=_do_patch` | Đọc từ `_chk_auto_patch.isChecked()` ✅ |

New Content pipeline **LUÔN bật Auto-Patch** bất kể checkbox. Fix cần: đọc `self._chk_auto_patch.isChecked()` tại thời điểm submit job và pass vào `_run_single_fw()`.

> [!IMPORTANT]
> Fix đơn giản: 1 dòng thay `auto_patch=True` → `auto_patch=_do_patch` (cần cache giá trị checkbox vào closure trước khi thread chạy).

---

## B) Bug Report: Blueprint Filter bị gãy logic (DATA LOSS)

### Kết luận: ✅ BUG REPORT ĐÚNG — có data loss thực sự

Tôi đã verify bằng data thực (Einstein, v1_Sử_Thi). Có **2 lỗi chính**:

### Lỗi 1: `key_data` items KHÔNG match bất cứ gì

```
Outline key_data: ["Job at the Swiss Patent Office",
                    "The four 'Annus Mirabilis' papers of 1905",
                    "The birth and mysterious fate of his illegitimate daughter, Lieserl"]

Filter logic: split(".", 1) → top_key = "Job at the Swiss Patent Office"
→ NOT IN blueprint keys (core_topic, core_identity, life_phases, ...)
→ ❌ LOST
```

Filter code dùng `split(".")` để tách `key_data` thành `top_key.sub_key`. Nhưng outline AI trả về **những câu mô tả tiếng Anh** (e.g. "Job at the Swiss Patent Office") — không phải dotted paths (e.g. "life_phases.The Patent Office"). Nên `top_key` = toàn bộ câu → không match bất cứ blueprint key nào → **bị bỏ hết**.

### Lỗi 2: `life_phase_covered` bị gộp → không match

```
Outline: life_phase_covered = "The Struggling Academic, The Patent Office and Annus Mirabilis"

Filter maps to: "life_phases.The Struggling Academic, The Patent Office and Annus Mirabilis"
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                         2 phases gộp thành 1 chuỗi

Blueprint phases: ["The Struggling Academic", "The Patent Office and Annus Mirabilis"]
                    (2 items riêng biệt)

sub_query = "the struggling academic, the patent office and annus mirabilis"
→ substring search in each item → NO MATCH (vì mỗi item chỉ chứa 1 nửa)
→ ❌ LOST
```

### Dữ liệu thực tế (Einstein Ch3):

| Field | FULL blueprint | FILTERED blueprint | Status |
|---|---|---|---|
| core_identity | 9 keys | 9 keys | ✅ Hardcoded |
| personal_profile | 6 keys | 6 keys | ✅ Hardcoded |
| life_phases | 6 items | **0 items** | ❌ **LOST** |
| achievements | có | **missing** | ❌ **LOST** |
| conflicts | có | **missing** | ❌ **LOST** |
| turning_points | có | **missing** | ❌ **LOST** |
| key_relationships | 3 items | 3 items | ✅ (riêng handler) |

Ch3 filtered blueprint chỉ còn **8,937 chars** từ 56,487 — mất **84% data**. Ch1 tệ hơn: chỉ còn core_identity + personal_profile = **6,663 chars** — mất **88%**.

### Tại sao script vẫn "ok"?

Writer AI nhận `{blueprint}` (filtered) VÀ `{full_outline}` (đầy đủ). Outline chứa summary, key_data text, life_phase_covered → AI **bù đắp** bằng cách viết từ outline thay vì blueprint data. Kết quả: nội dung câu chuyện "đọc được" nhưng **thiếu chi tiết cụ thể** (dates, quotes, numbers) mà chỉ blueprint có.

### Hướng fix đề xuất:

Có 2 hướng:

**Hướng 1 (Fix code — `_extract_chapter_blueprint`)**: 
- Split `life_phase_covered` bằng dấu phẩy trước khi match
- Với `key_data`: dùng items làm **substring search** across ALL blueprint sections, thay vì dùng làm dotted keys

**Hướng 2 (Fix prompt — đổi format key_data)**:
- Yêu cầu outline AI xuất `key_data` dạng dotted paths: `"life_phases.The Struggling Academic"` thay vì text tóm tắt
- Nhưng: sẽ ép AI thay đổi hành vi tự nhiên, có thể gây lỗi khác

> [!WARNING]
> **Hướng 1 an toàn hơn** — fix code để adapt format AI đã output, thay vì ép AI đổi format.

---

## C) Đánh giá đề xuất thêm fields vào Blueprint Schema

### 1. `wealth_at_peak` + `wealth_at_death` 

**Đánh giá: ✅ NÊN THÊM — nhưng gộp vào `core_identity`**

| Ưu điểm | Nhược điểm |
|---|---|
| Tạo dramatic contrast (giàu → phá sản hoặc ngược lại) | AI có thể thiếu data chính xác cho nhiều nhân vật |
| Hữu ích cho Van Gogh (chết nghèo), Tesla (chết nghèo), Carnegie (cực giàu) | Không phải nhân vật nào cũng có thông tin tài chính đáng kể |

**Đề xuất**: Gộp thành 1 field `financial_arc` trong `core_identity` với sub-fields: `peak_wealth`, `death_financial_state`, `financial_trajectory` (e.g. "rags-to-riches", "rich-to-ruin", "always modest").

### 2. `final_words` + `who_was_present` trong `death`

**Đánh giá: ✅ NÊN THÊM — rất hữu ích cho narrative**

Đây là những chi tiết **tạo cảnh cuối mạnh nhất** — Einstein output hiện tại ĐÚNG LÀ thiếu:
- Output hiện có: *"He refused surgery. 'I want to go when I want.'"* — câu này đến từ general knowledge, KHÔNG từ blueprint
- Nếu blueprint có `final_words` + `who_was_present`, writer sẽ có material chi tiết hơn

**Đề xuất**: Thêm thẳng vào `core_identity.death`:
```json
"death": {
  "cause": "...",
  "circumstances": "...",
  "final_words": "...",
  "who_was_present": "...",
  "age_at_death": "..."
}
```

### 3. `vices_and_obsessions` trong `personal_profile`

**Đánh giá: ✅ NÊN THÊM — quan trọng nhất trong 4 đề xuất**

Bug report đúng: `behavioral_quirks` quá "hiền". AI có xu hướng trả về thói quen vô hại. Thêm field riêng cho "vết nhơ" là cách chính xác để **signal** cho AI research rằng cần tìm thông tin này.

**Đề xuất**: Thêm `vices_and_obsessions` vào `personal_profile` với description rõ ràng:
```
"vices_and_obsessions": "Addictions, destructive habits, obsessive behaviors, 
 morally questionable pleasures (alcohol, drugs, gambling, affairs, cruelty)"
```

### 4. `near_misses` / `sliding_doors` trong `turning_points`

**Đánh giá: ⚠️ NÊN THẬN TRỌNG — risk hallucination cao**

| Ưu điểm | Rủi ro |
|---|---|
| "What-if" moments rất engaging cho khán giả | AI rất dễ **bịa** near-misses vì đây là speculation |
| Tạo dramatic tension: "suýt nữa thì..." | Khó verify — không phải nhân vật nào cũng có documented near-misses |
| Ví dụ tốt: Hitler suýt chết năm 1918, Einstein suýt không thoát Đức | Có thể tạo thông tin sai lệch nếu AI invent "sliding doors" |

**Đề xuất**: Thêm, nhưng đặt tên `documented_close_calls` (nhấn mạnh "documented") và thêm vào `turning_points` với instruction: *"Only include events that are historically documented, not speculative what-ifs."*

### Tóm tắt recommendations:

| Đề xuất | Verdict | Đặt ở đâu | Tên field |
|---|:---:|---|---|
| Tài chính | ✅ | `core_identity` | `financial_arc` |
| Lời cuối + Ai bên cạnh | ✅ | `core_identity.death` | `final_words`, `who_was_present` |
| Thói hư tật xấu | ✅ | `personal_profile` | `vices_and_obsessions` |
| Suýt chết / quyết định suýt đảo lộn | ⚠️ | `turning_points` | `documented_close_calls` |
