# Self-Audit: Xung Đột & Cải Tiến Implementation Plan

Sau khi đọc lại toàn bộ code liên quan, tôi phát hiện **6 xung đột/bug tiềm ẩn** và **4 đề xuất cải tiến**.

---

## 🔴 Xung đột & Bug

### Bug 1: `validate_phase_plan_sub_keys()` — 2 chỗ hardcode biography, KHÔNG chỉ 1

Plan hiện tại chỉ đề cập hardcoded prompt filename (line 2966). Nhưng **`_build_excerpt()` cũng hardcoded biography fields**:

```python
# rewriter.py line 2970-2984
bp_life_phases = blueprint.get("life_phases", [])     # ← biography field
bp_turning_points = blueprint.get("turning_points", []) 
bp_conflicts = blueprint.get("conflicts", [])

def _build_excerpt(phase_data):
    excerpt = {}
    if bp_turning_points:
        excerpt["turning_points"] = bp_turning_points
    if bp_conflicts:
        excerpt["conflicts"] = bp_conflicts
    if bp_life_phases:
        excerpt["life_phases"] = bp_life_phases         # ← battle KHÔNG CÓ field này
    return excerpt
```

**Hậu quả**: Battle blueprint có `battle_phases`, `commanders`, `chronological_campaign_phases` — KHÔNG có `life_phases`. Excerpt sẽ trống hoặc thiếu context → AI validate sub-keys mù lòa.

**Fix cần**: `_build_excerpt()` phải niche-aware:
- Biography: `life_phases`, `turning_points`, `conflicts`
- Battle: `battle_phases`, `commanders`, `chronological_campaign_phases`, `climactic_turning_points`

---

### Bug 2: `_extract_chapter_blueprint()` — `_always_keys` KHÔNG compatible với battle

```python
# rewriter.py line 309-315
if "core_identity" in blueprint:
    result["core_identity"] = blueprint["core_identity"]
if "personal_profile" in blueprint:
    result["personal_profile"] = blueprint["personal_profile"]

# line 411-413 — Fallback
_always_keys = {"core_identity", "personal_profile"}
if set(result.keys()) <= _always_keys:
    return blueprint  # ← trả FULL blueprint nếu chỉ có always keys
```

**Hậu quả**: Battle blueprint có `core_topic` (không phải `core_identity`) và KHÔNG có `personal_profile`. → `result` sẽ **trống hoàn toàn** → fallback trả FULL blueprint **MỌI CHAPTER** → context overflow, mất mục đích filtering.

**Fix cần**: Thêm battle-equivalent always-include keys:
```python
# Niche-aware always-keys
if "core_topic" in blueprint:        # Battle
    result["core_topic"] = blueprint["core_topic"]
if "political_context" in blueprint: # Battle  
    result["political_context"] = blueprint["political_context"]
```
Hoặc tốt hơn: config-driven `always_include_keys` trong style JSON.

---

### Bug 3: `style_data` CHƯA ĐƯỢC truyền vào `_run_shared_fw_pipeline()`

Plan đề xuất dùng `style_data.get("pipeline_features", {})` bên trong `_run_shared_fw_pipeline()`. Nhưng:

```python
# Signature hiện tại (line 1603-1612):
def _run_shared_fw_pipeline(
    self, *, fw_name, fw_output_dir, fw_pipeline_dir, fw_log,
    blueprint, style_json_raw, endpoints, tier, lang, niche,
    stop_check, get_wc_rule, get_ch_range,
    log_api=None, on_chapter_saved=None, auto_patch=True, resume=False,
):
```

**`style_data` (dict) KHÔNG có trong params — chỉ có `style_json_raw` (string).**

Có **3 call sites** (line 2151, 2455, 3482) cần cập nhật. 

**2 options**:
- **Option A**: Thêm param `style_data` vào `_run_shared_fw_pipeline()` — sạch nhưng sửa 4 chỗ (1 definition + 3 callers)
- **Option B**: Parse `json.loads(style_json_raw)` bên trong function — dirty nhưng không sửa callers. 
  ⚠️ Nhưng `style_json_raw` có thể là compact style (đã extract framework), mất `pipeline_features`!

**Kết luận**: **Option A an toàn hơn**. Parse lại JSON bên trong cũng chạy nhưng hơi wasteful. Tuy nhiên `style_json_raw` ở đây vẫn là **FULL** style JSON (chưa extract), nên Option B vẫn hoạt động. Cần kiểm tra lại caller ở line 2455 và 3482.

---

### Bug 4: Resume flow — `pipeline_features` sẽ MẤT

Resume flow (line 2063-2072) load `style_data` từ `r_style` filename → đọc lại style JSON file. OK.

Nhưng resume KHÔNG truyền `style_data` vào `_run_shared_fw_pipeline()` (line 2151-2167) — nó chỉ truyền `style_json_raw`. Đây là **cùng bug** với Bug 3 nhưng ở một call path khác.

**Fix**: Cùng fix với Bug 3 — thêm `style_data=style_data` hoặc parse bên trong.

---

### Bug 5: `apply_chapter_splits()` — Threshold chia chương cho battle có thể BẤT HỢP LÝ

```python
# rewriter.py line 3196-3201
if node_count <= 3:
    num_chapters = 1
elif node_count <= 6:
    num_chapters = 2
else:
    num_chapters = 3
```

Threshold này thiết kế cho biography (1 life event ~ 500-600 words narrative). 
Nhưng battle engagements có thể CẦN nhiều words hơn (technical depth: weapons, terrain, tactics per engagement). 1 engagement ~ 800-1000 words → threshold nên thấp hơn (2 main = 1 chapter?).

**Đây KHÔNG phải bug** nhưng cần cân nhắc: có nên config hóa threshold không?

**Đề xuất**: Thêm vào `pipeline_features`:
```json
"pipeline_features": {
    "phase_plan": true,
    "split_threshold": [2, 4]  // ← 1-2=1ch, 3-4=2ch, 5+=3ch (stricter for battle)
}
```
Fallback default = `[3, 6]` (biography behavior).

---

### Bug 6: `_NICHE_OUTLINE_FIELDS` — thiếu mapping cho battle Phase Plan output

```python
# rewriter.py line 418-450
_NICHE_OUTLINE_FIELDS = {
    # Battle
    "{battle_phase}": "battle_phase",           # ✅ có
    "{commanders_featured}": "commanders_featured", # ✅ có
    "{tactical_focus}": "tactical_focus",        # ✅ có
    "{factions_focus}": "factions_focus",        # ✅ có
    "{pacing_style}": "pacing_style",          # ✅ có
    ...
}
```

Mapping battle fields **ĐÃ CÓ** trong `_NICHE_OUTLINE_FIELDS`. **KHÔNG phải bug** nhưng cần đảm bảo Phase Plan prompt output field names MATCH CHÍNH XÁC với entries này.
Nếu Phase Plan prompt dùng `"campaign_phase"` thay vì `"battle_phase"` → mismatch → writer nhận `N/A`.

**Fix**: Validate naming consistency giữa:
1. Phase Plan prompt output → Outline prompt input → `_NICHE_OUTLINE_FIELDS` mapping → Writer prompt placeholders

---

## 🟡 Đề xuất cải tiến

### Cải tiến 1: Tách `_build_excerpt()` thành niche-aware function

Thay vì hardcode fields, làm dispatch:

```python
_VALIDATE_EXCERPT_FIELDS = {
    "biography": ["life_phases", "turning_points", "conflicts"],
    "battle":    ["battle_phases", "commanders", "chronological_campaign_phases",
                  "climactic_turning_points", "weapon_asymmetry"],
}

def _build_excerpt(blueprint, niche):
    niche_lower = (niche or "").lower()
    for kw, fields in _VALIDATE_EXCERPT_FIELDS.items():
        if kw in niche_lower:
            return {f: blueprint.get(f, []) for f in fields if blueprint.get(f)}
    # Fallback: send all non-core sections
    return {k: v for k, v in blueprint.items() if k not in {"core_identity", "core_topic"}}
```

Lợi ích: khi thêm mystery niche sau → chỉ thêm 1 dòng vào dict, KHÔNG sửa logic.

---

### Cải tiến 2: Config-driven `always_include_keys` trong style JSON

```json
"pipeline_features": {
    "phase_plan": true,
    "always_include_keys": ["core_topic", "political_context"]
}
```

`_extract_chapter_blueprint()` đọc list này thay vì hardcode `{"core_identity", "personal_profile"}`.

Fallback: nếu không có config → dùng default biography keys (backward compat).

---

### Cải tiến 3: `validate_phase_plan_sub_keys()` — Thêm param `niche` (MANDATORY)

Function hiện tại **KHÔNG nhận `niche`** → phải sửa:

```python
# OLD signature:
def validate_phase_plan_sub_keys(phase_plan, blueprint, api_endpoints, log_callback=None, stop_check=None):

# NEW signature:
def validate_phase_plan_sub_keys(phase_plan, blueprint, api_endpoints, 
                                  niche="", log_callback=None, stop_check=None):
```

Bên trong:
```python
# OLD:
system_prompt = _load_prompt("system_validate_sub_key_biography.txt")

# NEW — dispatch by niche:
_VALIDATE_PROMPT_MAP = {
    "biography": "system_validate_sub_key_biography.txt",
    "tiểu sử": "system_validate_sub_key_biography.txt",
    "battle":   "system_validate_sub_key_battle.txt",
    "trận":     "system_validate_sub_key_battle.txt",
    "chiến":    "system_validate_sub_key_battle.txt",
}
prompt_file = "system_validate_sub_key_biography.txt"  # default fallback
for kw, pf in _VALIDATE_PROMPT_MAP.items():
    if kw in (niche or "").lower():
        prompt_file = pf
        break
system_prompt = _load_prompt(prompt_file)
```

Call sites (2 chỗ, line 1650 và 1685):
```python
# OLD:
phase_plan = validate_phase_plan_sub_keys(phase_plan, blueprint, endpoints, ...)

# NEW — thêm niche:
phase_plan = validate_phase_plan_sub_keys(phase_plan, blueprint, endpoints, niche=niche, ...)
```

---

### Cải tiến 4: `research_blueprint()` — `_RESEARCH_PROMPT_MAP` cần mở rộng cho battle

Hiện tại `research_blueprint()` (line 1508-1520) có local `_RESEARCH_PROMPT_MAP` **CHỈ chứa biography**. Battle chưa có entry → `"No research prompt for niche 'trận đánh'"` error.

Cần thêm:
```python
_RESEARCH_PROMPT_MAP = {
    # Biography (existing)
    "biography": "system_research_blueprint_biography.txt",
    ...
    # Battle (NEW)
    "battle":   "system_research_blueprint_battle.txt",
    "trận":     "system_research_blueprint_battle.txt",
    "chiến":    "system_research_blueprint_battle.txt",
    "war":      "system_research_blueprint_battle.txt",
    "military": "system_research_blueprint_battle.txt",
}
```

---

## Tóm tắt Priority

| # | Loại | Mức độ | Mô tả |
|---|------|--------|-------|
| Bug 1 | 🔴 Breaks | Cao | `_build_excerpt()` hardcode biography fields → validate mù lòa |
| Bug 2 | 🔴 Breaks | Cao | `_extract_chapter_blueprint()` fallback → context overflow mọi chapter |
| Bug 3 | 🔴 Breaks | Cao | `style_data` chưa truyền → `pipeline_features` không đọc được |
| Bug 4 | 🟠 Bug | TB | Resume path cùng vấn đề Bug 3 |
| Bug 5 | 🟡 Design | Thấp | Split threshold có thể bất hợp lý cho battle |
| Bug 6 | 🟡 Design | Thấp | Field naming consistency cần validate |
| CT 1 | 🟢 Improve | TB | `_build_excerpt()` niche-aware dispatch |
| CT 2 | 🟢 Improve | Thấp | Config-driven `always_include_keys` |
| CT 3 | 🔴 Required | Cao | `validate_phase_plan_sub_keys()` thêm param `niche` |
| CT 4 | 🔴 Required | Cao | `research_blueprint()` thêm battle entries |

> [!CAUTION]
> **Bug 1 + Bug 2 + Bug 3 + CT 3 là BLOCKING** — nếu không fix, pipeline sẽ crash hoặc cho output sai khi chạy battle niche v2. Plan hiện tại ĐÃ ĐỀ CẬP Bug 3 và CT 3 ở mục "Open Questions" nhưng chưa nhận diện Bug 1 và Bug 2.

> [!NOTE]
> Không có xung đột nào giữa các component đề xuất. Tất cả changes đều backward-compatible với biography pipeline hiện tại. Style v2 là file MỚI, prompts là file MỚI, code changes đều có fallback.
