import json, os, glob

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn'

# Find all step2_characters files
for f in glob.glob(os.path.join(base, '**', '*step2_characters*'), recursive=True):
    print(f"=== {os.path.basename(f)} ===")
    with open(f, encoding='utf-8') as fh:
        data = json.load(fh)
    for c in data.get('characters', []):
        label = c.get('label', '')
        name = c.get('original_name', '')
        desc = c.get('visual_description', '')[:150]
        sheet = c.get('sheet_prompt', '')[:100]
        print(f"  Label: {label}")
        print(f"  Name: {name}")
        print(f"  Desc: {desc}...")
        print(f"  Sheet: {sheet}...")
        print()
