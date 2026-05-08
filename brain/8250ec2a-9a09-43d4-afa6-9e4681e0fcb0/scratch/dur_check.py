import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test', 'video_prompt')

# Sentences
with open(os.path.join(base, 'ch_01_Level_1__Vulnerable_step0_sentences.json'), encoding='utf-8') as f:
    sents = {s['sentence_id']: s for s in json.load(f)}

# Filmable scenes (Step 3.1)
with open(os.path.join(base, 'ch_01_Level_1__Vulnerable_step3_1_filmable.json'), encoding='utf-8') as f:
    filmable = json.load(f)

print("Sentence Duration vs Sum of Scene Durations:\n")
mismatches = 0
for seq_id, entries in filmable.items():
    for entry in entries:
        sid = entry.get('sentence_id')
        scenes = entry.get('scenes', [])
        scene_total = round(sum(sc.get('duration', 0) for sc in scenes), 3)
        sent_dur = round(sents.get(sid, {}).get('duration', 0), 3)
        diff = round(abs(scene_total - sent_dur), 3)
        
        flag = ""
        if diff > 0.01:
            flag = " ← MISMATCH!"
            mismatches += 1
        
        print(f"  sent_{sid}: sentence={sent_dur}s, scenes_total={scene_total}s ({len(scenes)} scenes), diff={diff}{flag}")

print(f"\nTotal mismatches (>0.01s): {mismatches}")
