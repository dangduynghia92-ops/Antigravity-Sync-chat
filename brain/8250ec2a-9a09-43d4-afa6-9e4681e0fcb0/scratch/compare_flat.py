import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test 3\video_prompt'

with open(f'{base}\\ch_08_Level_8__Chilled_step4_prompts.json', encoding='utf-8') as f:
    s4 = json.load(f)

action_words = ['standing', 'walking', 'sitting', 'leaning', 'looking', 'riding', 
                'pointing', 'holding', 'raises', 'turns', 'lifts', 'grips', 'reaches',
                'lunges', 'kneels', 'runs', 'charges', 'bows', 'draws', 'swings',
                'shoves', 'pulls', 'pushes', 'sprints', 'hunches', 'crouches',
                'gestures', 'waves', 'steps', 'climbs', 'ducks', 'shields']

missing = []
has_action = []

for p in s4:
    if not p.get('characters'):
        continue  # skip crowd-only
    fp = p.get('flat_prompt', '').lower()
    found = [w for w in action_words if w in fp]
    if not found:
        missing.append(p)
    else:
        has_action.append((p, found))

print("=" * 90)
print(f"THIẾU ACTION: {len(missing)} prompts (có character nhưng flat_prompt thiếu hành động)")
print("=" * 90)

for p in missing[:8]:
    sid = p['global_scene_id']
    chars = p['characters']
    fp = p['flat_prompt']
    print(f"\n--- {sid} | chars: {chars} ---")
    print(fp[:300])
    print("...")

print("\n" + "=" * 90)
print(f"CÓ ACTION: {len(has_action)} prompts (ví dụ)")
print("=" * 90)

for p, words in has_action[:3]:
    sid = p['global_scene_id']
    print(f"\n--- {sid} | action words: {words} ---")
    print(p['flat_prompt'][:300])
    print("...")
