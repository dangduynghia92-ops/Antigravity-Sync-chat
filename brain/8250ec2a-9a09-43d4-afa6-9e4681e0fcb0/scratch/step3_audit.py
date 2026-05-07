import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'
with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    data = json.load(f)

out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\step3_audit.txt'
with open(out, 'w', encoding='utf-8') as f:
    for seq in data:
        sid = seq.get('sequence_id', '')
        f.write(f"\n{'='*70}\n")
        f.write(f"SEQUENCE: {sid}\n")
        f.write(f"total_duration: {seq.get('total_sequence_duration', 0)}s\n")
        f.write(f"locked_location: '{seq.get('locked_location', '')}'\n")
        f.write(f"location_anchor: '{seq.get('location_anchor', '')}'\n")
        f.write(f"visual_event: {seq.get('visual_event', '')}\n")
        
        scenes = seq.get('scenes', [])
        scene_dur_sum = sum(s.get('duration', 0) for s in scenes)
        target = seq.get('total_sequence_duration', 0)
        error = abs(scene_dur_sum - target) / target * 100 if target else 0
        f.write(f"scenes: {len(scenes)} | sum_dur: {scene_dur_sum:.2f}s | error: {error:.1f}%\n")
        
        for s in scenes:
            gid = s.get('global_scene_id', '')
            f.write(f"\n  --- {gid} ---\n")
            f.write(f"  duration: {s.get('duration', 0)}s\n")
            f.write(f"  shot_type: {s.get('shot_type', '')}\n")
            f.write(f"  roll_type: {s.get('roll_type', '')}\n")
            f.write(f"  camera_motion: {s.get('camera_motion', '')}\n")
            f.write(f"  time_of_day: {s.get('time_of_day', '')}\n")
            f.write(f"  character_labels: {s.get('character_labels', [])}\n")
            f.write(f"  has_crowd: {s.get('has_crowd', False)}\n")
            f.write(f"  physical_action: {s.get('physical_action', '')}\n")
            f.write(f"  audio_sync: {s.get('audio_sync', '')[:80]}...\n")
            
            # Quality checks
            issues = []
            
            # Check shot_type
            if s.get('shot_type') not in ('Wide Shot', 'Medium Shot', 'Close-up'):
                issues.append(f"INVALID shot_type: {s.get('shot_type')}")
            
            # Check camera_motion
            valid_motions = ('Static', 'Slow Pan', 'Slow Tracking', 'Extreme Slow Zoom In')
            if s.get('camera_motion') not in valid_motions:
                issues.append(f"INVALID camera_motion: {s.get('camera_motion')}")
            
            # Rule 7: Pan on Close-up
            if s.get('shot_type') == 'Close-up' and s.get('camera_motion') == 'Slow Pan':
                issues.append("RULE 7 VIOLATION: Pan on Close-up")
            
            # Rule 7: Opening = Wide + Slow Pan
            if gid.endswith('_SCN_01') and s.get('camera_motion') != 'Slow Pan':
                issues.append(f"Opening scene not Slow Pan: {s.get('camera_motion')}")
            if gid.endswith('_SCN_01') and s.get('shot_type') != 'Wide Shot':
                issues.append(f"Opening scene not Wide Shot: {s.get('shot_type')}")
            
            # B-Roll with characters?
            if s.get('roll_type') == 'B-Roll' and s.get('character_labels'):
                issues.append("B-Roll but has character_labels!")
            
            # A-Roll without characters?
            if s.get('roll_type') == 'A-Roll' and not s.get('character_labels'):
                issues.append("A-Roll but no character_labels!")
            
            # Physical action has forbidden words?
            action = s.get('physical_action', '').lower()
            for word in ['blood', 'wound', 'bleeding', 'cut', 'stab', 'kill', 'dead', 'die']:
                if word in action:
                    issues.append(f"SAFETY: '{word}' in physical_action")
            
            # Abstract words?
            for word in ['defeated', 'sad', 'triumphant', 'victorious', 'desperate']:
                if word in action and word not in s.get('audio_sync', '').lower():
                    issues.append(f"ABSTRACT word: '{word}' in physical_action")
            
            # Duration range
            dur = s.get('duration', 0)
            if dur < 1.0:
                issues.append(f"Duration too short: {dur}s (min 1.0s)")
            
            # time_of_day valid?
            valid_tod = ('dawn', 'morning', 'midday', 'afternoon', 'dusk', 'night')
            if s.get('time_of_day', '').lower() not in valid_tod:
                issues.append(f"INVALID time_of_day: {s.get('time_of_day')}")
            
            if issues:
                for iss in issues:
                    f.write(f"  !! {iss}\n")
        
        # Sequence-level checks
        seq_issues = []
        rolls = [s['roll_type'] for s in scenes]
        broll_count = rolls.count('B-Roll')
        if broll_count > 2:
            seq_issues.append(f"Too many B-Roll: {broll_count} (max 2)")
        
        # Adjacent same shot_type
        shots = [s['shot_type'] for s in scenes]
        for i in range(1, len(shots)):
            if shots[i] == shots[i-1] and shots[i] == 'Close-up':
                seq_issues.append(f"Adjacent Close-ups: {scenes[i-1]['global_scene_id']} + {scenes[i]['global_scene_id']}")
        
        # Adjacent opposing motions
        motions = [s['camera_motion'] for s in scenes]
        for i in range(1, len(motions)):
            if motions[i] != 'Static' and motions[i-1] != 'Static' and motions[i] != motions[i-1]:
                seq_issues.append(f"Adjacent non-static motions: {motions[i-1]} -> {motions[i]}")
        
        if seq_issues:
            f.write(f"\n  SEQUENCE ISSUES:\n")
            for iss in seq_issues:
                f.write(f"  !! {iss}\n")

print("Done")
