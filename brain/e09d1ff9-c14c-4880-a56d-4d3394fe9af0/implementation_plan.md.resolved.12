# Step 2 Refactor — Implementation Plan (Updated)

## Mục tiêu
1. Input từ sequences (Step 1) thay vì raw script
2. Bỏ factions hoàn toàn
3. Thêm **World Bible** (auto-generate theo thời kỳ lịch sử)
4. Age_stage 5 level
5. Dọn downstream bỏ faction references

---

## Proposed Changes

### 1. Prompts — Rewrite

#### STEP2_CHARACTERS_SYSTEM_PROMPT
- Input: danh sách sequences (có `characters`, `full_text`)
- Bỏ FACTIONS section
- Age_stage 5 level: child/teen/young_adult/mature_adult/elder
- Output: `{"characters": [...]}`

#### STEP2_LOCATIONS_SYSTEM_PROMPT  
- Input: danh sách sequences (có `location_shift`, `full_text`)
- Output: `{"locations": [...]}`

#### [NEW] STEP2_WORLD_BIBLE_PROMPT
- Input: danh sách sequences
- LLM tự nhận diện thời kỳ lịch sử
- Output:
```json
{
  "era": "Kingdom of Jerusalem, 1161-1185 AD",
  "periods": [
    {
      "period": "Early Crusader reign (1174-1177)",
      "military": {
        "crusader_infantry": "...",
        "crusader_knight": "...",
        "ayyubid_soldier": "..."
      },
      "civilian": {
        "commoner": "...",
        "noble": "...",
        "court_official": "..."
      },
      "weapons": { ... },
      "architecture": { ... }
    }
  ]
}
```

---

### 2. Code Changes — `_run_step2a/2b` + new `_run_step2c`

#### [MODIFY] `_run_step2a()` — Characters
```python
# Input: sequences từ Step 1
seq_data = [{"seq": s["sequence_id"], "characters": s.get("characters", []),
             "full_text": s["full_text"]} for s in self.sequences]
user_msg = json.dumps(seq_data, ensure_ascii=False, indent=2)
```
- Bỏ `factions` count/log
- Output: `{"characters": [...]}`

#### [MODIFY] `_run_step2b()` — Locations
```python
seq_data = [{"seq": s["sequence_id"], "location_shift": s.get("location_shift", ""),
             "full_text": s["full_text"]} for s in self.sequences]
user_msg = json.dumps(seq_data, ensure_ascii=False, indent=2)
```

#### [NEW] `_run_step2c()` — World Bible
- Checkpoint: `_step2_world_bible.json`
- Lưu vào `self.world_bible`
- Inject vào Step 3/4 như context

---

### 3. Downstream — Bỏ factions + thêm world_bible

| Vị trí | Thay đổi |
|---|---|
| `__init__` | Thêm `self.world_bible = {}`, bỏ `factions` từ `valid_labels` |
| `_extract_valid_labels()` | Bỏ faction labels |
| `_build_labels_block()` | Bỏ "Factions: ..." |
| `_validate_scene_labels()` | Bỏ `faction_labels` validation |
| STEP3 prompt schema | Bỏ `faction_labels`, thêm world_bible context |
| `_build_mini_bible()` | Bỏ factions, thêm world_bible |
| STEP4 prompt | Bỏ faction refs, inject world_bible |
| `_export_excel()` | Bỏ factions column + sheet rows |
| `StepStatus` | "Characters+Factions" → "Characters" |
| `run()` | Thêm `_run_step2c()` vào flow |

---

### 4. Pipeline Flow (Updated)

```
Step 0: Parse + Merge
Step 1: Semantic Chunking (per-chapter) → sequences with characters
Step 2a: Character Bible (from sequences) → characters
Step 2b: Location Bible (from sequences) → locations
Step 2c: World Bible (from sequences) → era/military/civilian/architecture
  ↓ Label Extraction
Step 3: Scene Design (1 call per sequence)
Step 4: Prompt Writing
Step 5: Excel Export
```

---

## Verification Plan
1. Import test
2. Xóa checkpoints Step 2/3/4 → chạy lại Baldwin IV
3. Kiểm tra: không còn `factions`/`faction_labels` trong output
4. Kiểm tra: world_bible.json có era + periods hợp lý
5. Kiểm tra: Step 3 scenes mô tả đám đông trực tiếp trong action/background
