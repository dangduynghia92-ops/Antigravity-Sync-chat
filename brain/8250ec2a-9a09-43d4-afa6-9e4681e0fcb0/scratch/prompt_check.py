import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'

with open(f'{base}\\ch_01_Level_1__Vulnerability_step4_prompts.json', encoding='utf-8') as f:
    prompts = json.load(f)
with open(f'{base}\\ch_01_Level_1__Vulnerability_step2_characters.json', encoding='utf-8') as f:
    chars = json.load(f)

print("=== CHARACTER DESCRIPTIONS FROM STEP 2B ===")
for c in chars.get('characters', []):
    label = c.get('label', '')
    desc = c.get('visual_description', '')
    print(f"\n[{label}]")
    print(f"  {desc[:200]}")

print("\n\n=== FLAT PROMPTS (checking for mask/skin issues) ===")
for p in prompts:
    fp = p.get('flat_prompt', '')
    sid = p.get('global_scene_id', '')
    # Search for problematic terms
    issues = []
    for term in ['mask', 'white face', 'pale face', 'dark skin', 'dark-skinned', 'tanned']:
        if term.lower() in fp.lower():
            issues.append(term)
    
    if issues:
        print(f"\n{'!'*60}")
        print(f"  {sid}: ISSUES FOUND: {issues}")
        print(f"  {fp[:300]}")
    else:
        print(f"  {sid}: OK")
        # Still print first 150 chars to spot visual issues
        print(f"    {fp[:150]}")
