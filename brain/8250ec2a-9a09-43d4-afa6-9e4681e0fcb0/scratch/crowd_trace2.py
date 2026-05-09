import json, os, glob

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
    'v1_Cuộc_Đời_Bạn', 'Test 3', 'video_prompt')

# Check Step 4 output
step4 = os.path.join(base, 'ch_08_Level_8__Chilled_step4_prompts.json')
if os.path.exists(step4):
    data = json.load(open(step4, encoding='utf-8'))
    print(f"=== Step 4 prompts: {len(data)} items ===\n")
    for i, p in enumerate(data[:5]):
        print(f"--- Prompt {i+1}: {p.get('global_scene_id', '?')} ---")
        print(f"  characters: {p.get('characters', '')}")
        print(f"  has_crowd: {p.get('has_crowd', '?')}")
        print(f"  crowd_labels: {p.get('crowd_labels', 'MISSING')}")
        flat = p.get('flat_prompt', '')
        print(f"  flat_prompt (first 200): {flat[:200]}")
        print()
else:
    print("Step 4 file not found, checking other files...")

# Check Step 3.2 output - does it have crowd_labels?
for f in sorted(glob.glob(os.path.join(base, '*_step3_scenes.json'))):
    data = json.load(open(f, encoding='utf-8'))
    print(f"\n=== Step 3.2: {os.path.basename(f)} ===")
    for seq in data[:2]:
        sid = seq.get('sequence_id', '?')
        for scene in seq.get('scenes', [])[:3]:
            gsid = scene.get('global_scene_id', '?')
            cl = scene.get('crowd_labels', 'MISSING')
            chars = scene.get('character_labels', [])
            hc = scene.get('has_crowd', '?')
            print(f"  {gsid}: chars={chars}, crowd_labels={cl}, has_crowd={hc}")

# Check Step 3.1 output - does it have crowd_labels?
for f in sorted(glob.glob(os.path.join(base, '*_step3_1_filmable.json'))):
    data = json.load(open(f, encoding='utf-8'))
    print(f"\n=== Step 3.1: {os.path.basename(f)} ===")
    for seq_id, entries in list(data.items())[:2]:
        print(f"  {seq_id}:")
        for entry in entries[:2]:
            cl = entry.get('character_labels', entry.get('present_labels', 'MISSING'))
            crowd = entry.get('crowd_labels', 'MISSING')
            print(f"    sent {entry.get('sentence_id')}: char_labels={cl}, crowd_labels={crowd}")

# Check final export CSV/JSON
for f in sorted(glob.glob(os.path.join(base, '*.json'))):
    bn = os.path.basename(f)
    if 'final' in bn.lower() or 'export' in bn.lower() or 'prompt' in bn.lower():
        if 'step' not in bn:
            print(f"\n=== Export: {bn} ===")
            data = json.load(open(f, encoding='utf-8'))
            if isinstance(data, list) and len(data) > 0:
                p = data[0]
                print(f"  Keys: {list(p.keys())}")
                print(f"  crowd_labels: {p.get('crowd_labels', 'MISSING')}")
