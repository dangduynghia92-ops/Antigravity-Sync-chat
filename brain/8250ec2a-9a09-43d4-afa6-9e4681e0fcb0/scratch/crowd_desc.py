import json
base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test 3\video_prompt'
with open(f'{base}\\ch_08_Level_8__Chilled_step2d_crowd.json', encoding='utf-8') as f:
    crowd = json.load(f)
for c in crowd.get('characters', [])[:3]:
    label = c.get('label', '')
    vd = c.get('visual_description', '')
    print(f'{label}:')
    print(f'  visual_description: {vd[:300]}')
    print()
