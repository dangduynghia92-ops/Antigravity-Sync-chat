import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'

with open(f'{base}\\ch_01_Level_1__Vulnerability_step1_sequences.json', encoding='utf-8') as f:
    seqs = json.load(f)

with open(f'{base}\\ch_01_Level_1__Vulnerability_step3_scenes.json', encoding='utf-8') as f:
    scenes_data = json.load(f)

print('=== SEQUENCES ===')
for s in seqs:
    sid = s['sequence_id']
    dur = s['total_duration']
    sents = s.get('sentence_ids', [])
    print(f"{sid}: {dur}s, {len(sents)} sentences")

print()

# Simulate audio overlay approach
print('=== FEASIBILITY: Audio Overlay Simulation ===')

# Get sentence timing from step1
# Build sentence list with cumulative time per sequence
for seq_data in scenes_data:
    sid = seq_data['sequence_id']
    sc_list = seq_data.get('scenes', [])
    
    # Current: each scene has audio_sync (LLM assigned)
    # New: audio would be assigned by timing math
    
    cumulative = 0.0
    print(f"\n--- {sid} ---")
    for sc in sc_list:
        start = cumulative
        end = cumulative + sc['duration']
        audio = sc.get('audio_sync', '')[:80]
        print(f"  {sc['global_scene_id']}: [{start:.1f}s - {end:.1f}s] {sc['shot_type']}")
        print(f"    Current audio_sync: {audio}...")
        cumulative = end
    
    # Find matching sequence from step1
    matching_seq = next((s for s in seqs if s['sequence_id'] == sid), None)
    if matching_seq:
        print(f"  Total scenes duration: {cumulative:.1f}s vs sequence duration: {matching_seq['total_duration']}s")
        diff = abs(cumulative - matching_seq['total_duration'])
        if diff > 0.5:
            print(f"  !! TIMING MISMATCH: {diff:.1f}s")
        else:
            print(f"  [OK] Timing OK (diff: {diff:.2f}s)")

print("\n=== KEY QUESTION: Can audio be overlaid by timing math? ===")
print("For each shot [start_time, end_time], find sentences that overlap")
print("Sentences have exact durations from SRT → cumulative start/end times")
print("This is pure code calculation, no LLM needed")
print("→ FEASIBLE")

print()
