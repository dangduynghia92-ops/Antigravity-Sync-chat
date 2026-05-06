import json

path = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step3_scenes.json'

with open(path, encoding='utf-8') as f:
    scenes = json.load(f)

for seq in scenes[:3]:  # first 3 sequences
    for s in seq.get('scenes', []):
        sid = s.get('global_scene_id', '')
        bg = s.get('background_and_extras', '')
        print(f"--- {sid} ---")
        print(f"  BG: {bg}")
        print()
