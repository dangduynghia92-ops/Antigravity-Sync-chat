import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test 3\video_prompt'

# Load all data
with open(f'{base}\\ch_08_Level_8__Chilled_step2_characters.json', encoding='utf-8') as f:
    chars = json.load(f)
with open(f'{base}\\ch_08_Level_8__Chilled_step2d_crowd.json', encoding='utf-8') as f:
    crowd = json.load(f)
with open(f'{base}\\ch_08_Level_8__Chilled_step3_scenes.json', encoding='utf-8') as f:
    scenes = json.load(f)
with open(f'{base}\\ch_08_Level_8__Chilled_step4_prompts.json', encoding='utf-8') as f:
    prompts = json.load(f)

print("=" * 90)
print("SO SÁNH FIELDS: CHARACTER vs CROWD — qua từng Step")
print("=" * 90)

# ─── Step 2: Character Sheet Data ───
print("\n" + "─" * 90)
print("STEP 2: DỮ LIỆU GỐC (Character Sheet)")
print("─" * 90)

char1 = chars.get("characters", [])[0]
crowd1 = crowd.get("characters", [])[0]

char_fields = sorted(char1.keys())
crowd_fields = sorted(crowd1.keys())
all_fields = sorted(set(char_fields + crowd_fields))

print(f"\n{'Field':<25} {'Character':<15} {'Crowd':<15} {'Match?'}")
print("-" * 70)
for f in all_fields:
    in_char = "✅" if f in char_fields else "❌"
    in_crowd = "✅" if f in crowd_fields else "❌"
    match = "✅" if (f in char_fields and f in crowd_fields) else "⚠ THIẾU"
    print(f"  {f:<23} {in_char:<15} {in_crowd:<15} {match}")

print(f"\nCharacter fields ({len(char_fields)}): {char_fields}")
print(f"Crowd fields ({len(crowd_fields)}): {crowd_fields}")

# Show sample values
print(f"\n--- Character mẫu: {char1.get('label')} ---")
for k in sorted(char1.keys()):
    print(f"  {k}: {str(char1[k])[:120]}")

print(f"\n--- Crowd mẫu: {crowd1.get('label')} ---")
for k in sorted(crowd1.keys()):
    print(f"  {k}: {str(crowd1[k])[:120]}")

# ─── Step 3: Scene Data ───
print("\n" + "─" * 90)
print("STEP 3: SCENE — Character vs Crowd fields per scene")
print("─" * 90)

# Find a scene with both char and crowd
sample_both = None
sample_crowd_only = None
for seq in scenes:
    for sc in seq.get("scenes", []):
        if sc.get("character_labels") and sc.get("crowd_labels"):
            if not sample_both:
                sample_both = sc
        if not sc.get("character_labels") and sc.get("crowd_labels"):
            if not sample_crowd_only:
                sample_crowd_only = sc

if sample_both:
    print(f"\nScene có CẢ character + crowd: {sample_both['global_scene_id']}")
    for k in sorted(sample_both.keys()):
        print(f"  {k}: {str(sample_both[k])[:150]}")

# ─── Step 4: Prompt Data ───
print("\n" + "─" * 90)
print("STEP 4: PROMPT — Data fields per prompt")
print("─" * 90)

# Find prompts with char vs crowd-only
char_prompt = None
crowd_prompt = None
both_prompt = None
for p in prompts:
    has_c = bool(p.get("characters"))
    has_cr = bool(p.get("crowd_labels"))
    if has_c and has_cr and not both_prompt:
        both_prompt = p
    if has_c and not has_cr and not char_prompt:
        char_prompt = p
    if not has_c and has_cr and not crowd_prompt:
        crowd_prompt = p

print("\n--- Prompt CHỈ CÓ character (no crowd) ---")
if char_prompt:
    for k in sorted(char_prompt.keys()):
        val = str(char_prompt[k])[:150]
        print(f"  {k}: {val}")
else:
    print("  Không tìm thấy")

print("\n--- Prompt CHỈ CÓ crowd (no character) ---")
if crowd_prompt:
    for k in sorted(crowd_prompt.keys()):
        val = str(crowd_prompt[k])[:150]
        print(f"  {k}: {val}")
else:
    print("  Không tìm thấy")

print("\n--- Prompt CÓ CẢ character + crowd ---")
if both_prompt:
    for k in sorted(both_prompt.keys()):
        val = str(both_prompt[k])[:150]
        print(f"  {k}: {val}")

# ─── Key comparison: what Step 4 sends to LLM ───
print("\n" + "─" * 90)
print("STEP 4 INPUT: Gửi gì cho LLM khi viết flat_prompt?")
print("─" * 90)
print("""
  CHARACTER:
    ✅ character_labels  → danh sách label
    ✅ costume_lookup    → COSTUME chi tiết từ visual_description 
    ✅ physical_action   → hành động
    ✅ character_interaction → tương tác
    
  CROWD:
    ✅ crowd_labels      → danh sách EXT-* label
    ❌ costume_lookup    → KHÔNG GỬI costume crowd cho LLM
    ❌ crowd_action      → không có field riêng
    ❌ default_stance    → không gửi
""")
