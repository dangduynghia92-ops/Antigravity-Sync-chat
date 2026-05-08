import json

v5 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\V5\video_prompt'

# Check Step 4 output fields
with open(f'{v5}\\ch_01_Level_1__Vulnerability_step4_prompts.json', encoding='utf-8') as f:
    prompts = json.load(f)

# Print first scene with all fields
p = prompts[0]
print("=== STEP 4 FIELDS (scene 1) ===")
for k, v in p.items():
    if k == 'flat_prompt':
        print(f"  {k}: {str(v)[:100]}...")
    elif isinstance(v, list):
        print(f"  {k}: {json.dumps(v, ensure_ascii=False)[:100]}")
    else:
        print(f"  {k}: {v}")

# Check Step 3 scene fields
with open(f'{v5}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    scenes = json.load(f)

print("\n=== STEP 3 SCENE FIELDS (scene 1) ===")
s = scenes[0]['scenes'][0]
for k, v in s.items():
    if isinstance(v, str) and len(v) > 100:
        print(f"  {k}: {v[:100]}...")
    else:
        print(f"  {k}: {v}")
