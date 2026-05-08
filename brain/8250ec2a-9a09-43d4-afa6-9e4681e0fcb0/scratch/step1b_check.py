import json, os

# Check both output directories
dirs = [
    r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerable',
    r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt',
    r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\V5\video_prompt',
]

for d in dirs:
    print(f"\n{'='*60}")
    print(f"DIR: {d}")
    print('='*60)
    
    if not os.path.isdir(d):
        print("  NOT FOUND")
        continue
    
    # Check for step1b debug files
    debug_dir = None
    for item in os.listdir(d):
        if 'debug' in item.lower():
            debug_dir = os.path.join(d, item)
    
    if debug_dir and os.path.isdir(debug_dir):
        step1b_files = [f for f in os.listdir(debug_dir) if 'step1b' in f.lower()]
        if step1b_files:
            print(f"  Step 1b debug files: {step1b_files}")
        else:
            print(f"  No step1b debug files (debug dir has {len(os.listdir(debug_dir))} files)")
    else:
        print("  No debug dir")
    
    # Check step1 sequences for character lists
    step1_files = [f for f in os.listdir(d) if 'step1_sequences' in f]
    for sf in step1_files:
        fp = os.path.join(d, sf)
        with open(fp, encoding='utf-8') as f:
            seqs = json.load(f)
        print(f"\n  {sf}: {len(seqs)} sequences")
        for s in seqs:
            sid = s.get('sequence_id', '?')
            chars = s.get('characters', [])
            loc = s.get('location_shift', '')[:50]
            print(f"    {sid}: chars={chars}")
            print(f"           loc={loc}")
