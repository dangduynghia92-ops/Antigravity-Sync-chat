import json, os

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerable'
target_label = "Zengid-Commander-A"

# 1. Character sheet
chars_file = os.path.join(base, 'ch_01_Level_1__Vulnerable_step2_characters.json')
with open(chars_file, encoding='utf-8') as f:
    data = json.load(f)
chars = data.get('characters', data) if isinstance(data, dict) else data

print("=" * 70)
print("CHARACTER SHEET — Costume Reference")
print("=" * 70)
for c in chars:
    label = c.get('label', '')
    if target_label.lower() in label.lower():
        print(f"Label: {label}")
        desc = c.get('visual_description', '')
        for line in desc.split('\n'):
            line_s = line.strip()
            if line_s:
                print(f"  {line_s}")
        print()

# 2. Step 4 prompts
prompts_file = os.path.join(base, 'ch_01_Level_1__Vulnerable_step4_prompts.json')
with open(prompts_file, encoding='utf-8') as f:
    prompts = json.load(f)

print("=" * 70)
print("COSTUME IN EACH SCENE")
print("=" * 70)
costumes = []
for p in prompts:
    scene_id = p.get('global_scene_id', p.get('scene_id', ''))
    for cd in p.get('characters_detail', []):
        label = cd.get('label', '')
        if target_label.lower() in label.lower():
            costume = cd.get('costume', 'N/A')
            costumes.append(costume)
            print(f"\n{scene_id}: [{label}]")
            print(f"  {costume}")

# 3. Consistency
print("\n" + "=" * 70)
print("CONSISTENCY CHECK")
print("=" * 70)
unique = set(costumes)
if len(costumes) == 0:
    print("No scenes found for this character")
elif len(unique) == 1:
    print(f"✅ CONSISTENT — Same costume in all {len(costumes)} scenes")
else:
    print(f"⚠️ INCONSISTENT — {len(unique)} different costumes across {len(costumes)} scenes:")
    for i, c in enumerate(sorted(unique), 1):
        count = costumes.count(c)
        print(f"\n  Variant {i} ({count}x): {c}")
