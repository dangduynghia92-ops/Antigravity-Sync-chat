import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'

with open(f'{base}\\ch_01_Level_1__Vulnerability_step2_characters.json', encoding='utf-8') as f:
    chars = json.load(f)
with open(f'{base}\\ch_01_Level_1__Vulnerability_step1_sequences.json', encoding='utf-8') as f:
    seqs = json.load(f)

print("=== STEP 2B: Character Label Map ===")
for c in chars.get('characters', []):
    print(f"  label: {c.get('label'):25s} | original_name: {c.get('original_name')}")

print("\n=== MAPPING TRACE ===")
# Replicate _map_raw_to_labels logic
char_map = {}
for c in chars.get('characters', []):
    label = c.get('label', '')
    orig = c.get('original_name', '').lower()
    if label and orig:
        char_map[orig] = label

print(f"\nchar_map (original_name.lower -> label):")
for k, v in char_map.items():
    print(f"  '{k}' -> '{v}'")

print("\n=== PER-SEQUENCE MAPPING ===")
for seq in seqs:
    sid = seq['sequence_id']
    raw_chars = seq.get('characters', [])
    if not raw_chars:
        print(f"\n{sid}: no characters")
        continue
    
    print(f"\n{sid}:")
    for raw in raw_chars:
        raw_lower = raw.lower().strip()
        matched = None
        match_reason = ""
        for orig, label in char_map.items():
            if orig in raw_lower:
                matched = label
                match_reason = f"orig '{orig}' IN raw '{raw_lower}'"
                break
            elif raw_lower in orig:
                matched = label
                match_reason = f"raw '{raw_lower}' IN orig '{orig}'"
                break
        
        if matched:
            print(f"  RAW: '{raw}'")
            print(f"    -> LABEL: '{matched}'")
            print(f"    -> reason: {match_reason}")
        else:
            print(f"  RAW: '{raw}'")
            print(f"    -> NO MATCH!")
