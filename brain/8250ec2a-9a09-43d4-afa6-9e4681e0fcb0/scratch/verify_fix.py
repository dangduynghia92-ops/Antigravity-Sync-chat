"""Simulate the fix: apply normalization to Test 3 data and verify all labels resolve."""
import json, os, re

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

char_map = json.load(open(os.path.join(base, 'ch_08_Level_8__Chilled_step2b_character_map.json'), encoding='utf-8'))
chars = json.load(open(os.path.join(base, 'ch_08_Level_8__Chilled_step2_characters.json'), encoding='utf-8'))
seqs = json.load(open(os.path.join(base, 'ch_08_Level_8__Chilled_step1_sequences.json'), encoding='utf-8'))

if isinstance(chars, list):
    valid_chars = [c.get('label','') for c in chars if c.get('label')]
else:
    valid_chars = [c.get('label','') for c in chars.get('characters', []) if c.get('label')]

print(f"Valid labels: {valid_chars}\n")

# Layer 1: Normalize
normalized = 0
for seq_id, mapping in char_map.items():
    for raw_name, mapped_label in list(mapping.items()):
        if not mapped_label:
            continue
        if mapped_label in valid_chars:
            continue
        base_label = re.sub(r'-(Child|Teen|YoungAdult|MatureAdult|Elder)$', '', mapped_label)
        if base_label in valid_chars:
            mapping[raw_name] = base_label
            normalized += 1

print(f"Layer 1: Normalized {normalized} labels\n")

# Simulate _map_raw_to_labels for each sequence
print("=== Simulated mapping results ===")
for seq in seqs:
    seq_id = seq.get('sequence_id', '')
    raw_chars = seq.get('characters', [])
    seq_map = char_map.get(seq_id, {})
    
    labels = []
    for raw in raw_chars:
        mapped = seq_map.get(raw)
        if not mapped:
            raw_lower = raw.lower().strip()
            for k, v in seq_map.items():
                if k.lower().strip() == raw_lower:
                    mapped = v
                    break
        if mapped and mapped in valid_chars:
            labels.append(mapped)
        elif mapped:
            base_label = re.sub(r'-(Child|Teen|YoungAdult|MatureAdult|Elder)$', '', mapped)
            if base_label in valid_chars:
                labels.append(base_label)
    
    status = "✅" if len(labels) == len(raw_chars) else "❌"
    print(f"  {status} {seq_id}: raw={raw_chars} → labels={labels}")

# Count total resolved
total_raw = sum(len(seq.get('characters', [])) for seq in seqs)
total_resolved = 0
for seq in seqs:
    seq_id = seq.get('sequence_id', '')
    seq_map = char_map.get(seq_id, {})
    for raw in seq.get('characters', []):
        mapped = seq_map.get(raw)
        if mapped and mapped in valid_chars:
            total_resolved += 1

print(f"\nTotal: {total_resolved}/{total_raw} characters resolved")
