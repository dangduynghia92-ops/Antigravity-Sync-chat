# Full POV Pipeline Cross-Audit — All 11 Prompts + Style JSON

## Files Audited

| # | File | Lines | Role |
|---|---|---|---|
| 1 | `system_research_blueprint_pov.txt` | 259 | Research → create blueprint |
| 2 | `system_extract_blueprint_pov.txt` | 115 | Extract from existing script |
| 3 | `system_enrich_blueprint_pov.txt` | 85 | Fill blueprint gaps |
| 4 | `system_audit_pov_blueprint.txt` | 108 | Audit blueprint completeness |
| 5 | `system_crossref_pov_blueprint.txt` | 71 | Cross-ref with search results |
| 6 | `system_narrative_phase_plan_pov.txt` | 218 | Pick events → phases |
| 7 | `system_validate_sub_key_pov.txt` | 198 | Validate main/sub classification |
| 8 | `system_narrative_outline_pov.txt` | 159 | Generate chapter outline |
| 9 | `system_narrative_audit_pov.txt` | 49 | Audit outline structure |
| 10 | `system_narrative_write_pov.txt` | 155 | Write chapters |
| 11 | `system_narrative_review_pov.txt` | 57 | Review written chapters |
| — | `narrative_pov_tiểu_sử.json` | 238 | Style JSON |

---

## A. CONTRADICTIONS (rules mâu thuẫn giữa files)

### ❌ A1. WORD COUNT — 3 files vẫn hardcode "100-200"

| File | Line | Hardcode | Xung đột với |
|---|---|---|---|
| `outline_pov.txt` | 8 | "100-200 words of visceral, action-driven prose" | User word count từ UI |
| `outline_pov.txt` | 94-95 | "ALL chapters: 100-200 words" / "End chapter: 100-200 words" | User word count từ UI |
| `audit_pov.txt` | 18 | "Are all chapters targeted at 100-200 words? Flag outliers." | User word count từ UI |
| `review_pov.txt` | 18 | "Is every chapter within 100-200 words?" | User word count từ UI |

**Style JSON** — ĐÃ FIX (chuyển sang "follow user specified")
**Write prompt** — ĐÃ FIX
**Outline, audit, review** — CHƯA FIX

### ❌ A2. SENTENCE MAX 25 WORDS — review_pov.txt

| File | Line | Rule |
|---|---|---|
| `review_pov.txt` | 24 | "Flag any sentence exceeding 25 words." |
| `style JSON` | 67 | ĐÃ FIX: "Aim for brevity but allow longer when rhythm demands" |

Review prompt vẫn enforce "25 words" → AI sẽ flag câu dài dù style JSON cho phép.

### ❌ A3. COLD OPEN — outline_pov.txt vẫn có

| File | Line | Content |
|---|---|---|
| `outline_pov.txt` | 82 | `COLD_OPEN (target ~2%) — No "Level" word.` |
| `style JSON` | — | ĐÃ XÓA cold_open |
| `write_pov.txt` | — | ĐÃ XÓA cold_open |

Outline prompt tạo outline có opening_style = "cold_open" → write prompt không biết cold_open là gì.

### ❌ A4. CLOSING TYPES MISMATCH — outline_pov.txt vs style JSON

| File | Closing types listed |
|---|---|
| `outline_pov.txt` line 64-67 | cold_fact, paradox, forward_pull, weight (4 types) |
| `outline_pov.txt` line 71 | + echo (end chapter) |
| `style JSON` | cold_fact, paradox, forward_pull, weight, **echo** (5 types) — ĐÃ FIX |
| `write_pov.txt` | Defers to style JSON ✅ |

Outline lists 4 types + echo riêng. Style JSON lists 5. Nhất quán nhưng format khác → có thể gây confuse.

---

## B. REDUNDANCIES (nội dung nói lại giữa files)

### ⚠️ B1. Scene Test — 2 files copy gần giống nhau

| File | Lines | Content |
|---|---|---|
| `phase_plan_pov.txt` | 17-31 | Scene Test (3 requirements: place, action, consequence) |
| `validate_sub_key_pov.txt` | 9-28 | Scene Test (same 3 requirements, same examples) |

→ Không phải lỗi (2 files dùng cho 2 bước khác nhau), nhưng nếu sửa 1 file phải sửa cả 2.

### ⚠️ B2. Body State Rule — 2 files

| File | Lines |
|---|---|
| `phase_plan_pov.txt` | 33-37 |
| `validate_sub_key_pov.txt` | 23-28 |

Cùng rule, cùng ví dụ. Phải sync khi sửa.

### ⚠️ B3. Opening styles — outline_pov.txt vs style JSON

| File | Content |
|---|---|
| `outline_pov.txt` lines 78-82 | 5 styles with percentages (bao gồm COLD_OPEN 2%) |
| `style JSON` `body_chapter_opening` | 4 styles (ĐÃ XÓA cold_open) |

→ Mâu thuẫn (A3 ở trên).

### ⚠️ B4. Closing types — outline_pov.txt vs style JSON

| File | Content |
|---|---|
| `outline_pov.txt` lines 63-67 | 4 types defined |
| `style JSON` `closing_types` | 5 types (thêm echo) |

→ Outline thiếu echo trong section, chỉ nhắc echo ở line 71 riêng biệt.

### ⚠️ B5. Chapter structure types — outline_pov.txt vs style JSON

`outline_pov.txt` defines 3 chapter_structure types (action_scene, transformation_scene, legacy_close).
Style JSON KHÔNG có field này → chỉ tồn tại trong outline prompt. OK, không mâu thuẫn.

---

## C. CÁC FILE KHÔNG CÓ VẤN ĐỀ

| File | Status |
|---|---|
| `research_blueprint_pov.txt` | ✅ Clean — pure data extraction, no style rules |
| `extract_blueprint_pov.txt` | ✅ Clean — same schema as research |
| `enrich_blueprint_pov.txt` | ✅ Clean — only adds data, no style rules |
| `audit_pov_blueprint.txt` | ✅ Clean — reviews data completeness |
| `crossref_pov_blueprint.txt` | ✅ Clean — compares with search results |
| `validate_sub_key_pov.txt` | ✅ Clean — scene test consistent with phase_plan |

---

## D. FIX LIST (chỉ sửa mâu thuẫn, không thêm rule mới)

### Fix 1: `outline_pov.txt` — xóa hardcode word count
- Line 8: "100-200 words" → xóa số cụ thể
- Lines 94-95: "100-200 words" → tham chiếu style guide

### Fix 2: `outline_pov.txt` — xóa COLD_OPEN
- Line 82: xóa COLD_OPEN option
- Line 88: xóa "Cold open reserved for..."

### Fix 3: `audit_pov.txt` — xóa hardcode word count
- Line 18: "100-200 words" → tham chiếu style guide

### Fix 4: `review_pov.txt` — xóa hardcode word count + sentence max
- Line 18: "100-200 words" → tham chiếu style guide  
- Line 24: "exceeding 25 words" → xóa rule cứng

### Fix 5: `outline_pov.txt` — thêm echo vào closing types list
- Line 64-67: thêm echo vào danh sách chính thức (hiện chỉ nhắc ở line 71)
