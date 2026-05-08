import json, os

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerable'

# 1. Check Step 2b character sheet — where Teen label is defined
chars_file = os.path.join(base, 'ch_01_Level_1__Vulnerable_step2_characters.json')
with open(chars_file, encoding='utf-8') as f:
    data = json.load(f)

print("=== CHARACTER SHEET ===")
for c in data.get('characters', data):
    label = c.get('label', '')
    if 'Teen' in label or 'teen' in label:
        print(f"Label: {label}")
        print(f"  Name: {c.get('name', '')}")
        print(f"  Description: {c.get('visual_description', '')[:200]}")
        print()

# 2. Check Step 1 sequences — which sequences mention teen-age characters
seqs_file = os.path.join(base, 'ch_01_Level_1__Vulnerable_step1_sequences.json')
with open(seqs_file, encoding='utf-8') as f:
    seqs = json.load(f)

print("=== SEQUENCES WITH TEEN CHARACTERS ===")
for s in seqs:
    chars = s.get('characters', [])
    for c in chars:
        if 'teen' in c.lower():
            print(f"{s['sequence_id']}: {c}")
            print(f"  full_text: {s.get('full_text', '')[:200]}")
            print()

# 3. Check Step 3 scenes — where Teen label appears
step3_file = os.path.join(base, 'ch_01_Level_1__Vulnerable_step3_scenes.json')
with open(step3_file, encoding='utf-8') as f:
    scenes = json.load(f)

print("=== STEP 3 SCENES WITH TEEN LABEL ===")
for seq in scenes:
    for sc in seq.get('scenes', []):
        labels = sc.get('character_labels', [])
        for l in labels:
            if 'Teen' in l or 'teen' in l:
                print(f"{sc.get('global_scene_id', '')}: {l}")
                print(f"  action: {sc.get('physical_action', '')[:150]}")
                print()

# 4. Check Step 4 prompts — where Teen appears in flat_prompt
step4_file = os.path.join(base, 'ch_01_Level_1__Vulnerable_step4_prompts.json')
with open(step4_file, encoding='utf-8') as f:
    prompts = json.load(f)

print("=== STEP 4 FLAT PROMPTS WITH TEEN ===")
for p in prompts:
    flat = p.get('flat_prompt', '')
    if 'Teen' in flat or 'Ayyubid-Noble-A-Teen' in flat:
        print(f"{p.get('global_scene_id', p.get('scene_id', ''))}: ...{flat[flat.find('Teen')-30:flat.find('Teen')+50]}...")
        print()

# 5. Check the raw script — what does ch01 actually describe?
cleaned_file = os.path.join(base, 'ch_01_Level_1__Vulnerable_cleaned_script.txt')
if os.path.exists(cleaned_file):
    with open(cleaned_file, encoding='utf-8') as f:
        text = f.read()
    print("=== CLEANED SCRIPT (first 500 chars) ===")
    print(text[:500])
    print("\n...")
    print(text[500:1000])
