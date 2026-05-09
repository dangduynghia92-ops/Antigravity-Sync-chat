import os

base = os.path.join(r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700',
                    'v1_Cu\u1ed9c_\u0110\u1eddi_B\u1ea1n', 'Test 3', 'video_prompt',
                    'ch_08_Level_8__Chilled_debug')

req = os.path.join(base, '033_step3_1_seq0_request.txt')
with open(req, encoding='utf-8') as f:
    content = f.read()

# Find user message part (after system prompt)
idx = content.find('=== USER MESSAGE ===')
if idx >= 0:
    print(content[idx:idx+800])
else:
    # Show last 800 chars
    print("=== LAST 800 chars ===")
    print(content[-800:])
