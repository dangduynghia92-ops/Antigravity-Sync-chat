# CapCut Assembler Tab — Final Implementation Plan

## Tổng quan

Tab mới trong app PyQt6 đọc file `*_assembly.json` → tạo draft CapCut offline (không cần server).

```
[Bạn tạo riêng]                    [Tab mới build]
step3 + SRT + ảnh                   assembly.json → CapCut draft
    ↓                                    ↓
assembly_manifest.json  ──input──→  CapCut Assembler Tab
                                         ↓
                                    Draft folder → CapCut
```

---

## Input Contract: `assembly_manifest.json`

```json
{
  "chapter": "ch_01_Level_1__Vulnerability",
  "tracks": [
    {
      "index": 1,
      "image_file": "1_A_stylized_historical_animatio_s1.jpg",
      "start": 0.000,
      "end": 2.537,
      "subtitle": "Black water rushes beneath a makeshift raft."
    },
    {
      "index": 2,
      "image_file": "2_A_stylized_historical_animatio_s1.jpg",
      "start": 3.267,
      "end": 8.189,
      "subtitle": "The wind off the Tigris River is freezing, biting through the damp wool wrapped around your fragile frame."
    }
  ]
}
```

| Field | Type | Bắt buộc | Mô tả |
|-------|------|----------|--------|
| `chapter` | string | ✅ | Tên chapter — dùng match audio file |
| `tracks[].index` | int | ✅ | STT sắp xếp trên timeline |
| `tracks[].image_file` | string | ✅ | Tên file ảnh (không path) |
| `tracks[].start` | float | ✅ | Giây bắt đầu (trong chapter, từ 0) |
| `tracks[].end` | float | ✅ | Giây kết thúc (trong chapter, từ 0) |
| `tracks[].subtitle` | string | ❌ | Text subtitle (optional) |

---

## UI Layout

```
┌─────────────────────────────────────────────────────────┐
│  📁 Input Folders                                        │
│  Manifest folder:  [________________________] [Browse]   │
│  Image folder:     [________________________] [Browse]   │
│  Audio folder:     [________________________] [Browse]   │
│                                                          │
│  ⚙ Project Settings                                     │
│  ┌─────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │ Resolution   │ │ Transition   │ │ Trans. dur.  │     │
│  │ [1920x1080▼] │ │ [Dissolve ▼] │ │ [0.5s     ▼] │     │
│  └─────────────┘ └──────────────┘ └──────────────┘     │
│  ☑ Ken Burns (slow zoom)                                │
│  ☑ Include subtitle track                               │
│                                                          │
│  ⏱ Chapter Gap                                          │
│  ○ Fixed:    [2.5  ] seconds                            │
│  ● Random:   Min [2.0]s  —  Max [3.5]s                 │
│                                                          │
│  📋 Preview (auto-populated khi chọn folders)            │
│  ┌──────────────────────────────────────────────┐       │
│  │ Ch │ #  │ Image File        │ Start  │ End   │       │
│  │ 01 │ 1  │ 1_A_stylized...   │  0.000 │ 2.537 │       │
│  │ 01 │ 2  │ 2_A_stylized...   │  3.267 │ 8.189 │       │
│  │ 01 │ 3  │ 4_A_stylized...   │  8.906 │15.296 │       │
│  │ ...│    │                   │        │       │       │
│  │ 02 │ 1  │ 1_Stylized...     │  0.000 │ 3.100 │       │
│  └──────────────────────────────────────────────┘       │
│  ✅ 3 chapters / 75 tracks / 73 images found            │
│                                                          │
│  [🔨 Assemble Draft]                    [⏹ Stop]        │
│                                                          │
│  📝 Log                                                  │
│  ┌─────────────────────────────────────────────┐        │
│  │ [10:30:01] Loaded 3 manifests               │        │
│  │ [10:30:02] Ch1: 27 tracks, gap=2.7s         │        │
│  │ [10:30:03] Ch2: 25 tracks, gap=3.1s         │        │
│  │ [10:30:05] ✅ Draft → CapCut Drafts folder   │        │
│  └─────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────┘
```

---

## Multi-Chapter Offset + Gap Logic

```python
offset = 0.0
for chapter in sorted_chapters:
    audio_duration = get_mp3_duration(chapter.audio_file)
    
    for track in chapter.tracks:
        real_start = track.start + offset
        real_end   = track.end   + offset
        # → add image to timeline at (real_start, real_end)
    
    # Add audio to timeline at (offset, offset + audio_duration)
    
    # Gap before next chapter
    if not last_chapter:
        gap = random.uniform(gap_min, gap_max)  # round to 0.1
        gap = round(gap, 1)
        offset += audio_duration + gap
```

---

## Proposed Changes

### Dependency

```
pip install pyJianYingDraft
```

---

### [NEW] `core/capcut_draft_builder.py`

Core logic, hoàn toàn độc lập:

```python
class CapCutDraftBuilder:
    def __init__(self, config):
        """
        config = {
            "resolution": (1920, 1080),
            "transition": "Dissolve",
            "transition_duration": 0.5,
            "ken_burns": True,
            "include_subtitle": True,
            "gap_mode": "random",      # "fixed" | "random"
            "gap_fixed": 2.5,
            "gap_min": 2.0,
            "gap_max": 3.5,
        }
        """
    
    def build(self, manifests, image_folder, audio_folder, output_folder):
        """
        manifests: list of parsed assembly.json dicts, sorted by chapter
        image_folder: path to folder containing image files
        audio_folder: path to folder containing mp3 files
        output_folder: CapCut drafts folder path
        
        Returns: path to created draft folder
        """
```

**Responsibilities**:
1. Sort manifests by chapter name
2. Calculate cumulative offsets with gaps
3. Create pyJianYingDraft script
4. Add video track (images with timecodes)
5. Add audio track (mp3 files)
6. Add subtitle track (if enabled)
7. Add transitions, Ken Burns keyframes
8. Save draft to CapCut drafts folder

---

### [NEW] `ui/capcut_assembler_tab.py`

PyQt6 tab widget:
- 3 folder browse inputs
- Settings dropdowns + checkboxes
- Chapter gap radio + inputs
- Preview table (QTableWidget)
- Assemble button + progress log
- Worker thread (QThread) for non-blocking assemble

---

### [MODIFY] `ui/main_window.py`

Add 2 lines:
```python
from ui.capcut_assembler_tab import CapCutAssemblerTab

# After SRT Generator tab (line ~96)
self._capcut_tab = CapCutAssemblerTab()
self._tabs.addTab(self._capcut_tab, "🎬 CapCut Assembler")
```

Update `TAB_HELP_IDS` list to include `"capcut-assembler"`.

---

## Verification Plan

### Step 1: Install dependency
```
pip install pyJianYingDraft
```

### Step 2: Compile check
```
python -m py_compile core/capcut_draft_builder.py
python -m py_compile ui/capcut_assembler_tab.py
```

### Step 3: Test with sample data
- Tạo 1 file `ch_01_..._assembly.json` mẫu
- Chạy builder → verify draft folder structure
- Copy vào CapCut Drafts → mở CapCut → verify timeline

### Step 4: Manual verification in CapCut
- Ảnh đúng timecode
- Audio sync
- Subtitle hiển thị
- Transition hoạt động
- Multi-chapter gap đúng
