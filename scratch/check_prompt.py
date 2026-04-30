import json, os

base = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt'

# Step 4 prompts
f4 = os.path.join(base, 'Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step4_prompts.json')
data = json.loads(open(f4, encoding='utf-8').read())

# Show first 2 prompts
for i, prompt in enumerate(data[:2]):
    print(f"{'='*80}")
    print(f"Prompt #{i+1}")
    print(f"{'='*80}")
    for k, v in prompt.items():
        val = str(v)
        if len(val) > 200:
            val = val[:200] + "..."
        print(f"  {k}: {val}")
    print()
