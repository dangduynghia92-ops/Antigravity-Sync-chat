"""
Audit ALL data handoffs between pipeline steps for format mismatches.
Checks: label formats, field names, data types, missing fields.
"""
import json, os, re

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

def load(name):
    fp = os.path.join(base, f'ch_08_Level_8__Chilled_{name}.json')
    with open(fp, encoding='utf-8') as f:
        return json.load(f)

sents = load('step0_sentences')
seqs = load('step1_sequences')
chars = load('step2_characters')
char_map = load('step2b_character_map')
filmable = load('step3_1_filmable')
scenes = load('step3_scenes')
prompts = load('step4_prompts')

# Get valid labels from Step 2
if isinstance(chars, list):
    valid_char_labels = [c.get('label','') for c in chars if c.get('label')]
elif isinstance(chars, dict):
    valid_char_labels = [c.get('label','') for c in chars.get('characters', []) if c.get('label')]
else:
    valid_char_labels = []

print("=" * 70)
print("AUDIT 1: Step 2b map values vs Step 2 valid_labels")
print("=" * 70)
print(f"Valid labels: {valid_char_labels}")
mismatches = 0
for seq_id, mapping in char_map.items():
    for raw, mapped in mapping.items():
        if mapped and mapped not in valid_char_labels:
            mismatches += 1
            # Check if base matches
            base_label = re.sub(r'-(Child|Teen|YoungAdult|MatureAdult|Elder)$', '', mapped)
            match_base = base_label in valid_char_labels
            print(f"  ❌ {seq_id}: '{mapped}' NOT in valid_labels (base '{base_label}' match={match_base})")
print(f"Total mismatches: {mismatches}\n")

print("=" * 70)
print("AUDIT 2: Step 3.1 filmable - present_labels values vs valid_labels")
print("=" * 70)
unknown_labels = set()
for seq_id, entries in filmable.items():
    for entry in entries:
        for lbl in entry.get('present_labels', []):
            if lbl not in valid_char_labels:
                unknown_labels.add(lbl)
if unknown_labels:
    for lbl in unknown_labels:
        print(f"  ❌ '{lbl}' in present_labels but NOT in valid_labels")
else:
    print(f"  ✅ All present_labels values are valid (or empty)")
print()

print("=" * 70)
print("AUDIT 3: Step 3.2 scenes - character_labels vs valid_labels")
print("=" * 70)
unknown_scene_labels = set()
for seq in scenes:
    for sc in seq.get('scenes', []):
        for lbl in sc.get('character_labels', []):
            if lbl not in valid_char_labels:
                unknown_scene_labels.add(lbl)
if unknown_scene_labels:
    for lbl in unknown_scene_labels:
        print(f"  ❌ '{lbl}' in character_labels but NOT in valid_labels")
else:
    print(f"  ✅ All character_labels values are valid (or empty)")
print()

print("=" * 70)
print("AUDIT 4: Step 3.2 scene IDs consistency")
print("=" * 70)
scene_ids_32 = set()
for seq in scenes:
    for sc in seq.get('scenes', []):
        scene_ids_32.add(sc.get('global_scene_id', ''))

prompt_ids = set(p.get('global_scene_id', '') for p in prompts)
missing_in_prompts = scene_ids_32 - prompt_ids
extra_in_prompts = prompt_ids - scene_ids_32
if missing_in_prompts:
    print(f"  ⚠ Scenes in Step 3.2 but NOT in Step 4: {missing_in_prompts}")
if extra_in_prompts:
    print(f"  ⚠ Scenes in Step 4 but NOT in Step 3.2: {extra_in_prompts}")
if not missing_in_prompts and not extra_in_prompts:
    print(f"  ✅ All {len(scene_ids_32)} scene IDs match between Step 3.2 and Step 4")
print()

print("=" * 70)
print("AUDIT 5: Step 1 sentence_ids vs Step 0 sentences")
print("=" * 70)
sent_ids_step0 = set(s.get('sentence_id') for s in sents)
all_sent_ids_step1 = set()
for seq in seqs:
    for sid in seq.get('sentence_ids', []):
        all_sent_ids_step1.add(sid)
missing = all_sent_ids_step1 - sent_ids_step0
if missing:
    print(f"  ❌ sentence_ids in Step 1 but NOT in Step 0: {missing}")
else:
    print(f"  ✅ All {len(all_sent_ids_step1)} sentence_ids in Step 1 exist in Step 0")
print()

print("=" * 70)
print("AUDIT 6: Step 3.1 sentence coverage")
print("=" * 70)
filmable_sent_ids = set()
for seq_id, entries in filmable.items():
    for entry in entries:
        filmable_sent_ids.add(entry.get('sentence_id'))
missing_sents = all_sent_ids_step1 - filmable_sent_ids
extra_sents = filmable_sent_ids - all_sent_ids_step1
if missing_sents:
    print(f"  ⚠ Sentences in Step 1 but NOT in Step 3.1: {missing_sents}")
if extra_sents:
    print(f"  ⚠ Sentences in Step 3.1 but NOT in Step 1: {extra_sents}")
if not missing_sents and not extra_sents:
    print(f"  ✅ All {len(filmable_sent_ids)} sentences covered")
print()

print("=" * 70)
print("AUDIT 7: Step 4 characters field - has data vs empty")
print("=" * 70)
has_chars = sum(1 for p in prompts if p.get('characters', '').strip())
no_chars = sum(1 for p in prompts if not p.get('characters', '').strip())
has_crowd = sum(1 for p in prompts if p.get('has_crowd'))
no_chars_suffix = sum(1 for p in prompts if 'NO characters' in p.get('flat_prompt', ''))
print(f"  Prompts with characters: {has_chars}")
print(f"  Prompts without characters: {no_chars}")
print(f"  Prompts with has_crowd=True: {has_crowd}")
print(f"  Prompts with 'NO characters' suffix: {no_chars_suffix}")
# Check contradiction: NO characters suffix but flat_prompt describes people
people_words = ['guard', 'soldier', 'warrior', 'figure', 'man ', 'woman', 'person', 'rider', 'commander', 'king']
contradictions = 0
for p in prompts:
    fp = p.get('flat_prompt', '')
    if 'NO characters' in fp:
        before = fp.split('NO characters')[0].lower()
        if any(w in before for w in people_words):
            contradictions += 1
print(f"  ❌ Contradictions (NO characters but describes people): {contradictions}")
print()

print("=" * 70)
print("AUDIT 8: Step 4 chapter_id field presence")
print("=" * 70)
has_chid = sum(1 for p in prompts if p.get('chapter_id'))
print(f"  Prompts with chapter_id: {has_chid}/{len(prompts)}")
print()

print("=" * 70)
print("AUDIT 9: audio_sync coverage in Step 3.2 scenes")
print("=" * 70)
has_sync = 0
no_sync = 0
for seq in scenes:
    for sc in seq.get('scenes', []):
        if sc.get('audio_sync', '').strip():
            has_sync += 1
        else:
            no_sync += 1
print(f"  Scenes with audio_sync: {has_sync}")
print(f"  Scenes without audio_sync: {no_sync}")
