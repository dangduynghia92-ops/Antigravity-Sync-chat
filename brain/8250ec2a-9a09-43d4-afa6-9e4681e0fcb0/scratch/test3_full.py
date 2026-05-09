import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

# Read cleaned script
script_path = os.path.join(base, 'ch_08_Level_8__Chilled_cleaned_script.txt')
with open(script_path, encoding='utf-8') as f:
    script = f.read()

print("=== CLEANED SCRIPT (full) ===")
print(script[:3000])
print("...")
print(script[-1000:])
print(f"\nTotal length: {len(script)} chars")

# Check sentences for chapter distribution
sent_path = os.path.join(base, 'ch_08_Level_8__Chilled_step0_sentences.json')
with open(sent_path, encoding='utf-8') as f:
    sents = json.load(f)

chapter_counts = {}
for s in sents:
    ch = s.get("chapter_name", s.get("chapter_id", "?"))
    chapter_counts[ch] = chapter_counts.get(ch, 0) + 1

print(f"\n=== Sentences by chapter ===")
for ch, count in chapter_counts.items():
    print(f"  {ch}: {count} sentences")

# Check sequences for chapter distribution
seq_path = os.path.join(base, 'ch_08_Level_8__Chilled_step1_sequences.json')
with open(seq_path, encoding='utf-8') as f:
    seqs = json.load(f)

print(f"\n=== Sequences: {len(seqs)} total ===")
for seq in seqs:
    sid = seq.get("sequence_id", "?")
    ch = seq.get("chapter_id", seq.get("chapter_name", "?"))
    chars = seq.get("characters", [])
    print(f"  {sid}: chapter={ch}, chars={chars}")

# All unique character mentions
all_chars = set()
for seq in seqs:
    for c in seq.get("characters", []):
        all_chars.add(c)

print(f"\n=== ALL unique character mentions across all chapters: {len(all_chars)} ===")
for c in sorted(all_chars):
    print(f"  {c}")
