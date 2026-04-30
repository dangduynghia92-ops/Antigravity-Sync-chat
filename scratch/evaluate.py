import json

base = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt\Chapter 1 - Level 1 The Numb Arm and Childhood Signs'

# Step 1
with open(base + '_step1_sequences.json', 'r', encoding='utf-8') as f:
    seqs = json.load(f)
print(f"=== STEP 1: {len(seqs)} sequences ===")
for s in seqs:
    lt = s.get('location_type', 'N/A')
    ls = s.get('location_shift', '')
    sid = s.get('sequence_id', '')
    chars = s.get('characters', [])
    dur = s.get('total_duration', 0)
    print(f"  {sid:8s} | type={lt:10s} | dur={dur:5.1f}s | loc={ls[:35]:35s} | chars={len(chars)}")

# Step 2a
with open(base + '_step2_characters.json', 'r', encoding='utf-8') as f:
    chars_data = json.load(f)
chars_list = chars_data.get('characters', [])
print(f"\n=== STEP 2a: {len(chars_list)} characters ===")
for c in chars_list:
    label = c.get('label', '')
    name = c.get('original_name', '')
    print(f"  {label:35s} = {name}")

# Step 2 visual bible
with open(base + '_step2_visual_bible.json', 'r', encoding='utf-8') as f:
    locs = json.load(f)
locs_list = locs.get('locations', [])
print(f"\n=== STEP 2b: {len(locs_list)} locations ===")
for loc in locs_list:
    print(f"  {loc.get('label', '')}")

# World Bible
try:
    with open(base + '_step2_world_bible.json', 'r', encoding='utf-8') as f:
        wb = json.load(f)
    print(f"\n=== STEP 2c: World Bible ===")
    for period in wb.get('periods', []):
        print(f"  Era: {period.get('era', '')}")
        for k in ['military', 'civilian', 'weapons', 'architecture']:
            items = period.get(k, [])
            if items:
                print(f"    {k}: {len(items)} items")
except:
    print("\n=== STEP 2c: No world bible ===")

# Step 3
with open(base + '_step3_scenes.json', 'r', encoding='utf-8') as f:
    scenes_data = json.load(f)
total_scenes = sum(len(s.get('scenes', [])) for s in scenes_data)
print(f"\n=== STEP 3: {len(scenes_data)} sequences -> {total_scenes} scenes ===")
shot_types = {}
for seq in scenes_data:
    for sc in seq.get('scenes', []):
        st = sc.get('shot_type', 'unknown')
        shot_types[st] = shot_types.get(st, 0) + 1
print("  Shot types:", dict(sorted(shot_types.items(), key=lambda x: -x[1])))

# Check location consistency
print("\n  Location consistency:")
for seq in scenes_data[:5]:
    sid = seq.get('sequence_id', '')
    loc = seq.get('locked_location', '')
    n_scenes = len(seq.get('scenes', []))
    print(f"    {sid}: {loc} ({n_scenes} scenes)")

# Step 4
with open(base + '_step4_prompts.json', 'r', encoding='utf-8') as f:
    prompts = json.load(f)
print(f"\n=== STEP 4: {len(prompts)} prompts ===")

# Check label usage in prompts
label_used = 0
label_missing = 0
for p in prompts:
    fp = p.get('flat_prompt', '')
    if '[' in fp and ']' in fp:
        label_used += 1
    else:
        label_missing += 1
print(f"  Labels in flat_prompt: {label_used}/{len(prompts)} ({label_missing} missing)")

# Sample prompts
print(f"\n=== SAMPLE PROMPTS ===")
for p in prompts[:3]:
    sid = p.get('global_scene_id', '')
    fp = p.get('flat_prompt', '')
    print(f"\n  {sid}:")
    print(f"  {fp[:200]}...")
