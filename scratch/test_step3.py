import json

f = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt\Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step3_scenes.json'
data = json.loads(open(f, encoding='utf-8').read())

total_scenes = sum(len(s.get("scenes", [])) for s in data)
print(f"Total sequences: {len(data)}")
print(f"Total scenes: {total_scenes}")
print(f"Avg scenes/seq: {total_scenes/len(data):.1f}")

# Scene stats
all_scenes = []
for seq in data:
    for sc in seq.get("scenes", []):
        all_scenes.append(sc)

durations = [sc.get("duration", 0) for sc in all_scenes]
print(f"\nScene duration: {min(durations):.1f}s - {max(durations):.1f}s, avg={sum(durations)/len(durations):.1f}s")

# Shot types
from collections import Counter
shots = Counter(sc.get("shot_type", "?") for sc in all_scenes)
print(f"\nShot types:")
for st, cnt in shots.most_common():
    print(f"  {st}: {cnt} ({cnt*100//total_scenes}%)")

# A-Roll vs B-Roll
rolls = Counter(sc.get("roll_type", "?") for sc in all_scenes)
print(f"\nRoll types:")
for rt, cnt in rolls.most_common():
    print(f"  {rt}: {cnt} ({cnt*100//total_scenes}%)")

# Check time math: sum(scenes) vs total_sequence_duration
print(f"\nTime math check:")
violations = 0
for seq in data:
    sid = seq.get("sequence_id", "?")
    seq_dur = seq.get("total_sequence_duration", seq.get("total_duration", 0))
    scene_sum = sum(sc.get("duration", 0) for sc in seq.get("scenes", []))
    diff_pct = abs(scene_sum - seq_dur) / seq_dur * 100 if seq_dur > 0 else 0
    if diff_pct > 10:
        print(f"  VIOLATION {sid}: seq={seq_dur:.1f}s scenes={scene_sum:.1f}s diff={diff_pct:.0f}%")
        violations += 1
print(f"  Violations (>10%): {violations}/{len(data)}")

# Sample a few sequences
print(f"\n--- Sample sequences ---")
for seq in data[:3]:
    sid = seq.get("sequence_id", "?")
    locked = seq.get("locked_location", "?")
    n_scenes = len(seq.get("scenes", []))
    print(f"\n{sid} | location={locked} | {n_scenes} scenes")
    for sc in seq.get("scenes", []):
        shot = sc.get("shot_type", "?")
        roll = sc.get("roll_type", "?")
        dur = sc.get("duration", 0)
        desc = sc.get("scene_description", sc.get("visual_description", ""))[:80]
        chars = sc.get("character_labels", [])
        print(f"  [{roll}] {shot:12s} {dur:.1f}s | chars={chars} | {desc}...")
