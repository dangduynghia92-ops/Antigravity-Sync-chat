# Crowd Character Pipeline — Final Plan

## Field Name Audit Result

### Issue 1: `present_labels` vs `character_labels` ❌

| Where | Field name | Should be |
|---|---|---|
| Step 3.1 prompt (L534,543,582) | `present_labels` | `character_labels` |
| Step 3.1 output JSON | `present_labels` | `character_labels` |
| Step 3.2 prompt (L683) | `character_labels` | ✅ already correct |
| Step 3.2 code read (L1916,2391,2528,2597) | `character_labels` | ✅ already correct |

**Fix**: Rename `present_labels` → `character_labels` in Step 3.1 prompt only. **No code reads `present_labels`** — Step 3.1 output goes to Step 3.2 LLM which produces its own `character_labels`. So renaming the prompt field is a cosmetic fix for consistency, no code breakage.

### Issue 2: `scene_id` vs `global_scene_id` ⚠️

| Where | Field | Details |
|---|---|---|
| Step 3.2 output (L681) | `global_scene_id` | Main identifier |
| Step 4 prompt output (L736,800) | `scene_id` | ← Step 4 LLM produces this |
| Step 4 code read (L2581) | `scene_id` | `prompt_map = {p.get("scene_id"): p}` |
| Step 4 code read (L2584) | `global_scene_id` | `scene.get("global_scene_id")` |

Step 4 LLM outputs `scene_id`, code matches it to `global_scene_id` (L2581-2585). **Works but confusing.** Recommend: keep as-is since changing Step 4 LLM output field name risks breaking prompt matching.

### Issue 3: `chapter` vs `chapter_id` vs `chapter_name` ⚠️

| Where | Field | Value |
|---|---|---|
| Step 0 sentences | `chapter_id` (int), `chapter_name` (str) | `1`, `"ch_08_Level_8__Chilled"` |
| Step 1 sequences | `chapter_id`, `chapter_name` | Same |
| Step 4 prompt item | `chapter` (str), `chapter_id` | `"ch_08..."`, `1` |

`chapter` = alias for `chapter_name`. Minor inconsistency, low priority.

### Issue 4: No issues found ✅

- `has_crowd`, `audio_sync`, `duration`, `location_shift`, `locked_location` — all consistent.

---

## Pipeline Changes (Final)

### A. Step 2a-2: Remove fixed crowd categories

#### [MODIFY] `STEP2A_PEOPLE_PROMPT` (~L408-434)

Replace 6 hardcoded crowd categories with open-ended instruction:

```json
"crowd_archetypes": {
    // IDENTIFY from the script: all unnamed character types
    // Use descriptive keys: "heavy_cavalry", "palace_guard", "prisoner", etc.
    "<type>": "Head: ... Upper: ... Lower: ... Feet: ... Acc: ..."
}
```

Add prompt rule: *"Read the full script. Identify every UNNAMED character type that appears or is implied. Create a 5-layer costume description for each. Include military, civilian, religious, and any other types present."*

---

### B. Step 1: Add `crowd_types` field

#### [MODIFY] `STEP1_SYSTEM_PROMPT` (~L113-165)

Keep existing rule L141 (`Do NOT list unnamed crowds in characters`).
Add new field to output:

```json
{
  "sequence_id": "SEQ_01",
  "characters": ["mature_adult Commander"],
  "crowd_types": ["sentries", "soldiers"],
  ...
}
```

Add instruction: *"Also list `crowd_types`: unnamed background character types visible in this sequence (e.g., 'soldiers', 'guards', 'prisoners'). Use lowercase descriptive names."*

#### [MODIFY] `STEP1B_AUDIT_SYSTEM_PROMPT` (~L167-184)

Add: *"Also audit `crowd_types` — add crowd types implied by location/action."*

---

### C. Step 2d: Crowd Character Sheets (NEW)

#### [NEW] `STEP2D_CROWD_PROMPT`

**Position**: After Step 2b, before Step 2b-map

**Input**:
- Deduplicated `crowd_types` from all sequences
- World Bible `crowd_archetypes` per faction
- Era/geography context

**Output**:
```json
{
  "characters": [
    {
      "label": "EXT-Ayyubid-Soldier-Infantry",
      "group": "CROWD",
      "faction": "Ayyubid Army",
      "crowd_type": "soldier",
      "visual_description": "BODY: 5 heads tall, stocky. COSTUME: Head: iron conical helmet. Upper: iron chainmail under yellow cotton tunic. Lower: wool trousers. Feet: leather boots. Acc: round shield, steel saif.",
      "sheet_prompt": "Character reference sheet, clean white background. Bold rounded sans-serif text 'EXT-Ayyubid-Soldier-Infantry'..."
    }
  ]
}
```

**Label convention**: `EXT-{Faction}-{Role}-{Variant}` — `EXT-` prefix distinguishes from named chars.

#### Code additions:
- `self.crowd_data = {}` (data holder, L920)
- `_run_step2d()` method
- Step status: `"step2d": StepStatus(step="Step 2d: Crowd Sheets")`

---

### D. `_extract_valid_labels()` — Add crowd

```python
self.valid_labels = {
    "characters": [...named labels...],
    "crowd": [c.get("label") for c in self.crowd_data.get("characters", [])],
    "locations": [...],
}
```

---

### E. Step 3.1: Rename + add crowd

#### [MODIFY] `STEP3_1_SYSTEM_PROMPT` (~L517-595)

1. Rename `present_labels` → `character_labels` in prompt text + output format
2. Add `crowd_labels` field to output format
3. Add Q for crowd: identify which `crowd_labels` are visible per sentence

**Input** user data — add fields:
```python
user_data = {
    "sequence_id": seq_id,
    "characters": char_labels,
    "crowd_labels": crowd_labels,      # NEW
    "location": seq.get("location_shift"),
    "sentences": sentences,
}
```

**Output format** in prompt:
```json
{
  "sentence_id": 1,
  "character_labels": ["Ayyubid-Commander-A"],    // RENAMED
  "crowd_labels": ["EXT-Ayyubid-Guard-Sentry"],   // NEW
  "is_broll": false,
  "character_interaction": "...",
  "scenes": [...]
}
```

---

### F. Step 3.2: Add `crowd_labels`

#### [MODIFY] `STEP3_SYSTEM_PROMPT` (~L598-695)

Add `crowd_labels` to output format (parallel to `character_labels`):
```json
{
  "global_scene_id": "SEQ_01_SCN_03",
  "character_labels": ["Ayyubid-Commander-A"],
  "crowd_labels": ["EXT-Ayyubid-Guard-Sentry"],
  "has_crowd": true,
  ...
}
```

---

### G. Step 4: Reference crowd in prompts

#### [MODIFY] `STEP4_USER_TEMPLATE` + `STEP4_USER_TEMPLATE_INLINE`

Add crowd labels to scene data block (~L2536):
```python
f"  Crowd: {', '.join(scene.get('crowd_labels', []))}\n"
```

#### [MODIFY] `_build_mini_bible()` (~L2379)

Include crowd character sheets in mini_bible:
```python
for c in self.crowd_data.get("characters", []):
    if c.get("label") in needed_crowd:
        parts.append(f"[{c['label']}]: {c.get('visual_description', '')}")
```

#### [MODIFY] Prompt result processing (~L2597)

Add `crowd_labels` to final prompt item:
```python
"crowd_labels": scene.get("crowd_labels", []),
```

---

### H. "NO characters" suffix fix

#### [MODIFY] L2725

```python
# Before:
if not p.get("characters", "").strip() and not p.get("has_crowd", False):

# After:
if (not p.get("characters", "").strip() 
    and not p.get("has_crowd", False)
    and not p.get("crowd_labels")):
```

---

### I. Pipeline execution order

```python
steps = [
    ("step0", self._run_step0),
    ("step1", self._run_step1),
    ("step1b", self._run_step1b),
    ("step2a", self._run_step2a),
    ("step2b", self._run_step2b),
    ("step2d", self._run_step2d),         # NEW
    ("_labels", self._extract_valid_labels),
    ("step2b_map", self._run_step2b_map),
    ("step2c", self._run_step2c),
    ("step3_1", self._run_step3_1),
    ("step3", self._run_step3),
    ("step4", self._run_step4),
    ("step5", self._run_step5),
]
```

---

## Code Impact Summary

| Line range | What changes |
|---|---|
| L141 | Step 1 prompt: add `crowd_types` instruction |
| L152-162 | Step 1 output format: add `crowd_types` field |
| L167-184 | Step 1b audit: add crowd_types audit |
| L408-434 | Step 2a-2: remove 6 fixed categories |
| NEW | Step 2d prompt + `_run_step2d()` method |
| L534,582 | Step 3.1 prompt: `present_labels` → `character_labels` |
| NEW | Step 3.1 prompt: add `crowd_labels` field |
| L683 | Step 3.2 prompt output: add `crowd_labels` |
| L920 | Data holder: add `self.crowd_data` |
| L1883-1890 | `_extract_valid_labels()`: add crowd labels |
| L2110-2127 | Step 3.1 input: add crowd_labels |
| L2379-2400 | `_build_mini_bible()`: include crowd sheets |
| L2536-2544 | Step 4 scene data: add crowd info |
| L2597 | Prompt item: add crowd_labels |
| L2725 | "NO characters" check: add crowd_labels |
| L3027-3044 | Pipeline order: insert step2d |

## Verification Plan

1. `ast.parse()` syntax check
2. Run 3-chapter test (ch 8-10)
3. Verify:
   - Step 1: `crowd_types` in each sequence
   - Step 2d: `EXT-*` labels + sheet_prompts generated
   - Step 3.1: `character_labels` (not present_labels) + `crowd_labels` per sentence
   - Step 3.2: `crowd_labels` propagated to scenes
   - Step 4: flat_prompt references `EXT-*` labels with costume details
   - "NO characters" only on truly empty scenes
