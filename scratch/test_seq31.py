import json
f = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt\Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step3_scenes.json'
data = json.loads(open(f, encoding='utf-8').read())
seq31 = data[30]
print("sequence_id:", seq31.get("sequence_id"))
print("total_sequence_duration:", seq31.get("total_sequence_duration"))
print("total_duration:", seq31.get("total_duration"))
scenes = seq31.get("scenes", [])
durs = [sc.get("duration", 0) for sc in scenes]
print(f"Scenes: {len(scenes)}, durations: {durs}, sum: {sum(durs)}s")
