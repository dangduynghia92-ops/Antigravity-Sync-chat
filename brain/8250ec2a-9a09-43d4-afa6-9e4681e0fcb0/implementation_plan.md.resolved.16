# Per-Sentence Visual Interpreter (Step 3.1 v2)

## Nguyên lý

Mỗi câu (sentence) trong 1 sequence được đọc **tuần tự từ đầu đến cuối** và phân loại:
- **Filmable** → giữ nguyên, chỉ bổ sung context (character, location)
- **Không filmable** → rewrite sang ngôn ngữ điện ảnh, giữ context

Mỗi câu → **1 hoặc nhiều scenes** (dựa trên duration vs scene_max).
Không bao giờ 1 scene chứa nửa câu A + nửa câu B.

```
1 câu ≤ scene_max  →  1 scene (duration = duration câu)
1 câu > scene_max  →  N scenes (chia đều, mỗi scene = 1 hành động con)
```

---

## Data Analysis (chapter test thực tế)

| Metric | Giá trị |
|---|---|
| Tổng sentences | 25 |
| Cần split (>6s) | 1 (4%) |
| Cần rewrite (abstract/metaphor) | 17 (68%) |
| Không nhắc đến người | 2 (8%) |
| Nhắc đến người nhưng gián tiếp (your, you) | 15 (60%) |

> [!IMPORTANT]
> 68% câu cần rewrite → Step 3.1 có giá trị thực sự, không phải overhead thừa.
> Chỉ 4% cần split → hầu hết câu = 1 scene, logic đơn giản.

---

## Step 3.1 — Per-Sentence Visual Interpreter

### Input (1 API call per sequence)
```json
{
  "sequence_id": "SEQ_01",
  "total_duration": 17.81,
  "characters": ["Kurdish-Leader-A", "Kurdish-Prince-A"],
  "characters_raw": ["child Yusuf ibn Ayyub, newborn"],
  "location": "Tigris-River-Raft-Night",
  "sentences": [
    {"id": 1, "text": "Black water rushes beneath a makeshift raft.", "duration": 2.54},
    {"id": 2, "text": "The wind off the Tigris River is freezing,", "duration": 1.82},
    ...
  ]
}
```

### Output
```json
{
  "sequence_id": "SEQ_01",
  "filmable_scenes": [
    {
      "sentence_id": 1,
      "original_text": "Black water rushes beneath a makeshift raft.",
      "classification": "filmable",
      "characters_present": true,
      "is_broll": false,
      "scenes": [
        {
          "visual": "Dark churning water rushes beneath a rough timber raft, [Kurdish-Leader-A] kneels gripping the edge",
          "duration": 2.54
        }
      ]
    },
    {
      "sentence_id": 4,
      "original_text": "You are a newborn, blind to the darkness,",
      "classification": "abstract_narration",
      "characters_present": true,
      "is_broll": false,
      "scenes": [
        {
          "visual": "Tiny [Kurdish-Prince-A] lies wrapped in damp wool, eyes shut, face barely visible in darkness",
          "duration": 2.13
        }
      ]
    },
    {
      "sentence_id": 8,
      "original_text": "Hours ago, your uncle drove a blade into a high-ranking official inside the walls of Tikrit.",
      "classification": "past_event",
      "characters_present": false,
      "is_broll": true,
      "scenes": [
        {
          "visual": "Dim torch-lit stone corridor inside Tikrit fortress, a toppled wooden chair, a scattered document on the floor",
          "duration": 3.0
        },
        {
          "visual": "Shadow of a man running through an arched stone doorway, torchlight flickering behind",
          "duration": 3.06
        }
      ]
    }
  ]
}
```

### Prompt — 4-Point Checklist

```
You are a Visual Interpreter for cinematic production.

## YOUR JOB
Read each sentence in order. For each sentence, run this checklist:

### Q1: FILMABLE?
Is this sentence describing a visible, physical action or event?
- YES → keep the visual content
- NO → classify and rewrite:
  * Metaphor/philosophy → CHARACTER REACTION (body language, gesture)
  * Abstract narration (you are, your life) → CHARACTER PHYSICAL STATE
  * Past/future event → ATMOSPHERIC B-ROLL (aftermath scene, empty spaces)
  * Internal feeling → CHARACTER EXPRESSION (facial, hands, posture)

### Q2: CHARACTER PRESENCE?
Are the sequence's named characters physically at this location at this moment?
- YES → the visual MUST include at least one character (position, posture, or reaction)
  Even if the sentence only describes environment (wind, water, noise),
  characters who are present MUST appear in the visual.
- NO → B-Roll scene (environment only, is_broll = true)
  Only mark NO when the sentence explicitly describes a different location
  where characters are NOT present.

### Q3: CONTINUITY?
Does this scene connect logically to the previous scene?
- Character positions must be consistent
- Actions must progress, not repeat or jump
- If previous scene shows character standing, this scene cannot show them sitting
  without a transition action

### Q4: SCENE COUNT?
- If sentence duration ≤ {SCENE_MAX}s → 1 scene, duration = sentence duration
- If sentence duration > {SCENE_MAX}s → split into N scenes
  Each sub-scene must describe a DIFFERENT action moment
  Total sub-durations must equal sentence duration

## RULES
- Process sentences IN ORDER from first to last
- Use ONLY character labels from the input
- Ground every visual in the provided location
- Write in ENGLISH
- physical descriptions must be SAFE for AI image generation
  (no blood, wounds, graphic injury — use reactions instead)
- Do NOT describe camera angles or shot types — that is NOT your job
- Each visual must be self-contained (understandable without the original text)

## OUTPUT FORMAT
Return JSON with filmable_scenes array (one entry per sentence, in order).
Return ONLY JSON, no explanation.
```

---

## Step 3.2 — Camera Cuts (giản lược)

### Input
Nhận `filmable_scenes` từ Step 3.1 (đã sentence-aligned, đã filmable).

### Việc cần làm (giữ nguyên prompt hiện tại, chỉ đổi input)
- Map `is_broll` → roll_type
- Assign shot_type (Wide/Medium/Close-up)
- Assign camera_motion (theo rules hiện có)
- Assign time_of_day
- has_crowd
- `audio_sync` = `original_text` từ Step 3.1 (tự động, không cần LLM)

### audio_sync mapping (code, không LLM)
```python
for entry in filmable_scenes:
    original_text = entry['original_text']
    for scene in entry['scenes']:
        scene['audio_sync'] = original_text  # Tất cả scenes từ 1 câu → cùng audio_sync
```

> [!TIP]
> audio_sync luôn khớp hoàn hảo vì 1 câu → 1+ scenes, không bao giờ cắt giữa câu.

---

## Edge Cases

### 1. Câu rất ngắn (<1.5s)
```
"Go." (0.8s) → 1 scene 0.8s
```
Vẫn tạo 1 scene. Scene ngắn không phải vấn đề — CapCut hiển thị ảnh 0.8s bình thường.

### 2. Câu rất dài (>2x scene_max)
```
"He gathered troops, crossed desert, reached the fortress." (15s)
→ 3 scenes: gather(5s) + cross(5s) + reach(5s)
```
LLM tách hành động trong câu thành sub-scenes.

### 3. Câu mô tả nơi khác (B-Roll)
```
"Behind them, torches ignite along the fortress walls." 
→ characters NOT present at fortress → is_broll = true
→ Scene: torch-lit fortress walls, guards moving
```

### 4. Câu metaphor nhưng characters có mặt
```
"Your bloodline carries a death sentence."
→ Q1: NOT filmable → rewrite
→ Q2: Father IS present on raft → must include him
→ Rewrite: "Father's grip tightens on the baby, jaw clenched"
```

### 5. SEQ không có named characters (SEQ_04)
```
characters: []
→ Q2 always = NO → all scenes are B-Roll
→ Focus: environment, objects, crowd
```

---

## So sánh với phương án đã commit

| | Visual Treatment (đã commit) | Per-Sentence (phương án mới) |
|---|---|---|
| Alignment | Cắt giữa câu được | Luôn khớp câu |
| Visual flow | 1 đoạn liên tục | Tuần tự câu-by-câu |
| Rewrite scope | Toàn bộ | Chỉ câu cần thiết |
| audio_sync | Tính bằng overlap math | Tự động (= original text) |
| Complexity | Đơn giản | Phức tạp hơn (checklist) |
| Character grounding | Dựa vào 1 đoạn text | Bắt buộc per-sentence (Q2) |

---

## Thay đổi code

### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

#### Step 3.1
- Thay `STEP3_1_SYSTEM_PROMPT` → prompt mới (per-sentence checklist)
- Sửa `_process_sequence_step3_1()` → gửi sentences array thay vì full_text
- Sửa `_run_step3_1()` → lưu filmable_scenes thay vì visual_treatments
- Bỏ `_overlay_audio()` → không cần nữa (audio_sync tự động)

#### Step 3.2
- Sửa `_process_sequence_step3()` → nhận filmable_scenes, gửi cho LLM assign camera
- Sửa `_run_step3()` → gán `audio_sync = original_text` bằng code sau khi LLM trả về

#### Data flow
```
Step 1 → sequences (sentence_ids, characters, location)
Step 3.1 → filmable_scenes per sequence (sentence-aligned)
Step 3.2 → scenes with camera specs + audio_sync (code-assigned)
Step 4 → prompts (dùng physical_action per scene, không cần visual_treatment)
```

---

## Verification
1. Chạy pipeline test → kiểm tra output Step 3.1
2. Mỗi sentence_id xuất hiện đúng 1 lần trong filmable_scenes
3. Sum(scene durations) == total_sequence_duration
4. Tất cả scenes có characters khi Q2=YES
5. audio_sync = original_text (không cắt giữa câu)
6. Step 3.2 scenes có shot variety (không toàn Medium Shot)

---

## Audit Findings (đã fix)

| # | Vấn đề | Trạng thái |
|---|---|---|
| 1 | characters dùng tên gốc vs label | Cần map label từ Step 2b vào input Step 3.1 |
| 2 | `physical_action` cho Step 4 | Step 3.2 gán `physical_action` = `visual` từ Step 3.1 |
| 3 | `visual_treatment` empty ở Step 4 | ✅ Đã bỏ khỏi template (code đã sửa) |
| 4 | `_overlay_audio()` thừa | Bỏ hoặc không gọi |
