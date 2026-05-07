import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt'
with open(f'{base}\\ch_01_Level_1__Vulnerability_step2_characters.json', encoding='utf-8') as f:
    data = json.load(f)

out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\char_audit.txt'
with open(out, 'w', encoding='utf-8') as f:
    for c in data.get('characters', []):
        f.write(f"{'='*60}\n")
        f.write(f"LABEL: {c.get('label','')}\n")
        f.write(f"NAME: {c.get('original_name','')}\n")
        f.write(f"GROUP: {c.get('group','')}\n")
        f.write(f"AGE: {c.get('age_stage','')}\n")
        f.write(f"\nVISUAL_DESCRIPTION:\n{c.get('visual_description','')}\n")
        f.write(f"\nBODY_LANGUAGE:\n{c.get('body_language','')}\n")
        f.write(f"\nSHEET_PROMPT:\n{c.get('sheet_prompt','')}\n\n")

print("Done")
