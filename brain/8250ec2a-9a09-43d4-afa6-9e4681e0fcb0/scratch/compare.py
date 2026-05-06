import json

# Load Step 3 and Step 4 data for SEQ_01_SCN_05
path3 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step3_scenes.json'
path4 = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step4_prompts.json'

out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\compare.txt'

with open(path3, encoding='utf-8') as f:
    scenes = json.load(f)
with open(path4, encoding='utf-8') as f:
    prompts = json.load(f)

with open(out, 'w', encoding='utf-8') as f:
    # Find SCN_05
    for seq in scenes:
        if seq.get('sequence_id') == 'SEQ_01':
            for s in seq.get('scenes', []):
                if s.get('global_scene_id') == 'SEQ_01_SCN_05':
                    f.write("=== STEP 3: SEQ_01_SCN_05 ===\n")
                    f.write(json.dumps(s, indent=2, ensure_ascii=False))
                    f.write("\n\n")
    
    for p in prompts:
        if p.get('global_scene_id') == 'SEQ_01_SCN_05':
            f.write("=== STEP 4: SEQ_01_SCN_05 ===\n")
            f.write(json.dumps(p, indent=2, ensure_ascii=False))
            f.write("\n\n")
            f.write("=== FLAT PROMPT (full) ===\n")
            f.write(p.get('flat_prompt', ''))
            f.write("\n")
    
    # Also show a few other scenes for comparison
    for sid in ['SEQ_01_SCN_01', 'SEQ_01_SCN_03']:
        for p in prompts:
            if p.get('global_scene_id') == sid:
                f.write(f"\n=== FLAT PROMPT: {sid} ===\n")
                f.write(p.get('flat_prompt', ''))
                f.write("\n")

print("Done")
