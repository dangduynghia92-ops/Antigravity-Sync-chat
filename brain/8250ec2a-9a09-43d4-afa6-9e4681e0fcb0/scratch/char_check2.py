import json, os, glob

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt'

for f in sorted(glob.glob(os.path.join(base, '*step2_characters*'))):
    print(f"=== {os.path.basename(f)} ===\n")
    with open(f, encoding='utf-8') as fh:
        data = json.load(fh)
    for c in data.get('characters', []):
        print(f"  Label: {c.get('label','')}")
        print(f"  Name:  {c.get('original_name','')}")
        print(f"  Desc:  {c.get('visual_description','')[:200]}")
        print(f"  Sheet: {c.get('sheet_prompt','')[:200]}")
        print()
