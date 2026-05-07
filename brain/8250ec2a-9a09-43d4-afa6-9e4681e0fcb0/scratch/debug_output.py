import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'

# Check Step 1 sequences
with open(f'{base}\\ch_01_Level_1__Vulnerability_step1_sequences.json', encoding='utf-8') as f:
    seqs = json.load(f)

print("=== STEP 1: SEQUENCES ===")
for s in seqs:
    sid = s.get('sequence_id', '')
    loc = s.get('location_shift', '')
    dur = s.get('total_duration', 0)
    chars = s.get('characters', [])
    sids = s.get('sentence_ids', [])
    print(f"\n{sid}: {dur:.1f}s")
    print(f"  location: {loc}")
    print(f"  characters: {chars}")
    print(f"  sentence_ids: {sids}")

# Check Step 3.1 filmable
print("\n\n=== STEP 3.1: FILMABLE SCENES ===")
with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_1_filmable.json', encoding='utf-8') as f:
    filmable = json.load(f)

for seq_id, entries in filmable.items():
    print(f"\n{seq_id}: {len(entries)} sentence entries")
    for e in entries:
        n_scenes = len(e.get('scenes', []))
        orig = e.get('original_text', '')[:60]
        print(f"  sent_{e.get('sentence_id','?')}: {n_scenes} scene(s) | \"{orig}\"")

# Check Step 3 scenes
print("\n\n=== STEP 3.2: SCENES ===")
with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    scenes = json.load(f)

for seq in scenes:
    sid = seq.get('sequence_id', '')
    sc_list = seq.get('scenes', [])
    print(f"\n{sid}: {len(sc_list)} scenes")
    for sc in sc_list:
        gsid = sc.get('global_scene_id', '')
        loc = sc.get('locked_location', '')
        shot = sc.get('shot_type', '')
        dur = sc.get('duration', 0)
        act = sc.get('physical_action', '')[:60]
        print(f"  {gsid} | {shot:12s} | {dur:.1f}s | loc={loc}")
        print(f"    action: {act}")
