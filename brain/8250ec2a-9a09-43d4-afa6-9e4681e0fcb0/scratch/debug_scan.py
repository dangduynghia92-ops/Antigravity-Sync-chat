import os

d = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn\Test'
out = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\check.txt'

with open(out, 'w', encoding='utf-8') as f:
    f.write(f"Dir exists: {os.path.exists(d)}\n")
    for root, dirs, files in os.walk(d):
        f.write(f"\nRoot: {root}\n")
        for fn in sorted(files):
            full = os.path.join(root, fn)
            f.write(f"  {fn}  (exists={os.path.exists(full)})\n")
    
    # Test txt detection specifically
    srt_name = "ch_01_Level_1__Vulnerability.srt"
    srt_full = os.path.join(d, srt_name)
    basename = os.path.splitext(srt_name)[0]
    txt_path = os.path.join(d, f"{basename}.txt")
    f.write(f"\nSRT: {srt_full}\n")
    f.write(f"SRT exists: {os.path.exists(srt_full)}\n")
    f.write(f"TXT path: {txt_path}\n")
    f.write(f"TXT exists: {os.path.exists(txt_path)}\n")

print("Done")
