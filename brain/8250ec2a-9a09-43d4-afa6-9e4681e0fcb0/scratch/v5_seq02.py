import json

v5 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\V5\video_prompt'

with open(f'{v5}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    v5_scenes = json.load(f)

# Focus on SEQ_02 where the "inside walls of Tikrit" sentence is
for seq in v5_scenes:
    sid = seq.get('sequence_id', '')
    if sid == 'SEQ_02':
        loc = seq.get('locked_location', '') or seq.get('location_anchor', '')
        print(f"{sid}: loc='{loc}'")
        for sc in seq.get('scenes', []):
            gsid = sc.get('global_scene_id', '')
            sloc = sc.get('locked_location', '') or sc.get('location_anchor', '')
            act = sc.get('physical_action', '')
            audio = sc.get('audio_sync', '')
            print(f"\n  {gsid}")
            print(f"    loc: {sloc}")
            print(f"    action: {act}")
            print(f"    audio: {audio}")

# Also check V5 Step 1
print("\n\n=== V5 Step 1 ===")
import os
step1_path = f'{v5}\\ch_01_Level_1__Vulnerability_step1_sequences.json'
if os.path.exists(step1_path):
    with open(step1_path, encoding='utf-8') as f:
        v5_seqs = json.load(f)
    for s in v5_seqs:
        sid = s.get('sequence_id', '')
        loc = s.get('location_shift', '')
        print(f"  {sid}: location='{loc}'")
else:
    print("  No Step 1 file found in V5")
