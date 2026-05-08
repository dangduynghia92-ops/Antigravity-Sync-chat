import json

fp = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerable\ch_01_Level_1__Vulnerable_step3_1_filmable.json'

with open(fp, encoding='utf-8') as f:
    data = json.load(f)

print("=== ALL SEQUENCES — character_interaction field ===\n")
has_data = 0
has_none = 0

for seq_id, entries in data.items():
    for entry in entries:
        sid = entry.get('sentence_id', '?')
        interaction = entry.get('character_interaction', 'MISSING')
        chars_present = entry.get('characters_present', '?')
        
        if interaction not in ('none', 'MISSING', None):
            has_data += 1
            print(f"✅ {seq_id} sent_{sid}: interaction={interaction}")
        else:
            has_none += 1

print(f"\n--- Summary ---")
print(f"Has interaction data: {has_data}")
print(f"Has 'none' or missing: {has_none}")

# Show Step 3.2 scenes
fp3 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerable\ch_01_Level_1__Vulnerable_step3_scenes.json'

with open(fp3, encoding='utf-8') as f:
    scenes = json.load(f)

print("\n\n=== STEP 3.2 — character_interaction field ===\n")
has_data2 = 0
has_none2 = 0

for seq in scenes:
    for sc in seq.get('scenes', []):
        gid = sc.get('global_scene_id', '')
        interaction = sc.get('character_interaction', 'MISSING')
        chars = sc.get('character_labels', [])
        
        if interaction not in ('none', 'MISSING', None):
            has_data2 += 1
            print(f"✅ {gid}: chars={chars} | interaction={interaction}")
        else:
            has_none2 += 1

print(f"\n--- Summary ---")
print(f"Has interaction data: {has_data2}")
print(f"Has 'none' or missing: {has_none2}")
