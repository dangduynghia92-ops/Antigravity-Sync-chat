import json, os, glob

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
    'v1_Cuộc_Đời_Bạn', 'Test 3', 'video_prompt')

# 1. Check Step 2d — sheet_prompt present?
crowd_file = os.path.join(base, 'ch_08_Level_8__Chilled_step2d_crowd.json')
if os.path.exists(crowd_file):
    crowd = json.load(open(crowd_file, encoding='utf-8'))
    chars = crowd.get('characters', [])
    print(f"=== Step 2d: {len(chars)} crowd sheets ===")
    has_sp = sum(1 for c in chars if c.get('sheet_prompt'))
    has_vd = sum(1 for c in chars if c.get('visual_description'))
    print(f"  sheet_prompt: {has_sp}/{len(chars)}")
    print(f"  visual_description: {has_vd}/{len(chars)}")
    print(f"  Keys of first: {list(chars[0].keys()) if chars else 'N/A'}")
    if chars:
        print(f"\n  Sample [{chars[0]['label']}]:")
        for k, v in chars[0].items():
            print(f"    {k}: {str(v)[:120]}")

# 2. Check Step 3.1 partial output (if exists)
filmable_files = sorted(glob.glob(os.path.join(base, '*_step3_1_filmable.json')))
if filmable_files:
    for f in filmable_files:
        data = json.load(open(f, encoding='utf-8'))
        bn = os.path.basename(f)
        total = 0
        with_crowd = 0
        crowd_samples = []
        for seq_id, entries in data.items():
            for entry in entries:
                total += 1
                cl = entry.get('crowd_labels', [])
                if cl:
                    with_crowd += 1
                    if len(crowd_samples) < 3:
                        crowd_samples.append((seq_id, entry.get('sentence_id'), cl))
        
        print(f"\n=== Step 3.1: {bn} ===")
        print(f"  Entries: {total}, with crowd_labels: {with_crowd} ({round(with_crowd/total*100,1) if total else 0}%)")
        if crowd_samples:
            print(f"  Samples with crowd:")
            for sid, sent_id, cl in crowd_samples:
                print(f"    {sid}/sent_{sent_id}: {cl}")
        else:
            print(f"  ❌ NO entries have crowd_labels!")
else:
    print("\nStep 3.1 not finished yet — no checkpoint file")
