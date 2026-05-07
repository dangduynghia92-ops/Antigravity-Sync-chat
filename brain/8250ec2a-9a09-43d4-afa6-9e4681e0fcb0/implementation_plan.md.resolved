# Tách Track: Step 3.1 (Visual Treatment) + Step 3.2 (Camera Cuts)

## Nguyên lý
Mỗi Sequence = 1 **khối thời gian**. Audio và Video là 2 track song song:
- **Audio Track** = voiceover gốc (cố định, từ SRT)
- **Video Track** = chuỗi hình liên tục (Step 3.1 viết, Step 3.2 cắt)

```
Step 3.1: Đọc toàn bộ text → viết 1 Visual Treatment liên tục
Step 3.2: Nhận Visual Treatment → cắt thành shots + gán kỹ thuật camera
Code:     Rải audio lên shots bằng toán timing (contrapuntal editing tự nhiên)
```

---

## Step 3.1 — Visual Treatment Writer

### Vai trò
Đọc narrative text → viết **1 đoạn mô tả hành động liên tục** cho cả sequence. Không quan tâm từng câu. Chỉ lấy tổng ý nghĩa.

### Input
```json
{
  "sequence_id": "SEQ_01",
  "total_duration": 17.81,
  "characters": ["Kurdish-Leader-A", "Kurdish-Prince-A"],
  "location": "Tigris-River-Raft-Night",
  "full_text": "Black water rushes beneath a makeshift raft..."
}
```

### Output
```json
{
  "sequence_id": "SEQ_01",
  "visual_treatment": "A makeshift timber raft pitches violently on churning black water of the Tigris River at night. Freezing spray crashes over the rough-hewn logs. [Kurdish-Leader-A] kneels on the lashed timber in a soaked dark wool kaftan, his broad shoulders hunched against the wind. He clutches a tiny wool bundle — [Kurdish-Prince-A] — tightly against his chest, one large mitten-shaped hand cupping the baby's head. The raft lurches and groans. He shifts his weight to keep balance, jaw clenched, eyes scanning the dark riverbank behind them. His grip on the bundle tightens as the current drags the raft further from shore."
}
```

### Prompt (STEP3_1_SYSTEM_PROMPT)

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
6. Do NOT describe camera angles, shot types, or editing — that is Step 3.2's job
7. Do NOT copy the narration word-for-word. REWRITE into visual action
8. The treatment must feel like ONE CONTINUOUS MOMENT, not a list of images

## ACTION DENSITY (CRITICAL)
Each action must describe a DIFFERENT physical movement.
Do NOT write one long flowing action — write multiple short distinct actions.
Required density based on duration:
   - <10s: 2-3 distinct actions
   - 10-20s: 4-6 distinct actions
   - 20-30s: 6-8 distinct actions

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

## Step 3.2 — Camera Cuts

### Vai trò
Nhận visual_treatment (đã filmable) → cắt thành camera shots + gán kỹ thuật.
**Chỉ lo kỹ thuật camera**, không cần đọc narrative gốc.

### Input
```json
{
  "sequence_id": "SEQ_01",
  "total_duration": 17.81,
  "visual_treatment": "A makeshift timber raft pitches violently...",
  "characters": ["Kurdish-Leader-A", "Kurdish-Prince-A"],
  "location": "Tigris-River-Raft-Night"
}
```

### Output (giữ format hiện tại, bỏ `audio_sync` — code tính sau)
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
      "physical_action": "Raft pitches on churning water, father kneels shielding baby",
      "has_crowd": false
    }
  ]
}
```

### Thay đổi prompt so với Step 3 hiện tại
| Bỏ | Lý do |
|---|---|
| Phase 1 (Visual Event Synthesis) | Đã có visual_treatment |
| Rule 8 (Visual Translation Strategy) | Đã dịch ở Step 3.1 |
| `audio_sync` trong output | Code tính bằng toán |
| `visual_event` trong output | Đã có visual_treatment |

| Giữ nguyên | |
|---|---|
| Rule 1: Label Lock | |
| Rule 2: Time Math | |
| Rule 3: A-Roll / B-Roll | |
| Rule 4: Shot Types (3 loại) | |
| Rule 5: Physical Action Only | |
| Rule 6: Has Crowd | |
| Rule 7: Camera Motion | |
| Rule 9: Content Safety | |

| Thêm mới | |
|---|---|
| Anti-Repeat Rule | "Do NOT repeat the same physical action across multiple scenes. If actions from visual_treatment run out, use environment detail or character's lingering expression for B-Roll." |
| Input instruction | "Decompose the visual_treatment into camera angles. Each scene = a different angle of the SAME continuous event." |

---

## Audio Overlay — Code (không LLM)

### Thuật toán
```python
def overlay_audio(scenes: list, sentences: list) -> list:
    """Rải audio lên scenes bằng timing overlap."""
    # Cumulative time cho scenes
    t = 0.0
    for sc in scenes:
        sc['start_time'] = t
        sc['end_time'] = t + sc['duration']
        t += sc['duration']

    # Cumulative time cho sentences
    t = 0.0
    for sent in sentences:
        sent['start_time'] = t
        sent['end_time'] = t + sent['duration']
        t += sent['duration']

    # Overlap: sentence thuộc scene nếu có giao thời gian
    for sc in scenes:
        parts = []
        for sent in sentences:
            if sent['start_time'] < sc['end_time'] and sent['end_time'] > sc['start_time']:
                parts.append(sent['text'])
        sc['audio_sync'] = ' '.join(parts)

    return scenes
```

### Lưu ý: Contrapuntal Editing
Audio và visual **không cần khớp nghĩa đen**:
```
🎧 "Black water rushes beneath a raft"
🎬 Close-up mặt em bé

→ Hiệu ứng montage: nghe nguy hiểm + thấy mong manh = tension
```
Đây là kỹ thuật voiceover chuẩn trong phim tài liệu/tiểu sử. Tách Track tạo hiệu ứng này **tự nhiên**.

---

## Thay đổi code

### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

#### Thêm mới
- `STEP3_1_VISUAL_TREATMENT_PROMPT` — prompt constant (~800 chars)
- `_run_step3_1()` — gọi LLM cho mỗi sequence, lưu visual_treatment vào `self.visual_treatments`
- `overlay_audio(scenes, sentences)` — hàm thuần code

#### Sửa
- `STEP3_SYSTEM_PROMPT` → `STEP3_2_SYSTEM_PROMPT` — bỏ Phase 1, bỏ Rule 8, bỏ audio_sync, thêm Anti-Repeat
- `_run_step3()` → `_run_step3_2()` — inject visual_treatment thay full_text
- `_process_sequence_step3()` — user message dùng visual_treatment
- Pipeline flow: step2c → **step3.1** → **step3.2** → step4
- Sau Step 3.2: gọi `overlay_audio()` để tính audio_sync

#### UI
- Thêm step3.1 progress indicator (giữa step2c và step3.2)

---

## Verification
1. Chạy pipeline test → so sánh scenes cũ vs mới
2. visual_treatment: đủ filmable actions cho duration
3. Step 3.2: không còn 1:1 slideshow
4. Audio overlay: tất cả sentences được cover (không bỏ sót)
5. Timing: sum(scene.duration) == total_sequence_duration
