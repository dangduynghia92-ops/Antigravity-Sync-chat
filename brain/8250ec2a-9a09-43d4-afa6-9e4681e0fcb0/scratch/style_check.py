import os

debug_dir = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test\video_prompt\ch_01_Level_1__Vulnerability_debug'
out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\style_check.txt'

# Read step4_seq0 system prompt (= style file content)
sys_prompt = ''
for f in os.listdir(debug_dir):
    if 'step4_seq0_system_prompt' in f:
        with open(os.path.join(debug_dir, f), encoding='utf-8') as fh:
            sys_prompt = fh.read()
        break

with open(out, 'w', encoding='utf-8') as f:
    f.write(f"Length: {len(sys_prompt)}\n")
    f.write(f"First 500 chars:\n{sys_prompt[:500]}\n\n")
    # Find mandatory style
    import re
    ms = re.search(r'Mandatory\s+Style[:\s]*(.+?)(?:Negative|$)', sys_prompt, re.DOTALL | re.IGNORECASE)
    if ms:
        f.write(f"MANDATORY STYLE:\n{ms.group(1).strip()}\n")
    else:
        f.write("No Mandatory Style found\n")

print("Done")
