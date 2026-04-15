# Phase Naming Standard — Ship Framework

## Naming Convention

| # | Old `name` (Vietnamese) | New `name` (English key) | `purpose` | `description` (giữ tiếng Việt) |
|---|------------------------|--------------------------|-----------|-------------------------------|
| 1 | Mồi Nhử Huyền Thoại | Hook | Hook | Phô diễn SCALE tàu |
| 2 | Bản Vẽ & Nguồn Gốc | Blueprint | Blueprint | Lòng tham Đế quốc + thiết kế gốc |
| 3 | Đột Biến | Mutation | Mutation | Vụ cướp + naming + giải phẫu đột biến |
| 4 | Bánh Răng Sinh Học | Human Engine | Human Engine | Đời sống + Pirate Code + Pirate Medicine |
| 5 | Thử Lửa | Apex Test | Apex Test | 1-2 sự kiện PEAK + hậu quả nạn nhân |
| 6 | Cái Chết Vật Lý | Death | System Collapse | Suy tàn + sự kiện chết + twist |
| 7 | Bóng Ma Khảo Cổ | Ghost | Archaeological Ghost | Time-jump + hiện vật + legacy question |

## Field Structure (JSON)

```json
{
  "name": "Human Engine",          // ← English key (used for matching/reference)
  "description": "Đời sống...",    // ← Vietnamese (context for AI khi viết)
  "purpose": "Human Engine",       // ← English (keep synced with name)
  "lens": "FREEZE-FRAME..."       // ← Tone/style guidance
}
```

## Rules
- `name` = English key, used in ALL prompts and references
- `description` = giữ tiếng Việt (AI cần đọc khi viết script tiếng Việt)
- `lens` = giữ mix Anh-Việt (instructions + ví dụ tiếng Việt)
- Prompts reference phases by `name` (e.g., "Human Engine chapters do NOT bridge")

## Files to Update

| File | What changes |
|------|-------------|
| `narrative_lịch_sử_hải_tặc.json` | `steps[].name` → English keys |
| `system_narrative_phase_plan_pirate.txt` | All phase references |
| `system_narrative_outline_pirate.txt` | Phase lens section + critical rules |
| `system_narrative_write_pirate.txt` | "Bánh Răng" → "Human Engine" |
| `rewriter.py` | **Không cần sửa** (code không match tên phase) |

> [!IMPORTANT]
> Đổi `name` sẽ ảnh hưởng output của phase_plan và outline. Các file pipeline cũ (`_phase_plan.json`, `_renew_outline.json`) sẽ dùng tên cũ → cần chạy lại từ phase_plan.
