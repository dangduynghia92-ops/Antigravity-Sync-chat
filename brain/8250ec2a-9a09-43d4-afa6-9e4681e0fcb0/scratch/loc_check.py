import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'

with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    scenes = json.load(f)

for seq in scenes:
    sid = seq.get('sequence_id', '')
    print(f"\n{sid}:")
    print(f"  locked_location: '{seq.get('locked_location', '')}'")
    print(f"  location_anchor: '{seq.get('location_anchor', '')}'")
    for sc in seq.get('scenes', []):
        gsid = sc.get('global_scene_id', '')
        loc = sc.get('locked_location', '')
        anchor = sc.get('location_anchor', '')
        print(f"  {gsid}: loc='{loc}' anchor='{anchor}'")
