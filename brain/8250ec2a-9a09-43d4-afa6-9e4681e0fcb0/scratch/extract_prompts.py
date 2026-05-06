"""Extract all prompt constants from video_pipeline.py into separate .txt files."""
import re, os

src = r'f:\1. Edit Videos\8.AntiCode\1.Prompt_Image\1.Prompt_Image\core\video_pipeline.py'
out_dir = r'f:\1. Edit Videos\8.AntiCode\1.Prompt_Image\1.Prompt_Image\prompts'
os.makedirs(out_dir, exist_ok=True)

with open(src, encoding='utf-8') as f:
    code = f.read()

# Map: constant name -> output filename
targets = {
    'STEP1_SYSTEM_PROMPT': 'step1_system_prompt.txt',
    'STEP2_CHARACTERS_SYSTEM_PROMPT': 'step2b_characters_system_prompt.txt',
    'STEP2_LOCATIONS_SYSTEM_PROMPT': 'step2c_locations_system_prompt.txt',
    'STEP2A_IDENTIFY_PROMPT': 'step2a_1_identify_prompt.txt',
    'STEP2A_PEOPLE_PROMPT': 'step2a_2_people_prompt.txt',
    'STEP2A_WORLD_PROMPT': 'step2a_3_world_prompt.txt',
    'STEP3_SYSTEM_PROMPT': 'step3_system_prompt.txt',
    'STEP4_USER_TEMPLATE': 'step4_user_template.txt',
    'STEP4_USER_TEMPLATE_INLINE': 'step4_user_template_inline.txt',
}

for const_name, filename in targets.items():
    # Match: CONST_NAME = """..."""
    pattern = rf'^{const_name}\s*=\s*"""(.*?)"""'
    m = re.search(pattern, code, re.DOTALL | re.MULTILINE)
    if m:
        content = m.group(1).strip()
        # Unescape {{}} -> {} for template strings
        filepath = os.path.join(out_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"OK: {filename} ({len(content)} chars)")
    else:
        print(f"NOT FOUND: {const_name}")

# Also extract PROMPT_SUFFIX
m = re.search(r'^PROMPT_SUFFIX\s*=\s*"(.*?)"', code, re.MULTILINE)
if m:
    filepath = os.path.join(out_dir, 'prompt_suffix.txt')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(m.group(1))
    print(f"OK: prompt_suffix.txt ({len(m.group(1))} chars)")

print(f"\nAll files saved to: {out_dir}")
