"""
DEEP AUDIT — Simulate actual data flow on real output.
Check every step's output for crowd data presence.
"""
import json, os, glob

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
    'v1_Cuộc_Đời_Bạn', 'Test 3', 'video_prompt')

errors = []
warnings = []
info = []

# ═══════════ 1. Step 1: crowd_types in sequences ═══════════
seq_files = sorted(glob.glob(os.path.join(base, '*_step1_sequences.json')))
all_seqs = []
seqs_with_crowd = 0
seqs_without_crowd = 0
for f in seq_files:
    seqs = json.load(open(f, encoding='utf-8'))
    for s in seqs:
        all_seqs.append(s)
        ct = s.get('crowd_types', [])
        if ct:
            seqs_with_crowd += 1
        else:
            seqs_without_crowd += 1

if seqs_with_crowd > 0:
    info.append(f"✅ Step 1: {seqs_with_crowd}/{len(all_seqs)} sequences have crowd_types")
else:
    errors.append(f"❌ Step 1: NO sequences have crowd_types")

# ═══════════ 2. Step 2d: crowd sheets ═══════════
crowd_file = os.path.join(base, 'ch_08_Level_8__Chilled_step2d_crowd.json')
if os.path.exists(crowd_file):
    crowd_data = json.load(open(crowd_file, encoding='utf-8'))
    crowd_chars = crowd_data.get('characters', [])
    info.append(f"✅ Step 2d: {len(crowd_chars)} crowd sheets")
    
    # Check sheet_prompt exists
    has_sheet_prompt = sum(1 for c in crowd_chars if c.get('sheet_prompt'))
    has_visual_desc = sum(1 for c in crowd_chars if c.get('visual_description'))
    has_default_stance = sum(1 for c in crowd_chars if c.get('default_stance'))
    
    if has_sheet_prompt > 0:
        info.append(f"  ✅ sheet_prompt: {has_sheet_prompt}/{len(crowd_chars)}")
    else:
        warnings.append(f"  ⚠ sheet_prompt: 0/{len(crowd_chars)} — NO reference image prompts for crowd!")
    
    if has_visual_desc == len(crowd_chars):
        info.append(f"  ✅ visual_description: {has_visual_desc}/{len(crowd_chars)}")
    else:
        errors.append(f"  ❌ visual_description: only {has_visual_desc}/{len(crowd_chars)}")
    
    info.append(f"  default_stance: {has_default_stance}/{len(crowd_chars)}")
    
    # Show sample
    if crowd_chars:
        c = crowd_chars[0]
        info.append(f"  Sample: {c.get('label')}")
        info.append(f"    Keys: {list(c.keys())}")
else:
    errors.append("❌ Step 2d: crowd file NOT FOUND")
    crowd_chars = []

# ═══════════ 3. Step 3.1: filmable_scenes — crowd_labels ═══════════
filmable_files = sorted(glob.glob(os.path.join(base, '*_step3_1_filmable.json')))
total_entries = 0
entries_with_crowd = 0
for f in filmable_files:
    data = json.load(open(f, encoding='utf-8'))
    for seq_id, entries in data.items():
        for entry in entries:
            total_entries += 1
            cl = entry.get('crowd_labels', [])
            if cl:
                entries_with_crowd += 1

if total_entries > 0:
    pct = round(entries_with_crowd / total_entries * 100, 1)
    if entries_with_crowd > 0:
        info.append(f"✅ Step 3.1: {entries_with_crowd}/{total_entries} entries have crowd_labels ({pct}%)")
    else:
        errors.append(f"❌ Step 3.1: 0/{total_entries} entries have crowd_labels — LLM returned empty!")
else:
    warnings.append("⚠ Step 3.1: no filmable data found")

# Also check if present_labels still exists (should be renamed)
has_present_labels = 0
for f in filmable_files:
    data = json.load(open(f, encoding='utf-8'))
    for seq_id, entries in data.items():
        for entry in entries:
            if 'present_labels' in entry:
                has_present_labels += 1
if has_present_labels > 0:
    warnings.append(f"⚠ Step 3.1 OUTPUT: 'present_labels' still appears in {has_present_labels} entries (old field name)")

has_char_labels = 0
for f in filmable_files:
    data = json.load(open(f, encoding='utf-8'))
    for seq_id, entries in data.items():
        for entry in entries:
            if 'character_labels' in entry:
                has_char_labels += 1
if has_char_labels > 0:
    info.append(f"  Step 3.1 OUTPUT uses 'character_labels': {has_char_labels} entries")
else:
    warnings.append(f"  ⚠ Step 3.1 OUTPUT: 0 entries have 'character_labels' — still using old name?")

# ═══════════ 4. Step 3.2: scenes — crowd_labels ═══════════
scene_files = sorted(glob.glob(os.path.join(base, '*_step3_scenes.json')))
total_scenes = 0
scenes_with_crowd = 0
for f in scene_files:
    data = json.load(open(f, encoding='utf-8'))
    for seq in data:
        for scene in seq.get('scenes', []):
            total_scenes += 1
            cl = scene.get('crowd_labels', [])
            if cl:
                scenes_with_crowd += 1

if total_scenes > 0:
    pct = round(scenes_with_crowd / total_scenes * 100, 1)
    if scenes_with_crowd > 0:
        info.append(f"✅ Step 3.2: {scenes_with_crowd}/{total_scenes} scenes have crowd_labels ({pct}%)")
    else:
        errors.append(f"❌ Step 3.2: 0/{total_scenes} scenes have crowd_labels — NOT propagated!")
else:
    warnings.append("⚠ Step 3.2: no scene data found")

# ═══════════ 5. Step 4: prompts — crowd_labels ═══════════
prompt_files = sorted(glob.glob(os.path.join(base, '*_step4_prompts.json')))
total_prompts = 0
prompts_with_crowd = 0
prompts_crowd_in_text = 0
for f in prompt_files:
    data = json.load(open(f, encoding='utf-8'))
    for p in data:
        total_prompts += 1
        cl = p.get('crowd_labels', [])
        if cl:
            prompts_with_crowd += 1
        # Also check if flat_prompt mentions EXT-
        fp = p.get('flat_prompt', '')
        if 'EXT-' in fp:
            prompts_crowd_in_text += 1

if total_prompts > 0:
    pct = round(prompts_with_crowd / total_prompts * 100, 1)
    if prompts_with_crowd > 0:
        info.append(f"✅ Step 4: {prompts_with_crowd}/{total_prompts} prompts have crowd_labels ({pct}%)")
    else:
        errors.append(f"❌ Step 4: 0/{total_prompts} prompts have crowd_labels — MISSING!")
    
    if prompts_crowd_in_text > 0:
        info.append(f"  Step 4 flat_prompt mentions EXT-: {prompts_crowd_in_text}/{total_prompts}")
    else:
        errors.append(f"  ❌ Step 4 flat_prompt: 0/{total_prompts} mention EXT- crowd labels in text")
else:
    warnings.append("⚠ Step 4: no prompt data found")

# ═══════════ 6. Export: final CSV/JSON ═══════════
export_files = sorted(glob.glob(os.path.join(base, 'prompts_*.json')) + 
                       glob.glob(os.path.join(base, 'prompts_*.csv')))
for f in export_files:
    bn = os.path.basename(f)
    if f.endswith('.json'):
        data = json.load(open(f, encoding='utf-8'))
        if isinstance(data, list) and len(data) > 0:
            keys = list(data[0].keys())
            has_cl = 'crowd_labels' in keys
            info.append(f"  Export {bn}: {'✅' if has_cl else '❌'} crowd_labels in keys")

# ═══════════ REPORT ═══════════
print("=" * 70)
print("DEEP DATA FLOW AUDIT — REAL OUTPUT")
print("=" * 70)

print(f"\n📋 INFO ({len(info)}):")
for item in info:
    print(f"  {item}")

print(f"\n⚠ WARNINGS ({len(warnings)}):")
for item in warnings:
    print(f"  {item}")

print(f"\n❌ ERRORS ({len(errors)}):")
if errors:
    for item in errors:
        print(f"  {item}")
else:
    print("  None!")

print(f"\n{'=' * 70}")
print(f"SUMMARY: {len(info)} OK | {len(warnings)} warnings | {len(errors)} errors")
print(f"{'=' * 70}")
