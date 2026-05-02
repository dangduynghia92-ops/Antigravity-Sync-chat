# Phân Tích Debug Files: Phase Plan + Outline + Audit

## A. `physical_state` — Từ Đâu?

**KHÔNG phải từ blueprint trực tiếp.** Flow:

```
Blueprint (physical_state_arc)
    ↓
Phase Plan AI → tạo physical_state cho mỗi event
    ↓
Outline AI → copy physical_state từ phase plan vào mỗi chapter
    ↓
Writer AI → nhận physical_state trong chapter data
```

Blueprint chứa `physical_state_arc` — một mảng mô tả body state theo age_range:
```json
"physical_state_arc": [
  {"age_range": "0-8", "condition": "Appears healthy..."},
  {"age_range": "9-12", "condition": "Peripheral neuropathy..."},
  {"age_range": "16-18", "condition": "Progressive loss of sensation..."}
]
```

Phase Plan AI **tổng hợp** `physical_state_arc` thành 1 câu cho mỗi event. Outline copy.

**Kết luận**: `physical_state` là AI-generated field — KHÔNG hardcode cho Baldwin. Mỗi nhân vật sẽ có `physical_state_arc` khác nhau trong blueprint.

---

## B. Bỏ FULL OUTLINE → Phương Án Xử Lý

Hiện tại writer AI nhận **70,894 chars** system prompt gồm:
1. Style JSON (~5,000 chars)
2. **FULL Blueprint** (~40,000 chars) 
3. **FULL Outline** (10 chapters, ~4,000 chars)
4. Write prompt rules (~4,000 chars)

**Phương án**: BỎ FULL OUTLINE khỏi write prompt.

| Hiện tại | Sau khi bỏ |
|---|---|
| Writer nhận toàn bộ 10 chapters | Writer chỉ nhận chapter outline riêng |
| Writer biết future chapters → có thể tạo forward tension (vi phạm rule) | Writer chỉ biết current + previous → tự đóng chapter |
| ~4,000 chars outline + chapter riêng = trùng | Giảm ~3,500 chars |

**Không mất gì**: Writer đã nhận `YOUR CHAPTER OUTLINE` (chapter riêng) + `PREVIOUS CHAPTERS` (context trước đó). Full outline thừa.

> [!IMPORTANT]
> Cần sửa trong `core/rewriter.py` — function build write prompt, bỏ inject full outline JSON.

---

## C. Phân Tích Phase Plan + Outline + Audit

---

### C.1 — Phase Plan: `─── USER (56,827 chars) ─── STYLE GUIDE` để làm gì?

File phase plan debug hiển thị:
```
─── SYSTEM (8,906 chars) ───
[Phase plan prompt — event selection rules, scene test, etc.]

─── USER (56,827 chars) ───
STYLE GUIDE: {...}
MANDATORY FRAMEWORK: "Cuộc Đời Bạn"
CONTENT BLUEPRINT: {...full blueprint...}
```

**Giải thích**: Code gửi 2 phần cho AI:
- **SYSTEM** = instruction prompt (cách tạo event timeline)
- **USER** = data (style guide + blueprint để AI đọc và lọc events)

**Vấn đề**: Phase Plan AI **KHÔNG CẦN** full Style Guide!

Phase Plan AI chỉ làm 1 việc: lọc events từ blueprint → sắp xếp chronological → gán phase labels.

Nó không cần biết:
- `sentence_rhythm` (viết kiểu gì)
- `vocabulary` rules (dùng verb gì)
- `chapter_ending_protocol` (kết chapter kiểu gì)
- `pov_rules` (viết POV thế nào)
- `metaphor_family`, `anti_patterns`, v.v.

**56,827 chars** = Style Guide (~5K) + Blueprint (~40K) + Framework steps (~11K)

Chỉ cần:
- Blueprint (cho data) ✓
- Framework name + phase labels (cho tagging) ✓
- **KHÔNG CẦN** style guide cho Phase Plan

> [!WARNING]
> **Token waste**: ~5,000 chars Style Guide gửi cho Phase Plan AI hoàn toàn vô dụng. Phase Plan chỉ cần scene test + blueprint + phase labels.

---

### C.2 — Outline: CHAPTER TYPE / CLOSING TYPE / OPENING STYLE — Mâu thuẫn?

Outline prompt (lines 72-115) định nghĩa:

```
CHAPTER TYPE ASSIGNMENT:
  1. ACTION_SCENE — Physical confrontation, battle, escape, kill
  2. TRANSFORMATION_SCENE — Power shift, identity change
  3. LEGACY_CLOSE — Death, aftermath (end chapter ONLY)

CLOSING TYPE ASSIGNMENT:
  1. COLD_FACT  2. PARADOX  3. COST  4. WEIGHT  5. ECHO

OPENING STYLE ASSIGNMENT:
  1. STANDARD (~60%)  2. THESIS (~20%)  3. ATMOSPHERE (~20%)
```

**Mục đích**: Outline AI gán metadata cho mỗi chapter → writer AI đọc metadata → biết style mở/đóng.

**Mâu thuẫn với write prompt?**

| Aspect | Outline Prompt | Write Prompt | Conflict? |
|---|---|---|---|
| Opening style | "Level anchor within first 2 sentences" | "FIRST SENTENCE of every chapter MUST contain Level" | **YES** — 2 sentences vs 1 sentence |
| Closing | COLD_FACT, PARADOX, COST, WEIGHT, ECHO | PART 4 WEIGHT LINE + Section 3 CLOSING CONTENT RULE | **YES** — 3 chỗ nói closing |
| Chapter type | ACTION_SCENE, TRANSFORMATION_SCENE, LEGACY_CLOSE | PRINCIPLE 3: "Develop through variety" + Chapter structure types | **YES** — outline gán structure type nhưng write prompt lại nói "don't force template" |

**Chi tiết mâu thuẫn closing**:
- Outline gán `closing_type: "paradox"` cho chapter 3
- Write prompt PART 4 nói: "State what CHANGED, what was LOST"
- Write prompt Section 3 nói: 4 lựa chọn content (CHANGED, LEARNED, COST, COMING)
- Style JSON `chapter_ending_protocol` nói: 4 closing types
- → **4 chỗ nói closing** → AI confused

**Chi tiết mâu thuẫn opening**:
- Outline prompt: "Level anchor within first **2** sentences"
- Outline `body_chapter_opening` (style JSON): "Level anchor within first **2** sentences"
- Write prompt PART 1: "FIRST **SENTENCE** must contain Level"
- Style JSON `hook.anchor`: "FIRST **SENTENCE** must be Level anchor"
- → 2 chỗ nói "2 sentences", 2 chỗ nói "1 sentence" → **TRỰC TIẾP MÂU THUẪN**

> [!CAUTION]
> Outline prompt nói "within 2 sentences" — Write prompt nói "FIRST sentence". AI nhận cả 2 → skip Level anchor hoàn toàn vì confused.

---

### C.3 — Outline: `─── USER (66,556 chars) ───` Để Làm Gì?

```
─── SYSTEM (8,325 chars) ───
[Outline generation rules — level structure, scene fields, closing types, etc.]

─── USER (66,556 chars) ───
STYLE GUIDE: {...}
MANDATORY FRAMEWORK: "Cuộc Đời Bạn"
PRE-PLANNED EVENT TIMELINE (10 events)
CONTENT BLUEPRINT: {...full blueprint...}
```

**Giải thích**: Giống C.1 — Code gửi data trong USER message:
- Style Guide (~5K) — cho outline AI biết writing rules
- Event timeline (~4K) — từ Phase Plan output → outline AI enriches thành chapters
- Blueprint (~40K+) — cho outline AI access toàn bộ data

**Vấn đề tương tự Phase Plan**: 

Outline AI cần:
- ✓ Event timeline (enriches into chapters)
- ✓ Blueprint (cho scene fields chi tiết)
- ✓ Framework structure (cho pacing, phase labels)
- ⚠ **Style Guide phần lớn KHÔNG CẦN**

Outline AI chỉ gán metadata (opening_style, closing_type, chapter_structure). Nó không viết prose. Vậy nó **KHÔNG CẦN**:
- `vocabulary` rules
- `sentence_rhythm`
- `voice_over_clarity`
- `anti_copy`
- `terminology_handling`
- `metaphor_family`

Chỉ cần: `chapter_ending_protocol` (để biết closing types), `outline_rules` (opening styles), `pacing`.

> [!WARNING]
> 66,556 chars cho outline AI — ít nhất 20,000 chars có thể cắt bỏ (vocabulary, sentence_rhythm, anti_copy, metaphor_family, voice_over_clarity, terminology_handling).

---

### C.4 — Vấn Đề Khác Trong Phase Plan + Outline

#### Phase Plan — Vấn đề phát hiện:

1. **Phase Plan AI tạo THÊM events so với outline gốc**
   - Phase Plan output có 9 events (event_id 1-9)
   - Nhưng outline gốc đã có 10 events (từ user command line 328: "10 events, each = 1 chapter")
   - Phase Plan AI **merge** events 4+5 (Marj Ayyun + Jacob's Ford) thành 1 event
   - Nhưng user prompt đã yêu cầu 10 chapters → Phase Plan chỉ tạo 9 → **thiếu 1 event**
   
   → Code xử lý: user prompt nói "Generate exactly 10 chapters from these events" → Outline AI phải tách lại.

2. **Phase Plan gửi event_cause nhưng AI KHÔNG tạo event_cause đúng**
   - Phase plan system prompt KHÔNG có field `event_cause` trong output format
   - Nhưng phase plan output thực tế CÓ `event_cause` cho mỗi event
   - → event_cause được Phase Plan AI tự thêm? Hay code inject?

   Kiểm tra: Phase Plan system prompt line 134-161:
   ```json
   "event_timeline": [
     {
       "event_id": 1,
       "age": 0,
       "phase_label": "Nguồn Gốc",
       "event_title": "The Blood Clot",
       "event_description": "...",
       "sub_key_data": ["..."],
       "physical_state": "..."
     }
   ]
   ```
   → **KHÔNG CÓ** `event_cause` trong output schema!
   
   Nhưng line 336-341 (USER input) CÓ `event_cause`:
   ```json
   "event_cause": "King Amalric I appoints the scholar William of Tyre..."
   ```
   
   → **event_cause được inject bởi code** vào event_timeline trước khi gửi cho outline AI.

#### Outline — Vấn đề phát hiện:

1. **scene_close quá giống event_description ending**
   - event_description: "...The enemy line shatters, Saladin barely escapes, and you save Jerusalem."
   - scene_close: "The enemy line shatters, Saladin barely escapes, and you save Jerusalem."
   - → Outline AI just **split** event_description, không enrich → writer phải tự develop

2. **Style JSON gửi FULL nhưng outline chỉ dùng 10%**
   - Outline prompt SYSTEM (8,325 chars) đã có đầy đủ rules
   - Style JSON trong USER (66K chars) lặp lại phần lớn rules
   - → Redundant ~60K chars

3. **Outline không validate event_cause logic**
   - event_cause cho ch6: "Raymond of Tripoli and Bohemond of Antioch lead an army toward Jerusalem to force a political marriage"
   - → Đây là trigger CHÍNH XÁC → tốt
   - Nhưng ch5 event_cause: "Saladin launches a sudden, massive assault on the strategic fortress of Chastellet"
   - → Đây mô tả WHAT happens, không phải WHY → **cause ≈ description**

---

### C.5 — Audit File — Vấn Đề

Audit file analysis:

**Cấu trúc**:
```
SYSTEM (2,756 chars) — audit checklist
USER (84,584 chars) — style guide + blueprint + FULL outline
AI RESPONSE — JSON audit fixes
```

**Vấn đề phát hiện**:

1. **84,584 chars cho USER** — quá lớn
   - Style Guide: ~5K (KHÔNG CẦN cho audit — audit kiểm tra structure, không phải prose)
   - Blueprint: ~40K (KHÔNG CẦN cho audit — audit kiểm tra outline, không phải data)
   - Outline: ~35K (CẦN — đây là input audit)
   
   → **Audit chỉ cần outline (~35K)**, không cần style guide + blueprint = **tiết kiệm ~49K chars**

2. **Audit THAY ĐỔI content** — vi phạm scope
   - Audit fix: `{"action": "set", "chapter": 1, "field": "scene_close", "value": "Your tutor, William of Tyre, drops his quill..."}`
   - Audit fix: `{"action": "set", "chapter": 5, "field": "scene_action", "value": "You grip the reins of your litter..."}`
   - Audit fix: `{"action": "set", "chapter": 9, "field": "scene_action", "value": "You strike the wood with your hands until the skin splits..."}`
   
   → Audit AI **viết lại scene fields** — đây là job của writer, KHÔNG phải auditor
   → Audit prompt nói "Fix variety violations by reassigning types" nhưng AI lại rewrite content

3. **Audit dùng gemini-3-flash-preview** — model yếu hơn
   - Phase Plan + Outline dùng `gemini-3-pro-preview`
   - Audit dùng `gemini-3-flash-preview` 
   - → Flash model dễ hallucinate scene rewrites

4. **vocabulary fix = overreach**
   - Audit type "vocabulary": "Forbidden cognitive/emotional verbs ('realizing', 'rage')"
   - `realizing` xuất hiện trong event_description (phase plan output): "realizing you have contracted leprosy"
   - Audit fix: rewrite scene_close entirely
   - → Audit KHÔNG nên rewrite scenes — chỉ nên flag issues

---

## Tổng Kết Token Waste Across Pipeline

| Stage | System | User | Total | Wasted |
|---|---|---|---|---|
| Phase Plan | 8,906 | 56,827 | **65,733** | ~5K (style guide) |
| Outline | 8,325 | 66,556 | **74,881** | ~20K (style guide thừa) |
| Audit | 2,756 | 84,584 | **87,340** | ~49K (style + blueprint) |
| Writer (ch03) | | | **70,894** | ~7K (full outline + redundant rules) |

**Total wasted per run**: ~81,000 chars = **~20,000 tokens** lãng phí

> [!CAUTION]
> **Pipeline đang gửi ~298,848 chars** cho 4 API calls chỉ để viết 1 chapter. Trong đó **~81K chars (~27%) là data thừa** — Style Guide gửi cho stages không cần, Blueprint gửi cho Audit, Full Outline gửi cho Writer.

---

## Phương Án Sửa Tổng Thể

| # | Action | Stage | Impact |
|---|---|---|---|
| 1 | BỎ Style Guide khỏi Phase Plan USER | Phase Plan | -5K chars |
| 2 | GỌN Style Guide cho Outline (chỉ giữ outline_rules, pacing, closing types) | Outline | -20K chars |
| 3 | BỎ Style Guide + Blueprint khỏi Audit | Audit | -49K chars |
| 4 | BỎ Full Outline khỏi Writer | Writer | -4K chars |
| 5 | Thống nhất opening rule: Level anchor = sentence 1 ALWAYS | Outline + Style JSON + Write prompt | Fix conflict |
| 6 | Gộp closing rules thành 1 chỗ duy nhất | Write prompt | Fix conflict |
| 7 | Audit chỉ flag issues, KHÔNG rewrite content | Audit prompt | Fix overreach |
