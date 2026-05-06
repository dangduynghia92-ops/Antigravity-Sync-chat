import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt'
out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\quality_check.txt'

with open(out, 'w', encoding='utf-8') as f:
    # ═══ STEP 1: Sequences ═══
    with open(f'{base}\\ch_01_Level_1__Vulnerability_step1_sequences.json', encoding='utf-8') as fh:
        seqs = json.load(fh)
    f.write("=" * 70 + "\n")
    f.write("STEP 1: SEQUENCES (all)\n")
    f.write("=" * 70 + "\n")
    for s in seqs:
        f.write(f"\n{s['sequence_id']} | dur={s.get('total_duration',0)}s | loc={s.get('location_shift','')}\n")
        f.write(f"  subject: {s.get('main_subject','')}\n")
        f.write(f"  chars: {s.get('characters',[])}\n")
        f.write(f"  text: {s.get('full_text','')[:150]}...\n")

    # ═══ STEP 2b: Characters ═══
    with open(f'{base}\\ch_01_Level_1__Vulnerability_step2_characters.json', encoding='utf-8') as fh:
        chars = json.load(fh)
    f.write("\n\n" + "=" * 70 + "\n")
    f.write("STEP 2b: CHARACTERS\n")
    f.write("=" * 70 + "\n")
    for c in chars.get('characters', []):
        f.write(f"\n  [{c.get('group','')}] {c.get('label','')} = {c.get('original_name','')}\n")
        f.write(f"    age: {c.get('age_stage','')}\n")
        f.write(f"    visual: {c.get('visual_description','')[:200]}\n")

    # ═══ STEP 3: Full scenes for SEQ_01, SEQ_03 ═══
    with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as fh:
        scenes = json.load(fh)
    f.write("\n\n" + "=" * 70 + "\n")
    f.write("STEP 3: SCENES (SEQ_01, SEQ_03, SEQ_05)\n")
    f.write("=" * 70 + "\n")
    for seq in scenes:
        sid = seq.get('sequence_id', '')
        if sid not in ('SEQ_01', 'SEQ_03', 'SEQ_05'):
            continue
        f.write(f"\n--- {sid} | loc={seq.get('locked_location','')} ---\n")
        f.write(f"  visual_event: {seq.get('visual_event','')}\n")
        for s in seq.get('scenes', []):
            f.write(f"\n  {s['global_scene_id']} | {s['shot_type']} | {s['camera_motion']} | {s['duration']}s | {s['roll_type']}\n")
            f.write(f"    time: {s.get('time_of_day','')}\n")
            f.write(f"    chars: {s.get('character_labels',[])}\n")
            f.write(f"    action: {s.get('physical_action','')}\n")
            f.write(f"    has_crowd: {s.get('has_crowd')}\n")

    # ═══ STEP 4: Full prompts for SEQ_01, SEQ_03 ═══
    with open(f'{base}\\ch_01_Level_1__Vulnerability_step4_prompts.json', encoding='utf-8') as fh:
        prompts = json.load(fh)
    f.write("\n\n" + "=" * 70 + "\n")
    f.write("STEP 4: PROMPTS (SEQ_01, SEQ_03, SEQ_05)\n")
    f.write("=" * 70 + "\n")
    for p in prompts:
        sid = p.get('global_scene_id', '')
        if not any(sid.startswith(x) for x in ('SEQ_01', 'SEQ_03', 'SEQ_05')):
            continue
        f.write(f"\n--- {sid} ---\n")
        f.write(f"  lighting: {p.get('lighting','')}\n")
        f.write(f"  background: {p.get('background','')}\n")
        f.write(f"  extras: {p.get('extras','')}\n")
        f.write(f"  key_props: {p.get('key_props',[])}\n")
        f.write(f"  camera_angle: {p.get('camera_angle','')}\n")
        f.write(f"  effects: {p.get('effects','')}\n")
        for cd in p.get('characters_detail', []):
            f.write(f"  CHAR {cd.get('label','?')}:\n")
            f.write(f"    costume: {cd.get('costume','')}\n")
            f.write(f"    blocking: {cd.get('blocking','')}\n")
            f.write(f"    emotion: {cd.get('emotion','')}\n")
            f.write(f"    action: {cd.get('action','')}\n")
        f.write(f"  FLAT_PROMPT:\n    {p.get('flat_prompt','')}\n")

print("Done")
