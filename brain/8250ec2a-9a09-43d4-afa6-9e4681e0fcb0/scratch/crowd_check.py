import json

path = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_step2_world_bible.json'
out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\crowd_check.txt'

with open(path, encoding='utf-8') as f:
    wb = json.load(f)

with open(out, 'w', encoding='utf-8') as f:
    for faction in wb.get('factions', []):
        f.write(f"=== Faction: {faction.get('name','')} ===\n")
        crowd = faction.get('crowd_archetypes', {})
        if crowd:
            f.write("  crowd_archetypes:\n")
            for role, desc in crowd.items():
                if isinstance(desc, list):
                    for v in desc:
                        f.write(f"    {role}: {v}\n")
                else:
                    f.write(f"    {role}: {desc}\n")
        f.write("\n")

print("Done")
