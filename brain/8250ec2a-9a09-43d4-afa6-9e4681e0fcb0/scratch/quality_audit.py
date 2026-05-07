import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'

# Load all data
with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_1_filmable.json', encoding='utf-8') as f:
    filmable = json.load(f)
with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    scenes = json.load(f)
with open(f'{base}\\ch_01_Level_1__Vulnerability_step0_sentences.json', encoding='utf-8') as f:
    sents = json.load(f)
with open(f'{base}\\ch_01_Level_1__Vulnerability_step4_prompts.json', encoding='utf-8') as f:
    prompts = json.load(f)

print("=" * 70)
print("STEP 3.1 — FILMABLE SCENES QUALITY AUDIT")
print("=" * 70)

sent_map = {s['sentence_id']: s for s in sents}
total_filmable_scenes = 0
total_sentences = 0
classifications = {}

for seq_id, entries in filmable.items():
    print(f"\n{'─'*60}")
    print(f"  {seq_id} ({len(entries)} sentence entries)")
    print(f"{'─'*60}")
    
    for entry in entries:
        sid = entry.get('sentence_id', '?')
        orig = entry.get('original_text', '')[:70]
        cls = entry.get('classification', 'unknown')
        chars = entry.get('characters_present', False)
        broll = entry.get('is_broll', False)
        sub_scenes = entry.get('scenes', [])
        n_sub = len(sub_scenes)
        total_filmable_scenes += n_sub
        total_sentences += 1
        classifications[cls] = classifications.get(cls, 0) + 1
        
        # Get original sentence duration
        orig_dur = sent_map.get(sid, {}).get('duration', 0)
        scene_dur_sum = sum(s.get('duration', 0) for s in sub_scenes)
        dur_match = "✅" if abs(scene_dur_sum - orig_dur) < 0.1 else f"⚠️ {scene_dur_sum:.1f} vs {orig_dur:.1f}"
        
        char_icon = "👤" if chars else "🏔️"
        roll_icon = "B" if broll else "A"
        
        print(f"  [{sid}] {cls:20s} {char_icon}{roll_icon} {n_sub}sc {dur_match}")
        print(f"       orig: \"{orig}\"")
        for i, sc in enumerate(sub_scenes):
            vis = sc.get('visual', '')[:80]
            print(f"       └─ sc{i+1} ({sc.get('duration',0)}s): {vis}")

print(f"\n{'='*70}")
print("STEP 3.1 SUMMARY")
print(f"{'='*70}")
print(f"  Total sentences processed: {total_sentences}")
print(f"  Total filmable scenes: {total_filmable_scenes}")
print(f"  Classifications: {classifications}")

# Check audio_sync in Step 3 scenes
print(f"\n{'='*70}")
print("STEP 3.2 — AUDIO SYNC CHECK")
print(f"{'='*70}")

total_step3_scenes = 0
has_audio = 0
empty_audio = 0
for seq in scenes:
    sid = seq.get('sequence_id', '')
    for sc in seq.get('scenes', []):
        total_step3_scenes += 1
        audio = sc.get('audio_sync', '')
        if audio:
            has_audio += 1
        else:
            empty_audio += 1
            print(f"  ⚠️ {sc.get('global_scene_id', '?')}: empty audio_sync")

print(f"  Total scenes: {total_step3_scenes}")
print(f"  With audio_sync: {has_audio}")
print(f"  Empty audio_sync: {empty_audio}")

# Check Step 4 prompts quality
print(f"\n{'='*70}")
print("STEP 4 — PROMPT QUALITY")
print(f"{'='*70}")
print(f"  Total prompts: {len(prompts)}")
empty_flat = 0
short_flat = 0
for p in prompts:
    fp = p.get('flat_prompt', '')
    if not fp:
        empty_flat += 1
        print(f"  ⚠️ {p.get('global_scene_id','?')}: EMPTY flat_prompt")
    elif len(fp) < 50:
        short_flat += 1
        print(f"  ⚠️ {p.get('global_scene_id','?')}: SHORT ({len(fp)} chars)")
print(f"  Empty: {empty_flat}, Short (<50): {short_flat}")

# Duration alignment check
print(f"\n{'='*70}")
print("DURATION ALIGNMENT")
print(f"{'='*70}")
for seq in scenes:
    sid = seq.get('sequence_id', '')
    scene_total = sum(s.get('duration', 0) for s in seq.get('scenes', []))
    seq_dur = seq.get('total_duration', seq.get('total_sequence_duration', 0))
    diff = abs(scene_total - seq_dur)
    status = "✅" if diff < 1.0 else "⚠️"
    print(f"  {status} {sid}: scenes={scene_total:.1f}s vs seq={seq_dur:.1f}s (diff={diff:.1f}s)")
