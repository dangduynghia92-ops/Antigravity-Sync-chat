import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test', 'video_prompt')

# Step 4 prompts
fp = os.path.join(base, 'ch_01_Level_1__Vulnerable_step4_prompts.json')
with open(fp, encoding='utf-8') as f:
    data = json.load(f)

print(f"Total prompts: {len(data)}")
print(f"Keys: {list(data[0].keys())}")
for p in data[:3]:
    print(f"  {p.get('global_scene_id', p.get('scene_id', ''))}: "
          f"dur={p.get('duration', '?')} "
          f"chapter={p.get('chapter', 'MISSING')} "
          f"audio_sync={repr(p.get('audio_sync', 'MISSING'))[:80]}")

# Step 0 sentences
fp2 = os.path.join(base, 'ch_01_Level_1__Vulnerable_step0_sentences.json')
with open(fp2, encoding='utf-8') as f:
    sents = json.load(f)

print(f"\nSentences: {len(sents)}")
print(f"Keys: {list(sents[0].keys())}")
for s in sents[:5]:
    print(f"  {s.get('sentence_id')}: start={s.get('start_time', 'MISSING')} dur={s.get('duration')} text={s.get('text', '')[:50]}")

# Step 3 scenes
fp3 = os.path.join(base, 'ch_01_Level_1__Vulnerable_step3_scenes.json')
with open(fp3, encoding='utf-8') as f:
    scenes = json.load(f)

print(f"\nStep 3 scenes: {len(scenes)} sequences")
for seq in scenes[:1]:
    print(f"  {seq.get('sequence_id')}: {len(seq.get('scenes', []))} scenes")
    for sc in seq.get('scenes', [])[:3]:
        print(f"    {sc.get('global_scene_id')}: dur={sc.get('duration')} audio_sync={repr(sc.get('audio_sync', 'MISSING'))[:60]}")
