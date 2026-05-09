"""Trace how present_labels from Step 3.1 flows into Step 3.2 character_labels."""
import re

fp = r'f:\1. Edit Videos\8.AntiCode\1.Prompt_Image\1.Prompt_Image\core\video_pipeline.py'
with open(fp, encoding='utf-8') as f:
    lines = f.readlines()

# Find _run_step3 and _process_sequence_step3 — where Step 3.1 output is consumed
print("=== Where Step 3.1 output (filmable_scenes) is consumed ===")
for i, line in enumerate(lines, 1):
    if 'filmable' in line.lower() and ('present_labels' in line or 'character_labels' in line or 'is_broll' in line):
        print(f"  L{i}: {line.strip()[:130]}")

print("\n=== Step 3.2 _process_sequence_step3 — input construction ===")
for i, line in enumerate(lines, 1):
    if ('filmable' in line or 'visual_treatment' in line) and not line.strip().startswith('#'):
        if i > 2150 and i < 2400:
            print(f"  L{i}: {line.strip()[:130]}")

# Find has_crowd references in code (not prompts)
print("\n=== has_crowd in code logic ===")
for i, line in enumerate(lines, 1):
    if 'has_crowd' in line and '.get(' in line:
        print(f"  L{i}: {line.strip()[:130]}")

# Find "NO characters" logic
print("\n=== 'NO characters' suffix logic ===")
for i, line in enumerate(lines, 1):
    if 'NO characters' in line or 'NO people' in line:
        print(f"  L{i}: {line.strip()[:130]}")

# Find scene_id vs global_scene_id usage
print("\n=== scene_id vs global_scene_id ===")
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if 'scene_id' in stripped and '.get(' in stripped and not stripped.startswith('#'):
        print(f"  L{i}: {stripped[:130]}")
