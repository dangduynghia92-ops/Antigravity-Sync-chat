import json, os
base = r'C:\Users\Admin\Downloads\001_[C41uC9wzVTY]_Your Life as King Baldwin IV\Split\001_[C41uC9wzVTY]_Your Life as King Baldwin IV_S\video_prompt'

# World Bible size
wb_file = os.path.join(base, 'Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step2_world_bible.json')
if os.path.exists(wb_file):
    wb = json.loads(open(wb_file, encoding='utf-8').read())
    wb_str = json.dumps(wb, ensure_ascii=False)
    print(f"World Bible JSON: {len(wb_str)} chars")
else:
    print("No old world bible found")

# Check new world bible
for f in os.listdir(base):
    if 'world_bible' in f or 'step2' in f:
        fpath = os.path.join(base, f)
        size = os.path.getsize(fpath)
        print(f"  {f}: {size} bytes")

# Sequences input size
seq_file = os.path.join(base, 'Chapter 1 - Level 1 The Numb Arm and Childhood Signs_step1_sequences.json')
seq = json.loads(open(seq_file, encoding='utf-8').read())
seq_data = []
for s in seq:
    seq_data.append({
        "sequence_id": s["sequence_id"],
        "characters": s.get("characters", []),
        "full_text": s.get("full_text", "")
    })
seq_input = json.dumps(seq_data, ensure_ascii=False, indent=2)
print(f"Sequences input: {len(seq_input)} chars ({len(seq)} sequences)")
