import json

fp = json.load(open(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\_pipeline\_phase_plan_final.json','r',encoding='utf-8'))

# Find event 14 (where Tyre was demoted to)
for e in fp.get('event_timeline', []):
    eid = e.get('event_id')
    if eid == 14:
        title = e.get("event_title", "?")
        age = e.get("age", "?")
        print(f"Event {eid}: {title} (age {age})")
        print("sub_key_data:")
        for s in e.get('sub_key_data', []):
            print(f"  - {str(s)[:200]}")
        print()

# Also check demoted event in _chapter_planning.json
cp = json.load(open(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\_pipeline\_chapter_planning.json','r',encoding='utf-8'))
print("=== Demoted Events Detail ===")
for d in cp.get('demoted_events', []):
    print(json.dumps(d, indent=2, ensure_ascii=False))
