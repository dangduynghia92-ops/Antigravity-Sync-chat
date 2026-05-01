# POV Biography Niche — Implementation Plan

## Pipeline So Sánh Tổng Quan

### Câu trả lời ngắn: Khung pipeline **GIỐNG NHAU** — nội dung prompt **KHÁC NHAU**

POV niche đi qua **đúng các bước giống biography**. Code pipeline (rewriter.py) gần như không cần thay đổi — chỉ thêm niche branches. Cái khác nhau là **nội dung prompt** ở mỗi bước.

```
                    BIOGRAPHY                          POV BIOGRAPHY
                    ─────────                          ─────────────
Step 1: Research    system_research_blueprint_          system_research_blueprint_
        Blueprint   biography.txt (26KB)                pov.txt (~12KB) ← CLONE + CẮT BỎ
                    ↓                                   ↓
Step 2: Select      pre_score + recommend               pre_score + recommend
        Framework   → chọn 1 trong 5 frameworks         → LUÔN chọn "Cuộc Đời" (chỉ có 1)
                    ↓                                   ↓
Step A1: Phase      system_narrative_phase_plan_         system_narrative_phase_plan_
         Plan       biography.txt (8.7KB)               pov.txt (~5KB) ← CLONE + ADAPT
                    ↓                                   ↓
Step A2: Validate   system_validate_sub_key_             ❌ BỎ (validate_sub_keys: false)
         Sub-Key    biography.txt (9KB)                 POV chỉ 1 event/chapter, ko cần
                    ↓                                   ↓
Step A3: Chapter    CODE CHUNG — deterministic           CODE CHUNG — chỉ đổi threshold
         Split      split_threshold: [3, 6]             split_threshold: [2, 4]
                    ↓                                   ↓
Step B: Generate    system_narrative_outline_             system_narrative_outline_
        Outline     biography.txt (18.5KB)              pov.txt (~8KB) ← CLONE + CẮT BỎ NHIỀU
                    ↓                                   ↓
Step C: Audit       system_narrative_audit_               system_narrative_audit_
        Outline     biography.txt (6.5KB)               pov.txt (~3KB) ← CLONE + GIẢN HÓA
                    ↓                                   ↓
Step D: Write       system_narrative_write_              system_narrative_write_
        Chapters    biography.txt (38KB, 675 dòng)      pov.txt (~8KB, 150 dòng) ← VIẾT MỚI 🔴
                    ↓                                   ↓
Step E: Review      system_narrative_review_             system_narrative_review_
        Chapters    biography.txt (4.4KB)               pov.txt (~2KB) ← CLONE + ADAPT
                    ↓                                   ↓
Step F: Auto-Patch  CODE CHUNG                          CODE CHUNG
Step G: Merge       CODE CHUNG                          CODE CHUNG
```

---

## Chi Tiết Từng Bước: GIỐNG / KHÁC / MỚI

### 🟢 DÙNG CHUNG (không cần sửa)

| Bước | Code | Giải thích |
|---|---|---|
| **Step 2: Select Framework** | `pre_score_frameworks()` + `recommend_framework_new_content()` | Code chung. POV chỉ có 1 framework nên AI sẽ luôn chọn nó |
| **Step A3: Chapter Split** | `apply_chapter_splits()` | Code chung, deterministic. Chỉ đổi `split_threshold` trong style JSON |
| **Step F: Auto-Patch** | `patch_chapter_overlap()` | Code chung |
| **Step G: Merge Final** | `merge_to_version()` | Code chung |

### 🟡 CLONE + ADAPT (có cơ sở, sửa vừa phải)

| Bước | File gốc (biography) | File mới (POV) | Cái GIỮ | Cái BỎ | Cái THÊM |
|---|---|---|---|---|---|
| **Research Blueprint** | `system_research_blueprint_biography.txt` (26KB) | `system_research_blueprint_pov.txt` (~12KB) | `core_topic`, `life_phases`, `key_events`, `turning_points`, `key_relationships`, `legacy` | `myths_vs_reality`, `dark_psychology`, `dual_nature`, `systemic_opposition`, `personal_profile` chi tiết | `age_timeline`, `physical_state_arc`, `death_scene` |
| **Phase Plan** | `system_narrative_phase_plan_biography.txt` (8.7KB, 148 dòng) | `system_narrative_phase_plan_pov.txt` (~5KB) | Scene Test logic (dòng 12-41), Output format JSON, chronological rules (dòng 74-112) | Source tracing `_source_map` (dòng 114-136), Coverage checklist chi tiết (dòng 138-148), Origin vs Foundation litmus test | Bắt buộc `age_at_chapter` per phase, bắt buộc `physical_state` per phase, giới hạn 1 main_key_data/phase |
| **Outline** | `system_narrative_outline_biography.txt` (18.5KB, 284 dòng) | `system_narrative_outline_pov.txt` (~8KB) | Framework-driven arc logic (dòng 22-44), Chapter count rules (dòng 253), Chronological body rule (dòng 31-37) | Myth vs Reality integration (dòng 101-123), dual_nature logic, 8 chapter_structures → giảm còn 3, 5 closing_types → giảm còn 3, relationships_featured/humanizing_details/pacing_texture fields | Chapter title format `"Level N: [Label]"`, `age_anchor` field bắt buộc, `physical_state` field, `word_count_target: 150` |
| **Audit Outline** | `system_narrative_audit_biography.txt` (6.5KB) | `system_narrative_audit_pov.txt` (~3KB) | Basic validation structure | Myth distribution check, dual_nature balance check | POV voice check, age_anchor presence check, word count ≤200 check |
| **Review** | `system_narrative_review_biography.txt` (4.4KB) | `system_narrative_review_pov.txt` (~2KB) | Scoring structure | Narrator voice scoring, myth-busting scoring | 2nd person compliance check, "no context paragraph" check |

### 🔴 VIẾT MỚI HOÀN TOÀN

| Bước | Lý do | Chi tiết |
|---|---|---|
| **Style JSON** | Triết lý hoàn toàn khác | Biography: 82KB, 5 frameworks, 8 chapter structures. POV: ~15KB, 1 framework, 3 structures. core_rules khác 100% |
| **Writer Prompt** | **Đây là file quan trọng nhất và khác nhất** | Biography writer prompt (675 dòng) dạy AI viết documentary. POV writer prompt (~150 dòng) dạy AI viết action scene. Không có gì để clone |
| **Enrich Blueprint** | Fields khác nhau | Biography enrich 12 fields. POV enrich 3 fields (`age_timeline`, `physical_state_arc`, `death_scene`) |
| **Extract Blueprint** | Schema output khác | Nếu dùng rewrite mode |
| **Crossref Blueprint** | Rules khác | Nếu dùng rewrite mode |

### ❌ BỎ HẲN (không cần cho POV)

| Bước | Lý do |
|---|---|
| **Step A2: Validate Sub-Key** | POV chỉ có 1 event/chapter. Không có sub_key phức tạp cần validate |

---

## Tại Sao Writer Prompt PHẢI Viết Mới?

So sánh trực tiếp 2 writer prompts:

| Section trong biography writer (675 dòng) | Dùng cho POV? | Lý do |
|---|---|---|
| **SCENE HIERARCHY** (2-3 key scenes + bridges) | ❌ BỎ | POV chỉ có 1 scene/chapter, không cần hierarchy |
| **NARRATOR PERSONALITY** (reaction, question, modern bridge) | ❌ BỎ | POV không có narrator |
| **HOOK CHAPTER** (ANCHOR → TWIST → SCORECARD → QUESTION → BRIDGE OUT) | ❌ BỎ | POV hook = Chapter 1 = first scene of life, không cần cấu trúc hook |
| **BODY CHAPTER** (3-beat opening: BRIDGE → CONTEXT → CONTENT) | ❌ BỎ | POV mở bằng "Level N, [label]. You are [age]." — fixed format |
| **END CHAPTER** (callback + synthesis + anti-recap) | 🟡 ADAPT | POV end = death scene + legacy scorecard |
| **MYTH VS REALITY** | ❌ BỎ | POV không debunk myths |
| **DUAL NATURE** | ❌ BỎ | POV không phân loại light/dark |
| **AUDIENCE CONNECTION** (cost of achievement, before/after, POV shift 0-1/chapter) | ❌ BỎ | POV dùng "You" 100% thời gian, không cần techniques |
| **SPOKEN RHYTHM** (wave pattern, breath points) | 🟡 ADAPT | POV dùng staccato-dominant, không wave |
| **FOREIGN LANGUAGE RULE** | ✅ GIỮ | Vẫn cần cho TTS |
| **LOCALIZATION** | ✅ GIỮ | Vẫn cần |

**Kết quả:** 90% nội dung biography writer prompt bị bỏ hoặc thay thế → viết mới nhanh hơn và sạch hơn clone.

---

## Open Questions

> [!IMPORTANT]
> **Q1: Ngôn ngữ output?**
> 3 script mẫu đều là English. POV niche sẽ viết English, Vietnamese, hay cả hai?

> [!IMPORTANT]
> **Q2: Blueprint source?**
> POV niche sẽ dùng **Research Blueprint** (AI research từ đầu), **Extract Blueprint** (từ script gốc), hay cả hai?
> - Nếu chỉ Research → bỏ extract/crossref prompts, giảm 2 files
> - Nếu cả hai → cần thêm extract + crossref prompts

> [!IMPORTANT]
> **Q3: Video target length?**
> 3 script mẫu = 8–12 phút (10–13 chapters × 100–200 words/chapter). Giữ range này?

---

## Danh Sách Files Cần Tạo/Sửa

### Files MỚI (tạo từ đầu hoặc clone+adapt):

| # | File | Dạng | Kích thước ước tính |
|---|---|---|---|
| 1 | `niches/pov_tiểu_sử.txt` | Mới | ~200 bytes |
| 2 | `styles/narrative_pov_tiểu_sử.json` | **Mới hoàn toàn** | ~15KB |
| 3 | `prompts/system_research_blueprint_pov.txt` | Clone biography → cắt bỏ 50% | ~12KB |
| 4 | `prompts/system_narrative_phase_plan_pov.txt` | Clone biography → adapt | ~5KB |
| 5 | `prompts/system_narrative_outline_pov.txt` | Clone biography → cắt bỏ 55% | ~8KB |
| 6 | `prompts/system_narrative_write_pov.txt` | **Mới hoàn toàn** 🔴 | ~8KB |
| 7 | `prompts/system_narrative_audit_pov.txt` | Clone biography → giản hóa | ~3KB |
| 8 | `prompts/system_narrative_review_pov.txt` | Clone biography → adapt | ~2KB |
| 9 | `prompts/system_enrich_blueprint_pov.txt` | **Mới** (nhẹ) | ~3KB |
| 10 | `prompts/system_extract_blueprint_pov.txt` | Clone biography → adapt (nếu Q2=cả hai) | ~10KB |
| 11 | `prompts/system_crossref_pov_blueprint.txt` | Clone biography → adapt (nếu Q2=cả hai) | ~4KB |
| 12 | `prompts/system_validate_sub_key_pov.txt` | ❌ Không cần | — |

### Files SỬA (thêm niche branch):

| # | File | Thay đổi |
|---|---|---|
| 1 | `core/rewriter.py` | Thêm `_RESEARCH_SECTIONS_POV`, dispatch maps, `_is_pov` branches |

### Files KHÔNG SỬA:

Tất cả files biography, battle, pirate, mystery → **không chạm vào**.

---

## Verification Plan

### Automated Tests
1. JSON validation cho style JSON mới
2. Dispatch coverage: `_get_research_sections('pov_tiểu_sử')` phải trả về POV sections
3. **Biography regression**: chạy biography pipeline → output phải unchanged

### Manual Verification
4. **Smoke test**: chạy POV pipeline với "Genghis Khan"
5. So sánh output với script mẫu gốc
6. Đọc to output — phải có cảm giác "action movie POV"
