import json

# Compare V5 (working) vs current
v5 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\V5\video_prompt'
cur = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'

print("=" * 70)
print("V5 (WORKING)")
print("=" * 70)
with open(f'{v5}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    v5_scenes = json.load(f)

for seq in v5_scenes:
    sid = seq.get('sequence_id', '')
    loc = seq.get('locked_location', '') or seq.get('location_anchor', '')
    print(f"\n{sid}: loc='{loc}'")
    for sc in seq.get('scenes', []):
        gsid = sc.get('global_scene_id', '')
        sloc = sc.get('locked_location', '') or sc.get('location_anchor', '')
        act = sc.get('physical_action', '')[:80]
        audio = sc.get('audio_sync', '')[:60]
        print(f"  {gsid}: loc='{sloc}'")
        print(f"    action: {act}")
        print(f"    audio: {audio}")

print("\n\n" + "=" * 70)
print("CURRENT (NEW)")
print("=" * 70)
with open(f'{cur}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    cur_scenes = json.load(f)

for seq in cur_scenes:
    sid = seq.get('sequence_id', '')
    loc = seq.get('locked_location', '') or seq.get('location_anchor', '')
    print(f"\n{sid}: loc='{loc}'")
    for sc in seq.get('scenes', []):
        gsid = sc.get('global_scene_id', '')
        sloc = sc.get('locked_location', '') or sc.get('location_anchor', '')
        act = sc.get('physical_action', '')[:80]
        audio = sc.get('audio_sync', '')[:60]
        print(f"  {gsid}: loc='{sloc}'")
        print(f"    action: {act}")
        print(f"    audio: {audio}")
