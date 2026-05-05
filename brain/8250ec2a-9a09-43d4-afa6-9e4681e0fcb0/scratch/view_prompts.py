import json

path4 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step4_prompts.json'
with open(path4, encoding='utf-8') as f:
    prompts = json.load(f)

for p in prompts:
    if p.get('global_scene_id', '').startswith('SEQ_01'):
        print(f"{'='*60}")
        print(f"{p['global_scene_id']}  |  {p.get('location', '')}")
        print(f"{'='*60}")
        print(p.get('flat_prompt', ''))
        print()
