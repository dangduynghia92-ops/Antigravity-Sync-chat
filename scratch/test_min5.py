import json

f = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt\Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step1_sequences.json'
data = json.loads(open(f, encoding='utf-8').read())

under5 = [s for s in data if s.get('total_duration', 0) < 5]
print(f"Under 5s sequences: {len(under5)}")
for s in under5:
    idx = data.index(s)
    sid = s.get('sequence_id', '?')
    dur = s.get('total_duration', 0)
    text = s.get('full_text', '')[:80]
    prev_dur = data[idx-1].get('total_duration', 0) if idx > 0 else 0
    prev_sid = data[idx-1].get('sequence_id', '?') if idx > 0 else '-'
    next_dur = data[idx+1].get('total_duration', 0) if idx < len(data)-1 else 0
    next_sid = data[idx+1].get('sequence_id', '?') if idx < len(data)-1 else '-'
    merged_prev = prev_dur + dur
    merged_next = dur + next_dur
    status_prev = "OK" if merged_prev <= 25 else "OVER"
    print(f"\n{sid} ({dur:.1f}s)")
    print(f"  Text: {text}...")
    print(f"  Prev: {prev_sid} ({prev_dur:.1f}s) -> merged={merged_prev:.1f}s [{status_prev}]")
    print(f"  Next: {next_sid} ({next_dur:.1f}s) -> merged={merged_next:.1f}s")
