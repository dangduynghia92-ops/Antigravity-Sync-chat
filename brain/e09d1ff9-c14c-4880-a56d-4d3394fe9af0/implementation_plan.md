# POV Pipeline — Full Rebuild Plan (v2)

## Problem Statement

27 rule conflicts, ~81K chars token waste/run, unstable output. Root cause: rules duplicated across 3-4 files → AI reads contradictions → random behavior.

**Solution**: Rebuild toàn bộ theo **Single Source of Truth** + code-injected Level Anchor.

---

## User Decisions

### Q1 — Level Anchor: Code Inject ✅

**Decision**: Code tự prepend `"Level {N}, {label}."` vào output. AI writer KHÔNG cần tạo Level anchor.

**Why**: Level anchor đã là nguyên nhân #1 gây conflict (4 nơi nói khác nhau). Nếu code tự thêm thì:
- Prompt không cần nói về Level anchor → bỏ được 4 chỗ conflict
- AI writer chỉ tập trung viết nội dung
- 100% consistent — không bao giờ bị thiếu

**Implementation**:
```python
# In write_from_blueprint() — AFTER receiving AI output
def _inject_level_anchor(text: str, chapter_outline: dict) -> str:
    """Prepend Level anchor line if not already present."""
    level_num = chapter_outline.get("level_number", chapter_outline.get("chapter_number", 1))
    title = chapter_outline.get("chapter_title", "")
    # Extract label from "Level 3: The Dead Flesh" → "the dead flesh"
    label = title.split(":", 1)[1].strip().lower() if ":" in title else ""
    
    age = chapter_outline.get("age_anchor", "")
    
    anchor = f"Level {_num_to_word(level_num)}, {label}."
    if age:
        anchor += f" {age}."
    
    # Check if output already starts with "Level"
    if text.strip().lower().startswith("level"):
        return text
    return f"{anchor}\n\n{text}"
```

**Write prompt change**: REMOVE tất cả instructions về Level anchor. Thay bằng:
```
NOTE: The Level anchor line ("Level N, label. You are age.") is 
automatically prepended by the pipeline. Do NOT write it yourself.
Start your chapter directly with CAUSE/CONTEXT.
```

**Opening styles simplified**:
- STANDARD: Cause/context → scene
- THESIS: Bold statement → cause → scene  
- ATMOSPHERE: Physical environment → cause → scene
- Tất cả đều có Level anchor tự động ở sentence 1 bởi code

---

### Q2 — Closing Types: Tách + Rõ Ràng ✅

**Giải thích hệ thống closing type**:

Hiện tại có **2 layer** dễ nhầm:

| Layer | Owner | What | Example |
|---|---|---|---|
| **closing_type** (metadata) | Outline AI assigns | HOW to phrase ending | `cold_fact`, `paradox`, `cost`, `weight`, `echo` |
| **closing content** (rule) | Write prompt defines | WHAT to express | What changed? What was lost? |

**Cách hoạt động**:
1. Outline AI gán `closing_type: "cost"` cho chapter 5
2. Writer AI đọc → biết: kết thúc chapter 5 phải nêu COST (cái gì đã mất)
3. Writer viết: `"Every Templar in the garrison is dead. The fortress is ash."`

**4 closing types** (rotation — 3 liên tiếp không được trùng):

| Type | Writer instruction | Example |
|---|---|---|
| `cold_fact` | 1-2 câu consequence, im lặng. Không bình luận. | `"The body count: 700."` |
| `paradox` | Mâu thuẫn bộc lộ sự thật. | `"You saved the kingdom. Your hand is dead."` |
| `cost` | Nêu rõ cái đã MẤT hoặc cái GIÁ phải trả. | `"You will never walk again."` |
| `weight` | 1-2 câu nặng, consequence qua hành động vật lý. | `"The crown sits on a skull."` |
| `echo` | Chỉ END chapter. Callback về Level 1. | `"The arm still doesn't feel. It never did."` |

**Tại sao cần rotation?** Nếu 3 chapter liên tiếp đều kết bằng `cold_fact` → monotone, nhàm. Rotation tạo variety.

**scene_close vs weight_line** — giữ tách:
- `scene_close` = kết quả tức thì của action (Outline AI viết) → writer dùng làm skeleton
- `weight_line` = closing type applied (Writer tạo) → 1-2 câu cuối cùng của chapter

```
scene_close: "Saladin retreats without a fight."
            ↓ writer develops into ↓
weight_line (cost): "You saved the fortress. But you cannot see the
victory banner — your eyes are already gone."
```

**Rule**: scene_close và weight_line KHÔNG ĐƯỢC trùng nội dung. scene_close = what happened. weight_line = what it COST.

---

### Q3 — Model AI Mapping

Từ code analysis, đây là **bảng đầy đủ** các bước và model:

#### POV Pipeline — Model Tier Map

| # | Step | step_label | Tier | Model | Hardcoded? | Source |
|---|---|---|---|---|---|---|
| 1 | **Phase Plan** | `phase_plan` | `tier` (user) | User-selected | ❌ No | `script_creation_tab.py:1802` |
| 2 | **Validate Timeline** | `validate_event_timeline` | `flash` | Flash | ✅ **YES** | `rewriter.py:4583` |
| 3 | **Chapter Planning** | `chapter_planning_pov` | `flash` | Flash | ✅ **YES** | `rewriter.py:5026` |
| 4 | **Outline** | `outline` | `tier` (user) | User-selected | ❌ No | `script_creation_tab.py:1905` |
| 5 | **Audit** | `audit` | `flash` | Flash | ✅ **YES** | `script_creation_tab.py:1932` |
| 6 | **Write** | `write_ch{NN}` | `tier` (user) | User-selected | ❌ No | `script_creation_tab.py:2151` |

#### Internal Sub-Steps (inside rewriter.py)

| Step | Tier | Hardcoded? | Note |
|---|---|---|---|
| Validate sub keys | `flash` | ✅ YES | `rewriter.py:4583` — lightweight JSON fix |
| Chapter plan (POV) | `flash` | ✅ YES | `rewriter.py:5026` — demote/promote events |

#### `tier` Variable

`tier` = user chọn từ UI dropdown `_combo_tier` (`script_creation_tab.py:2466`). Options: `flash` hoặc `pro`.

**Kết luận**:
- **3 bước hardcoded flash**: validate, chapter_plan, audit
- **3 bước user-selected**: phase_plan, outline, write
- Flash steps là lightweight tasks (JSON fix, metadata check) → hợp lý dùng flash
- **Audit hardcoded flash là vấn đề** — audit hay rewrite content (vượt scope) vì flash model kém hơn

> [!IMPORTANT]
> **Recommendation**: Giữ validate + chapter_plan ở flash (lightweight). Audit nên giữ flash nhưng **thắt chặt scope trong prompt** (chỉ reassign metadata, KHÔNG rewrite content). Nếu vẫn overreach → đổi sang user tier.

---

### Q4 — Chống Trùng Lặp / Xung Đột: Rule Ownership Architecture

#### Vấn đề hiện tại

```
Level anchor rule xuất hiện ở:
  1. style JSON → core_rules.anti_framework_leak
  2. style JSON → framework.hook.anchor  
  3. style JSON → framework.outline_rules.body_chapter_opening
  4. style JSON → framework.structure.chapter_design
  5. outline prompt → OPENING STYLE ASSIGNMENT (line 106)
  6. write prompt → PART 1 LEVEL ANCHOR (line 69-78)
  7. write prompt → OPENING STYLES (line 120-124)
  = 7 chỗ, 2 nói "sentence 1", 3 nói "within 2 sentences", 2 nói cả hai
```

#### Giải pháp: Rule Ownership Table

**Nguyên tắc**: Mỗi rule thuộc về **DÚng 1 file**. Các file khác **KHÔNG ĐƯỢC** lặp lại rule đó, chỉ được nói `"follow the {X} from {source}"`.

| Rule Category | Owner | Other files say |
|---|---|---|
| **Level Anchor format** | CODE (inject) | Prompt: "Level anchor is auto-injected. Do NOT write it." |
| **Opening styles** (standard/thesis/atmosphere) | `outline_pov.txt` | Write prompt: "Follow the opening_style assigned in the outline." |
| **Closing types** (cold_fact/paradox/cost/weight/echo) | `write_pov.txt` PART 4 | Outline prompt: "Assign closing_type metadata for variety rotation." |
| **Closing rotation rule** (3 liên tiếp không trùng) | `outline_pov.txt` | Write prompt: DO NOT mention rotation |
| **POV contract** (you/your/third person) | `write_pov.txt` | Style JSON: brief identity note only |
| **Sentence rhythm** (staccato/wave/build/stillness) | Style JSON `core_rules.sentence_rhythm` | Write prompt: DO NOT mention |
| **Vocabulary rules** (action verbs, forbidden words) | Style JSON `core_rules.vocabulary` | Write prompt: DO NOT mention |
| **Scene test** (place/action/consequence) | `phase_plan_pov.txt` | Chapter plan: reference only |
| **Event cause** | `chapter_plan_pov.txt` | Outline prompt: "PRESERVE event_cause" |
| **Scene fields** (open/action/close) | `outline_pov.txt` | Write prompt: "Use scene fields as skeleton" |
| **Word count** | UI variable `{word_count_rule}` | All prompts: reference only |
| **Phase labels** | Style JSON `framework.steps` | Phase plan prompt: reference only |
| **Chapter structure types** (action/transformation/legacy) | `outline_pov.txt` | Write prompt: DO NOT define types |
| **Physical state** | `phase_plan_pov.txt` generates | Outline: copy. Write: weave into action. |
| **Zero narrator** | Style JSON `core_rules.zero_narrator_rule` | Write prompt: brief reference |
| **Anti-framework leak** | `write_pov.txt` CONSTRAINTS | Style JSON: REMOVE |
| **Special chapters** (Level 1 / End chapter) | `write_pov.txt` | Outline prompt: DO NOT define |

#### Enforcement Pattern — Prompt Header Comment

Mỗi prompt file bắt đầu bằng ownership comment:

```
# ═══════════════════════════════════════
# RULE OWNERSHIP — THIS FILE OWNS:
#   - Scene test (place/action/consequence)
#   - Event description format
#   - Same-age independence test  
#   - Phase labels assignment
#   - physical_state generation
#   - _source_map generation
#
# THIS FILE DOES NOT OWN (reference only):
#   - Opening styles → outline_pov.txt
#   - Closing types → write_pov.txt
#   - Vocabulary → style JSON
#   - Level anchor → code injection
# ═══════════════════════════════════════
```

#### Cross-Audit Checklist (before any edit)

Khi sửa BẤT KỲ rule nào:

```
1. Xác định rule thuộc file nào (xem Ownership Table)
2. Nếu rule KHÔNG thuộc file đang sửa → KHÔNG ĐƯỢC thêm/sửa tại đây
3. Nếu rule thuộc file đang sửa → sửa tại đây, sau đó:
   a. Search tất cả file khác có mention rule này không
   b. Nếu có → xóa/update reference
   c. Verify không tạo contradiction mới
4. Update Ownership Table nếu thay đổi ownership
```

---

## Updated Architecture

```
Phase Plan AI receives:
  SYSTEM: phase_plan_pov.txt (8K)
  USER:   Blueprint (40K) + Framework name + Phase labels
  ❌ NO Style Guide

Outline AI receives:
  SYSTEM: outline_pov.txt (≤6K) — metadata rules only
  USER:   Event timeline + Blueprint (40K)
  ❌ NO full Style Guide (only phase label extract)

Audit AI receives:
  SYSTEM: audit_pov.txt (≤3K) — metadata-only checklist
  USER:   Outline only (35K)
  ❌ NO Style Guide, NO Blueprint

Writer AI receives:
  SYSTEM: write_pov.txt (≤6K) — structural rules + Style JSON (voice)
        + Filtered Blueprint + Chapter data + Previous context
  USER:   Write command
  ❌ NO full outline
  ✅ Level anchor injected by CODE after AI output
```

---

## Proposed Changes (Updated)

### Component 1: Style JSON

#### [MODIFY] [narrative_pov_tiểu_sử.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_pov_tiểu_sử.json)

**KEEP** (voice rules for writer):
- `core_rules.identity`, `tone`, `sentence_rhythm`, `vocabulary`, `voice_over_clarity`, `pov_rules`, `data_density`, `zero_narrator_rule`
- `framework.pov_strategy`, `language`, `steps`, `emotional_arc`, `tension_curve`
- `pipeline_features`

**REMOVE** (moved elsewhere or deleted):
- `core_rules.anti_framework_leak` → moved to write prompt CONSTRAINTS
- `core_rules.chapter_ending_protocol` → moved to write prompt PART 4
- `core_rules.anti_copy` → DELETE (useless)
- `framework.hook` → DELETE (write prompt SPECIAL CHAPTERS owns this)
- `framework.pacing.rule` → DELETE (hardcoded chapter numbers)
- `framework.pacing.chapter_rhythm` → DELETE (write prompt owns flow)
- `framework.outline_rules` → moved to outline prompt
- `framework.weight_line_types` → moved to write prompt PART 4
- `framework.technique_emphasis` → DELETE (redundant)
- `framework.counter_argument` → DELETE (useless)
- `framework.anti_patterns` → DELETE (duplicates core_rules)
- `chapter_rhythm` (top-level) → DELETE (duplicate)
- `checklist` → DELETE (duplicate of write prompt)
- `framework.structure.chapter_design` → SIMPLIFY (remove Level anchor mention — code handles)

---

### Component 2: Phase Plan — Code Only

#### [KEEP] [system_narrative_phase_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pov.txt)

Prompt is clean. **Code change only**: stop sending Style Guide.

---

### Component 3: Chapter Plan — No Changes

#### [KEEP] [system_narrative_chapter_plan_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_chapter_plan_pov.txt)

Already clean.

---

### Component 4: Outline Prompt — Simplify

#### [MODIFY] [system_narrative_outline_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pov.txt)

**Changes**:
1. KEEP: LEVEL STRUCTURE, SCENE FIELDS, OUTPUT FORMAT, CRITICAL RULES
2. SIMPLIFY opening styles: remove Level anchor positioning (code handles)
3. REMOVE lines 59-62 (BEAT references — writer concept)
4. ADD event_cause requirement
5. ADD ownership header comment

---

### Component 5: Audit Prompt — Restrict Scope

#### [MODIFY] [system_narrative_audit_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_audit_pov.txt)

**Changes**:
1. ADD: "You may ONLY reassign metadata. NEVER rewrite content."
2. REMOVE: word count check, vocabulary check
3. Code: stop sending Style + Blueprint

---

### Component 6: Write Prompt — Clean Rewrite

#### [REWRITE] [system_narrative_write_pov.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pov.txt)

**NEW structure** (~120 lines):

```
HEADER: Variables (style_json, blueprint, chapter data, previous_context)
  ❌ NO {full_outline}
  ✅ ADD: "Level anchor is auto-injected. Do NOT write it."

SECTION 1 — POV CONTRACT (compact, 10 lines)
  "You" = subject. Third person = others.
  Forbidden voices (5 examples).

SECTION 2 — CHAPTER FLOW (4 parts)
  PART 1: NOTE — Level anchor auto-injected. Start with CAUSE.
  PART 2: CAUSE — Develop event_cause. No sentence limit.
  PART 3: SCENE — Use scene_open/action/close. Weave sub_key_data + physical_state.
  PART 4: WEIGHT LINE — Follow closing_type from outline.
    Define 4 types HERE (single source).
    scene_close ≠ weight_line (scene_close = what happened, weight_line = what it cost).

SECTION 3 — SPECIAL CHAPTERS
  Level 1: viewer IN body, physical omen, hostile world
  End: death scene + legacy scorecard + echo callback

SECTION 4 — CONSTRAINTS
  TTS safety, framework leak ban, output format
```

**Deleted**:
- Opening styles menu (outline already assigns)
- Section 3 CLOSING CONTENT RULE (merged into PART 4)
- Content Principles (redundant with flow)
- "WHAT IS COMING?" closing option (contradicts "no forward tension")

---

### Component 7: Code Changes

#### [MODIFY] [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

**7 changes** (all gated behind `_is_pov`):

1. **`generate_narrative_phase_plan()`** (~4418): Remove Style Guide from user_content
2. **`generate_narrative_outline()`** (~5260): Replace full Style Guide → phase labels extract only
3. **`audit_outline()`** (~5327): Remove Style Guide + Blueprint from user_content
4. **`write_from_blueprint()`** (~5667): Remove `{full_outline}` replacement
5. **`write_from_blueprint()`** (after API call): Add `_inject_level_anchor()` post-processing
6. **New helper**: `_extract_phase_labels(style_json, framework_name)` → compact phase-only extract
7. **New helper**: `_inject_level_anchor(text, chapter_outline)` → prepend Level line

---

## Verification Plan

### Automated
1. Run pipeline on King Baldwin IV → compare before/after
2. Token count check: measure SYSTEM+USER size per stage
3. Verify Level anchor appears in sentence 1 of ALL chapters
4. Verify `STYLE GUIDE` NOT in phase_plan/audit debug files
5. Verify biography pipeline NOT affected (run biography test)

### Manual
1. Read chapter output → verify 4-part structure
2. Read audit output → verify NO content rewrites
3. Compare quality with biography pipeline

---

## Execution Order

| Step | File | Risk | Depends On |
|---|---|---|---|
| 0 | Backup all POV files | None | — |
| 1 | `narrative_pov_tiểu_sử.json` | Medium | — |
| 2 | `system_narrative_write_pov.txt` | High | Step 1 |
| 3 | `system_narrative_outline_pov.txt` | Medium | Step 1 |
| 4 | `system_narrative_audit_pov.txt` | Low | — |
| 5 | `core/rewriter.py` — data injection | High | Steps 1-4 |
| 6 | `core/rewriter.py` — Level anchor inject | Medium | Step 2 |
| 7 | Test run + verify | — | All |

> [!CAUTION]
> **Biography Protection**: ALL code changes MUST be gated behind `_is_pov` checks. Biography pipeline must NOT be affected.
