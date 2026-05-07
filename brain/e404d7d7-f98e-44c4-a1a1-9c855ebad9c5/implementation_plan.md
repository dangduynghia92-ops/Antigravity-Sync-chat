# CapCut Assembler Tab — Implementation Plan

Tạo tab mới trong app PyQt để tự động ghép ảnh + audio + SRT thành draft CapCut, sử dụng thư viện `pyJianYingDraft`.

## Kiến trúc tổng quan

```
Pipeline hiện tại:
Script (.txt) → TTS Audio (.mp3) → SRT (Whisper) → AI Verify

Tab mới nối tiếp:
SRT + Audio + Ảnh  →  CapCut Assembler Tab  →  Draft folder
                                                    ↓
                                            Copy vào CapCut → Review → Export
```

---

## UI Layout

```
┌─────────────────────────────────────────────────────────┐
│  📁 Input                                                │
│  ┌─────────────────────────────────────────────┐        │
│  │ Folder chứa ảnh + audio + SRT:   [Browse]   │        │
│  └─────────────────────────────────────────────┘        │
│  ┌─────────────────────────────────────────────┐        │
│  │ Output draft folder:              [Browse]   │        │
│  │ (mặc định = CapCut Drafts folder)            │        │
│  └─────────────────────────────────────────────┘        │
│                                                          │
│  ⚙ Settings                                             │
│  ┌─────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │ Resolution   │ │ Transition   │ │ Animation    │     │
│  │ [1920x1080▼] │ │ [Dissolve ▼] │ │ [Fade In ▼]  │     │
│  └─────────────┘ └──────────────┘ └──────────────┘     │
│  ┌────────────────┐ ┌──────────────┐                    │
│  │ Subtitle style  │ │ Bg Blur      │                    │
│  │ [Default    ▼]  │ │ [Level 2  ▼] │                    │
│  └────────────────┘ └──────────────┘                    │
│  ☑ Auto Ken Burns (zoom effect on images)               │
│  ☑ Include subtitle from SRT                            │
│  ☑ Include audio track                                  │
│                                                          │
│  📋 Preview                                              │
│  ┌─────────────────────────────────────────────┐        │
│  │ #  │ Timecode         │ Image        │ Text  │        │
│  │ 1  │ 00:00 → 00:03    │ scene_01.png │ Blac… │        │
│  │ 2  │ 00:03 → 00:05    │ scene_02.png │ The…  │        │
│  │ 3  │ 00:05 → 00:08    │ scene_03.png │ biti… │        │
│  │ ...│                   │              │       │        │
│  └─────────────────────────────────────────────┘        │
│                                                          │
│  [🔨 Assemble Draft]                    [⏹ Stop]        │
│                                                          │
│  📝 Log                                                  │
│  ┌─────────────────────────────────────────────┐        │
│  │ [10:30:01] Creating draft 1920x1080...       │        │
│  │ [10:30:02] Adding image 1/25: scene_01.png   │        │
│  │ [10:30:03] Adding audio track...              │        │
│  │ [10:30:04] Adding 25 subtitle entries...      │        │
│  │ [10:30:05] ✅ Draft saved to: dfd_xxxxx       │        │
│  └─────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────┘
```

---

## Chức năng khả dụng từ VectCutAPI

### Core (Bắt buộc)

| Chức năng | API | Mô tả |
|-----------|-----|--------|
| Tạo draft project | `create_draft` | Tạo project CapCut mới với resolution tùy chọn |
| Thêm ảnh vào timeline | `add_image` | Ghép ảnh theo timecode từ SRT, mỗi segment = 1 ảnh |
| Thêm audio track | `add_audio_track` | Import file mp3 narration vào track audio |
| Thêm subtitle | `add_subtitle` | Import SRT entries thành subtitle track |
| Lưu draft | `save_draft` | Export thành folder draft CapCut |

### Enhancement (Tùy chọn — checkbox/dropdown)

| Chức năng | API | Mô tả |
|-----------|-----|--------|
| **Transition** giữa ảnh | `add_image(transition=...)` | Dissolve, Fade, Move, Compress... |
| **Animation** vào/ra | `add_image(intro_animation=..., outro_animation=...)` | Zoom In, Fade In, Rotate... |
| **Ken Burns** (zoom effect) | `add_video_keyframe` | Scale keyframe từ 1.0→1.1 suốt segment (cinematic) |
| **Background blur** | `add_image(background_blur=...)` | Blur nền khi ảnh không full-frame (level 1-4) |
| **Text styling** | `add_text(font_size=..., font_color=...)` | Font, màu, shadow cho subtitle |
| **Mask** | `add_image(mask_type=...)` | Circle, Rectangle, Heart mask cho ảnh |

---

## Matching Logic: Ảnh ↔ SRT

### Quy tắc match ảnh với segment SRT

**Cách 1 — Theo tên file (ưu tiên):**
```
SRT segment 1 (00:00→00:03) → tìm file: scene_01.png hoặc 001.png
SRT segment 2 (00:03→00:05) → tìm file: scene_02.png hoặc 002.png
```

**Cách 2 — Theo thứ tự file:**
```
Nếu không match được tên → sắp xếp ảnh theo tên → gán lần lượt
```

**Cách 3 — Theo nhóm (nhiều segment chia sẻ 1 ảnh):**
```
Nếu có 25 segments nhưng chỉ 10 ảnh → mỗi ảnh cover 2-3 segments liên tiếp
Ảnh 1: segment 1-3, Ảnh 2: segment 4-6, ...
```

> [!IMPORTANT]
> **Cần quyết định**: Dùng cách match nào? Hay hỗ trợ cả 3 với dropdown chọn?

---

## Dependency

### Thư viện cần cài

```
pip install pyJianYingDraft
```

`pyJianYingDraft` là thư viện Python tạo draft CapCut/Jianying offline — **không cần server**, **không cần VectCutAPI server** chạy. Chỉ cần thư viện này là đủ.

> [!NOTE]
> VectCutAPI repo dùng `pyJianYingDraft` dưới hood. Ta chỉ cần import thư viện đó, không cần clone cả repo VectCutAPI.

---

## File Structure

### Proposed Changes

#### [NEW] `ui/capcut_assembler_tab.py`
- Widget PyQt5 cho tab mới
- UI layout, config load/save, preview table
- Worker thread cho assemble process

#### [NEW] `core/capcut_draft_builder.py`
- Core logic: đọc SRT + match ảnh + tạo draft
- Gọi `pyJianYingDraft` API trực tiếp
- Không phụ thuộc bất kỳ file nào khác trong project

#### [MODIFY] `main.py` (hoặc file chứa tab manager)
- Import và thêm tab mới vào tab widget

---

## Open Questions

> [!IMPORTANT]
> **1. CapCut Drafts folder**: Bạn dùng CapCut PC hay Jianying? Drafts folder ở đâu?
> - CapCut: `C:\Users\Admin\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft\`
> - Jianying: `C:\Users\Admin\Movies\JianyingPro\User Data\Projects\com.lveditor.draft\`

> [!IMPORTANT]  
> **2. Matching ảnh**: Pipeline hiện tại tạo ảnh theo chapter hay theo câu? Tên file ảnh có format gì?
> Ví dụ: `scene_01.png`, `ch01_001.png`, hay `prompt_1.png`?

> [!IMPORTANT]
> **3. Resolution**: Video output thường dùng resolution gì?
> - 1920×1080 (YouTube landscape)
> - 1080×1920 (TikTok/Shorts portrait)  
> - 2560×1440 (YouTube 2K)

> [!IMPORTANT]
> **4. Mỗi ảnh cover bao nhiêu segments?** 
> - 1 ảnh = 1 câu SRT (nhiều ảnh nhất, mỗi ảnh ~3-5s)?
> - 1 ảnh = 1 đoạn/scene (ít ảnh, mỗi ảnh ~15-30s)?

---

## Verification Plan

### Automated Tests
- `python -m py_compile ui/capcut_assembler_tab.py`
- `python -m py_compile core/capcut_draft_builder.py`
- Test tạo draft với file SRT + ảnh mẫu

### Manual Verification
- Copy draft folder vào CapCut Drafts
- Mở CapCut → verify: ảnh đúng timecode, audio đúng, subtitle đúng
- Export video → playback test
