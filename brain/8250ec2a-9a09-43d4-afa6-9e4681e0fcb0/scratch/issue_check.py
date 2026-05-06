import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt'

# ═══ Issue 2: locked_location trống ═══
print("=" * 60)
print("ISSUE 2: locked_location CHECK (all sequences)")
print("=" * 60)
with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    scenes = json.load(f)
for seq in scenes:
    sid = seq.get('sequence_id', '')
    loc = seq.get('locked_location', '')
    loc_anchor = seq.get('location_anchor', '')
    print(f"  {sid}: locked_location='{loc}' | location_anchor='{loc_anchor}'")

# Check Step 1 sequences for location_shift
print()
with open(f'{base}\\ch_01_Level_1__Vulnerability_step1_sequences.json', encoding='utf-8') as f:
    seqs = json.load(f)
print("STEP 1 location_shift:")
for s in seqs:
    print(f"  {s['sequence_id']}: location_shift='{s.get('location_shift','')}'")

# Check Step 2c locations
print()
files = [f for f in __import__('glob').glob(f'{base}\\*locations*.json')]
if not files:
    # Check world bible for locations
    with open(f'{base}\\ch_01_Level_1__Vulnerability_step2_world_bible.json', encoding='utf-8') as f:
        wb = json.load(f)
    if 'locations' in wb:
        print("LOCATIONS IN WORLD BIBLE:")
        for loc in wb.get('locations', []):
            print(f"  {loc.get('label','?')}: {loc.get('bible_description','')[:80]}")
    else:
        print("NO LOCATIONS DATA FOUND")
else:
    for fp in files:
        with open(fp, encoding='utf-8') as f:
            data = json.load(f)
        print(f"LOCATIONS FILE: {__import__('os').path.basename(fp)}")
        for loc in data.get('locations', []):
            print(f"  {loc.get('label','?')}")

# ═══ Issue 3: camera_angle misuse ═══
print()
print("=" * 60)
print("ISSUE 3: camera_angle VALUES (all prompts)")
print("=" * 60)
with open(f'{base}\\ch_01_Level_1__Vulnerability_step4_prompts.json', encoding='utf-8') as f:
    prompts = json.load(f)
angles = {}
for p in prompts:
    angle = p.get('camera_angle', '')
    angles[angle] = angles.get(angle, 0) + 1
for angle, count in sorted(angles.items(), key=lambda x: -x[1]):
    valid = angle.lower() in ('eye-level', 'low-angle', 'high-angle', 'dutch-angle')
    mark = 'OK' if valid else 'BAD'
    print(f"  {mark} '{angle}': {count} scenes")

# Show which scenes have wrong angle
print("\nScenes with non-standard camera_angle:")
for p in prompts:
    angle = p.get('camera_angle', '').lower()
    if angle not in ('eye-level', 'low-angle', 'high-angle', 'dutch-angle'):
        print(f"  {p.get('global_scene_id','')}: camera_angle='{p.get('camera_angle','')}'")
