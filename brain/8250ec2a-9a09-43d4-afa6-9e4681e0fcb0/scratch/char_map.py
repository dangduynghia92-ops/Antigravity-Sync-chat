import json
base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'
with open(f'{base}\\ch_01_Level_1__Vulnerability_step2_characters.json', encoding='utf-8') as f:
    chars = json.load(f)
for c in chars.get('characters', []):
    print(f"  {c.get('label')} = {c.get('original_name')}")

with open(f'{base}\\ch_01_Level_1__Vulnerability_step1_sequences.json', encoding='utf-8') as f:
    seqs = json.load(f)
print("\nSequence characters (raw names):")
for s in seqs:
    print(f"  {s['sequence_id']}: {s.get('characters', [])}")
