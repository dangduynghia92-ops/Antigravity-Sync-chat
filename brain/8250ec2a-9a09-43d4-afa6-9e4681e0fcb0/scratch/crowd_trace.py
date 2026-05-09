import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

# Step 3 scenes — where has_crowd comes from
fp3 = os.path.join(base, 'ch_08_Level_8__Chilled_step3_scenes.json')
with open(fp3, encoding='utf-8') as f:
    scenes = json.load(f)

print("=== SEQ_01 from Step 3.2 ===")
for seq in scenes:
    if seq.get('sequence_id') != 'SEQ_01':
        continue
    for sc in seq.get('scenes', []):
        gid = sc.get('global_scene_id', '')
        has_crowd = sc.get('has_crowd', 'MISSING')
        chars = sc.get('character_labels', [])
        extras = sc.get('extras', 'MISSING')
        print(f"  {gid}: chars={chars} has_crowd={has_crowd} extras={extras}")

# Step 3.1 filmable — check sentence for SCN_06
print("\n=== Step 3.1 filmable (sentences near SCN_06) ===")
fp31 = os.path.join(base, 'ch_08_Level_8__Chilled_step3_1_filmable.json')
with open(fp31, encoding='utf-8') as f:
    filmable = json.load(f)

for entry in filmable.get('SEQ_01', []):
    sid = entry.get('sentence_id')
    cls = entry.get('classification')
    present = entry.get('present_labels', entry.get('characters_present', 'MISSING'))
    broll = entry.get('is_broll')
    text = entry.get('original_text', '')[:80]
    print(f"  sent_{sid}: [{cls}] present_labels={present} broll={broll}")
    print(f"    text: {text}")
