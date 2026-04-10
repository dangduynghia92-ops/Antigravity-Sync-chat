# Pipeline chấm điểm Framework — 3 files liên quan

## Luồng xử lý

```
Step 3: EXTRACT (extract prompt)     → Tạo blueprint data
Step 3.5: ENRICH (enrich prompt)     → Bổ sung data trống
Step 4: RECOMMEND (recommend prompt) → Chấm điểm framework
         ↑ đọc evaluation_focus từ Style JSON
```

---

## FILE 1: Style JSON — Định nghĩa evaluation_focus

📄 [narrative_tiểu_sử_nhân_vật.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_tiểu_sử_nhân_vật.json)

Mỗi framework có block `evaluation_focus`:

### Hai Mặt
```json
"evaluation_focus": {
    "primary_data_field": "dual_nature",
    "richness_check": "Both light_side and dark_side must have 3+ entries each",
    "secondary_fields": ["myths_vs_reality", "conflicts"]
}
```

### Bước Ngoặt
```json
"evaluation_focus": {
    "primary_data_field": "turning_points",
    "richness_check": "At least 1 turning_point with vivid before_state and after_state",
    "secondary_fields": ["life_phases with clear turning_point entries"]
}
```

### Sử Thi
```json
"evaluation_focus": {
    "primary_data_field": "life_phases",
    "richness_check": "4+ life_phases spanning decades, each with key_events",
    "secondary_fields": ["achievements (multiple)", "key_relationships (5+)", "legacy"]
}
```

### Bản Án
```json
"evaluation_focus": {
    "primary_data_field": "systemic_opposition",
    "richness_check": "1+ entries with specific institutions and actions",
    "secondary_fields": ["conflicts with institutional opponents", "legacy.reassessment"]
}
```

### Kẻ Xét Lại
```json
"evaluation_focus": {
    "primary_data_field": "historiography",
    "richness_check": "primary_accounts_by identifies hostile or biased sources, perception_evolution shows change",
    "secondary_fields": ["myths_vs_reality (3+ entries)", "legacy.reassessment"]
}
```

---

## FILE 2: Extract Prompt — Nơi tạo ra data

📄 [system_extract_blueprint_biography.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_extract_blueprint_biography.txt)

Các field RIÊNG được extract như sau:

### dual_nature (cho Hai Mặt)
```
7. **DUAL NATURE (CRITICAL FOR BIOGRAPHY)**: Extract BOTH sides:
   - **light_side**: Virtues, achievements, positive qualities, admirable actions
   - **dark_side**: Flaws, failures, controversies, questionable actions, crimes
   - For each item, tag source: "transcript" or "ai_knowledge"
```

### turning_points (cho Bước Ngoặt)
```
13. **TURNING POINTS**: Moments where the person's life CHANGED DIRECTION. For EACH:
    - **moment**: What happened (1-2 sentences)
    - **year**: When
    - **before_state**: What their life/world was like BEFORE
    - **after_state**: What changed irreversibly
    - **source**: "transcript" or "ai_knowledge"
```

### systemic_opposition (cho Bản Án)
```
14. **SYSTEMIC OPPOSITION**: Institutions, governments, churches, or power structures 
    that SYSTEMATICALLY opposed this person. For EACH:
    - **institution**: Who opposed them
    - **action**: What they did
    - **motive**: Why the system opposed them
    - **outcome**: What happened as a result
    - **source**: "transcript" or "ai_knowledge"
    If none exist, leave as empty list [].
```

### historiography (cho Kẻ Xét Lại)
```
15. **HISTORIOGRAPHY**: Who wrote the history of this person and how it shaped perception:
    - **primary_accounts_by**: Who are the main biographers/historians?
    - **bias_direction**: Do the main accounts favor or disfavor this person?
    - **modern_reassessment**: Has modern scholarship changed the view?
    - **perception_evolution**: How has public perception changed over time?
    - **source**: "transcript" or "ai_knowledge"
```

### life_phases (cho Sử Thi — nhưng đây là field CHUNG)
```
3. **LIFE PHASES**: Break the person's life into ALL distinct phases. For EACH:
   - **phase_name**: Brief label
   - **age_range**: Approximate ages or year range
   - **location**: Where they lived
   - **key_events**: Major events (list)
   - **turning_point**: What changed their trajectory
   - **relationships_formed**: Key people they met
   - **emotional_state**: Their mental/emotional condition
```

---

## FILE 3: Recommend Prompt — Nơi chấm điểm

📄 [system_recommend_framework.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_recommend_framework.txt)

```
SCORING CRITERIA — for each framework, score 1-10 on:
1. **Data richness**: Check the framework's `evaluation_focus.primary_data_field` 
   in the blueprint. How RICH is that data? Count items, check depth. 
   A framework whose primary field has 0-1 items scores low. 
   A framework whose primary field has 3+ detailed items scores high.
2. **Topic fit**: Does the blueprint's content match this framework's 
   use_when description?
3. **Secondary data**: Check `evaluation_focus.secondary_fields` — 
   does the blueprint have supporting data?
4. **Narrative potential**: Would this framework create the most 
   ENGAGING and UNIQUE script for this specific content?

DATA RICHNESS CHECK (how to evaluate):
- Count items in LIST fields: `turning_points` has 3 items = rich.
- Check DEPTH of entries: `systemic_opposition` has 2 items with 
  specific institutions = rich.
- Check BOTH SIDES of dual fields: `dual_nature.light_side` has 5 
  AND `dark_side` has 4 = rich.
- Check COMPLETENESS: `historiography.primary_accounts_by` has named 
  sources = rich.

CRITICAL RULES:
4. **DATA RICHNESS IS PRIMARY** — a framework whose primary_data_field 
   is EMPTY cannot score above 6
5. **EVERY framework deserves fair evaluation** — do NOT default to 
   the "safest" option
6. If two frameworks have similar data richness, prefer the one with 
   higher narrative_potential
```

---

## Vấn đề chính

> [!WARNING]
> **Sử Thi** dùng `life_phases` (field CHUNG) → `data_richness` luôn = 9-10 vì MỌI tiểu sử đều có nhiều life phases.
> 
> Recommend prompt rule #4 nói "EMPTY = max 6" nhưng `life_phases` KHÔNG BAO GIỜ empty → Sử Thi không bao giờ bị phạt.
> 
> Rule #5 nói "fair evaluation" nhưng khi field chung luôn dày hơn field riêng → không fair.
