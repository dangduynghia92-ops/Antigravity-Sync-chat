import json
f = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt\Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step2_characters.json'
data = json.loads(open(f, encoding='utf-8').read())
for c in data.get('characters', []):
    label = c.get('label', '')
    age = c.get('age_stage', '')
    name = c.get('original_name', '')
    vis = c.get('visual_description', '')
    print(f"=== {label} ({age}) ===")
    print(f"  Name: {name}")
    print(f"  Visual: {vis[:350]}")
    print()
