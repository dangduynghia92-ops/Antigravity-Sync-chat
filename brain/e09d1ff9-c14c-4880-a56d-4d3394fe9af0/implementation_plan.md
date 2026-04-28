# Fix Style Integration Across Video Pipeline

Style file hiện giờ chỉ được Step 4 đọc (Mandatory Style + Negative Prompt). Step 2 và Step 3 không biết style → output không đúng phong cách.

## Proposed Changes

### Style File — Thêm 2 section mới

#### [MODIFY] [Chibi Storybook Historical.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/video_styles/Chibi%20Storybook%20Historical.txt)

Restructure thành 4 section có marker rõ ràng:

```
=== CHARACTER STYLE ===
(Ngắn gọn 3-5 dòng. Inject vào Step 2 system prompt)
"Mô tả nhân vật phải theo phong cách: mặt tròn trắng, mắt oval, lông mày biểu cảm, không mũi..."

=== SCENE STYLE ===
(Ngắn gọn 3-5 dòng. Inject vào Step 3 user message)
"physical_action phải mô tả theo phong cách animation stylized, không realistic..."

=== MANDATORY STYLE ===
(Keywords ghép vào flat_prompt — giữ nguyên)

=== NEGATIVE PROMPT ===
(Từ cấm — giữ nguyên)
```

Phần "Role & Expertise", "Visual Strategy", "STYLE RULES" → **bỏ hoàn toàn** vì không có step nào consume.

---

### Pipeline Code

#### [MODIFY] [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

**1. Thêm `_parse_style_sections()` helper:**
- Parse style file thành dict: `{"character_style": "...", "scene_style": "...", "mandatory_style": "...", "negative_prompt": "..."}`
- Gọi 1 lần trong `run()`, cache kết quả

**2. Step 2 — Inject CHARACTER STYLE:**
- Append vào cuối `STEP2_CHARACTERS_SYSTEM_PROMPT`:
  ```
  === VISUAL STYLE GUIDE ===
  {character_style from style file}
  Your visual_description MUST follow this style. Do NOT describe realistic human features.
  ```
- Step 2b (Locations) không cần inject style vì locations là mô tả bối cảnh chung

**3. Step 3 — Inject SCENE STYLE:**
- Append vào cuối user message (sau VISUAL REFERENCE):
  ```
  === ART STYLE ===
  {scene_style from style file}
  All physical_action and background_and_extras descriptions MUST follow this style.
  ```

**4. Step 4 — Thêm `flat_prompt` assembly:**
- Mỗi scene JSON bây giờ thêm field `flat_prompt` — 1 đoạn text prompt ghép từ:
  ```
  {mandatory_style}. {shot_type}, {camera_motion}. {subject_action}. {background_and_extras}. {location}. {lighting_and_atmosphere}.
  ```
- Field `negative_prompt` giữ riêng (nhiều AI tool nhận negative riêng)

### Data Flow sau khi sửa

```
Style File
├── CHARACTER STYLE ──→ Step 2 (LLM biết vẽ mặt trắng khi mô tả nhân vật)
├── SCENE STYLE ──────→ Step 3 (LLM viết physical_action theo phong cách)
├── MANDATORY STYLE ──→ Step 4 (ghép vào flat_prompt)
└── NEGATIVE PROMPT ──→ Step 4 (field riêng)
```

## Verification Plan

### Automated Tests
- Parse style file → verify 4 sections extracted correctly
- Verify Step 2 system prompt contains character style
- Verify Step 3 user message contains scene style
- Verify Step 4 output has `flat_prompt` field as text string
