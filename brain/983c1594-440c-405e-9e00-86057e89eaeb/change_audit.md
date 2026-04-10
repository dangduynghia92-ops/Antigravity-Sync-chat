# Audit Toàn Bộ Thay Đổi (so với git HEAD)

## Tóm Tắt

| File | Insertions | Deletions | Ảnh hưởng |
|---|---|---|---|
| `core/rewriter.py` | +534 | -1 | Biography + shared |
| `ui/rewrite_style_tab.py` | +157 | -39 | Biography + shared |
| `prompts/system_narrative_write_biography.txt` | +237 | (edit) | Chỉ biography |
| `prompts/system_narrative_outline_biography.txt` | +134 | (edit) | Chỉ biography |
| `prompts/system_narrative_audit_biography.txt` | +128 | (edit) | Chỉ biography |
| `prompts/system_narrative_review_biography.txt` | +6 | (edit) | Chỉ biography |
| `prompts/system_extract_blueprint_biography.txt` | +41 | (new) | Chỉ biography |
| `prompts/system_narrative_write_battle.txt` | +47 | (edit) | Chỉ battle |
| `styles/narrative_tiểu_sử_nhân_vật.json` | +6 | (edit) | Chỉ biography |
| `docs/niche_pipeline_builder_guide.md` | +4 | (edit) | Docs |
| `auto_pipeline_config_config.json` | +4 | (edit) | Config |
| `rewrite_style_config_config.json` | +8 | (edit) | Config |

---

## A. code/rewriter.py — 12 HUNKS

### ✅ Biography-only (không ảnh hưởng niche khác)

| Hunk | Nội dung | Risk |
|---|---|---|
| `_NICHE_PROMPT_MAP` L102 | Thêm `narrative_phase_plan` map cho biography | ✅ Safe — chỉ thêm key mới |
| `generate_phase_plan()` L2780 | Hàm mới cho biography phase planning | ✅ Safe — hàm mới, không sửa gì |
| `_TIER_FUZZY_MAP` + `_resolve_tier` + `_pre_score_frameworks` L3587 | Pre-scoring helpers cho biography | ✅ Safe — hàm mới, không sửa gì |
| `recommend_framework_biography()` L3883 | Recommend riêng cho biography | ✅ Safe — hàm mới, không sửa gì |

### ⚠️ SHARED CODE (ảnh hưởng tất cả niches)

| Hunk | Nội dung | Risk | Chi tiết |
|---|---|---|---|
| `_extract_chapter_blueprint()` L357 | `key_data` → `main_key_data` + `sub_key_data` | ⚠️ **MEDIUM** | Dùng fallback `chapter_outline.get("main_key_data", chapter_outline.get("key_data", []))` — nếu không có `main_key_data` thì dùng `key_data` cũ. **SAFE nhờ fallback**. |
| `_NICHE_OUTLINE_FIELDS` L430 | Xóa `open_loop_resolve/plant`, thêm `main_key_data/sub_key_data` | ⚠️ **MEDIUM** | Xóa 2 fields cũ, thêm 2 fields mới. Mystery/Battle outlines nếu dùng `open_loop_resolve` sẽ mất. Cần kiểm tra. |
| `generate_renew_outline_v2()` L2868 | Thêm param `phase_plan` | ✅ **SAFE** — optional param, default None |
| `generate_renew_outline_v2()` L2890 | Inject phase_plan block vào user content | ✅ **SAFE** — chỉ inject khi `phase_plan` có giá trị |
| `generate_renew_outline_v2()` L2941 | Ensure `phase_chapter_plan` in output | ✅ **SAFE** — chỉ khi `phase_plan` provided |
| `audit_outline()` L3047 | Thêm "Expecting value" JSON repair + retry logic | ✅ **SAFE** — thêm error handling, không thay đổi logic |
| `audit_outline()` L3087 | Diff-based audit fix (thay vì full outline copy) | ⚠️ **MEDIUM** | Thay đổi cách apply audit fixes. Có fallback cho legacy format. Ảnh hưởng tất cả niches dùng `audit_outline`. |
| `recommend_framework()` L3832 | Cập nhật docstring | ✅ **SAFE** — chỉ comment |

---

## B. ui/rewrite_style_tab.py — 9 HUNKS

### ✅ Biography-only

| Hunk | Nội dung |
|---|---|
| Import L33 | Thêm `generate_phase_plan`, `recommend_framework_biography` |
| New Content L2072 | `if niche_label == "Biography"` → dùng `recommend_framework_biography` |
| New Content L2098 | Biography: v1=General, v2=Specialized selection logic |
| Rewrite L3034 | Rewrite tab dùng `recommend_framework_biography` |
| Rewrite L3103 | Rewrite tab: biography-specific v1/v2 selection |

### ⚠️ SHARED

| Hunk | Nội dung | Risk |
|---|---|---|
| `get_ch_range()` L505 | Return `""` thay vì `"a suitable number of chapters"` | ⚠️ **LOW** — ảnh hưởng tất cả niches khi không set min/max |
| `_run_shared_fw_pipeline` L1607 | Thêm Step A: Phase Planning | ⚠️ **HIGH** — chạy cho TẤT CẢ niches qua shared pipeline |
| `_run_shared_fw_pipeline` L1669 | Fallback auto-generate phase_chapter_plan | ⚠️ **LOW** — chỉ chạy khi phase_plan trống |
| `_run_shared_fw_pipeline` L1707 | `pacing_evaluation.node_count` → `node_count` (top-level) | ⚠️ **LOW** — có fallback cho cả 2 format |

---

## C. ⚠️ VẤN ĐỀ CẦN KIỂM TRA

### 1. `_run_shared_fw_pipeline` gọi `generate_phase_plan` cho TẤT CẢ niches
- Phase plan chỉ có prompt cho biography (`system_narrative_phase_plan_biography.txt`)
- Mystery & Battle **chưa có prompt** → `_require_niche_prompt("phase_plan", niche)` sẽ **FAIL** nếu niche không match

### 2. `_NICHE_OUTLINE_FIELDS` xóa `open_loop_resolve/plant`
- Nếu mystery/battle outline dùng các fields này → **bị mất**

### 3. `audit_outline()` diff-based logic
- Mới: apply fixes từng issue thay vì nhận full outline
- Có fallback legacy: nếu audit trả `"outline"` key → dùng cũ
- Nhưng nếu audit trả format mới mà sai → mystery/battle bị ảnh hưởng

### 4. `get_ch_range()` return empty string
- Khi user không set min/max chapters → prompt nhận `""` thay vì `"a suitable number of chapters"`
- Có thể khiến AI không biết limit → tạo quá nhiều/ít chapters
