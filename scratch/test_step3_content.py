import json

f = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt\Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step3_scenes.json'
data = json.loads(open(f, encoding='utf-8').read())

samples = [0, 6, 20, 30, 42]
for idx in samples:
    if idx >= len(data):
        continue
    seq = data[idx]
    sid = seq.get("sequence_id", "?")
    locked = seq.get("locked_location", "?")
    full_text = seq.get("full_text", "")
    scenes = seq.get("scenes", [])
    
    print("=" * 80)
    print(f"{sid} | Location: {locked}")
    print(f"SCRIPT: {full_text[:250]}")
    print(f"\nSTORYBOARD ({len(scenes)} scenes):")
    for i, sc in enumerate(scenes):
        shot = sc.get("shot_type", "?")
        roll = sc.get("roll_type", "?")
        dur = sc.get("duration", 0)
        chars = sc.get("character_labels", [])
        motion = sc.get("camera_motion", "")
        audio = sc.get("audio_sync", "")[:100]
        action = sc.get("physical_action", "")
        costume = sc.get("costume_note", "")
        lighting = sc.get("lighting_and_atmosphere", "")
        bg = sc.get("background_and_extras", "")
        
        print(f"\n  Scene {i+1} [{roll}] {shot} {dur:.1f}s | Motion: {motion}")
        print(f"  Audio: {audio}...")
        print(f"  Action: {action[:150]}")
        print(f"  Costume: {costume[:150]}")
        print(f"  Lighting: {lighting[:100]}")
        print(f"  BG: {bg[:100]}")
    print()
