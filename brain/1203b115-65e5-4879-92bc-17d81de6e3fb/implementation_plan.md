# Google Check — Historical Fact Verification Pipeline

Thêm bước xác minh lịch sử cho Visual Bible và Character Bible bằng Gemini + Google Search Grounding. Mục tiêu: đảm bảo mọi mô tả (quân phục, vũ khí, cờ hiệu, kiến trúc, phong tục) **đúng 100% với thời kỳ lịch sử** trước khi tạo prompt.

## User Review Required

> [!IMPORTANT]
> Cần file `gemini_keys.json` chứa ít nhất 1 Gemini API key (AIza...) — **không dùng được** key từ `api_keys.json` (OpenAI proxy). Có thể dùng chung file `gemini_keys.json` với Script_Split_Chapter.

> [!WARNING]
> Mỗi lần verify = 1-2 lần gọi Gemini API. Google Search Grounding **miễn phí** với Gemini API nhưng có rate limit. Pipeline sẽ thêm ~15-30s mỗi project.

---

## Proposed Changes

### 1. API Client — Thêm Gemini Native Support

#### [MODIFY] [api_client.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/api_client.py)

- Copy `call_gemini_native()` từ Script_Split_Chapter (dòng 261-380)
- Thêm hàm `load_gemini_keys()` đọc `gemini_keys.json`
- Hàm này gọi Gemini trực tiếp qua `generativelanguage.googleapis.com` với `"tools": [{"google_search": {}}]`

---

### 2. Verification Module — Tạo mới

#### [NEW] [historical_verifier.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/historical_verifier.py)

Hàm chính: `verify_bible_google()`

**Flow:**
```
Input: character_bible + visual_bible text
  ↓
Build verification prompt:
  "Given this historical context [era, factions]:
   Verify EACH item below against real history:
   1. [Headwear] French-Soldier: tall black shako → Is this correct for Napoleonic infantry?
   2. [Outfit] French-Soldier: white tunic with blue facings → Correct?
   3. [Weapon] French-Soldier: Charleville musket → Correct for this era?
   4. [Banner] French-Soldier: tricolor flag → Did France use tricolor in this specific year?
   5. [Architecture] Gothic cathedral with flying buttresses → Correct for 13th century France?
   ..."
  ↓
Call Gemini + Google Search Grounding
  ↓
Parse response → list of corrections
  ↓
Output: corrected bible text + verification report
```

**Verification prompt sẽ check:**
| Category | Ví dụ kiểm tra |
|---|---|
| **Uniforms** | "Was Napoleonic French infantry uniform actually white?" → Google confirms YES (pre-1806) or NO (post-1806 changed to blue) |
| **Weapons** | "Did Roman soldiers use gladius or spatha?" → Depends on era: Republic = gladius, Late Empire = spatha |
| **Banners/Flags** | "Did France use tricolor in 1789?" → No, tricolor adopted 1794. In 1789 = Bourbon white flag |
| **Architecture** | "Gothic cathedral in ancient Rome?" → WRONG, Gothic = 12th century |
| **Headwear** | "Bicorne hat in 1750?" → No, bicorne = post-1790. In 1750 = tricorne |

**Output format:**
```json
{
  "era_detected": "Napoleonic Wars, 1805-1815",
  "verifications": [
    {"item": "French-Soldier Headwear", "original": "tall black shako", "correct": true, "note": "Shako adopted 1806, correct for this period"},
    {"item": "French-Soldier Banner", "original": "Bourbon white flag with fleur-de-lis", "correct": false, "correction": "France used the tricolor after 1794. Should be: tricolor with golden eagle standard", "source": "Google Search"}
  ],
  "corrections_applied": 1,
  "summary": "1 correction: French banner should be tricolor, not Bourbon flag"
}
```

Sau khi verify, hàm tự động **sửa** bible text bằng cách gọi AI lần 2 với corrections list.

#### [NEW] [verify_bible_prompt.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/prompts/verify_bible_prompt.txt)

System prompt cho Gemini verification call — hướng dẫn cách verify và format output JSON.

---

### 3. Gemini Keys Config

#### [NEW] [gemini_keys.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/gemini_keys.json)

```json
{
  "keys": [
    "AIzaSy..."
  ]
}
```

Dùng chung key pool với Script_Split_Chapter, rotate qua từng key nếu bị rate limit.

---

### 4. Pipeline Integration

#### [MODIFY] [process_controller.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/process_controller.py)

Insert verification step **sau** khi tạo bible, **trước** khi tạo prompt:

```
Current pipeline:
  Mode Verify → Character Pipeline → Visual Bible → Generate Prompts

New pipeline:
  Mode Verify → Character Pipeline → Visual Bible 
  → 🔍 Google Check (verify + auto-correct)
  → Generate Prompts
```

Cụ thể:
- Sau `run_character_pipeline()` (dòng ~275): verify `character_bible`
- Sau `generate_visual_bible()` (dòng ~300): verify `visual_bible`
- Chỉ chạy khi checkbox `google_check` = ON
- Truyền `gemini_keys` từ config

---

### 5. UI — Thêm Checkbox

#### [MODIFY] [config_section.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/config_section.py)

- Thêm checkbox `🔍 Google Check` cạnh `🎨 Character Sheet` (Row 5)
- Tooltip: "Verify historical accuracy of character/visual bible using Google Search before generating prompts"
- Default: unchecked (tốn thêm API calls)
- Save/load trong config.json
- Truyền qua `get_config()` → constraints dict

---

## Open Questions

> [!IMPORTANT]
> 1. **Dùng chung `gemini_keys.json`** với Script_Split_Chapter hay tạo file riêng? (Đề xuất: dùng chung — copy cùng thư mục)
> 2. **Verify cả Visual Bible hay chỉ Character Bible?** (Đề xuất: cả hai — Visual Bible cũng chứa architecture, props cần verify)

## Verification Plan

### Automated Tests
- Chạy app → chọn style historical → bật Google Check + Character Sheet + Historical
- Process 1 SRT file về trận chiến cụ thể
- Kiểm tra log: có hiện `[VERIFY]` steps không
- Kiểm tra `_character_bible.csv`: Banner có đúng thời kỳ không
- Kiểm tra output prompt: mô tả có nhất quán với bible đã verify không

### Manual Verification
- So sánh mô tả quân phục/vũ khí trong output với Wikipedia/tài liệu lịch sử
- Kiểm tra edge case: chuyển thời kỳ (ví dụ SRT bao gồm cả thời Cộng Hòa La Mã và Đế Chế La Mã — quân phục khác nhau)
