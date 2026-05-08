import re, os

base = r'F:\1. Edit Videos\7.Youtube\5. Tieu su nhan vat\Tom Tat'
for folder in sorted(os.listdir(base)):
    fpath = os.path.join(base, folder)
    if not os.path.isdir(fpath):
        continue
    for f in os.listdir(fpath):
        if f.endswith('_transcript.txt'):
            txt = open(os.path.join(fpath, f), 'r', encoding='utf-8').read()
            clean = re.sub(r'\(\d+:\d+\)', '', txt)
            clean = re.sub(r'\[music\]', '', clean)
            clean = re.sub(r'>>', '', clean)
            
            parts = re.split(r'(Level\s+\w+)', clean)
            chapters = []
            for i in range(1, len(parts), 2):
                header = parts[i].strip()
                body = parts[i+1].strip() if i+1 < len(parts) else ''
                full = header + ' ' + body
                words = len(full.split())
                chapters.append((header, words))
            
            print(f'=== {folder[:60]} ===')
            total = 0
            for h, w in chapters:
                print(f'  {h:<25s}: {w:4d} words')
                total += w
            print(f'  {"TOTAL":<25s}: {total:4d} words')
            print(f'  {"AVG/chapter":<25s}: {total//len(chapters):4d} words')
            print(f'  {"MAX":<25s}: {max(w for _,w in chapters):4d} words')
            print(f'  {"MIN":<25s}: {min(w for _,w in chapters):4d} words')
            print()
