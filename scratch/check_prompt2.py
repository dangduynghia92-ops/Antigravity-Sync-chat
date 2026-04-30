import json, os

base = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt'

f4 = os.path.join(base, 'Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step4_prompts.json')
data = json.loads(open(f4, encoding='utf-8').read())

# Show FULL flat_prompt for first prompt
print("=== FULL FLAT_PROMPT (Prompt #1) ===")
print(data[0].get("flat_prompt", ""))
print()
print("=== FULL NEGATIVE_PROMPT ===")
print(data[0].get("negative_prompt", ""))
