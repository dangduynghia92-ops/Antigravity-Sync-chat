# Battle V2 Key Data Audit & Expansion

## Overlap Audit — Current 17 Sections

### 🟢 Clean (giữ nguyên)
| # | Section | Vai trò | Overlap? |
|---|---------|---------|----------|
| 1 | `core_topic` | 2-3 câu tóm tắt | Không |
| 2 | `key_facts` | Dates, numbers, names | Không |
| 3 | `political_context` | Bối cảnh chính trị + catalyst | Không |
| 4 | `commanders` | Chỉ huy + quyết định + số phận | Không |
| 5 | `battle_phases` | Diễn biến từng phase | Không |
| 6 | `geography` | Địa hình, thời tiết, vị trí | Không |
| 9 | `resolution_and_aftermath` | Kết quả + hậu quả | Không |
| 10 | `arguments_and_legacy` | Tranh luận lịch sử | Không |

### 🟡 Overlap — cần gộp/tái cấu trúc
| # | Section | Vấn đề | Đề xuất |
|---|---------|--------|---------|
| 6 | `technology_and_weapons` | Mô tả chung vũ khí | **Giữ** — mô tả mechanics |
| 7 | `weapon_asymmetry` | So sánh 2 bên | **Giữ** — bổ sung cho #6 |
| 8 | `breakthrough_weapons` | Vũ khí đột phá | **Giữ** — riêng biệt đủ rõ |
| 11 | `narrative_moments` | Cảnh physical/sensory | ⚠️ **Overlap** với `soldier_experience` mới → **GỘP** |
| 12 | `emotional_drivers` | Tâm lý chiến trường | ⚠️ **Overlap** với `soldier_experience` mới → **GỘP** |
| 13 | `climactic_turning_points` | Bước ngoặt quyết định | ⚠️ Nhẹ overlap với `battle_phases.turning_point` → **Giữ** vì focus khác (close calls) |
| 14 | `chronological_campaign_phases` | Multi-day campaign | **Giữ** (optional cho campaigns) |
| 15 | `must_include` | Facts too powerful to omit | ⚠️ **Overlap** với `texture_and_hooks` → **GỘP** |
| 16 | `texture_and_hooks` | Quotes, ironies, human moments | ⚠️ **GỘP** `must_include` vào đây |

---

## Proposed Changes

### GỘP (reduce overlap, tăng clarity)

#### 1. `narrative_moments` + `emotional_drivers` → `battlefield_experience`
```json
"battlefield_experience": [
  {
    "phase": "...",
    "scene": "sensory scene description",
    "physical_details": ["sight", "sound", "smell"],
    "scale_indicator": "numbers/distances",
    "emotional_state": "fear/revenge/desperation/...",
    "emotional_cause": "what created this emotion",
    "behavioral_impact": "how it changed behavior",
    "source": "ai_knowledge"
  }
]
```
**Why:** Cảnh vật lý và cảm xúc BẤT KHẢ PHÂN LY — cùng 1 khoảnh khắc có cả 2. Tách → AI lặp lại cùng scene 2 lần.

#### 2. `must_include` → gộp vào `texture_and_hooks`
```json
"texture_and_hooks": {
  "memorable_quotes": [...],
  "dramatic_ironies": [...],
  "human_moments": [...],
  "scale_comparisons": [...],
  "must_include_details": ["fact too powerful to omit 1", "..."]
}
```
**Why:** `must_include` chỉ là catch-all cho facts thuộc `texture_and_hooks`. Gộp giảm confusion.

### THÊM MỚI (5 sections)

#### 3. `elite_units` (NEW)
```json
"elite_units": [
  {
    "unit_name": "Janissaries / Old Guard / Sacred Band...",
    "faction": "...",
    "size": "number of troops",
    "selection_and_training": "how recruited, how trained",
    "special_equipment": "unique weapons/armor/mounts",
    "reputation": "feared/legendary — why?",
    "role_in_this_battle": "what they did specifically",
    "decisive_moment": "their key action/charge/stand",
    "fate": "survived/wiped out/captured",
    "source": "ai_knowledge"
  }
]
```

#### 4. `logistics_and_supply` (NEW)
```json
"logistics_and_supply": {
  "supply_lines": "how each side supplied troops",
  "food_and_water": "rations, scarcity, impact on morale/performance",
  "ammunition_reserves": "how much, when did they run low",
  "medical_support": "battlefield medicine, evacuation, survival rates",
  "march_distances": "how far troops marched before battle, exhaustion factor",
  "supply_failures": "critical shortages that changed the battle",
  "source": "ai_knowledge"
}
```

#### 5. `intelligence_and_deception` (NEW — optional, empty [] if none)
```json
"intelligence_and_deception": [
  {
    "operation": "name or description",
    "side": "who performed it",
    "method": "scouts/spies/intercepted messages/feint maneuver/double agent",
    "what_was_learned_or_hidden": "...",
    "battle_impact": "how it changed the outcome",
    "source": "ai_knowledge"
  }
]
```

#### 6. `civilian_impact` (NEW — optional, empty {} if none)
```json
"civilian_impact": {
  "population_before": "city/region population before battle",
  "destruction": "what was destroyed — cities, infrastructure, farmland",
  "civilian_casualties": "estimated numbers",
  "displacement": "refugees, forced migration",
  "post_battle_famine_or_plague": "secondary effects on civilian population",
  "source": "ai_knowledge"
}
```

#### 7. `force_composition` (NEW — replaces vague `forces` in battle_phases)
```json
"force_composition": {
  "side_a": {
    "faction_name": "...",
    "total_strength": "number",
    "breakdown": {
      "infantry": "number + type (heavy/light/militia)",
      "cavalry": "number + type (heavy/light/horse archers)",
      "artillery": "number of guns + caliber",
      "naval": "number of ships + type (if applicable)",
      "special_units": "reference to elite_units[]"
    }
  },
  "side_b": { "..." },
  "numerical_ratio": "e.g. 3:1 advantage Side A",
  "quality_assessment": "which side was better trained/equipped despite numbers",
  "source": "ai_knowledge"
}
```

---

## Downstream Impact

| File | Impact | Action |
|------|--------|--------|
| `system_research_blueprint_battle.txt` | Main target — add/merge sections | ✅ Update |
| `system_audit_battle_blueprint.txt` | `merge_into_existing` fields | ✅ Update (`narrative_moments` → `battlefield_experience`, add new sections) |
| `system_crossref_battle_blueprint.txt` | `merge_into_existing` fields | ✅ Update (same) |
| `narrative_phân_tích_trận_đánh_v2.json` | `excerpt_fields` | ✅ Add new field names |
| `system_narrative_phase_plan_battle.txt` | References blueprint sections | ⚠️ Check — may need update |
| `rewriter.py` | No hardcoded field names | ✅ Safe |
| `script_creation_tab.py` | No field references | ✅ Safe |

## Summary: TRƯỚC → SAU

| Before (17 sections) | After (18 sections) |
|---|---|
| `narrative_moments` | → **gộp** vào `battlefield_experience` |
| `emotional_drivers` | → **gộp** vào `battlefield_experience` |
| `must_include` | → **gộp** vào `texture_and_hooks.must_include_details` |
| *(không có)* | + `elite_units` |
| *(không có)* | + `logistics_and_supply` |
| *(không có)* | + `intelligence_and_deception` |
| *(không có)* | + `civilian_impact` |
| *(không có)* | + `force_composition` |

**Net: 17 → 18** (gộp 3, thêm 5, bớt 1 standalone)
