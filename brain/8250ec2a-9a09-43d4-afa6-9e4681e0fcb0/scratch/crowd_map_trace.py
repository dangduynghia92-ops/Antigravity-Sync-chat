import json, os, glob

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
    'v1_Cuộc_Đời_Bạn', 'Test 3', 'video_prompt')

# 1. Load Step 1 sequences → crowd_types
seq_files = sorted(glob.glob(os.path.join(base, '*_step1_sequences.json')))
sequences = []
for f in seq_files:
    sequences.extend(json.load(open(f, encoding='utf-8')))

# 2. Load crowd_data → build crowd_type_to_labels
crowd_file = os.path.join(base, 'ch_08_Level_8__Chilled_step2d_crowd.json')
crowd_data = json.load(open(crowd_file, encoding='utf-8'))
crowd_chars = crowd_data.get('characters', [])

# Build exact same lookup as code does
crowd_type_to_labels = {}
for c in crowd_chars:
    ct = c.get("crowd_type", "").lower().strip()
    if ct:
        crowd_type_to_labels.setdefault(ct, []).append(c.get("label", ""))

print("=== crowd_type_to_labels lookup ===")
for k, v in sorted(crowd_type_to_labels.items()):
    print(f"  '{k}' → {v}")

# 3. Simulate mapping for each sequence
print("\n=== Mapping per sequence ===")
valid_crowd = [c.get("label", "") for c in crowd_chars if c.get("label")]

for seq in sequences:
    sid = seq.get('sequence_id', '?')
    raw_crowd = seq.get('crowd_types', [])
    if not raw_crowd:
        continue
    
    crowd_labels = []
    for ct in raw_crowd:
        ct_lower = ct.lower().strip()
        if ct_lower in crowd_type_to_labels:
            crowd_labels.extend(crowd_type_to_labels[ct_lower])
        else:
            # Fallback substring
            for cl in valid_crowd:
                if ct_lower in cl.lower():
                    crowd_labels.append(cl)
    crowd_labels = list(set(crowd_labels))
    
    print(f"  {sid}: crowd_types={raw_crowd}")
    print(f"         → crowd_labels={crowd_labels}")
    if not crowd_labels:
        print(f"         ❌ NO MATCH - checking why:")
        for ct in raw_crowd:
            ct_lower = ct.lower().strip()
            print(f"           '{ct_lower}' in lookup? {ct_lower in crowd_type_to_labels}")
