import json

with open(r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Prompt\Chapter 1 - Level 1 The Numb Arm and Childhood Signs\Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step3_scenes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

abstract_words = ['growing inside', 'sand castle', 'history', 'fragile', 'will fall', 'destiny', 'something that will eat', 'opportunity', 'calculating']

for seq in data:
    text = seq.get('full_text', '')
    if any(w in text.lower() for w in abstract_words):
        sid = seq.get('sequence_id', '')
        print(f"=== {sid} ===")
        print(f"TEXT: {text[:150]}...")
        for s in seq.get('scenes', []):
            scn_id = s.get('global_scene_id', '')
            action = s.get('physical_action', '')[:120]
            bg = s.get('background_and_extras', '')[:100]
            audio = s.get('audio_sync', '')[:80]
            print(f"  {scn_id}")
            print(f"    audio: {audio}")
            print(f"    action: {action}")
            print(f"    bg: {bg}")
        print()
