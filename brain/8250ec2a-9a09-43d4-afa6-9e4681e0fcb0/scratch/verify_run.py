import json, os, glob

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt'
out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\verify_run.txt'

with open(out, 'w', encoding='utf-8') as f:
    # List all files
    files = sorted(glob.glob(os.path.join(base, '*.json')))
    f.write("=" * 60 + "\n")
    f.write("ALL OUTPUT FILES\n")
    f.write("=" * 60 + "\n")
    for fp in files:
        size = os.path.getsize(fp)
        f.write(f"  {os.path.basename(fp)} ({size} bytes)\n")
    
    # CHECK STEP 3: verify no costume_note, lighting_and_atmosphere, background_and_extras
    f.write("\n" + "=" * 60 + "\n")
    f.write("STEP 3: FIELD CHECK (first 3 scenes)\n")
    f.write("=" * 60 + "\n")
    step3_files = [fp for fp in files if 'step3' in fp]
    for fp in step3_files:
        with open(fp, encoding='utf-8') as fh:
            data = json.load(fh)
        f.write(f"\n--- {os.path.basename(fp)} ---\n")
        for seq in data[:2]:  # first 2 sequences
            for s in seq.get('scenes', [])[:2]:  # first 2 scenes per seq
                sid = s.get('global_scene_id', '')
                f.write(f"\n  {sid}:\n")
                # Check OLD fields should NOT exist
                has_costume = 'costume_note' in s
                has_lighting = 'lighting_and_atmosphere' in s
                has_bg = 'background_and_extras' in s
                has_crowd = 'has_crowd' in s
                f.write(f"    costume_note: {'❌ STILL EXISTS' if has_costume else '✅ removed'}\n")
                f.write(f"    lighting_and_atmosphere: {'❌ STILL EXISTS' if has_lighting else '✅ removed'}\n")
                f.write(f"    background_and_extras: {'❌ STILL EXISTS' if has_bg else '✅ removed'}\n")
                f.write(f"    has_crowd: {'✅ ' + str(s.get('has_crowd')) if has_crowd else '❌ MISSING'}\n")
                f.write(f"    physical_action: {s.get('physical_action', 'MISSING')[:80]}\n")
                f.write(f"    shot_type: {s.get('shot_type', 'MISSING')}\n")
                f.write(f"    time_of_day: {s.get('time_of_day', 'MISSING')}\n")
    
    # CHECK STEP 4: verify characters_detail, no old fields
    f.write("\n" + "=" * 60 + "\n")
    f.write("STEP 4: FIELD CHECK (first 5 prompts)\n")
    f.write("=" * 60 + "\n")
    step4_files = [fp for fp in files if 'step4' in fp]
    for fp in step4_files:
        with open(fp, encoding='utf-8') as fh:
            data = json.load(fh)
        f.write(f"\n--- {os.path.basename(fp)} ---\n")
        for p in data[:5]:
            sid = p.get('global_scene_id', '')
            f.write(f"\n  {sid}:\n")
            # Check NEW fields
            has_chars_detail = 'characters_detail' in p
            has_extras = 'extras' in p
            has_lighting = 'lighting' in p
            has_background = 'background' in p
            # Check OLD fields should NOT exist
            has_old_costume = 'costume' in p and 'characters_detail' not in p
            has_old_blocking = 'character_blocking' in p
            has_old_emotion = 'emotion' in p
            has_old_crowd = 'crowd_description' in p
            
            f.write(f"    characters_detail: {'✅ ' + str(len(p.get('characters_detail', []))) + ' chars' if has_chars_detail else '❌ MISSING'}\n")
            if has_chars_detail:
                for cd in p.get('characters_detail', []):
                    f.write(f"      - {cd.get('label', '?')}: costume={cd.get('costume', '?')[:40]}, blocking={cd.get('blocking', '?')[:30]}, action={cd.get('action', '?')[:40]}\n")
            f.write(f"    extras: {'✅ ' + str(p.get('extras', ''))[:60] if has_extras else '❌ MISSING'}\n")
            f.write(f"    lighting: {'✅' if has_lighting else '❌ MISSING'}\n")
            f.write(f"    background: {'✅' if has_background else '❌ MISSING'}\n")
            f.write(f"    character_blocking (OLD): {'❌ STILL EXISTS' if has_old_blocking else '✅ removed'}\n")
            f.write(f"    emotion (OLD): {'❌ STILL EXISTS' if has_old_emotion else '✅ removed'}\n")
            f.write(f"    crowd_description (OLD): {'❌ STILL EXISTS' if has_old_crowd else '✅ removed'}\n")
            f.write(f"    flat_prompt: {p.get('flat_prompt', '')[:120]}...\n")
    
    # CHECK: no [civilian_man] in flat_prompt
    f.write("\n" + "=" * 60 + "\n")
    f.write("[civilian_man] CHECK IN FLAT_PROMPTS\n")
    f.write("=" * 60 + "\n")
    found = False
    for fp in step4_files:
        with open(fp, encoding='utf-8') as fh:
            data = json.load(fh)
        for p in data:
            fp_text = p.get('flat_prompt', '')
            if '[civilian_man]' in fp_text or '[civilian_woman]' in fp_text or '[soldier]' in fp_text:
                f.write(f"  ❌ {p.get('global_scene_id','')}: found bracket label in flat_prompt\n")
                found = True
    if not found:
        f.write("  ✅ No bracket labels for extras found\n")

    # CHECK: PROMPT_SUFFIX appended
    f.write("\n" + "=" * 60 + "\n")
    f.write("PROMPT_SUFFIX CHECK\n")
    f.write("=" * 60 + "\n")
    suffix = "full frame, no border, no text, no watermark, 16:9 aspect ratio."
    for fp in step4_files:
        with open(fp, encoding='utf-8') as fh:
            data = json.load(fh)
        count_with = sum(1 for p in data if p.get('flat_prompt', '').endswith(suffix))
        f.write(f"  {os.path.basename(fp)}: {count_with}/{len(data)} prompts have suffix ✅\n")

print("Done")
