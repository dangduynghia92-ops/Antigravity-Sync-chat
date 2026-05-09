import json, os, glob

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
    'v1_Cuộc_Đời_Bạn', 'Test 3', 'video_prompt')

# Check Step 1 crowd_types from all chapters
print("=== Step 1: crowd_types per sequence ===")
all_ct = set()
for f in sorted(glob.glob(os.path.join(base, '*_step1_sequences.json'))):
    seq = json.load(open(f, encoding='utf-8'))
    for s in seq:
        ct = s.get('crowd_types', [])
        if ct:
            print(f"  {s['sequence_id']}: {ct}")
            all_ct.update(ct)

print(f"\nTotal unique crowd_types: {len(all_ct)}")
for ct in sorted(all_ct):
    print(f"  - {ct}")

# Check crowd sheets
crowd_file = os.path.join(base, 'ch_08_Level_8__Chilled_step2d_crowd.json')
if os.path.exists(crowd_file):
    crowd = json.load(open(crowd_file, encoding='utf-8'))
    chars = crowd.get('characters', [])
    print(f"\n=== Step 2d: {len(chars)} crowd sheets ===")
    
    # Group by crowd_type
    by_type = {}
    for c in chars:
        ct = c.get('crowd_type', '?')
        by_type.setdefault(ct, []).append(c.get('label', ''))
    
    print(f"Unique crowd_types in sheets: {len(by_type)}")
    for ct, labels in sorted(by_type.items()):
        print(f"  {ct}: {labels}")

# Identify REDUNDANT types
print("\n=== REDUNDANCY ANALYSIS ===")
states = ['dying', 'fleeing', 'butchered', 'scattered', 'corpse']
base_types = ['soldiers', 'infantry', 'foot soldiers', 'vanguard infantry']
guard_types = ['guards', 'sentries', 'elite guards']
knight_types = ['crusader knights', 'knights', 'templars', 'heavy cavalry']

for name, group in [('State-based (not types)', states),
                     ('Soldier variants', base_types),
                     ('Guard variants', guard_types),
                     ('Knight variants', knight_types)]:
    found = [ct for ct in all_ct if any(s in ct.lower() for s in group)]
    if found:
        print(f"  {name}: {found}")
