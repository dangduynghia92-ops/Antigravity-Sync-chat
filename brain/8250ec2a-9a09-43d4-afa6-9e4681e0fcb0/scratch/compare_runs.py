import json, os

out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\compare_runs.txt'

# Run 1: video_prompt (new run)
path_new = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step4_prompts.json'
# Run 2: V2 (old run)
path_old = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\V2\video_prompt\ch_01_Level_1__Vulnerability_step4_prompts.json'

# Also check characters
chars_new = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step2_characters.json'
chars_old = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\V2\video_prompt\ch_01_Level_1__Vulnerability_step2_characters.json'

with open(out, 'w', encoding='utf-8') as f:
    # Characters comparison
    f.write("=" * 60 + "\n")
    f.write("CHARACTER LABELS COMPARISON\n")
    f.write("=" * 60 + "\n\n")
    
    for label, path in [("NEW (video_prompt)", chars_new), ("OLD (V2)", chars_old)]:
        if os.path.exists(path):
            with open(path, encoding='utf-8') as fh:
                data = json.load(fh)
            labels = [c.get('label', '') for c in data.get('characters', [])]
            f.write(f"{label}: {len(labels)} characters\n")
            for l in labels:
                f.write(f"  - {l}\n")
        else:
            f.write(f"{label}: FILE NOT FOUND\n")
        f.write("\n")
    
    # Prompts comparison - first 5 scenes
    f.write("=" * 60 + "\n")
    f.write("FLAT_PROMPT COMPARISON (first 5 scenes)\n")
    f.write("=" * 60 + "\n\n")
    
    for label, path in [("NEW", path_new), ("OLD", path_old)]:
        if os.path.exists(path):
            with open(path, encoding='utf-8') as fh:
                data = json.load(fh)
            for p in data[:5]:
                sid = p.get('global_scene_id', '')
                fp = p.get('flat_prompt', '')
                f.write(f"--- {label} | {sid} ---\n")
                f.write(fp[:500] + "\n\n")
        else:
            f.write(f"{label}: FILE NOT FOUND\n\n")
    
    # Find all [civilian_man] occurrences in new run
    f.write("=" * 60 + "\n")
    f.write("[civilian_man] OCCURRENCES IN NEW RUN\n")
    f.write("=" * 60 + "\n\n")
    
    if os.path.exists(path_new):
        with open(path_new, encoding='utf-8') as fh:
            data = json.load(fh)
        for p in data:
            fp = p.get('flat_prompt', '')
            if 'civilian_man' in fp.lower() or 'civilian' in fp.lower():
                f.write(f"  {p.get('global_scene_id','')}: ...{fp[fp.lower().find('civilian')-30:fp.lower().find('civilian')+80]}...\n\n")

    # Check Step 3 scenes for civilian_man references
    scenes_new = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step3_scenes.json'
    f.write("\n" + "=" * 60 + "\n")
    f.write("[civilian_man] IN STEP 3 SCENES\n")
    f.write("=" * 60 + "\n\n")
    if os.path.exists(scenes_new):
        with open(scenes_new, encoding='utf-8') as fh:
            scenes = json.load(fh)
        for seq in scenes:
            for s in seq.get('scenes', []):
                bg = s.get('background_and_extras', '')
                if 'civilian' in bg.lower():
                    f.write(f"  {s.get('global_scene_id','')}: {bg}\n\n")

print("Done")
