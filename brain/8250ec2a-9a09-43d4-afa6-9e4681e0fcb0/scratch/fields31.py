import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

fp = os.path.join(base, 'ch_08_Level_8__Chilled_step3_1_filmable.json')
with open(fp, encoding='utf-8') as f:
    data = json.load(f)

# Show all keys in first entry
seq01 = data.get('SEQ_01', [])
if seq01:
    entry = seq01[0]
    print(f"=== SEQ_01 entry 0 — ALL keys ===")
    print(json.dumps(entry, ensure_ascii=False, indent=2)[:600])
