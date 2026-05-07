import json, os

base1 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'
base_v4 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\V4\video_prompt'
out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\deep_quality.txt'

with open(out, 'w', encoding='utf-8') as f:

    # ========== LIST ALL FILES ==========
    f.write("=" * 70 + "\n")
    f.write("FILES IN BOTH RUNS\n")
    f.write("=" * 70 + "\n")
    for label, base in [("final2/Test", base1), ("final2/Test/V4", base_v4)]:
        f.write(f"\n--- {label} ---\n")
        if os.path.isdir(base):
            for fn in sorted(os.listdir(base)):
                if fn.endswith('.json'):
                    size = os.path.getsize(os.path.join(base, fn))
                    f.write(f"  {fn} ({size} bytes)\n")
        else:
            f.write("  DIR NOT FOUND\n")

    # ========== ISSUE 1: B-Roll / no-character prompts ==========
    f.write("\n\n" + "=" * 70 + "\n")
    f.write("ISSUE 1: PROMPTS WITHOUT CHARACTERS\n")
    f.write("=" * 70 + "\n")
    
    # Load step3 and step4
    step3_files = [fn for fn in os.listdir(base1) if 'step3' in fn and fn.endswith('.json')]
    step4_files = [fn for fn in os.listdir(base1) if 'step4' in fn and fn.endswith('.json')]
    
    all_scenes_step3 = []
    for fn in step3_files:
        with open(os.path.join(base1, fn), encoding='utf-8') as fh:
            data = json.load(fh)
        for seq in data:
            for s in seq.get('scenes', []):
                all_scenes_step3.append(s)
    
    all_prompts = []
    for fn in step4_files:
        with open(os.path.join(base1, fn), encoding='utf-8') as fh:
            all_prompts = json.load(fh)
    
    total = len(all_prompts)
    no_char = [p for p in all_prompts if not p.get('characters', '').strip()]
    has_char = [p for p in all_prompts if p.get('characters', '').strip()]
    
    f.write(f"\nTotal prompts: {total}\n")
    f.write(f"With characters: {len(has_char)} ({round(len(has_char)/total*100)}%)\n")
    f.write(f"Without characters (B-Roll/environment): {len(no_char)} ({round(len(no_char)/total*100)}%)\n\n")
    
    f.write("No-character prompts detail:\n")
    for p in no_char:
        sid = p.get('global_scene_id', '')
        # Find matching step3 scene
        s3 = None
        for s in all_scenes_step3:
            if s.get('global_scene_id') == sid:
                s3 = s
                break
        roll = s3.get('roll_type', '?') if s3 else '?'
        shot = s3.get('shot_type', '?') if s3 else '?'
        action = s3.get('physical_action', '')[:80] if s3 else ''
        fp = p.get('flat_prompt', '')[:100]
        f.write(f"\n  {sid} | {roll} | {shot}\n")
        f.write(f"    action: {action}\n")
        f.write(f"    prompt: {fp}...\n")
        # Check if prompt mentions people despite no character labels
        prompt_lower = p.get('flat_prompt', '').lower()
        has_people_words = any(w in prompt_lower for w in ['man', 'men', 'woman', 'women', 'soldier', 'guard', 'figure', 'person', 'crowd', 'people'])
        if has_people_words:
            f.write(f"    WARNING: prompt mentions people despite no character_labels!\n")

    # ========== ISSUE 2: Sequence segmentation + scene evaluation ==========
    f.write("\n\n" + "=" * 70 + "\n")
    f.write("ISSUE 2A: SEQUENCE SEGMENTATION\n")
    f.write("=" * 70 + "\n")
    
    seq_files = [fn for fn in os.listdir(base1) if 'step1' in fn and fn.endswith('.json')]
    all_seqs = []
    for fn in seq_files:
        with open(os.path.join(base1, fn), encoding='utf-8') as fh:
            all_seqs = json.load(fh)
    
    for s in all_seqs:
        f.write(f"\n{s['sequence_id']} | dur={s.get('total_duration',0)}s | sents={s.get('sentence_ids', [])}\n")
        f.write(f"  location: {s.get('location_shift','')}\n")
        f.write(f"  subject: {s.get('main_subject','')}\n")
        f.write(f"  chars: {s.get('characters',[])}\n")
        f.write(f"  text: {s.get('full_text','')}\n")

    # Evaluate 3 sequences in detail
    f.write("\n\n" + "=" * 70 + "\n")
    f.write("ISSUE 2B: SCENE EVALUATION (SEQ_01, SEQ_03, SEQ_04)\n")
    f.write("=" * 70 + "\n")
    
    for fn in step3_files:
        with open(os.path.join(base1, fn), encoding='utf-8') as fh:
            scenes_data = json.load(fh)
    
    for seq in scenes_data:
        sid = seq.get('sequence_id', '')
        if sid not in ('SEQ_01', 'SEQ_03', 'SEQ_04'):
            continue
        f.write(f"\n{'='*50}\n")
        f.write(f"{sid}\n")
        f.write(f"{'='*50}\n")
        f.write(f"visual_event: {seq.get('visual_event','')}\n")
        f.write(f"location_anchor: {seq.get('location_anchor','')}\n")
        total_dur = seq.get('total_sequence_duration', 0)
        scenes = seq.get('scenes', [])
        scene_dur = sum(s.get('duration', 0) for s in scenes)
        f.write(f"target_duration: {total_dur}s | actual: {scene_dur}s | scenes: {len(scenes)}\n\n")
        
        for s in scenes:
            f.write(f"  {s['global_scene_id']} | {s['shot_type']} | {s['camera_motion']} | {s['duration']}s | {s['roll_type']}\n")
            f.write(f"    chars: {s.get('character_labels',[])}\n")
            f.write(f"    action: {s.get('physical_action','')}\n")
            f.write(f"    has_crowd: {s.get('has_crowd')}\n\n")
        
        # Analysis
        rolls = [s['roll_type'] for s in scenes]
        shots = [s['shot_type'] for s in scenes]
        motions = [s['camera_motion'] for s in scenes]
        f.write(f"  Roll mix: A-Roll={rolls.count('A-Roll')}, B-Roll={rolls.count('B-Roll')}\n")
        f.write(f"  Shot variety: {set(shots)}\n")
        f.write(f"  Motion variety: {set(motions)}\n")

    # ========== ISSUE 3: Character count comparison ==========
    f.write("\n\n" + "=" * 70 + "\n")
    f.write("ISSUE 3: CHARACTER COUNT COMPARISON\n")
    f.write("=" * 70 + "\n")
    
    for label, base in [("final2/Test", base1), ("final2/Test/V4", base_v4)]:
        char_files = [fn for fn in os.listdir(base) if 'characters' in fn and fn.endswith('.json')]
        for fn in char_files:
            with open(os.path.join(base, fn), encoding='utf-8') as fh:
                data = json.load(fh)
            chars = data.get('characters', [])
            f.write(f"\n--- {label}/{fn} ({len(chars)} characters) ---\n")
            for c in chars:
                f.write(f"  [{c.get('group','')}] {c.get('label','')} = {c.get('original_name','')}\n")
                f.write(f"    age: {c.get('age_stage','')}\n")
                f.write(f"    visual: {c.get('visual_description','')[:150]}\n\n")

    # Also compare step1 sequences to see if same input
    f.write("\n--- Sequence comparison ---\n")
    for label, base in [("final2/Test", base1), ("final2/Test/V4", base_v4)]:
        seq_f = [fn for fn in os.listdir(base) if 'step1' in fn and fn.endswith('.json')]
        for fn in seq_f:
            with open(os.path.join(base, fn), encoding='utf-8') as fh:
                seqs = json.load(fh)
            f.write(f"\n{label}/{fn}: {len(seqs)} sequences\n")
            all_chars = set()
            for s in seqs:
                for c in s.get('characters', []):
                    all_chars.add(c)
            f.write(f"  All characters mentioned: {sorted(all_chars)}\n")

print("Done")
