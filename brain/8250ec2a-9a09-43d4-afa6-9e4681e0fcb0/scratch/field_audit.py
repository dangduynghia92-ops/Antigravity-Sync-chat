"""
FULL FIELD AUDIT: Trace every data field through pipeline steps.
Find all naming inconsistencies and code references.
"""
import re

fp = r'f:\1. Edit Videos\8.AntiCode\1.Prompt_Image\1.Prompt_Image\core\video_pipeline.py'
with open(fp, encoding='utf-8') as f:
    lines = f.readlines()
    content = ''.join(lines)

# Track all field names related to characters, labels, crowd
fields = [
    'present_labels', 'character_labels', 'characters', 'char_labels',
    'characters_present', 'characters_data', 'characters_detail',
    'character_info', 'character_interaction', 'character_label_map',
    'has_crowd', 'crowd_archetypes', 'extras', 'crowd_types', 'crowd_labels',
    'global_scene_id', 'scene_id', 'sequence_id',
    'location_shift', 'locked_location', 'location',
    'chapter_id', 'chapter_name', 'chapter',
    'audio_sync', 'original_text', 'full_text', 'text',
    'duration', 'total_duration', 'total_sequence_duration',
    'roll_type', 'is_broll', 'shot_type',
]

print("=" * 80)
print("FIELD USAGE AUDIT — Where each field is READ/WRITTEN in code")
print("=" * 80)

# Fields to check for inconsistency
char_fields = ['present_labels', 'character_labels', 'char_labels', 'characters_present']
print("\n=== CHARACTER LABEL FIELDS ===")
for field in char_fields:
    refs = []
    for i, line in enumerate(lines, 1):
        if field in line and not line.strip().startswith('#'):
            context = line.strip()[:100]
            refs.append(f"  L{i}: {context}")
    if refs:
        print(f"\n'{field}' ({len(refs)} refs):")
        for r in refs[:15]:
            print(r)
        if len(refs) > 15:
            print(f"  ... and {len(refs)-15} more")

# Check location naming
loc_fields = ['location_shift', 'locked_location', 'location']
print("\n\n=== LOCATION FIELDS ===")
for field in loc_fields:
    count = content.count(f'"{field}"') + content.count(f"'{field}'") + content.count(f".get(\"{field}\"")
    print(f"  '{field}': {count} refs")

# Check duration naming
dur_fields = ['duration', 'total_duration', 'total_sequence_duration']
print("\n=== DURATION FIELDS ===")
for field in dur_fields:
    count = content.count(f'"{field}"') + content.count(f"'{field}'")
    print(f"  '{field}': {count} refs")

# Check scene_id naming
id_fields = ['global_scene_id', 'scene_id']
print("\n=== SCENE ID FIELDS ===")
for field in id_fields:
    count = content.count(f'"{field}"') + content.count(f"'{field}'")
    print(f"  '{field}': {count} refs")

# Check chapter naming  
ch_fields = ['chapter_id', 'chapter_name', 'chapter']
print("\n=== CHAPTER FIELDS ===")
for field in ch_fields:
    # Only exact matches
    pattern = rf'["\']({re.escape(field)})["\']'
    matches = re.findall(pattern, content)
    print(f"  '{field}': {len(matches)} refs")

# Check text/content naming
txt_fields = ['audio_sync', 'original_text', 'full_text', 'text']
print("\n=== TEXT FIELDS ===")
for field in txt_fields:
    count = content.count(f'"{field}"') + content.count(f"'{field}'")
    print(f"  '{field}': {count} refs")

# Specifically find where present_labels is READ (consumed by later steps)
print("\n\n=== CRITICAL: Where 'present_labels' is READ by downstream code ===")
for i, line in enumerate(lines, 1):
    if 'present_labels' in line and '.get(' in line and not line.strip().startswith('#'):
        print(f"  L{i}: {line.strip()[:120]}")

# Find where character_labels is READ
print("\n=== Where 'character_labels' is READ ===")
for i, line in enumerate(lines, 1):
    if 'character_labels' in line and '.get(' in line and not line.strip().startswith('#'):
        print(f"  L{i}: {line.strip()[:120]}")
