import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'
with open(f'{base}\\ch_01_Level_1__Vulnerability_step1_sequences.json', encoding='utf-8') as f:
    seqs = json.load(f)
with open(f'{base}\\ch_01_Level_1__Vulnerability_step0_sentences.json', encoding='utf-8') as f:
    sents = json.load(f)

scene_max = 6

for seq in seqs:
    sid = seq['sequence_id']
    chars = seq.get('characters', [])
    print(f"\n{'='*60}")
    print(f"{sid} | {seq['total_duration']}s | chars: {chars}")
    print(f"{'='*60}")
    
    for sent_id in seq.get('sentence_ids', []):
        for s in sents:
            if s.get('sentence_id') == sent_id:
                dur = s['duration']
                text = s['text']
                
                # Duration analysis
                if dur > scene_max:
                    n_scenes = -(-int(dur) // scene_max)  # ceil
                    tag = f"SPLIT->{n_scenes}"
                else:
                    tag = "1_SCENE"
                
                # Filmable classification (heuristic)
                abstract_words = ['you are', 'your', 'yet', 'but', 'born into', 'bloodline', 'sensation']
                is_abstract = any(w in text.lower() for w in abstract_words)
                filmable = "REWRITE" if is_abstract else "KEEP"
                
                # Character presence check
                has_char_mention = any(c.lower() in text.lower() for c in ['father', 'he ', 'his ', 'your '])
                char_tag = "HAS_CHAR" if has_char_mention else "NO_CHAR_MENTION"
                
                print(f"  [{sent_id}] {dur}s | {tag} | {filmable} | {char_tag}")
                print(f"       \"{text[:100]}\"")
                break

print(f"\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
total_sents = sum(len(seq.get('sentence_ids',[])) for seq in seqs)
print(f"Total sentences: {total_sents}")
print(f"Scene max: {scene_max}s")

# Count how many need split
need_split = 0
need_rewrite = 0
no_char = 0
for seq in seqs:
    for sent_id in seq.get('sentence_ids', []):
        for s in sents:
            if s.get('sentence_id') == sent_id:
                if s['duration'] > scene_max:
                    need_split += 1
                abstract_words = ['you are', 'your', 'yet', 'but', 'born into', 'bloodline', 'sensation']
                if any(w in s['text'].lower() for w in abstract_words):
                    need_rewrite += 1
                has_char = any(c.lower() in s['text'].lower() for c in ['father', 'he ', 'his ', 'your '])
                if not has_char:
                    no_char += 1
                break

print(f"Need split (>{scene_max}s): {need_split}")
print(f"Need rewrite (abstract): {need_rewrite}")
print(f"No character mention: {no_char}")
