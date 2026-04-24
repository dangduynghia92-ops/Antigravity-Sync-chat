# Blueprint Contamination Audit — Full Report

## What Gets Sent to Outline vs Writer

| Stage | Data Source |
|-------|-----------|
| **Outline AI** | `outline_blueprint` (deep copy of blueprint, after shuffle + strip) |
| **Writer AI** | Full `blueprint` + `outline` chapter data |

---

## TOP-LEVEL Fields

| Field | Content | Risk | Currently Stripped for Outline? | Recommendation |
|-------|---------|------|---------------------------------|----------------|
| `core_topic` | "Revisión y selección de las 10 mejores armas..." | 🟡 Low | ❌ No | ✅ OK — generic topic description |
| `thesis_angle` | "Durante 30 años, millones de estadounidenses condujeron sin estar preparados..." | 🔴 **HIGH** | ❌ **No** | ⚠️ **STRIP** — this is the original author's exact thesis. AI reproduces it |
| `original_order` | `["Savage Arms 42 Takedown", "Henry Big Boy", ...]` | 🔴 **HIGH** | ✅ Yes (line 5019) | ✅ Fixed |
| `ranking_criteria` | "Practicidad, confiabilidad, tamaño..." | 🔴 **HIGH** | ✅ Yes (line 5020) | ✅ Fixed |
| `key_claims` | Author's specific claims (NFA, velocity data) | 🔴 **HIGH** | ✅ Yes (line 5021) | ✅ Fixed |
| `benchmark` | Reference product comparison data | 🟡 Medium | ❌ No | 🟡 Keep — useful factual baseline |

---

## PER-PRODUCT Fields

| Field | Content Example | Risk | Stripped for Outline? | Recommendation |
|-------|----------------|------|-----------------------|----------------|
| `product_name` | "Savage Arms 42 Takedown" | ✅ Safe | N/A | ✅ Raw data |
| `product_type` | "firearm" | ✅ Safe | N/A | ✅ Raw data |
| `category` | "Arma combinada superpuesta" | ✅ Safe | N/A | ✅ Raw data |
| `key_specs` | caliber, capacity, etc | ✅ Safe | N/A | ✅ Raw data |
| `origin_history` | Factory facts, founding year | ✅ Safe | N/A | ✅ Raw data |
| `cost_economics` | Price, CPR, availability | ✅ Safe | N/A | ✅ Raw data |
| `materials_finish` | Receiver material, barrel, finish | ✅ Safe | N/A | ✅ Raw data |
| `ergonomics_handling` | Weight, length, grip | ✅ Safe | N/A | ✅ Raw data |
| `action_mechanism` | Action type, trigger, safety | ✅ Safe | N/A | ✅ Raw data |
| `accuracy_precision` | Range, grouping, twist rate | ✅ Safe | N/A | ✅ Raw data |
| `reliability_durability` | Known issues, round count | ✅ Safe | N/A | ✅ Raw data |
| `maintenance_logistics` | Field strip difficulty, parts | ✅ Safe | N/A | ✅ Raw data |
| `aftermarket_customization` | Rails, stocks, support level | ✅ Safe | N/A | ✅ Raw data |
| `platform_variants` | Variants list | ✅ Safe | N/A | ✅ Raw data |
| `source_units` | "imperial" | ✅ Safe | N/A | ✅ Metadata |
| **`author_rhetoric`** | **"Número uno indiscutible"** | 🔴 **HIGH** | ✅ **Yes (just added)** | ✅ Fixed |
| **`comparisons`** | Author's specific A-vs-B arguments | 🟠 **MEDIUM** | ✅ Yes (line 5011) | ✅ Fixed |
| **`source_parts`** | "PART 2" (reveals chapter order) | 🔴 **HIGH** | ✅ Yes (line 5013) | ✅ Fixed |
| `alternative_rhetoric` | AI-generated replacement metaphors | ✅ Safe | N/A | ✅ This IS the clean data |
| **`myths_misconceptions`** | Myth: "people scared of $1200 stolen" → Reality: "PSA $600 solves it" | 🟠 **MEDIUM** | ❌ **No** | ⚠️ **Keep but risky** — `reality` field contains author's argument |
| **`practical_use_case`** | `reason`: "Limitado a solo dos cartuchos en un escenario defensivo" | 🟡 **LOW-MED** | ❌ No | 🟡 `reason` sometimes subjective but mostly factual |

---

## Summary — What Still Leaks

### ⚠️ Needs Fix:
1. **`thesis_angle`** (top-level) — Author's exact thesis, NOT stripped for outline
2. **`myths_misconceptions`** — `reality` field has author's subjective arguments (PSA theft logic)

### ✅ Already Fixed:
- `original_order`, `ranking_criteria`, `key_claims` — stripped
- `author_rhetoric` — **just added** to strip list
- `comparisons`, `source_parts` — stripped

### 🟡 Low Risk (keep):
- `practical_use_case.reason` — mostly factual, occasionally subjective
- `benchmark` — factual reference data
- All raw spec fields — pure data
