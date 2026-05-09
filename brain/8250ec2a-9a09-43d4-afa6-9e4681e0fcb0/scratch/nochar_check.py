import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

fp = os.path.join(base, 'ch_08_Level_8__Chilled_step4_prompts.json')
with open(fp, encoding='utf-8') as f:
    prompts = json.load(f)

# Find the problematic prompt
for p in prompts:
    if p.get('global_scene_id') == 'SEQ_01_SCN_06':
        print(f"=== {p['global_scene_id']} ===")
        print(f"characters: '{p.get('characters', '')}'")
        print(f"has_crowd: {p.get('has_crowd', 'MISSING')}")
        print(f"extras: '{p.get('extras', '')}'")
        print(f"character_info: '{p.get('character_info', '')}'")
        print(f"flat_prompt: {p.get('flat_prompt', '')[:300]}")
        break

# Count all prompts with "NO characters" suffix but characters in flat_prompt
print("\n=== Prompts with 'NO characters' contradiction ===")
count = 0
for p in prompts:
    fp_text = p.get('flat_prompt', '')
    has_no_chars = 'NO characters, NO people' in fp_text
    # Check if prompt describes people before the NO suffix
    before_suffix = fp_text.split('NO characters')[0] if 'NO characters' in fp_text else fp_text
    has_people_words = any(w in before_suffix.lower() for w in ['guard', 'soldier', 'man ', 'woman', 'warrior', 'figure', 'person'])
    
    if has_no_chars and has_people_words:
        count += 1
        gid = p.get('global_scene_id', '?')
        chars = p.get('characters', '')
        extras = p.get('extras', '')
        print(f"  {gid}: characters='{chars}' extras='{extras}'")
        print(f"    prompt: {before_suffix[:150]}...")

print(f"\nTotal contradictions: {count}")
