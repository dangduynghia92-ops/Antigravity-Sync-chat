import json

f = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt\Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step1_sequences.json'
data = json.loads(open(f, encoding='utf-8').read())

print("SEQ order vs chapter_id:")
for s in data:
    sid = s.get('sequence_id', '?')
    ch_id = s.get('chapter_id', '?')
    ch_name = s.get('chapter_name', '?')
    text = s.get('full_text', '')[:60]
    print(f"  {sid:8s} | ch_id={ch_id} | {ch_name[:50]:50s} | {text}...")
