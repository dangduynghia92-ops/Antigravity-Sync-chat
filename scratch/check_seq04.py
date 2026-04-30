import json, os

base = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt'

# Step 1 - what does SEQ_04 say?
f1 = os.path.join(base, 'Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step1_sequences.json')
seq1 = json.loads(open(f1, encoding='utf-8').read())
seq04 = [s for s in seq1 if s.get('sequence_id') == 'SEQ_04']
if seq04:
    s = seq04[0]
    print("=== STEP 1: SEQ_04 ===")
    print(f"Duration: {s.get('total_duration')}s")
    print(f"Location: {s.get('location_shift')}")
    print(f"Characters: {s.get('characters', [])}")
    print(f"Text: {s.get('full_text')}")
    print()

# Step 3 - what scene was generated?
f3 = os.path.join(base, 'Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step3_scenes.json')
scenes = json.loads(open(f3, encoding='utf-8').read())
for seq in scenes:
    if seq.get('sequence_id') == 'SEQ_04':
        print("=== STEP 3: SEQ_04 ===")
        print(f"locked_location: {seq.get('locked_location')}")
        for i, sc in enumerate(seq.get('scenes', [])):
            print(f"\n  Scene {i+1}: {sc.get('global_scene_id')}")
            print(f"  Characters: {sc.get('character_labels')}")
            print(f"  Audio: {sc.get('audio_sync', '')[:100]}")
            print(f"  Action: {sc.get('physical_action', '')[:150]}")
            print(f"  Costume: {sc.get('costume_note', '')[:150]}")
        break

# Step 2a characters - check age labels
f2 = os.path.join(base, 'Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step2_characters.json')
chars = json.loads(open(f2, encoding='utf-8').read())
print("\n=== STEP 2: CHARACTER LABELS ===")
for c in chars.get('characters', []):
    label = c.get('label', '')
    if 'King-A' in label or 'Baldwin' in label:
        print(f"  {label}: {c.get('visual_description', '')[:120]}")
