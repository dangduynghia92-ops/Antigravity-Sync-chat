# Niche Mới: Lịch Sử Hải Tặc (Pirate History)

Xây dựng pipeline narrative hoàn chỉnh cho niche **Hải Tặc** — bao gồm con tàu huyền thoại, sào huyệt vô luật pháp, và những nhân vật máu mặt nhất đại dương.

---

## User Review Required

> [!IMPORTANT]
> **Quyết định thiết kế quan trọng #1: Dual-Mode Framework**
> Niche này có 2 loại chủ đề khác biệt: **Tàu (Ship)** và **Địa điểm (Haven)**. Tôi sẽ thiết kế **1 framework duy nhất** gọi là **"Giải Phẫu Huyền Thoại"** với logic phân nhánh bên trong (giống như Battle v2 có HEAD/HEART phases), thay vì 2 framework riêng. Lý do: cả 2 đều follow cùng 6-phase arc (Hook → Context → Anatomy → Characters → Dark Reality → Fall & Legacy), chỉ khác nhau ở Phase 3 (Tech Specs vs Social Specs).

> [!IMPORTANT]
> **Quyết định thiết kế #2: Hook Strategy = Filtered (Lean)**
> Giống Battle v2, hook chapter chỉ cần scene-building data (sensory, scale, shock facts) — KHÔNG cần toàn bộ blueprint. Khác Biography vốn cần cross-section data cho paradox/contrast.

> [!WARNING]
> **Unique Key cho blueprint**: `pirate_phases` — key này sẽ được dùng để detect niche trong code (`_is_pirate = "pirate_phases" in blueprint`). Cần xác nhận key name này.

> [!IMPORTANT]
> **Quyết định thiết kế #3: 4 Kỹ thuật nâng cấp**
> User yêu cầu 4 techniques đặc biệt sẽ được nhúng vào core_rules và framework:
> 1. **Money Angle** — quy đổi tài sản sang USD hiện đại (core_rules.economic_translation)
> 2. **Pirate Medicine** — y khoa rùng rợn, chi tiết visceral (core_rules.macabre_detail_rule)  
> 3. **Anti-Hero Framing** — luôn thiết lập "kẻ phản diện thật" là hệ thống (framework.anti_hero_engine)
> 4. **Micro-Hooks** — câu hỏi mở / hé lộ gây sốc ở cuối EVERY phase (framework.micro_hook_mandate)

---

## Proposed Changes

### Phase A: Files to Create (9 files)

---

#### [NEW] [narrative_lịch_sử_hải_tặc.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_lịch_sử_hải_tặc.json)

Style JSON chính — clone structure từ `narrative_phân_tích_trận_đánh_v2.json` (battle v2)

**Schema chính:**

```json
{
  "pipeline": "narrative",
  "niche": "pirate hải tặc cướp biển tàu huyền thoại sào huyệt",
  "topic_keywords": ["pirate", "hải tặc", "cướp biển", "tàu", "huyền thoại",
                     "sào huyệt", "buccaneer", "corsair", "privateer",
                     "đảo", "cảng", "rum", "kho báu", "treasure"],
  "pipeline_features": {
    "phase_plan": true,
    "validate_sub_keys": true,
    "research_blueprint": true,
    "split_threshold": [3, 6],
    "always_include_keys": ["core_topic", "key_facts", "era_context"],
    "excerpt_fields": ["pirate_phases", "key_figures", "anatomy_specs",
                       "economic_data", "dark_reality"]
  }
}
```

**core_rules** (adapted từ battle v2, thêm 4 techniques mới):
- `identity`: "Cinematic maritime historian — part storyteller, part treasure hunter"
- `tone`: Dramatic, visceral khi mô tả chiến đấu/y khoa; analytical khi phân tích cơ chế/kinh tế; conspiratorial khi nói về Anti-Hero
- `economic_translation`: **"Money Angle"** — LUÔN quy đổi tiền cướp sang USD hiện đại, so sánh với GDP/siêu xe/lương CEO
- `macabre_detail_rule`: **"Pirate Medicine"** — khi mô tả thương tích, bệnh tật → chi tiết visceral (cưa chân, nung sắt cầm máu, thuốc mê = rượu rum)
- `anti_hero_engine`: **"Anti-Hero Framing"** — mỗi video PHẢI thiết lập 1 "kẻ phản diện thật" (Hải quân, Công ty Đông Ấn, chế độ nô lệ)
- `micro_hook_mandate`: **"Micro-Hooks"** — cuối EVERY phase (trừ phase cuối), phải có câu hỏi mở hoặc hé lộ gây sốc kéo sang phase tiếp
- `analogy_strategy`: Modern equivalents (flagship = aircraft carrier, Tortuga = Vegas meets Mad Max)
- `technical_depth`: Vũ khí hải quân HOW IT WORKS (đại bác, buồm, thủy chiến)

**1 Framework: "Giải Phẫu Huyền Thoại"**

| Phase | Tên | Purpose | Lens |
|-------|-----|---------|------|
| 1 | Mồi Nhử Huyền Thoại | Hook | Visual cue → Tối hậu thư (kỷ lục/shock) → Phá vỡ lầm tưởng (phim vs thật) → Title card |
| 2 | Bối Cảnh & Nguồn Gốc | Context | Thế giới lúc đó → Lỗ hổng/cơ hội (TÀU: công nghệ / ĐỊA ĐIỂM: địa hình) → Người đặt nền móng |
| 3 | Giải Phẫu Cơ Chế | Anatomy | **TÀU**: Vũ khí + Tốc độ & Cấu tạo + Kinh tế / **ĐỊA ĐIỂM**: Luật lệ ngầm + Kinh tế ngầm + Phòng thủ |
| 4 | Nhân Vật & Cao Trào | Climax | "Trùm cuối" + Vụ áp phe lớn nhất + Chiến thuật tâm lý |
| 5 | Góc Khuất Tàn Khốc | Dark Reality | Địa ngục trần gian (Pirate Medicine!) + Cái giá của tự do (nô lệ, bóc lột) |
| 6 | Sụp Đổ & Di Sản | Fall & Legacy | Cái chết kỷ nguyên + Số phận người ở lại + Di sản triết học + Outro |

**evaluation_focus:**
```json
{
  "primary_data_field": "legendary_status",
  "tier_field": "infamy_scale",
  "tier_scoring": {
    "Regional_Notoriety": 5,
    "Empire_Level_Threat": 8,
    "Civilizational_Legend": 10
  },
  "richness_check": "Score by HIGHEST infamy_scale. Regional = moderate. Empire_Level+ = strong.",
  "best_when": "Subject has Empire_Level_Threat or higher — feared by entire navies/empires"
}
```

---

#### [NEW] [system_research_blueprint_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_research_blueprint_pirate.txt)

Clone từ `system_research_blueprint_battle.txt`, adapted:

**Blueprint sections cho pirate:**

| # | Section | Key fields |
|---|---------|------------|
| 1 | `core_topic` | Subject (tàu/đảo), era, region, key_association |
| 2 | `key_facts` | Dates, numbers, records, shocking stats |
| 3 | `era_context` | `world_state`, `power_vacuum`, `naval_powers`, `trade_routes`, `catalyst` |
| 4 | `key_figures` | `name`, `nickname`, `role`, `background`, `key_actions`, `fate`, `connection_to_subject` |
| 5 | `pirate_phases` | **UNIQUE KEY** — các giai đoạn lịch sử: `phase_name`, `date_range`, `key_events`, `significance` |
| 6 | `anatomy_specs` | **Dual-mode**: Nếu TÀU → `armament`, `hull_design`, `speed_capability`, `cargo_economics` / Nếu ĐỊA ĐIỂM → `governance_system`, `underground_economy`, `defense_network` |
| 7 | `climactic_events` | Vụ cướp/trận đánh đỉnh cao: `event_name`, `before_state`, `during_action`, `after_state`, `tactics_used` |
| 8 | `dark_reality` | `daily_horrors`, `medical_practices`, `slavery_exploitation`, `mortality_stats` |
| 9 | `economic_data` | `loot_value_original`, `loot_value_modern_usd`, `comparison_to_modern`, `trade_impact` |
| 10 | `myths_vs_reality` | `popular_belief`, `actual_evidence`, `why_myth_persists` |
| 11 | `fall_and_legacy` | `cause_of_end`, `final_fates`, `lasting_impact`, `archaeological_evidence` |
| 12 | `narrative_moments` | Sensory scenes: `scene`, `physical_details`, `scale_indicator` |
| 13 | `texture_and_hooks` | `memorable_quotes`, `dramatic_ironies`, `human_moments`, `scale_comparisons` |

**Tier enums** (MUST match style JSON):
```
For infamy_scale, use EXACTLY ONE of: "Regional_Notoriety", "Empire_Level_Threat", "Civilizational_Legend"
```

---

#### [NEW] [system_narrative_phase_plan_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_pirate.txt)

Clone từ `system_narrative_phase_plan_battle.txt`, adapt phase names:
- Mồi Nhử Huyền Thoại → Bối Cảnh & Nguồn Gốc → Giải Phẫu Cơ Chế → Nhân Vật & Cao Trào → Góc Khuất Tàn Khốc → Sụp Đổ & Di Sản

Output: `main_key_data`, `sub_key_data`, `node_count` per phase

---

#### [NEW] [system_validate_sub_key_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_validate_sub_key_pirate.txt)

Clone từ `system_validate_sub_key_battle.txt`:
- 3 tests: Scene Test, Turning Point Test, Causal Independence Test
- Examples adapted to pirate domain (sea battles, betrayals, disease)

---

#### [NEW] [system_narrative_outline_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_outline_pirate.txt)

Clone từ `system_narrative_outline_battle_v2.txt`:
- CoT `pacing_evaluation` block
- Outline fields include: `pirate_phase`, `subject_type` (ship/haven), `figures_featured`, `anatomy_focus`, `economic_angle`
- key_data uses distinctive keywords from blueprint (Rule 16/17)

---

#### [NEW] [system_narrative_audit_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_audit_pirate.txt)

Clone từ `system_narrative_audit_battle.txt`:
- Validate: key_data coverage, hook uniqueness, pacing, 6-phase arc
- Special checks: Money Angle present? Anti-Hero established? Micro-hooks at phase transitions?

---

#### [NEW] [system_narrative_write_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pirate.txt)

Clone từ `system_narrative_write_battle_v2.txt` (latest template). **MUST include ALL sections**:

| Section | Adaptation |
|---------|-----------|
| SCENE HIERARCHY | main_key_data → FULL SCENES, sub_key_data → FAST BRIDGE |
| TRANSITIONS + CHAPTER OPENING DISCIPLINE | Conjunction Ban, No Blind Pronouns — same rules |
| ENDS_WITH ENFORCEMENT | Hard cut after ends_with |
| TIMELINE FLOW | Cause before Effect, Micro-Callback |
| QUESTION ENGINE | Question answered + Question opened |
| **PIRATE-SPECIFIC PHASE WRITING STYLE** | 6 phases instead of battle's HEAD/HEART. Mồi Nhử = visceral + myth-busting. Bối Cảnh = analytical. Giải Phẫu = technical/mechanical. Nhân Vật = character-driven + action. Góc Khuất = macabre + cold facts. Sụp Đổ = reflective + grand |
| **MONEY ANGLE RULE** | Every economic fact MUST have modern USD equivalent |
| **PIRATE MEDICINE RULE** | Medical/wound descriptions must be visceral, step-by-step |
| **ANTI-HERO ENGINE** | Establish the "real villain" (empire/company) before showing pirate cruelty |
| **MICRO-HOOK MANDATE** | End of every phase: shocking question or reveal |
| HOOK CHAPTER RULES | Visual Cue → Tối hậu thư → Phá vỡ lầm tưởng → Title card |
| END CHAPTER RULES | Cause of end → Final fates → Di sản triết học → CTA |
| SPOKEN RHYTHM | Wave pattern, breath points, one idea per sentence |
| FOREIGN LANGUAGE RULE | TTS Safety |
| PRIORITY ORDER | Word count > Spoken rhythm > Scene hierarchy > Structure > Detail |
| OUTPUT | Chapter text only, no headers |

All examples pirate-specific — NOT copy-paste from battle/biography.

---

#### [NEW] [system_narrative_review_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_review_pirate.txt)

Clone từ `system_narrative_review_battle.txt`:
- Review criteria adapted: Money Angle check, Anti-Hero presence, Micro-Hook compliance
- Scoring rubric for pirate-specific quality

---

### Phase B: Code Wiring

---

#### [MODIFY] [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

**B1. Dispatch Maps** — Add pirate keywords to ALL 7 maps in `_NICHE_PROMPT_MAP`:

```python
# ── Pirate / Hải tặc (MUST match before generic keywords) ──
"hải tặc":      "system_narrative_<step>_pirate.txt",
"cướp biển":    "system_narrative_<step>_pirate.txt",
"pirate":       "system_narrative_<step>_pirate.txt",
"buccaneer":    "system_narrative_<step>_pirate.txt",
"corsair":      "system_narrative_<step>_pirate.txt",
"lịch sử hải tặc": "system_narrative_<step>_pirate.txt",  # longest match first
```

Maps to update:
- `narrative_outline`
- `narrative_phase_plan`
- `narrative_validate_sub_key`
- `narrative_audit`
- `narrative_writer`
- `narrative_review`

**B2. Research Sections** — Define 3 new research section constants:

```python
_PIRATE_RESEARCH_SECTION_A = {
    "name": "Core Topic, Era Context, Key Figures & Geography",
    "fields": ["core_topic", "key_facts", "era_context", "key_figures", "geography"],
    ...
}
_PIRATE_RESEARCH_SECTION_B = {
    "name": "Pirate Phases, Anatomy Specs, Climactic Events, Economic Data",
    "fields": ["pirate_phases", "anatomy_specs", "climactic_events", "economic_data", ...],
    ...
}
_PIRATE_RESEARCH_SECTION_C = {
    "name": "Dark Reality, Myths vs Reality, Fall & Legacy, Texture",
    "fields": ["dark_reality", "myths_vs_reality", "fall_and_legacy", ...],
    ...
}
_RESEARCH_SECTIONS_PIRATE = [_PIRATE_RESEARCH_SECTION_A, _PIRATE_RESEARCH_SECTION_B, _PIRATE_RESEARCH_SECTION_C]
```

Add to `_NICHE_RESEARCH_MAP`:
```python
"lịch sử hải tặc": _RESEARCH_SECTIONS_PIRATE,
"hải tặc":         _RESEARCH_SECTIONS_PIRATE,
"cướp biển":       _RESEARCH_SECTIONS_PIRATE,
"pirate":          _RESEARCH_SECTIONS_PIRATE,
"buccaneer":       _RESEARCH_SECTIONS_PIRATE,
"corsair":         _RESEARCH_SECTIONS_PIRATE,
```

Also update `_RESEARCH_PROMPT_MAP` in `research_blueprint()`:
```python
"hải tặc": "system_research_blueprint_pirate.txt",
"cướp biển": "system_research_blueprint_pirate.txt",
"pirate": "system_research_blueprint_pirate.txt",
"lịch sử hải tặc": "system_research_blueprint_pirate.txt",
```

**B3. Niche Detection** — Add `_is_pirate` branching:

In `_extract_chapter_blueprint()`:
```python
_is_battle = "battle_phases" in blueprint
_is_pirate = "pirate_phases" in blueprint

if _is_pirate:
    for key in ("core_topic", "key_facts", "era_context"):
        if key in blueprint:
            result[key] = blueprint[key]
elif _is_battle:
    ...
```

In `write_from_blueprint()`:
```python
_is_pirate = "pirate_phases" in blueprint

if _is_hook:
    if _is_battle:
        chapter_bp = _extract_chapter_blueprint(blueprint, chapter_outline)
    elif _is_biography:
        chapter_bp = blueprint
    elif _is_pirate:
        # Pirate hooks: filtered (lean) — like battle
        chapter_bp = _extract_chapter_blueprint(blueprint, chapter_outline)
    else:
        raise RuntimeError(...)
```

**B4. Outline Fields** — Add pirate-specific placeholders to `_NICHE_OUTLINE_FIELDS`:

```python
# ── Pirate ──
"{pirate_phase}": "pirate_phase",
"{subject_type}": "subject_type",
"{figures_featured}": "figures_featured",
"{anatomy_focus}": "anatomy_focus",
"{economic_angle}": "economic_angle",
"{anti_hero_target}": "anti_hero_target",
"{myth_busted}": "myth_busted",
```

**B5. Key Normalization** — Add to `_KEY_NORMALIZE`:

```python
"key_figures_and_associates": "key_figures",
"climactic_events_and_battles": "climactic_events",
"dark_reality_and_horrors": "dark_reality",
"economic_data_and_loot": "economic_data",
"myths_and_reality": "myths_vs_reality",
```

**B6. Research blueprint log** — Update `research_blueprint()` log to detect pirate fields:

```python
pirate_phases = len(blueprint.get("pirate_phases", []))
figures = len(blueprint.get("key_figures", []))
# etc.
```

---

### Phase C: Verification

---

#### C1. Pre-flight Check
- [ ] Style JSON is valid JSON (`python -c "import json; json.load(open(...))"`)
- [ ] All 7 prompt files exist in `prompts/`
- [ ] All dispatch map entries point to existing files
- [ ] `pipeline_features` is set in style JSON
- [ ] `evaluation_focus.tier_scoring` values match research prompt instructions

#### C2. Existing Niche Regression Test
- [ ] Verify biography dispatch still maps correctly
- [ ] Verify battle v2 dispatch still maps correctly
- [ ] Check: hook chapters still receive correct blueprint data for both niches
- [ ] Check: no pirate keywords accidentally collide with existing niches

#### C3. New Niche Smoke Test
- [ ] Run with test topic (e.g., "Tàu Queen Anne's Revenge — Chiến hạm của Râu Đen")
- [ ] Verify research blueprint populates all expected fields including `pirate_phases`
- [ ] Verify pre-scoring matches tier values (no FUZZY warnings)
- [ ] Verify phase plan generates 6 correct phases
- [ ] Verify outline generates with correct pirate-specific field names
- [ ] Verify writer prompt injects all placeholders correctly
- [ ] Verify Money Angle, Anti-Hero, Micro-Hook rules are followed

#### C4. Git Commit
- [ ] `git add` all new files
- [ ] Commit with message: `feat: add pirate history narrative pipeline`

---

## Open Questions

> [!IMPORTANT]
> 1. **Tên niche tiếng Việt chính xác?** Tôi đề xuất `narrative_lịch_sử_hải_tặc.json`. Bạn muốn tên khác không?
> 2. **Có muốn thêm framework thứ 2?** Hiện tại tôi thiết kế 1 framework "Giải Phẫu Huyền Thoại" với dual-mode (Ship/Haven). Nếu muốn, có thể thêm framework chuyên cho "Nhân vật hải tặc" (tiểu sử riêng kiểu Blackbeard, Anne Bonny) — nhưng điều này sẽ overlap với niche Biography.
> 3. **Subject type detection**: Làm sao AI biết đây là **Tàu** hay **Địa điểm**? Tôi đề xuất thêm field `subject_type: "ship" | "haven"` trong blueprint, được AI auto-detect từ topic input.

---

## Verification Plan

### Automated Tests
1. JSON validation: `python -c "import json; json.load(open('styles/narrative_lịch_sử_hải_tặc.json', encoding='utf-8'))"`
2. Dispatch test: Import `_get_niche_prompt` và test with pirate keywords
3. Keyword collision test: Đảm bảo "hải tặc" không match vào battle/biography

### Manual Verification
1. Chạy full pipeline New Content mode với topic test
2. Review output chapters: kiểm tra Money Angle, Anti-Hero, Micro-hooks, Pirate Medicine
3. Chạy lại biography + battle v2 pipeline → xác nhận không regression
