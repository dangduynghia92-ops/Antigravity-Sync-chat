import json, re

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'
with open(f'{base}\\ch_01_Level_1__Vulnerability_step4_prompts.json', encoding='utf-8') as f:
    data = json.load(f)

out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\step4_audit.txt'
with open(out, 'w', encoding='utf-8') as f:
    issues_total = []
    
    for s in data:
        scene_id = s.get('global_scene_id', s.get('scene_id', ''))
        f.write(f"\n{'='*70}\n")
        f.write(f"SCENE: {scene_id} | dur: {s.get('duration',0)}s\n")
        
        # Characters detail
        chars = s.get('characters_detail', [])
        f.write(f"characters ({len(chars)}):\n")
        for c in chars:
            f.write(f"  [{c.get('label','')}]\n")
            f.write(f"    costume: {c.get('costume','')[:120]}\n")
            f.write(f"    blocking: {c.get('blocking','')}\n")
            f.write(f"    emotion: {c.get('emotion','')}\n")
            f.write(f"    action: {c.get('action','')[:120]}\n")
        
        f.write(f"extras: {s.get('extras','')[:120]}\n")
        f.write(f"lighting: {s.get('lighting','')[:120]}\n")
        f.write(f"background: {s.get('background','')[:150]}\n")
        f.write(f"key_props: {s.get('key_props', [])}\n")
        f.write(f"camera_angle: {s.get('camera_angle','')}\n")
        f.write(f"effects: {s.get('effects','')}\n")
        
        fp = s.get('flat_prompt', '')
        f.write(f"\nflat_prompt ({len(fp)} chars):\n{fp}\n")
        
        # Quality checks
        issues = []
        fp_lower = fp.lower()
        
        # 1. Length
        if len(fp) < 50: issues.append(f"TOO SHORT: {len(fp)} chars")
        if len(fp) > 1500: issues.append(f"TOO LONG: {len(fp)} chars")
        
        # 2. camera_angle has shot types
        angle = s.get('camera_angle', '').lower()
        for bad in ['wide shot', 'medium shot', 'close-up', 'close up', 'closeup']:
            if bad in angle: issues.append(f"camera_angle has shot_type: '{bad}'")
        
        # 3. Safety
        for w in ['blood', 'wound', 'bleeding', 'stab', 'gore']:
            if w in fp_lower: issues.append(f"SAFETY: '{w}' in flat_prompt")
        
        # 4. Skin tone leak
        for w in ['tanned', 'olive skin', 'dark skin', 'brown skin', 'sun-weathered', 'sun-darkened']:
            if w in fp_lower: issues.append(f"SKIN TONE: '{w}'")
        
        # 5. Style forbidden
        for w in ['chibi', 'anime', 'bobble', 'stick figure', '3d cgi', 'photorealistic', '8k', 'ultra hd']:
            if w in fp_lower: issues.append(f"STYLE BAN: '{w}'")
        
        # 6. "identical"
        if 'identical' in fp_lower: issues.append("'identical' found")
        
        # 7. Character label presence in flat_prompt
        for c in chars:
            lbl = c.get('label', '').strip('[]')
            if lbl and lbl not in fp:
                issues.append(f"Label [{lbl}] NOT in flat_prompt")
        
        # 8. B-Roll has characters in flat_prompt?
        roll = s.get('roll_type', '')
        char_str = s.get('characters', '')
        if roll == 'B-Roll' and chars:
            issues.append("B-Roll but has characters_detail!")
        
        # 9. Empty flat_prompt
        if not fp.strip():
            issues.append("flat_prompt is EMPTY!")
        
        # 10. Style prefix check
        starts_style = fp_lower.strip().startswith('a stylized historical animation')
        
        if issues:
            f.write(f"\n  ISSUES:\n")
            for iss in issues:
                f.write(f"  !! {iss}\n")
            issues_total.extend([(scene_id, iss) for iss in issues])
    
    f.write(f"\n\n{'='*70}\n")
    f.write(f"SUMMARY\n")
    f.write(f"{'='*70}\n")
    f.write(f"Total scenes: {len(data)}\n")
    f.write(f"Total issues: {len(issues_total)}\n")
    
    if issues_total:
        f.write(f"\nAll issues:\n")
        for sid, iss in issues_total:
            f.write(f"  {sid}: {iss}\n")
    
    # Stats
    lengths = [len(s.get('flat_prompt','')) for s in data]
    f.write(f"\nflat_prompt stats:\n")
    f.write(f"  min: {min(lengths)} chars\n")
    f.write(f"  max: {max(lengths)} chars\n")
    f.write(f"  avg: {sum(lengths)//len(lengths)} chars\n")

print("Done")
