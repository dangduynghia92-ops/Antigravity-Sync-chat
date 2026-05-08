import json

fp = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerable\ch_01_Level_1__Vulnerable_step3_1_filmable.json'

with open(fp, encoding='utf-8') as f:
    data = json.load(f)

# Get SEQ_01 data
seq01 = data.get('SEQ_01', [])

print("=== SEQ_01 FILMABLE SCENES ===\n")
for entry in seq01:
    sid = entry.get('sentence_id', '?')
    cls = entry.get('classification', '?')
    chars = entry.get('characters_present', '?')
    broll = entry.get('is_broll', False)
    interaction = entry.get('character_interaction', 'N/A')
    orig = entry.get('original_text', '')[:80]
    
    print(f"Sentence {sid}: [{cls}] chars_present={chars} broll={broll}")
    print(f"  text: {orig}...")
    print(f"  interaction: {interaction}")
    
    for i, sc in enumerate(entry.get('scenes', [])):
        visual = sc.get('visual', '')
        # Check which characters are mentioned
        has_child = any(w in visual.lower() for w in ['child', 'infant', 'newborn', 'baby', 'noble-a'])
        has_father = any(w in visual.lower() for w in ['father', 'najm', 'commander', 'man holding'])
        print(f"  Scene {i+1} ({sc.get('duration',0)}s):")
        print(f"    child_mentioned: {has_child} | father_mentioned: {has_father}")
        print(f"    visual: {visual[:150]}...")
    print()
