# Tách Track: Step 2.5 (Visual Treatment) + Step 3 (Camera Cuts)

## Nguyên lý
Coi mỗi Sequence là 1 **khối thời gian** (Time Block). Audio và Video là 2 track song song:
- **Audio Track** = voiceover gốc (cố định, từ SRT)
- **Video Track** = chuỗi hình liên tục (Step 2.5 viết, Step 3 cắt)

```
Step 2.5: Đọc toàn bộ text → viết 1 đoạn Visual Treatment liên tục
Step 3:   Nhận Visual Treatment → cắt thành shots + gán kỹ thuật camera
Code:     Rải audio lên shots bằng toán timing
```

---

## Step 2.5 — Visual Treatment Writer

### Vai trò
Đọc narrative text → viết **1 đoạn mô tả hành động liên tục** (kéo dài bằng duration của sequence). Không quan tâm từng câu. Chỉ lấy tổng ý nghĩa.

### Input (mỗi sequence)
```json
{
  "sequence_id": "SEQ_01",
  "total_duration": 17.81,
  "characters": ["Kurdish-Leader-A", "Kurdish-Prince-A"],
  "location": "Tigris-River-Raft-Night",
  "full_text": "Black water rushes beneath a makeshift raft. The wind off the Tigris River is freezing, biting through the damp wool wrapped around your fragile frame. You are a newborn, blind to the darkness, but your very first sensation is the violent pitch of a desperate escape. You are born into a prominent Kurdish family, yet your bloodline carries a sudden death sentence."
}
```

### Output
```json
{
  "sequence_id": "SEQ_01",
  "visual_treatment": "A makeshift timber raft pitches violently on churning black water of the Tigris River at night. Freezing spray crashes over the rough-hewn logs. [Kurdish-Leader-A] kneels on the lashed timber in a soaked dark wool kaftan, his broad shoulders hunched against the wind. He clutches a tiny wool bundle — [Kurdish-Prince-A] — tightly against his chest, one large mitten-shaped hand cupping the baby's head. The raft lurches and groans. He shifts his weight to keep balance, jaw clenched, eyes scanning the dark riverbank behind them. His grip on the bundle tightens as the current drags the raft further from shore."
}
```

### Prompt (STEP2_5_SYSTEM_PROMPT)
```
You are a Visual Treatment Writer for cinematic production.

## YOUR JOB
Read the narrative text of a sequence. Write ONE continuous visual description 
that covers the ENTIRE duration as a flowing cinematic moment.

## RULES
1. Write as if describing what a CAMERA SEES — continuous, flowing action
2. Use [Character-Labels] from the input. Do NOT invent new characters
3. Ground the action in the provided location
4. Every action must be PHYSICALLY VISIBLE (filmable)
5. Translate non-filmable text:
   - Metaphor/philosophy → CHARACTER REACTION (body language, gesture)
   - Abstract concept → CONCRETE OBJECT or ENVIRONMENTAL DETAIL
   - Past/future commentary → ATMOSPHERIC DETAIL (light, wind, stillness)
6. Do NOT describe camera angles, shot types, or editing — that's not your job
7. Do NOT copy the narration word-for-word. REWRITE into visual action
8. The treatment must feel like ONE CONTINUOUS MOMENT, not a list of disconnected images
9. Include enough physical detail for the given duration:
   - <10s: 2-3 actions
   - 10-20s: 4-6 actions
   - 20-30s: 6-8 actions

## CONTENT SAFETY
FORBIDDEN: blood, wounds, graphic injury, self-harm, weapons piercing bodies.
USE INSTEAD: reactions (grimacing face, turned-away gaze, clenched fists).

## OUTPUT FORMAT
Return JSON:
{
  "sequence_id": "SEQ_01",
  "visual_treatment": "Continuous visual description..."
}
Return ONLY the JSON, no explanation.
```

---

## Step 3 — Camera Cuts (sửa lại)

### Thay đổi so với hiện tại
| Hiện tại | Mới |
|---|---|
| Nhận `full_text` (narrative gốc) | Nhận `visual_treatment` (đã filmable) |
| Phase 1: LLM tự tổng hợp visual_event | **Bỏ Phase 1** — đã có sẵn |
| LLM gán `audio_sync` | **Bỏ** — code tính sau |
| LLM lo cả creative + technical | Chỉ lo **technical** (shot, motion, timing) |

### Input mới
```json
{
  "sequence_id": "SEQ_01",
  "total_duration": 17.81,
  "visual_treatment": "A makeshift timber raft pitches violently...",
  "characters": ["Kurdish-Leader-A", "Kurdish-Prince-A"],
  "location": "Tigris-River-Raft-Night"
}
```

### Output (giữ nguyên format, bỏ `audio_sync`)
```json
{
  "sequence_id": "SEQ_01",
  "locked_location": "Tigris-River-Raft-Night",
  "scenes": [
    {
      "global_scene_id": "SEQ_01_SCN_01",
      "duration": 5.0,
      "character_labels": ["Kurdish-Leader-A", "Kurdish-Prince-A"],
      "shot_type": "Wide Shot",
      "roll_type": "A-Roll",
      "camera_motion": "Slow Pan",
      "time_of_day": "night",
      "physical_action": "Raft pitches on churning water, father kneels holding baby",
      "has_crowd": false
    },
    ...
  ]
}
```

### Prompt sửa
- Bỏ Phase 1 (Visual Event Synthesis) — đã có `visual_treatment`
- Bỏ Rule 8 (Visual Translation) — đã dịch ở Step 2.5
- Bỏ `audio_sync` khỏi output format
- Thêm: "Decompose the `visual_treatment` into camera angles"
- Giữ nguyên: Rule 2 (Time Math), Rule 3-7 (shot/motion/safety rules)

---

## Audio Overlay — Thuần code, không LLM

### Thuật toán
```python
def overlay_audio(scenes, sentences):
    """Rải audio lên scenes bằng timing math."""
    # 1. Tính cumulative time cho scenes
    scene_start = 0.0
    for scene in scenes:
        scene['start_time'] = scene_start
        scene['end_time'] = scene_start + scene['duration']
        scene_start += scene['duration']
    
    # 2. Tính cumulative time cho sentences
    sent_start = 0.0
    for sent in sentences:
        sent['start_time'] = sent_start
        sent['end_time'] = sent_start + sent['duration']
        sent_start += sent['duration']
    
    # 3. Cho mỗi scene, tìm sentences overlap
    for scene in scenes:
        overlapping = []
        for sent in sentences:
            # Overlap nếu: sent_start < scene_end AND sent_end > scene_start
            if sent['start_time'] < scene['end_time'] and sent['end_time'] > scene['start_time']:
                overlapping.append(sent['text'])
        scene['audio_sync'] = ' '.join(overlapping)
    
    return scenes
```

### Ví dụ thực tế (SEQ_01)
```
Sentences:
  S1: [0.0 - 2.54] "Black water rushes beneath a makeshift raft."
  S2: [2.54 - 4.36] "The wind off the Tigris River is freezing,"
  S3: [4.36 - 7.26] "biting through the damp wool..."
  S4: [7.26 - 9.39] "You are a newborn..."
  S5: [9.39 - 13.10] "but your very first sensation..."
  S6: [13.10 - 15.17] "You are born into a prominent Kurdish family,"
  S7: [15.17 - 17.81] "yet your bloodline carries a sudden death sentence."

Scenes (Step 3 output):
  SCN_01: [0.0 - 5.0] Wide Shot
  SCN_02: [5.0 - 9.0] Medium Shot
  SCN_03: [9.0 - 13.0] Close-up
  SCN_04: [13.0 - 17.81] Medium Shot

Audio overlay result:
  SCN_01 audio_sync = S1 + S2 + S3(bắt đầu)  ← overlap [0-5]
  SCN_02 audio_sync = S3(tiếp) + S4            ← overlap [5-9]
  SCN_03 audio_sync = S5                        ← overlap [9-13]
  SCN_04 audio_sync = S6 + S7                   ← overlap [13-17.81]
```

---

## Thay đổi code

### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

#### Thêm mới
- `STEP2_5_VISUAL_TREATMENT_PROMPT` — prompt constant
- `_run_step2_5()` — gọi LLM cho mỗi sequence, lưu visual_treatment
- `_overlay_audio()` — hàm thuần code rải audio lên scenes

#### Sửa
- `_run_step3()` — inject visual_treatment vào input thay vì full_text
- `STEP3_SYSTEM_PROMPT` — bỏ Phase 1, bỏ audio_sync, bỏ Rule 8
- `_process_sequence_step3()` — user message dùng visual_treatment
- Pipeline flow: step2c → **step2.5** → step3

#### UI
- Thêm step2.5 progress indicator

---

## Verification
1. Chạy pipeline test → so sánh output cũ vs mới
2. Kiểm tra: sum(scene.duration) == total_sequence_duration
3. Kiểm tra: audio overlay bao phủ tất cả sentences (không bỏ sót)
4. Kiểm tra: visual_treatment có đủ filmable actions cho duration
5. Kiểm tra: Step 3 scenes có mạch lạc hơn (không còn 1:1 slideshow)
