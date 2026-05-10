import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test 3\video_prompt'

with open(f'{base}\\ch_08_Level_8__Chilled_step4_prompts.json', encoding='utf-8') as f:
    s4 = json.load(f)

# Reference prompt structure (from user's image, minus audio)
ref_elements = [
    "Art style opening",          # "In a minimalist 2D cel-shaded cartoon style with thin black lines..."
    "Character A face detail",    # "long narrow face, big blue-gray worried eyes, thin furrowed brows, small straight nose..."
    "Character A costume",        # "dark blue-gray crewneck sweatshirt"
    "Character A action",         # "hunches at his keyboard, fingers splayed mid-typing"
    "Props/environment detail",   # "books and scattered papers sit behind him"
    "Character B appearance",     # "a mid-20s pale woman in a simple dark coat"
    "Character B action",         # "stands near the brown-gray sofa"
    "Camera framing",             # "static eye-level medium-wide 35-50mm framing"
    "Lighting",                   # "lit only by a weak lamp grazing faces and the door edge"
    "Technical suffix",           # "Aspect ratio 16:9, no text overlays, no watermarks..."
]

print("=" * 90)
print("MẪU THAM CHIẾU (từ ảnh user gửi, bỏ phần âm thanh):")
print("=" * 90)
print("""
In a minimalist 2D cel-shaded cartoon style with thin black lines, worn dusty walls, 
and a desaturated cold palette, a slim pale young man with a long narrow face, big 
blue-gray worried eyes with dark circles, thin furrowed brows, a small straight nose, 
thin pressed lips, black ear plugs, and short dark-brown slightly messy hair hunches 
at his keyboard in a dark blue-gray crewneck sweatshirt, fingers splayed mid-typing 
as books and scattered papers sit behind him. In the dim living room, a mid-20s pale 
woman in a simple dark coat stands near the brown-gray sofa. The static eye-level 
medium-wide 35–50mm framing leaves empty space to the left, lit only by a weak lamp 
grazing faces and the door edge. Aspect ratio 16:9, no text overlays, no watermarks, 
no extra limbs, no floating objects, no blurry faces.
""")

print("CẤU TRÚC MẪU:")
for i, e in enumerate(ref_elements, 1):
    print(f"  {i}. {e}")

print("\n" + "=" * 90)
print("FLAT PROMPT PIPELINE (3 mẫu):")
print("=" * 90)

# Show 3 diverse prompts: char-only, crowd-only, multi-char
samples = []
for p in s4:
    chars = p.get('characters', '')
    crowd = p.get('crowd_labels', [])
    if ',' in chars and len(samples) < 3:
        samples.append(('MULTI-CHAR', p))
    elif not chars and crowd and len(samples) < 3:
        samples.append(('CROWD-ONLY', p))
    elif chars and not crowd and len(samples) < 3:
        samples.append(('CHAR-ONLY', p))
    if len(samples) >= 3:
        break

# Fill if needed
if len(samples) < 3:
    for p in s4[:3]:
        if len(samples) < 3:
            samples.append(('ANY', p))

for label, p in samples:
    print(f"\n--- [{label}] {p['global_scene_id']} ---")
    print(p.get('flat_prompt', ''))

# Element-by-element comparison
print("\n" + "=" * 90)
print("SO SÁNH TỪNG YẾU TỐ:")
print("=" * 90)

checks = {
    'art_style_opening': 0,
    'char_face_detail': 0,
    'char_costume_detail': 0,
    'char_action': 0,
    'props_environment': 0,
    'camera_framing': 0,
    'lighting_detail': 0,
    'technical_suffix': 0,
    'crowd_face': 0,
    'crowd_costume': 0,
    'crowd_action': 0,
}

for p in s4:
    fp = p.get('flat_prompt', '').lower()
    has_char = bool(p.get('characters'))
    has_crowd = bool(p.get('crowd_labels'))
    
    if 'stylized' in fp or 'animation' in fp or 'illustration' in fp:
        checks['art_style_opening'] += 1
    if any(w in fp for w in ['face', 'eyes', 'beard', 'eyebrow', 'head', 'circular']):
        checks['char_face_detail'] += 1
    if any(w in fp for w in ['wears', 'kaftan', 'armor', 'tunic', 'cloak', 'helmet', 'chainmail']):
        checks['char_costume_detail'] += 1
    if any(w in fp for w in ['standing', 'walking', 'sitting', 'leaning', 'looking', 'riding', 'pointing', 'holding', 'raises', 'turns', 'lifts', 'grips', 'lunges', 'kneels']):
        checks['char_action'] += 1
    if any(w in fp for w in ['lamp', 'campfire', 'throne', 'table', 'scroll', 'map', 'tent', 'palisade']):
        checks['props_environment'] += 1
    if any(w in fp for w in ['eye-level', 'low-angle', 'close-up', 'wide shot', 'medium shot', 'framing']):
        checks['camera_framing'] += 1
    if any(w in fp for w in ['moonlight', 'sunlight', 'torch', 'lamp light', 'shadow', 'warm', 'cool', 'lit by']):
        checks['lighting_detail'] += 1
    if '16:9' in fp or 'no border' in fp or 'no text' in fp:
        checks['technical_suffix'] += 1
    if has_crowd and 'ext-' in fp:
        if any(w in fp for w in ['circular head', 'white', '#ffffff']):
            checks['crowd_face'] += 1
        if any(w in fp for w in ['kazaghand', 'chainmail', 'surcoat', 'tunic', 'cotton', 'skullcap']):
            checks['crowd_costume'] += 1
        if any(w in fp for w in ['patrol', 'march', 'stand', 'huddle', 'guard', 'walk', 'lined', 'carry']):
            checks['crowd_action'] += 1

total = len(s4)
total_crowd = sum(1 for p in s4 if p.get('crowd_labels') and 'ext-' in p.get('flat_prompt', '').lower())

fmt = "{:<25} {:>6}/{:<6} ({:>3}%)"
print(f"\n{'Yếu tố':<25} {'Count':<15} {'%':>5}")
print("-" * 50)
print(fmt.format("Art style opening", checks['art_style_opening'], total, checks['art_style_opening']*100//total))
print(fmt.format("Char face detail", checks['char_face_detail'], total, checks['char_face_detail']*100//total))
print(fmt.format("Char costume detail", checks['char_costume_detail'], total, checks['char_costume_detail']*100//total))
print(fmt.format("Char action", checks['char_action'], total, checks['char_action']*100//total))
print(fmt.format("Props/environment", checks['props_environment'], total, checks['props_environment']*100//total))
print(fmt.format("Camera framing", checks['camera_framing'], total, checks['camera_framing']*100//total))
print(fmt.format("Lighting detail", checks['lighting_detail'], total, checks['lighting_detail']*100//total))
print(fmt.format("Technical suffix", checks['technical_suffix'], total, checks['technical_suffix']*100//total))
print(f"\n--- Crowd (base: {total_crowd} prompts with EXT-) ---")
print(fmt.format("Crowd face/head", checks['crowd_face'], total_crowd or 1, checks['crowd_face']*100//(total_crowd or 1)))
print(fmt.format("Crowd costume", checks['crowd_costume'], total_crowd or 1, checks['crowd_costume']*100//(total_crowd or 1)))
print(fmt.format("Crowd action", checks['crowd_action'], total_crowd or 1, checks['crowd_action']*100//(total_crowd or 1)))

# Show what the reference has that we DON'T
print("\n" + "=" * 90)
print("KHÁC BIỆT SO VỚI MẪU:")
print("=" * 90)
print("""
MẪU có mà PIPELINE thiếu/yếu:
  ❌ Mô tả khuôn mặt chi tiết (eye color, nose shape, lip shape, hair texture)
     → Pipeline chỉ viết "circular head, flat white #FFFFFF, minimalist features"
  ❌ Camera lens cụ thể (35-50mm framing)
     → Pipeline chỉ viết "eye-level" / "low-angle"
  ❌ Negative prompt nhúng trong flat_prompt ("no extra limbs, no floating objects")
     → Pipeline tách riêng negative_prompt

PIPELINE có mà MẪU không:
  ✅ [Label] brackets cho character identity consistency
  ✅ Index prefix (1_SEQ_01_SCN_01) cho tracking
  ✅ Art style rules chi tiết (outline, #FFFFFF fill)
""")
