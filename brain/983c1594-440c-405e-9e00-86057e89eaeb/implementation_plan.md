# Resume & Retry — Narrative New Content Pipeline

## Scope
- **Phase 1 only**: Narrative mode + New Content type
- Không động vào: Top/List mode, Rewrite type

---

## 1. Retry cho Validate Step

#### [MODIFY] [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

Trong `_validate_single_phase()`: wrap API call với 3 retries, 10s delay.
- Mỗi retry log: `"⚠ Validate {phase} failed (attempt 1/3), retry in 10s..."`
- Sau 3 lần fail: `"❌ Validate {phase} failed after 3 retries"` → return empty (phase giữ nguyên)
- Delay có thể bị interrupt bởi `stop_check`

---

## 2. Metadata File `_resume.json`

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

Lưu ngay khi pipeline bắt đầu (step 0, trước research):

```json
{
  "mode": "Narrative",
  "type": "new_content",
  "niche": "biography tiểu sử nhân vật chân dung cuộc đời",
  "style": "narrative_tiểu_sử_nhân_vật.json",
  "lang": "español",
  "started_at": "2026-04-09T15:54:28"
}
```

Vị trí: `{output_dir}/_pipeline/_resume.json`

---

## 3. Resume Button

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

**UI**: Thêm nút `"▶ Resume"` cạnh nút Stop/Retry (vùng khoanh đỏ)

**Logic khi ấn Resume**:
```
1. Đọc Output path từ UI
   └─ Trống? → log "No output path — set Output first" → return

2. Đọc {output}/_pipeline/_resume.json
   └─ Không có? → log "No resume data found" → return

3. Check mode + type
   └─ mode ≠ "Narrative"? → log "Resume only supports Narrative mode" → return
   └─ type ≠ "new_content"? → log "Resume only supports New Content" → return

4. Scan checkpoint files → chạy pipeline với resume=True
```

---

## 4. Resume Logic trong Pipeline

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

### A. Shared steps (research + framework)

| File tồn tại? | Action |
|---|---|
| `_blueprint.json` | Load → skip research |
| `_rankings.json` | Load → skip framework selection |

### B. Detect versions cần resume

```python
# Scan output dir cho v*_*/ subdirectories
version_dirs = [d for d in os.listdir(output_dir) if d.startswith("v") and os.path.isdir(d)]

for vdir in version_dirs:
    full_script = os.path.join(output_dir, vdir, "FULL_SCRIPT.txt")
    if os.path.exists(full_script):
        log(f"✓ [Resume] {vdir} complete — skip")
    else:
        # Resume this version
        ...
```

### C. Per-version checkpoint (trong `_run_shared_fw_pipeline`)

Thêm param `resume=False`. Khi `resume=True`:

| Step | Check file | Action nếu có |
|---|---|---|
| A1: Phase Plan | `_phase_plan.json` | Load, skip |
| A2: Validate | `_phase_plan_validated.json` | Load, skip |
| A3: Split | `_phase_plan_final.json` | Load, skip |
| B: Outline | `_renew_outline.json` | Load, skip (chạy audit nếu `_audited` chưa có) |
| C: Audit | `_renew_outline_audited.json` | Load, skip |
| D: Write Ch.N | `ch_{N:02d}_*.txt` | Load text cho context, skip chapter |
| E: Review | *(luôn chạy lại)* | Cross-chapter → phải re-review |
| F: Merge | *(luôn chạy lại)* | Re-merge từ tất cả chapters |

### D. Chapter-level resume (Step D)

```python
for i, ch_outline in enumerate(out_chapters):
    out_fname = f"ch_{i+1:02d}_{safe_title}.txt"
    out_path = os.path.join(fw_output_dir, out_fname)
    
    if resume and os.path.exists(out_path):
        # Load existing text for prev_context
        with open(out_path, "r", encoding="utf-8") as f:
            existing_text = f.read()
        rewritten_texts.append(existing_text)
        fw_log(f"✓ [Resume] Ch.{i+1}/{total}: loaded")
        continue
    
    # Write new chapter (existing code)
    ...
```

---

## 5. Files Modified

| File | Changes |
|---|---|
| `core/rewriter.py` | Retry logic trong `_validate_single_phase` |
| `ui/script_creation_tab.py` | Resume button, `_resume.json` save, resume param, checkpoint detection |

## Notes

> [!IMPORTANT]
> Resume luôn dùng checkpoint files đã có. Không tạo lại outline/phase plan nếu file tồn tại.

> [!WARNING]
> Review + Merge luôn chạy lại (không skip) vì chúng cần cross-chapter context.

## Verification

1. Chạy Newton → Stop giữa ch.3 → Resume → verify ch.1-2 skip, ch.3 tiếp tục
2. Chạy dual → Stop v1 giữa chừng, v2 hoàn thành → Resume → verify chỉ v1 chạy
3. Output trống → ấn Resume → verify log warning
