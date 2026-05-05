import json, sys

path = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step3_scenes.json'
with open(path, encoding='utf-8') as f:
    data = json.load(f)

for seq in data:
    if seq.get('sequence_id') == 'SEQ_01':
        print(f"SEQ_01: locked_location = {seq.get('locked_location', '')}")
        print(f"visual_event = {seq.get('visual_event', '')}")
        print(f"total_duration = {seq.get('total_sequence_duration', 0)}")
        print()
        for s in seq.get('scenes', []):
            sid = s['global_scene_id']
            shot = s.get('shot_type', '')
            dur = s.get('duration', 0)
            cam = s.get('camera_motion', '')
            action = s.get('physical_action', '')
            bg = s.get('background_and_extras', '')
            light = s.get('lighting_and_atmosphere', '')
            costume = s.get('costume_note', '')
            print(f"  {sid} | {shot} | {dur}s | {cam}")
            print(f"    action: {action}")
            print(f"    costume: {costume}")
            print(f"    bg: {bg[:100]}")
            print(f"    lighting: {light[:100]}")
            print()
        break

# Also show SEQ_01 prompts from step4
path4 = path.replace('step3_scenes', 'step4_prompts')
with open(path4, encoding='utf-8') as f:
    prompts = json.load(f)

print("=" * 60)
print("STEP 4 PROMPTS for SEQ_01:")
print("=" * 60)
for p in prompts:
    if p.get('global_scene_id', '').startswith('SEQ_01'):
        print(f"\n{p['global_scene_id']}:")
        print(f"  location: {p.get('location', '')}")
        fp = p.get('flat_prompt', '')
        print(f"  flat_prompt: {fp[:200]}")
        print()
