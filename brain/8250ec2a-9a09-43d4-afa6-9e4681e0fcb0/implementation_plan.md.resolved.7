# Step 0: SRT + TXT Alignment Pre-processor

## Mục tiêu

Step 0 là **bước tiền xử lý độc lập**: nhận SRT + TXT → output ra **file kết quả** (corrected SRT) lưu trong folder riêng → các bước sau đọc file này.

```
Input:                          Output (folder aligned/):
  ch_01.srt  +  ch_01.txt  →     ch_01.srt   ← corrected: text đúng + timing đúng + có dấu câu
  ch_02.srt  +  ch_02.txt  →     ch_02.srt
  ch_03.srt  +  ch_03.txt  →     ch_03.srt
```

> [!IMPORTANT]
> - Chỉ chạy khi có CẢ SRT + TXT pair
> - Output là file SRT chuẩn (text đúng + timing từ SRT gốc + dấu câu từ TXT)
> - Chapter nào pass verify → save vào `aligned/` → không chạy lại
> - Re-run chỉ xử lý chapters chưa có trong `aligned/`

---

## Phase 1: UI — Scan & Pair

### [MODIFY] [video_prompt_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/video_prompt_tab.py)

#### Tree Widget: 4 cột mới

```
| Chapter Name                    | SRT         | TXT         | Status      |
|---------------------------------|-------------|-------------|-------------|
| ch_01_Level_1__Vulnerability    | ✅ .srt     | ✅ .txt     | Ready       |
| ch_02_Level_2__Resignation      | ✅ .srt     | ❌ missing  | Missing TXT |
| ch_03_Level_3__Endurance        | ✅ .srt     | ✅ .txt     | Ready       |
```

- Bỏ cột **Style** (dùng combo ở config area)
- Bỏ cột **Progress** (dùng log)
- Bỏ buttons **Apply Style**, **Apply All**

#### Scan Logic

```python
def _scan_folder(self):
    # 1. Scan tất cả *.srt
    srt_files = {basename: path for *.srt in folder}
    
    # 2. Với mỗi SRT, tìm *.txt cùng basename
    for basename, srt_path in srt_files:
        txt_path = srt_path.replace('.srt', '.txt')
        has_txt = os.path.exists(txt_path)
        
        # 3. Thêm vào tree
        add_row(basename, srt="✅", txt="✅" or "❌", status="Ready" or "Missing TXT")
```

#### Run Validation

```python
def _run_all(self):
    missing = [row for row in rows if not row.has_txt]
    if missing:
        log(f"Cannot run: {len(missing)} chapter(s) missing TXT pair")
        return  # KHÔNG chạy
```

#### Data truyền vào pipeline

```python
chapter_pairs = [
    {"srt_path": "ch_01.srt", "txt_path": "ch_01.txt"},
    {"srt_path": "ch_02.srt", "txt_path": "ch_02.txt"},
    ...
]
```

---

## Phase 2: LLM Correct (per-chapter)

### [MODIFY] [srt_sentence_parser.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/srt_sentence_parser.py)

Thêm function `correct_srt_with_txt(srt_cues, txt_content, api_client, tier)`:

#### LLM Input

```
=== ORIGINAL SCRIPT (correct spelling, has punctuation) ===
Black water rushes beneath a makeshift raft. The wind off the Tigris River
is freezing, biting through the damp wool wrapped around your fragile frame...

=== SRT CUES (correct timing, may have wrong spelling, no punctuation) ===
1|0.000|2.800|black water rushes beneath a makeshift raft
2|3.166|5.266|the wind off the Tigris River is freezing
3|5.266|8.400|biting through the damp wool wrapped around your fragile frame
...

=== TASK ===
For each SRT cue:
1. Fix spelling to match the ORIGINAL SCRIPT
2. Add punctuation (. , ! ?) from the ORIGINAL SCRIPT at correct positions
3. Fix capitalization to match the ORIGINAL SCRIPT
Return ONLY corrected text per cue. Keep SAME number of cues. Do NOT merge or split cues.

Return JSON array:
[
  {"id": 1, "text": "Black water rushes beneath a makeshift raft."},
  {"id": 2, "text": "The wind off the Tigris River is freezing,"},
  ...
]
```

#### Code ghép timing

```python
for original_cue, llm_item in zip(srt_cues, llm_output):
    corrected = SRTSegment(
        index=original_cue.index,
        start_time=original_cue.start_time,   # ← giữ nguyên từ SRT
        end_time=original_cue.end_time,         # ← giữ nguyên từ SRT
        text=llm_item["text"],                   # ← text đã sửa từ LLM
    )
```

---

## Phase 3: Code Verify

### [MODIFY] [srt_sentence_parser.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/srt_sentence_parser.py)

Thêm function `verify_corrected_srt(corrected_cues, original_srt_cues, txt_content)`:

#### Check 1: Cue count
```python
if len(corrected) != len(original):
    return VerifyResult(ok=False, error="cue_count", 
                        detail=f"Expected {len(original)}, got {len(corrected)}")
```

#### Check 2: Timecode integrity
```python
for cue in corrected:
    if cue.end_time <= cue.start_time:
        return VerifyResult(ok=False, error="bad_timing", detail=f"Cue {cue.id}")
```

#### Check 3: Text coverage (word count ratio ±10%)
```python
corrected_words = count_words(join(all corrected texts))
original_words = count_words(txt_content)
ratio = corrected_words / original_words
if not (0.9 <= ratio <= 1.1):
    return VerifyResult(ok=False, error="word_count", 
                        detail=f"Ratio {ratio:.0%}, expected ~100%")
```

#### Check 4: Key name preservation
```python
# Lấy tên riêng từ TXT (viết hoa, > 1 từ)
proper_nouns = extract_proper_nouns(txt_content)  # ["Shirkuh", "Najm ad-Din Ayyub", ...]
corrected_full = join(all corrected texts)
missing = [name for name in proper_nouns if name not in corrected_full]
if missing:
    return VerifyResult(ok=False, error="missing_names", detail=missing)
```

### Verify Fail → LLM Retry

```
Verify fail
    ↓
Gửi LẠI cho LLM: kết quả cũ + danh sách lỗi cụ thể
    ↓
"Here is your previous output and the errors found:
 - Cue 15 missing: expected 33 cues, got 32
 - Name 'Shirkuh' not found in output
 Please fix ONLY the problematic cues and return the corrected JSON."
    ↓
LLM trả partial fix → Code merge vào kết quả cũ
    ↓
Re-verify
    ↓
Pass → save  |  Fail lần 2 → DỪNG pipeline + log chi tiết
```

---

## Phase 4: Output & Checkpoint

### Output folder structure

```
project_folder/
├── ch_01.srt                    ← input SRT gốc
├── ch_01.txt                    ← input TXT gốc
├── ch_02.srt
├── ch_02.txt
├── ...
└── aligned/                     ← OUTPUT folder
    ├── ch_01.srt                ← corrected SRT (text đúng + timing đúng)
    ├── ch_02.srt
    ├── ch_03.srt
    └── ...
```

#### File corrected SRT format (chuẩn SRT):
```
1
00:00:00,000 --> 00:00:02,800
Black water rushes beneath a makeshift raft.

2
00:00:03,166 --> 00:00:05,266
The wind off the Tigris River is freezing,

3
00:00:05,266 --> 00:00:08,400
biting through the damp wool wrapped around your fragile frame.
```

#### Per-chapter checkpoint logic

```python
def _run_step0(self):
    aligned_dir = os.path.join(project_folder, "aligned")
    
    for chapter in chapter_pairs:
        basename = os.path.splitext(os.path.basename(chapter["srt_path"]))[0]
        output_path = os.path.join(aligned_dir, f"{basename}.srt")
        
        # Skip nếu đã có file aligned
        if os.path.exists(output_path):
            self._log(f"[Step 0] ⏭ {basename}: already aligned")
            continue
        
        # Process: LLM correct → verify → save
        corrected = correct_srt_with_txt(...)
        result = verify_corrected_srt(...)
        
        if result.ok:
            save_as_srt(corrected, output_path)
            self._log(f"[Step 0] ✅ {basename}: saved to aligned/")
        else:
            # Retry logic...
    
    # Sau khi tất cả chapters aligned → pipeline đọc từ aligned/ folder
    aligned_files = sorted(glob(aligned_dir + "/*.srt"))
    # Parse aligned SRTs → sentences (giờ có punctuation → tách đúng)
```

---

## Phase 5: Pipeline Integration

### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

#### Constructor mới

```python
def __init__(self, ..., chapter_pairs: List[dict] = None, ...):
    self.chapter_pairs = chapter_pairs or []
    # chapter_pairs = [{"srt_path": "...", "txt_path": "..."}, ...]
```

#### Step 0 Flow

```
1. Tạo aligned/ folder
2. Per-chapter:
   a. Check aligned/ đã có → skip
   b. Parse SRT gốc → cues
   c. Read TXT gốc → clean text
   d. LLM correct (1 API call, tier_user)
   e. Code verify
   f. Fail → LLM retry with error details → re-verify
   g. Pass → save corrected SRT to aligned/
3. Đọc TẤT CẢ aligned/*.srt → parse_srt_to_sentences() (existing code)
4. Output: self.sentences, self.cleaned_text (giống hiện tại)
```

> [!NOTE]
> Từ bước 3 trở đi, flow **hoàn toàn giống hiện tại**. `parse_srt_to_sentences()` nhận corrected SRT (có punctuation) → tách sentences đúng. Steps 1-5 không thay đổi.

---

## Files Modified

| File | Thay đổi |
|---|---|
| `ui/video_prompt_tab.py` | Tree 4 cột mới, scan logic pair SRT↔TXT, bỏ Style column/buttons, validation trước run |
| `core/srt_sentence_parser.py` | Thêm `correct_srt_with_txt()`, `verify_corrected_srt()`, `save_as_srt()` |
| `core/video_pipeline.py` | Constructor nhận `chapter_pairs`, Step 0 flow mới (aligned/ folder + per-chapter checkpoint) |

## Verification Plan

### Test 1: UI
- Scan folder có 3 SRT + 2 TXT → 1 row hiện "Missing TXT" → Run bị chặn

### Test 2: Alignment
- Ch_01 Saladin SRT+TXT → verify aligned/ch_01.srt có:
  - "Najm ad-Din Ayyub" (không phải "Najmad Dina Yub")
  - Dấu câu đúng vị trí
  - 33 cues giữ nguyên
  - Timing giữ nguyên

### Test 3: Verify Retry
- Nếu LLM trả 32 cues → retry gửi lỗi lên → LLM fix → 33 cues → pass

### Test 4: Checkpoint
- Chạy 15 chapters, fail ở ch_08 → aligned/ có 7 files
- Re-run → skip 7 files đã có, chỉ chạy 8-15

### Test 5: Full Pipeline
- Aligned/ 15 files → Step 1 nhận ~488 sentences (không phải 15) → pipeline hoàn thành
