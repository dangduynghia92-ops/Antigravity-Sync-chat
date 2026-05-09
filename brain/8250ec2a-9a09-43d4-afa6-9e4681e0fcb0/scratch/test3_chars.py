import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

# List all files
print("=== Files ===")
for f in sorted(os.listdir(base)):
    print(f"  {f}")

# Find character file
char_files = [f for f in os.listdir(base) if 'step2_characters' in f and f.endswith('.json')]
print(f"\n=== Character files: {char_files} ===\n")

for cf in char_files:
    fp = os.path.join(base, cf)
    with open(fp, encoding='utf-8') as f:
        data = json.load(f)
    
    chars = data if isinstance(data, list) else data.get("characters", data.get("world_bible", {}).get("characters", []))
    if isinstance(data, dict) and not chars:
        # Try top-level keys
        print(f"Keys in {cf}: {list(data.keys())}")
        chars = data.get("characters", [])
    
    print(f"{cf}: {len(chars)} characters")
    for c in chars:
        label = c.get("label", "?")
        name = c.get("original_name", "?")
        age = c.get("age_stage", "?")
        group = c.get("group", "?")
        print(f"  {label} | {name} | {age} | {group}")

# Check sequences for all character mentions
seq_files = [f for f in os.listdir(base) if 'step1_sequences' in f and f.endswith('.json')]
print(f"\n=== Sequence character mentions ===")
for sf in seq_files:
    fp = os.path.join(base, sf)
    with open(fp, encoding='utf-8') as f:
        seqs = json.load(f)
    
    all_chars = set()
    for seq in seqs:
        for c in seq.get("characters", []):
            all_chars.add(c)
    
    print(f"{sf}: {len(all_chars)} unique character mentions")
    for c in sorted(all_chars):
        print(f"  {c}")
