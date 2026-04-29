import os, glob

base = r"F:\1. Edit Videos\7.Youtube\10. Gun\1. Channel 1\1.Video doi thu\@BallisticEdge08\New folder"

hooks = sorted(glob.glob(os.path.join(base, "*", "Chapter 0*")))[:20]

for f in hooks:
    folder = os.path.basename(os.path.dirname(f))[:60]
    with open(f, encoding='utf-8') as fh:
        lines = fh.readlines()
    # Skip header lines
    content = ""
    for line in lines:
        if line.startswith("Chapter 0") or line.startswith("===="):
            continue
        content += line
    content = content.strip()
    # Remove timestamps like (0:00) etc
    import re
    content = re.sub(r'\(\d+:\d+\)\s*', '', content)
    content = re.sub(r'>>\s*', '', content)
    content = re.sub(r'\[music\]\s*', '', content)
    print(f"=== {folder} ===")
    print(content[:600])
    print("\n---\n")
