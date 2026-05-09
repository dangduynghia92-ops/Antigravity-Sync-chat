import json, os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt')

wb = json.load(open(os.path.join(base, 'ch_08_Level_8__Chilled_step2_world_bible.json'), encoding='utf-8'))

for faction in wb.get('factions', []):
    name = faction.get('name', '?')
    print(f"\n=== {name} ===")
    rv = faction.get('role_variants', {})
    ca = faction.get('crowd_archetypes', {})
    print(f"  role_variants: {list(rv.keys())}")
    print(f"  crowd_archetypes: {list(ca.keys())}")
    for role, desc in ca.items():
        if isinstance(desc, list):
            print(f"    {role}: {len(desc)} types")
            for d in desc[:1]:
                print(f"      {d[:120]}...")
        else:
            print(f"    {role}: {str(desc)[:120]}...")
