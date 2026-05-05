# Step 0 Overhaul: SRT + TXT Alignment

## Problem

SRT từ TTS thường **không có dấu câu** + **sai chính tả** tên riêng → parser gộp toàn bộ thành 1 sentence → Step 1 fail.

Giải pháp: Dùng **TXT gốc** (text đúng) + **SRT** (timing đúng) → LLM merge → code verify.

> [!IMPORTANT]
> **Chỉ chạy pipeline khi có CẢ SRT + TXT pair.** Không có fallback. Không có callback.

---

## Phase 1: UI — Scan & Pair Files

### [MODIFY] [video_prompt_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py)

#### Scan Logic mới

```
User clicks "Scan Folder"
    ↓
1. Scan tất cả *.srt trong folder (recursive)
2. Với mỗi .srt → tìm .txt cùng basename trong cùng folder
3. Hiển thị trong tree widget
```

#### Tree Widget Columns mới

| Chapter | SRT File | TXT File | Status |
|---|---|---|---|
| ch_01_Level_1__Vulnerability | ✅ ch_01...srt | ✅ ch_01...txt | Ready |
| ch_02_Level_2__Resignation | ✅ ch_02...srt | ❌ _(missing)_ | **Missing TXT** |
| ch_03_Level_3__Endurance | ✅ ch_03...srt | ✅ ch_03...txt | Ready |

- **Cột 1**: SRT file (luôn có — đây là file scan chính)
- **Cột 2**: TXT file (auto-match bằng tên, nếu không có → hiện trống/đỏ)
- **Status**: `Ready` khi có cả 2, `Missing TXT` khi thiếu

#### Run validation

Trước khi chạy pipeline:
- Kiểm tra TẤT CẢ rows có cả SRT + TXT
- Nếu bất kỳ row nào thiếu → **hiện lỗi, KHÔNG cho chạy**
- Message: `"Cannot run: X chapter(s) missing TXT pair file"`

#### Data structure truyền vào pipeline

```python
# Mỗi chapter giờ là dict chứa cả 2 paths
chapter_pairs = [
    {"srt_path": "ch_01.srt", "txt_path": "ch_01.txt"},
    {"srt_path": "ch_02.srt", "txt_path": "ch_02.txt"},
    ...
]
```

Thay vì `srt_paths: List[str]` → chuyển sang `chapter_pairs: List[dict]`.

---

## Phase 2: LLM Correct SRT Text (Step 0.5)

### [MODIFY] [srt_sentence_parser.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/srt_sentence_parser.py)

Thêm function `correct_srt_with_txt()`:

#### Input

```
SRT cues:
  1|00:00:00.000|00:00:02.800|black water rushes beneath a makeshift raft
  2|00:00:03.166|00:00:05.266|the wind off the Tigris River is freezing
  ...

TXT gốc:
  Black water rushes beneath a makeshift raft. The wind off the Tigris River
  is freezing, biting through the damp wool wrapped around your fragile frame...
```

#### LLM Task

Prompt yêu cầu LLM:
1. So sánh từng SRT cue với TXT gốc
2. **Fix chính tả** mỗi cue cho khớp TXT (ví dụ "Najmad Dina Yub" → "Najm ad-Din Ayyub")
3. **Thêm dấu câu** từ TXT gốc vào đúng vị trí trong mỗi cue (`. , ! ?`)
4. **KHÔNG thay đổi số cue**, KHÔNG gộp/tách cue
5. **KHÔNG thay đổi timing** — copy nguyên từ SRT

#### LLM Output (JSON)

```json
[
  {"id": 1, "text": "Black water rushes beneath a makeshift raft."},
  {"id": 2, "text": "The wind off the Tigris River is freezing,"},
  {"id": 3, "text": "biting through the damp wool wrapped around your fragile frame."}
]
```

> [!NOTE]
> LLM **chỉ trả text đã sửa**. Timing giữ nguyên từ SRT — code sẽ ghép lại.

#### Code ghép timing

```python
# SRT cues giữ timing gốc
corrected_segments = []
for original_cue, llm_result in zip(srt_cues, llm_output):
    corrected_segments.append(SRTSegment(
        index=original_cue.index,
        start_time=original_cue.start_time,   # ← từ SRT
        end_time=original_cue.end_time,         # ← từ SRT
        text=llm_result["text"],                 # ← từ LLM (text đúng)
    ))
```

→ Sau đó gọi `parse_srt_to_sentences()` hiện tại với corrected segments. Giờ punctuation có → tách sentence đúng.

---

## Phase 3: Code Verification (Step 0.7)

### [MODIFY] [srt_sentence_parser.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/srt_sentence_parser.py)

Thêm function `verify_corrected_srt()` — **100% code, không dùng LLM**:

#### Check 1: Cue Count Match
```python
assert len(corrected_cues) == len(original_srt_cues), "Cue count mismatch"
```

#### Check 2: Timecode Integrity
```python
for cue in corrected_cues:
    assert cue.start_time < cue.end_time, f"Cue {cue.id}: negative duration"
    assert cue.start_time >= 0, f"Cue {cue.id}: negative start"

# Monotonically increasing
for i in range(1, len(corrected_cues)):
    assert corrected_cues[i].start_time >= corrected_cues[i-1].start_time, \
        f"Cue {i}: time goes backward"
```

#### Check 3: Text Coverage
```python
# Gộp tất cả corrected text → normalize → so sánh word count vs TXT gốc
corrected_words = normalize(join(all corrected texts))
original_words = normalize(txt_content)

# Word count tolerance: ±10%
ratio = len(corrected_words) / len(original_words)
assert 0.9 <= ratio <= 1.1, f"Word count mismatch: {ratio:.0%}"
```

#### Check 4: No Missing Sentences
```python
# Tách TXT gốc thành sentences bằng punctuation
# Với mỗi TXT sentence → check tồn tại (fuzzy) trong corrected text
for txt_sentence in original_sentences:
    key_words = extract_key_words(txt_sentence)  # tên riêng, số, v.v.
    assert any(kw in corrected_full_text for kw in key_words), \
        f"Missing sentence: {txt_sentence[:50]}..."
```

#### Kết quả verification

- **PASS** → tiếp tục pipeline
- **FAIL** → log chi tiết lỗi gì + dừng pipeline

---

## Phase 4: Pipeline Integration

### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

#### Constructor

```python
def __init__(self, ..., chapter_pairs: List[dict] = None, ...):
    # chapter_pairs = [{"srt_path": "...", "txt_path": "..."}, ...]
    self.chapter_pairs = chapter_pairs or []
```

#### Step 0 Flow mới

```python
def _run_step0(self):
    for chapter in self.chapter_pairs:
        srt_path = chapter["srt_path"]
        txt_path = chapter["txt_path"]

        # 1. Parse SRT → raw cues
        srt_cues = parse_srt_file(srt_path)

        # 2. LLM correct text (1 API call)
        corrected_cues = correct_srt_with_txt(
            srt_cues, txt_path,
            api_client=self.api_client,
            tier=self.tier_user,
        )

        # 3. Code verify
        verify_corrected_srt(corrected_cues, srt_cues, txt_path)

        # 4. Parse corrected cues → Sentences
        sentences = parse_corrected_to_sentences(corrected_cues)

        all_sentences.extend(sentences)
```

#### Checkpoint

Corrected SRT sẽ **save checkpoint** (tránh re-call LLM khi re-run):
```
_step0_corrected_ch01.json
_step0_corrected_ch02.json
...
```

---

## Summary: Complete Step 0 Flow

```
User scans folder
    ↓
UI: Match SRT ↔ TXT pairs (hiển thị cả 2 cột)
    ↓
User confirms all pairs ready → Click Run
    ↓
Step 0 (per chapter):
    ├── Parse SRT → raw cues (timing)
    ├── Read TXT → original text
    ├── LLM: Fix spelling + add punctuation (1 call)
    ├── Code: Ghép timing SRT + text LLM → corrected cues
    ├── Code: Verify (cue count, timecodes, text coverage)
    └── Code: Split sentences by punctuation + interpolate timing
    ↓
Output: sentences[] (text đúng + timing đúng)
    ↓
Step 1, 2, 3, 4... (unchanged)
```

---

## Files Modified

| File | Changes |
|---|---|
| `ui/video_prompt_tab.py` | Scan logic, tree columns, pair validation, constructor params |
| `core/srt_sentence_parser.py` | `correct_srt_with_txt()`, `verify_corrected_srt()`, `parse_corrected_to_sentences()` |
| `core/video_pipeline.py` | Constructor (`chapter_pairs`), `_run_step0()` flow |

## Verification Plan

### Test 1: UI Pairing
- Scan folder có 3 SRT + 2 TXT → verify 1 row hiện "Missing TXT"
- Click Run → verify bị chặn

### Test 2: Correction Quality
- Chạy ch_01 (Saladin) SRT+TXT → verify:
  - "Najmad Dina Yub" → "Najm ad-Din Ayyub"
  - Dấu câu xuất hiện đúng vị trí
  - ~15-25 sentences (không phải 1)

### Test 3: Verification Catches Errors
- Mock LLM trả về thiếu 1 cue → verify pipeline dừng + log lỗi

### Test 4: Full Pipeline
- Chạy full 15 chapters Saladin → verify Step 1 nhận đúng ~488 sentences thay vì 15
