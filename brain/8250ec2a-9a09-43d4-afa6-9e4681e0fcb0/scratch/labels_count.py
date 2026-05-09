import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

fp = os.path.join(base, 'ch_08_Level_8__Chilled_step3_1_filmable.json')
with open(fp, encoding='utf-8') as f:
    data = json.load(f)

has_labels = 0
empty_labels = 0

for seq_id, entries in data.items():
    for entry in entries:
        pl = entry.get('present_labels', 'MISSING')
        if pl == 'MISSING':
            print(f"  {seq_id} sent_{entry.get('sentence_id')}: MISSING present_labels")
        elif pl:
            has_labels += 1
        else:
            empty_labels += 1

print(f"\nTotal: has_labels={has_labels}, empty_labels={empty_labels}")
