import json

cur = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'

with open(f'{cur}\\ch_01_Level_1__Vulnerability_step0_sentences.json', encoding='utf-8') as f:
    sents = json.load(f)

print(f"Total sentences: {len(sents)}")
for s in sents:
    print(f"  [{s['sentence_id']:2d}] {s['duration']:.2f}s | {s['text'][:80]}")
