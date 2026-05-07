import json

# Read step0 output
step0_path = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\v1_Cuộc_Đời_Bạn_final2\Test\video_prompt\ch_01_Level_1__Vulnerability_step0_sentences.json'
with open(step0_path, encoding='utf-8') as f:
    sentences = json.load(f)

# Read original SRT
srt_path = r'C:\Users\Admin\OneDrive\Documents\Biography_Saladin_(Ayyubid)_20260503_1700\Test voice srt\ch_01_Level_1__11Vulnerability.srt'
with open(srt_path, encoding='utf-8') as f:
    srt_raw = f.read()

out_path = r'C:\Users\Admin\.gemini\antigravity\brain\8250ec2a-9a09-43d4-afa6-9e4681e0fcb0\scratch\srt_check.txt'
with open(out_path, 'w', encoding='utf-8') as f:
    # SRT format check
    f.write("=" * 60 + "\n")
    f.write("SRT FORMAT CHECK\n")
    f.write("=" * 60 + "\n")
    
    import re
    blocks = re.split(r'\n\s*\n', srt_raw.strip())
    f.write(f"Total SRT blocks: {len(blocks)}\n")
    
    issues = []
    prev_end = 0
    for i, block in enumerate(blocks):
        lines = block.strip().split('\n')
        if len(lines) < 3:
            issues.append(f"Block {i+1}: only {len(lines)} lines (expected >= 3)")
            continue
        
        # Check index
        try:
            idx = int(lines[0].strip())
        except:
            issues.append(f"Block {i+1}: invalid index '{lines[0]}'")
        
        # Check timestamp
        ts_match = re.match(r'(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})', lines[1])
        if not ts_match:
            issues.append(f"Block {i+1}: invalid timestamp '{lines[1]}'")
        else:
            def ts_to_sec(ts):
                h, m, rest = ts.split(':')
                s, ms = rest.split(',')
                return int(h)*3600 + int(m)*60 + int(s) + int(ms)/1000
            
            start = ts_to_sec(ts_match.group(1))
            end = ts_to_sec(ts_match.group(2))
            gap = start - prev_end
            
            if end <= start:
                issues.append(f"Block {i+1}: end <= start ({end} <= {start})")
            if start < prev_end - 0.001:
                issues.append(f"Block {i+1}: overlaps with previous (start={start:.3f}, prev_end={prev_end:.3f})")
            if gap > 2.0:
                issues.append(f"Block {i+1}: large gap {gap:.3f}s from previous")
            
            prev_end = end
    
    if issues:
        for iss in issues:
            f.write(f"  WARNING: {iss}\n")
    else:
        f.write("  OK: All blocks properly formatted\n")
    
    total_srt_dur = prev_end
    f.write(f"  Total SRT duration: {total_srt_dur:.3f}s\n")
    
    # Step 0 output check
    f.write("\n" + "=" * 60 + "\n")
    f.write("STEP 0 OUTPUT CHECK\n")
    f.write("=" * 60 + "\n")
    
    f.write(f"Total sentences: {len(sentences)}\n\n")
    
    total_step0_dur = 0
    for s in sentences:
        sid = s.get('sentence_id', '?')
        text = s.get('text', '')
        start = s.get('start_time', 0)
        end = s.get('end_time', 0)
        dur = s.get('duration', 0)
        total_step0_dur += dur
        
        # Check completeness
        has_end_punct = text.strip()[-1] in '.!?;' if text.strip() else False
        
        f.write(f"  [{sid}] {start:.3f}s - {end:.3f}s ({dur}s)\n")
        f.write(f"    text: {text}\n")
        if not has_end_punct:
            f.write(f"    WARNING: no ending punctuation!\n")
    
    f.write(f"\n  Total Step0 duration: {total_step0_dur:.2f}s\n")
    f.write(f"  SRT duration: {total_srt_dur:.3f}s\n")
    diff = abs(total_step0_dur - total_srt_dur)
    f.write(f"  Difference: {diff:.3f}s ({diff/total_srt_dur*100:.1f}%)\n")
    
    # Check sentence merging quality
    f.write("\n" + "=" * 60 + "\n")
    f.write("MERGE QUALITY\n")
    f.write("=" * 60 + "\n")
    
    # Reconstruct full text from SRT
    srt_texts = []
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) >= 3:
            srt_texts.append(' '.join(lines[2:]))
    srt_full = ' '.join(srt_texts)
    
    # Full text from step0
    step0_full = ' '.join(s['text'] for s in sentences)
    
    # Compare
    srt_words = srt_full.split()
    step0_words = step0_full.split()
    
    f.write(f"  SRT word count: {len(srt_words)}\n")
    f.write(f"  Step0 word count: {len(step0_words)}\n")
    
    if srt_words == step0_words:
        f.write("  OK: Perfect word match\n")
    else:
        f.write("  MISMATCH: Words differ!\n")
        # Show first difference
        for i, (sw, pw) in enumerate(zip(srt_words, step0_words)):
            if sw != pw:
                f.write(f"    First diff at word {i}: SRT='{sw}' vs Step0='{pw}'\n")
                break
    
    # Timing continuity
    f.write("\n" + "=" * 60 + "\n")
    f.write("TIMING CONTINUITY\n")
    f.write("=" * 60 + "\n")
    gaps = []
    for i in range(1, len(sentences)):
        prev = sentences[i-1]
        curr = sentences[i]
        gap = curr['start_time'] - prev['end_time']
        if abs(gap) > 0.5:
            gaps.append(f"  Gap between sent {prev['sentence_id']} and {curr['sentence_id']}: {gap:.3f}s")
    
    if gaps:
        for g in gaps:
            f.write(g + "\n")
    else:
        f.write("  OK: No major timing gaps\n")

print("Done")
