# Thống Nhất Pipeline: Battle Niche v2

## Mục tiêu
Mở rộng pipeline "3-Step Holy Trinity" (Phase Plan → Validate Sub-keys → Apply Splits) từ biography-only sang architecture data-driven, bắt đầu bằng bản thử nghiệm `phân_tích_trận_đánh_v2`.

## Bối cảnh & Vấn đề hiện tại

### Hardcoded biography-only gating
Toàn bộ logic Phase Plan bị khóa bởi 1 dòng hardcoded:

```python
# script_creation_tab.py line 1620-1622
_BIO_KW = ("biography", "tiểu sử", "nhân vật", "chân dung", "cuộc đời")
_is_biography = any(kw in (niche or "").lower() for kw in _BIO_KW)
```

Nếu `_is_biography = False` → **toàn bộ Step A (Phase Plan + Validate + Split) bị bỏ qua** → `phase_plan = None` → outline AI tự do chia chương không kiểm soát.

### Missing files cho battle pipeline
So sánh với biography pipeline (đầy đủ), battle thiếu:

| Pipeline Step | Biography | Battle |
|---|---|---|
| Phase Plan prompt | ✅ `system_narrative_phase_plan_biography.txt` | ❌ **chưa có** |
| Validate Sub-key prompt | ✅ `system_validate_sub_key_biography.txt` | ❌ **chưa có** |
| Research Blueprint prompt | ✅ `system_research_blueprint_biography.txt` | ❌ **chưa có** |
| Research Sections config | ✅ `_RESEARCH_SECTIONS_BIOGRAPHY` | ❌ **chưa có** |
| `_NICHE_PROMPT_MAP["narrative_phase_plan"]` | ✅ 5 keywords | ❌ **không có entry** |
| Style JSON `steps` / `tension_curve` / `evaluation_focus` | ✅ chi tiết | ⚠ cơ bản |

---

## User Review Required

> [!IMPORTANT]
> ### Quyết định kiến trúc: Data-Driven vs Hardcoded
> Thay vì thêm battle keywords vào `_BIO_KW`, plan này chuyển sang **config-driven detection**:
> Style JSON có `"pipeline_features": {"phase_plan": true}` → Python engine tự bật/tắt.
> Điều này đúng tinh thần "Data-Driven Auto-Fallback" từ `battle_niche_architecture.md`.

> [!IMPORTANT]
> ### Bản v2 thử nghiệm — KHÔNG sửa file gốc
> Tất cả thay đổi đều tạo file MỚI (`_v2` suffix) hoặc thêm code mới. 
> File production hiện tại (`narrative_phân_tích_trận_đánh.json`, các prompt battle gốc) giữ nguyên 100%.

> [!WARNING]
> ### Thay đổi nhỏ duy nhất trong code production
> `script_creation_tab.py` line 1620-1622: thay `_is_biography` hardcode bằng config lookup.
> Logic mới hoàn toàn backward-compatible: biography vẫn hoạt động y như cũ.

---

## Proposed Changes

### Component 1: Style JSON v2

#### [NEW] [narrative_phân_tích_trận_đánh_v2.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_phân_tích_trận_đánh_v2.json)

Tạo style JSON v2 mới kế thừa từ bản gốc, **thêm**:
- `"pipeline_features": {"phase_plan": true, "validate_sub_keys": true, "research_blueprint": true}` — config-flag cho engine
- `"steps"` array đầy đủ cho mỗi framework (tương đương biography), định nghĩa 5 Pacing Slots: Buildup → Deployment → Escalation → Chaos → Aftermath
- `"tension_curve"` cho mỗi framework  
- `"evaluation_focus"` với `primary_data_field` + `tier_scoring` 
- `"chapter_structures"` + `"closing_types"` cho battle

---

### Component 2: Battle Phase Plan + Validate Prompts

#### [NEW] [system_narrative_phase_plan_battle.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_phase_plan_battle.txt)

Prompt cho Step A1 (Phase Planning). Adapted từ biography version:
- Thay `life_phases` → `chronological_campaign_phases` / `battle_phases`
- `main_key_data`: engagements, turning_points, casus_belli, surrenders, commander deaths
- `sub_key_data`: weapon_asymmetry, logistics, weather, emotional_drivers
- Hook: ANCHOR (trận đánh nổi tiếng) + TWIST (bí mật/nghịch lý ít ai biết)
- End: main_key_data = [] (dùng callbacks + aftermath)
- Chronological mapping: Buildup → Deployment → Escalation → Chaos → Aftermath

#### [NEW] [system_validate_sub_key_battle.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_validate_sub_key_battle.txt)

Prompt cho Step A2 (Validate Sub-keys). Adapted:
- 3 tests giữ nguyên (Scene / Turning Point / Causal Independence)
- Anti-patterns mới cho battle: 
  - ✗ Logistics without drama ("Supply chain was weak")
  - ✗ Weather conditions without tactical impact ("It was cold")
  - ✗ Troop movements without stakes ("Army marched to X")
  - ✓ PROMOTE: "Fog caused friendly fire destroying the left flank" (weather → turning point)

#### [NEW] [system_research_blueprint_battle.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_research_blueprint_battle.txt)

Prompt cho New Content mode — AI tự nghiên cứu trận đánh, output schema theo Blueprint 2.0 (6-Block):
- origins_and_context, buildup_and_march, chronological_campaign_phases, climactic_turning_points, resolution_and_aftermath, texture_and_hooks

---

### Component 3: Code Wiring (rewriter.py)

#### [MODIFY] [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

1. **`_NICHE_PROMPT_MAP["narrative_phase_plan"]`** — Thêm battle keywords:
   ```python
   "narrative_phase_plan": {
       # Biography (existing)
       "biography": "system_narrative_phase_plan_biography.txt",
       ...
       # Battle (NEW)
       "battle":   "system_narrative_phase_plan_battle.txt",
       "war":      "system_narrative_phase_plan_battle.txt",
       "trận":     "system_narrative_phase_plan_battle.txt",
       "chiến":    "system_narrative_phase_plan_battle.txt",
       ...
   }
   ```

2. **`validate_phase_plan_sub_keys()`** — thay hardcoded `system_validate_sub_key_biography.txt` bằng niche-aware dispatch:
   ```python
   # Line 2966: thay hardcoded filename
   # OLD: system_prompt = _load_prompt("system_validate_sub_key_biography.txt")
   # NEW: detect niche → load correct prompt
   ```

3. **`_NICHE_RESEARCH_MAP`** — Thêm Battle research sections:
   ```python
   _RESEARCH_SECTIONS_BATTLE = [_RESEARCH_SECTION_BATTLE_A, _RESEARCH_SECTION_BATTLE_B, _RESEARCH_SECTION_BATTLE_C]
   _NICHE_RESEARCH_MAP["battle"] = _RESEARCH_SECTIONS_BATTLE
   _NICHE_RESEARCH_MAP["trận"] = _RESEARCH_SECTIONS_BATTLE
   ...
   ```

4. **`research_blueprint()`** — Thêm battle keywords vào `_RESEARCH_PROMPT_MAP`:
   ```python
   "battle": "system_research_blueprint_battle.txt",
   "trận":   "system_research_blueprint_battle.txt",
   ...
   ```

5. **`_extract_chapter_blueprint()`** — Thêm battle-specific field mapping:
   - `battle_phase` → match `battle_phases[]`
   - `commanders_featured` → match `commanders[]`
   - `tactical_focus` → match `technology_and_weapons[]`

---

### Component 4: Engine Config Detection (script_creation_tab.py)

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

Thay `_is_biography` hardcode bằng **config-driven detection**:

```python
# OLD (line 1620-1622):
_BIO_KW = ("biography", "tiểu sử", "nhân vật", "chân dung", "cuộc đời")
_is_biography = any(kw in (niche or "").lower() for kw in _BIO_KW)

# NEW:
# Read from style_data loaded earlier
_pipeline_features = style_data.get("pipeline_features", {})
_has_phase_plan = _pipeline_features.get("phase_plan", False)

# Backward compat: biography styles without pipeline_features still work
if not _has_phase_plan:
    _BIO_KW = ("biography", "tiểu sử", "nhân vật", "chân dung", "cuộc đời")
    _has_phase_plan = any(kw in (niche or "").lower() for kw in _BIO_KW)
```

Sau đó thay `if _is_biography:` → `if _has_phase_plan:` (1 chỗ, line 1626).

Cần truyền `style_data` vào `_run_shared_fw_pipeline()`. Kiểm tra xem callers đã có biến này chưa.

---

### Component 5: Niche Config v2

#### [NEW] [narrative_phân_tích_trận_đánh_v2.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/niche_configs/narrative_phân_tích_trận_đánh_v2.json)

Config mới với word count phù hợp cho battle narrative (dài hơn config hiện tại):
```json
{
  "lang": "Tiếng Việt",
  "framework": "Auto (detect & switch)",
  "tier": "Pro",
  "threads": 3,
  "ch_min": 5,
  "ch_max": 15,
  "wc_open_min": 1300,
  "wc_open_max": 1800,
  "wc_body_min": 1300,
  "wc_body_max": 1800,
  "wc_end_min": 1200,
  "wc_end_max": 1500,
  "google_check": true,
  "auto_patch": true
}
```

---

## Open Questions

> [!IMPORTANT]
> ### 1. Validate sub-key prompt: Cần truyền niche vào `validate_phase_plan_sub_keys()`
> Hiện tại function **không nhận param `niche`** → hardcode biography prompt. Cần thêm param `niche` và cập nhật tất cả call sites (3 chỗ trong `script_creation_tab.py`).
> Đây là thay đổi backward-compatible (default `niche=""` → fallback biography).

> [!IMPORTANT]
> ### 2. `_extract_chapter_blueprint()` — Battle field mapping
> Function hiện tại dùng biography-specific fields (`life_phase_covered`, `relationships_featured`, `myths_debunked`). 
> Battle cần equivalent (`battle_phase`, `commanders_featured`, `tactical_focus`).
> **Proposal**: Thêm battle field patterns bên cạnh biography patterns (cả hai hoạt động song song, phát hiện theo niche).

> [!IMPORTANT]
> ### 3. Style v2 filename — Cần hiển thị trong UI dropdown
> Style file v2 cần naming convention nhất quán. Đề xuất: `narrative_phân_tích_trận_đánh_v2.json` (thêm `_v2`).
> UI dropdown tự detect từ `styles/` folder → sẽ tự hiện ra, user chọn v2 để thử nghiệm.

---

## Verification Plan

### Automated Tests

1. **JSON validity**: Load tất cả JSON files mới bằng `json.load()` — không lỗi
2. **Prompt dispatch**: Test `_get_niche_prompt("narrative_phase_plan", "trận đánh")` → returns battle prompt file
3. **Config detection**: Test `style_data.get("pipeline_features", {}).get("phase_plan")` → `True` cho v2
4. **Python syntax**: `py_compile.compile("core/rewriter.py")` + `py_compile.compile("ui/script_creation_tab.py")` → pass
5. **Backward compat**: Chạy pipeline biography → phase plan vẫn kích hoạt → output không thay đổi

### Manual Verification
1. Chọn style `narrative_phân_tích_trận_đánh_v2` trong UI
2. Chạy với 1 battle topic (VD: "Trận Thermopylae") → kiểm tra:
   - Phase plan JSON có 5 Pacing Slots 
   - Validate sub-keys chạy với battle prompt
   - Chapter splits hợp lý (engagements = main, logistics = sub)
   - Output chapters follow blueprint structure
