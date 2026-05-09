import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

# Step 2b map
map_path = os.path.join(base, 'ch_08_Level_8__Chilled_step2b_character_map.json')
with open(map_path, encoding='utf-8') as f:
    char_map = json.load(f)

print("=== Step 2b Character Map ===")
print(json.dumps(char_map, ensure_ascii=False, indent=2)[:2000])

# Characters (valid labels)
char_path = os.path.join(base, 'ch_08_Level_8__Chilled_step2_characters.json')
with open(char_path, encoding='utf-8') as f:
    chars = json.load(f)

print("\n=== Valid Labels ===")
for c in chars:
    print(f"  {c.get('label')}")

# Sequences
seq_path = os.path.join(base, 'ch_08_Level_8__Chilled_step1_sequences.json')
with open(seq_path, encoding='utf-8') as f:
    seqs = json.load(f)

print("\n=== SEQ_01 raw characters ===")
print(f"  {seqs[0].get('characters')}")
