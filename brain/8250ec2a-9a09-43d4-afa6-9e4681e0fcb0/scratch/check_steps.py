import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test 3\video_prompt'

with open(f'{base}\\ch_08_Level_8__Chilled_step4_prompts.json', encoding='utf-8') as f:
    s4 = json.load(f)

# Audit each prompt for completeness
checklist = {
    'char_appearance': 0,   # character body/face described
    'char_costume': 0,      # character costume detail
    'char_action': 0,       # character doing something
    'crowd_costume': 0,     # crowd costume described
    'crowd_action': 0,      # crowd doing something
    'interaction': 0,       # character interaction described
    'no_char_no_crowd': 0,  # empty scene?
}

problems = []

for i, p in enumerate(s4):
    fp = p.get('flat_prompt', '')
    chars = p.get('characters', '')
    extras = p.get('extras', '')
    crowd = p.get('crowd_labels', [])
    interaction = p.get('character_info', '')
    
    has_char = bool(chars)
    has_crowd = bool(crowd)
    
    # Check character appearance (body/face/head)
    if has_char:
        if any(w in fp.lower() for w in ['circular', 'head', 'face', 'eyes', 'beard']):
            checklist['char_appearance'] += 1
        else:
            problems.append(f"Prompt {i+1} ({p['global_scene_id']}): CHAR missing appearance in flat_prompt")
        
        # Check costume
        if any(w in fp.lower() for w in ['wears', 'kaftan', 'armor', 'helmet', 'tunic', 'robe', 'cloak']):
            checklist['char_costume'] += 1
        else:
            problems.append(f"Prompt {i+1} ({p['global_scene_id']}): CHAR missing costume in flat_prompt")
        
        # Check action
        if any(w in fp.lower() for w in ['standing', 'walking', 'sitting', 'leaning', 'looking', 'riding', 'pointing', 'holding', 'raises', 'turns', 'lifts', 'grips', 'reaches']):
            checklist['char_action'] += 1
        else:
            problems.append(f"Prompt {i+1} ({p['global_scene_id']}): CHAR missing action in flat_prompt")
    
    # Check crowd
    if has_crowd and 'EXT-' in fp:
        if any(w in fp.lower() for w in ['wear', 'kazaghand', 'armor', 'helmet', 'tunic', 'chainmail', 'surcoat', 'cotton']):
            checklist['crowd_costume'] += 1
        else:
            problems.append(f"Prompt {i+1} ({p['global_scene_id']}): CROWD missing costume in flat_prompt")
        
        if any(w in fp.lower() for w in ['patrol', 'march', 'stand', 'huddle', 'guard', 'charge', 'ride', 'walk', 'carry', 'lined', 'row', 'formation']):
            checklist['crowd_action'] += 1
        else:
            problems.append(f"Prompt {i+1} ({p['global_scene_id']}): CROWD missing action in flat_prompt")
    
    if not has_char and not has_crowd:
        checklist['no_char_no_crowd'] += 1

    # Check interaction (multi-character scenes)
    char_labels = p.get('characters', '').split(', ') if p.get('characters') else []
    if len(char_labels) >= 2:
        checklist['interaction'] += 1

total_with_char = sum(1 for p in s4 if p.get('characters'))
total_with_crowd = sum(1 for p in s4 if p.get('crowd_labels') and 'EXT-' in p.get('flat_prompt', ''))

print('=' * 80)
print('AUDIT: Mô tả đầy đủ trong flat_prompt?')
print('=' * 80)
print(f"Total prompts: {len(s4)}")
print(f"Có named character: {total_with_char}")
print(f"Có crowd (EXT- in flat_prompt): {total_with_crowd}")
print()
print(f"Character appearance (face/head): {checklist['char_appearance']}/{total_with_char}")
print(f"Character costume detail: {checklist['char_costume']}/{total_with_char}")
print(f"Character action: {checklist['char_action']}/{total_with_char}")
print(f"Crowd costume detail: {checklist['crowd_costume']}/{total_with_crowd}")
print(f"Crowd action: {checklist['crowd_action']}/{total_with_crowd}")
print(f"Multi-char interaction: {checklist['interaction']}")
print(f"No char, no crowd: {checklist['no_char_no_crowd']}")

if problems:
    print(f"\n⚠ THIẾU ({len(problems)} issues):")
    for p in problems[:20]:
        print(f"  {p}")
else:
    print("\n✅ Tất cả prompts đầy đủ mô tả!")

# Show a multi-character scene full prompt
print('\n' + '=' * 80)
print('MẪU: Scene có interaction / multi-character')
print('=' * 80)
for p in s4:
    chars = p.get('characters', '')
    if ',' in chars:
        print(f"\n--- {p['global_scene_id']} ---")
        print(f"characters: {chars}")
        print(f"extras: {p.get('extras', '')}")
        print(f"flat_prompt:\n{p['flat_prompt']}")
        break

# Show a crowd-heavy scene
print('\n' + '=' * 80)
print('MẪU: Scene nặng crowd')
print('=' * 80)
for p in s4:
    if not p.get('characters') and p.get('crowd_labels'):
        print(f"\n--- {p['global_scene_id']} ---")
        print(f"crowd_labels: {p.get('crowd_labels')}")
        print(f"extras: {p.get('extras', '')}")
        print(f"flat_prompt:\n{p['flat_prompt']}")
        break
