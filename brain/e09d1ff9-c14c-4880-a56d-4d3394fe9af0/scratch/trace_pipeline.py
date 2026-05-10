import json

base = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\_pipeline'

# Step 1: Phase Plan output
pp = json.load(open(f'{base}\\_phase_plan.json','r',encoding='utf-8'))
events1 = pp.get('event_timeline', [])
print('=== STEP 1: Phase Plan ===')
print(f'Events: {len(events1)}')
step1_titles = set()
for e in events1:
    eid = e.get("event_id","?")
    age = e.get("age","?")
    title = e.get("event_title","?")
    label = e.get("phase_label","")
    step1_titles.add(title)
    print(f'  event {eid}: age {age} -- {title} [{label}]')

# Step 2: Validate output  
vv = json.load(open(f'{base}\\_phase_plan_validated.json','r',encoding='utf-8'))
events2 = vv.get('event_timeline', [])
print(f'\n=== STEP 2: Validate ===')
print(f'Events: {len(events2)}')
for e in events2:
    eid = e.get("event_id","?")
    age = e.get("age","?")
    title = e.get("event_title","?")
    marker = ' <-- ADDED' if title not in step1_titles else ''
    print(f'  event {eid}: age {age} -- {title}{marker}')

# Step 3: Chapter Plan output
cp = json.load(open(f'{base}\\_chapter_planning.json','r',encoding='utf-8'))
print(f'\n=== STEP 3: Chapter Plan ===')
print(f'Before: {cp.get("total_before")}, After: {cp.get("total_after")}')
for d in cp.get('demoted_events', []):
    st = d.get('scene_test', {})
    title = d.get("event_title","?")
    target = d.get("moved_to_event_id","?")
    print(f'  DEMOTE: {title} --> event {target}')
    if st:
        for k,v in st.items():
            print(f'    {k}: {v}')
    else:
        print(f'    reason: {d.get("reason","?")}')

# Final
fp = json.load(open(f'{base}\\_phase_plan_final.json','r',encoding='utf-8'))
events3 = fp.get('event_timeline', [])
print(f'\n=== FINAL: {len(events3)} chapters ===')
for e in events3:
    eid = e.get("event_id","?")
    age = e.get("age","?")
    title = e.get("event_title","?")
    print(f'  ch{eid}: age {age} -- {title}')
