import json, os, glob, re

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
    'v1_Cuộc_Đời_Bạn', 'Test 3', 'video_prompt')

for f in sorted(glob.glob(os.path.join(base, '*_step4_prompts.json')))[:1]:
    data = json.load(open(f, encoding='utf-8'))
    shown = 0
    for p in data:
        cl = p.get('crowd_labels', [])
        fp = p.get('flat_prompt', '')
        if cl and 'EXT-' in fp:
            sid = p.get('global_scene_id', '?')
            exts = re.findall(r'\[EXT-[^\]]+\]', fp)
            print(f"--- {sid} ---")
            print(f"  crowd_labels: {cl}")
            print(f"  has_crowd: {p.get('has_crowd')}")
            print(f"  EXT refs in prompt: {exts}")
            print(f"  flat_prompt (300ch): {fp[:300]}...")
            print()
            shown += 1
            if shown >= 4:
                break
