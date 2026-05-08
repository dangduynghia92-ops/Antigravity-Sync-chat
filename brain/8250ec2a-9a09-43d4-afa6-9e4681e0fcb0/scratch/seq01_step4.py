import json

# Check Step 4 prompts for SEQ_01
fp = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerable\ch_01_Level_1__Vulnerable_step4_prompts.json'

with open(fp, encoding='utf-8') as f:
    prompts = json.load(f)

print("=== SEQ_01 STEP 4 — Characters + Interaction ===\n")
for p in prompts:
    scene_id = p.get('global_scene_id', p.get('scene_id', ''))
    if not scene_id.startswith('SEQ_01'):
        continue
    
    chars = [cd.get('label', '') for cd in p.get('characters_detail', [])]
    interaction = p.get('character_interaction', 'NOT IN DATA')
    
    print(f"{scene_id}: {chars}")
    print(f"  interaction: {interaction}")
    print(f"  flat_prompt (first 200): {p.get('flat_prompt', '')[:200]}")
    print()

# Check Step 3.2 scenes for interaction field
fp3 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerable\ch_01_Level_1__Vulnerable_step3_scenes.json'

with open(fp3, encoding='utf-8') as f:
    scenes = json.load(f)

print("\n=== SEQ_01 STEP 3.2 — Interaction field ===\n")
for seq in scenes:
    if seq.get('sequence_id', '') != 'SEQ_01':
        continue
    for sc in seq.get('scenes', []):
        sid = sc.get('global_scene_id', '')
        interaction = sc.get('character_interaction', 'NOT IN DATA')
        char_labels = sc.get('character_labels', [])
        print(f"{sid}: chars={char_labels} | interaction={interaction}")
