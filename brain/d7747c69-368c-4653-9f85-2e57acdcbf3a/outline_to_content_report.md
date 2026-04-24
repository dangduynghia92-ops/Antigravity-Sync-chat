# Firearms V2: Outline → Chapter Content — Chi tiết luồng dữ liệu

## Tổng quan: 3 loại body chapter

| Loại | Framework | Mỗi chapter viết về | data_focus chọn |
|------|-----------|---------------------|-----------------|
| `body` | Ranking, Catalog | 1 sản phẩm | Field groups liên quan đến ranking criterion |
| `topic_block` | Deep Dive | 1 khía cạnh (facet) của 1 SP | 1-2 field groups (e.g., `internal_ballistics`) |
| `criterion` | Head-to-Head | 1 tiêu chí so sánh 2 SP | 1 field group áp dụng cho CẢ 2 SP |

## Luồng dữ liệu 4 bước

```mermaid
graph LR
    A[Blueprint đầy đủ<br/>30+ fields/product] --> B[Outline AI<br/>chọn data_focus per chapter]
    B --> C["_extract_firearms_v2_blueprint()<br/>filter theo data_focus"]
    C --> D[Writer AI<br/>nhận CHỈ data cần thiết]
```

---

## VÍ DỤ 1: Deep Dive — `.45 ACP` (topic_block)

> Framework: **Deep Dive** | Angle: **myth_busting** | Sản phẩm: `.45 ACP`

### Bước 1: Blueprint (trích — chỉ internal_ballistics & recoil_profile)

```json
{
  "product_evaluation": [{
    "product_name": ".45 ACP",
    "product_type": "ammunition",
    "key_specs": {"caliber": ".45 ACP", "bullet_weight": "230 gr", "velocity": "830 fps"},
    "internal_ballistics": {
      "chamber_pressure_psi": "21,000 PSI",
      "muzzle_velocity_fps": "830 fps",
      "muzzle_energy_ftlb": "356 ft-lbs",
      "test_barrel_length": "5 inches"
    },
    "recoil_profile": {
      "recoil_impulse_ftlb": "7.5 ft-lbs",
      "felt_recoil_description": "Smooth, straight-back push",
      "physical_translation": "More of a shove than a snap"
    },
    "myths_misconceptions": [
      {"myth": ".45 has unmanageable recoil", "reality": "21,000 PSI = smooth push, not snap", "source": "transcript"},
      {"myth": ".45 is too slow for self-defense", "reality": "830fps × 230gr = 356 ft-lbs — plenty for FBI gel protocol", "source": "transcript"}
    ]
  }]
}
```

### Bước 2: Outline AI output — chapter 3 (topic_block)

```json
{
  "chapter_number": 3,
  "chapter_type": "topic_block",
  "title": "The Pressure Equation",
  "products_covered": [".45 ACP"],
  "data_focus": ["internal_ballistics", "recoil_profile"],
  "primary_criterion": "Chamber pressure and its real-world implications",
  "depth_focus": "21,000 PSI — barely half what 9mm generates",
  "unique_selling_point": null,
  "ranking_reason": null,
  "target_user": null,
  "cons_to_mention": "Lower pressure = lower velocity = more bullet drop at distance",
  "techniques_to_use": ["physical_translation", "myth_attack"],
  "tone_category": "nerd_out",
  "emotional_beat": "Fascination — 'I never thought about pressure that way'",
  "ends_with": "Transition: 'Low pressure affects more than just feel — it reshapes terminal performance. And that's where .45 ACP fights back.'",
  "debate_seed": "Is lower pressure actually an ADVANTAGE?"
}
```

### Bước 3: Code filter — `_extract_firearms_v2_blueprint()` output

Dựa vào `data_focus: ["internal_ballistics", "recoil_profile"]` + `products_covered: [".45 ACP"]`, code filter ra:

```json
{
  "core_topic": "Deep dive into .45 ACP — debunking myths with data",
  "thesis_angle": "Everything you think about .45 ACP is based on outdated data",
  "product_evaluation": [{
    "product_name": ".45 ACP",
    "product_type": "ammunition",
    "category": "Pistol Caliber",
    "key_specs": {"caliber": ".45 ACP", "bullet_weight": "230 gr", "velocity": "830 fps"},
    "author_rhetoric": [
      {"type": "physical_translation", "content": "solid straight-back push vs snappy kick"}
    ],
    "source_units": "imperial",
    "internal_ballistics": {
      "chamber_pressure_psi": "21,000 PSI",
      "muzzle_velocity_fps": "830 fps",
      "muzzle_energy_ftlb": "356 ft-lbs",
      "test_barrel_length": "5 inches"
    },
    "recoil_profile": {
      "recoil_impulse_ftlb": "7.5 ft-lbs",
      "felt_recoil_description": "Smooth, straight-back push",
      "physical_translation": "More of a shove than a snap"
    }
  }]
}
```

> **Lưu ý:** `myths_misconceptions`, `terminal_performance`, `cost_economics`, `origin_history`, v.v. đều bị CẮT — writer không thấy, không viết.

### Bước 4: Writer AI — chapter content (kỳ vọng)

Writer nhận template variables từ outline + filtered blueprint, viết theo pattern **topic_block**:

```
── Elements bắt buộc ──

1. TOPIC ANCHOR (1 câu sắc bén):
   "Most people call .45 ACP a 'low-pressure pushover.' The data says that's
    exactly why it outlasts everything else in your gun."

2. DATA FOUNDATION (1-3 con số + đơn vị):
   "21,000 PSI. That's the SAAMI maximum chamber pressure for .45 ACP.
    For context, 9mm operates at 35,000 PSI — 67% higher."

3. PHYSICAL TRANSLATION (BẮT BUỘC cho MỌI số):
   "21,000 PSI means less stress on every component every time you pull
    the trigger. Your barrel lasts longer. Your frame flexes less.
    And in your hand? Instead of a sharp snap that yanks your muzzle up,
    you feel a smooth, straight-back shove — 7.5 ft-lbs of recoil
    impulse spread across a wider time window."

4. PROOF LAYER (scenario from specs):
   "Picture a home defense scenario at 2 AM. Three rounds, rapid fire.
    With 9mm at 35,000 PSI, each shot generates a sharper, faster recoil
    pulse that pulls your muzzle higher between shots. With .45 at 21,000 PSI,
    each 7.5 ft-lb push comes and goes like a wave — your sights recover
    faster than your heart rate."

5. PRACTICAL IMPLICATION:
   "If you're a shooter who prioritizes split times over round count,
    this pressure difference is your secret weapon. But there's a trade:
    less pressure means 830 fps — and at 25+ yards, that 230-grain
    bowling ball starts dropping faster than 9mm. Close range? .45 owns it.
    Long range? Physics wins."

── Kết chapter (ends_with from outline): ──
   "Low pressure affects more than just feel — it reshapes what happens
    when that bullet hits soft tissue. And that's where .45 ACP fights back."
```

---

## VÍ DỤ 2: Head-to-Head — `.45 ACP vs 9mm` (criterion chapter)

> Framework: **Head-to-Head** | Angle: **combat_self_defense** | Round: Recoil

### Bước 2: Outline AI output — chapter 4 (criterion)

```json
{
  "chapter_number": 4,
  "chapter_type": "criterion",
  "title": "The Recoil Truth",
  "products_covered": [".45 ACP", "9mm Parabellum"],
  "data_focus": ["recoil_profile"],
  "primary_criterion": "Recoil management for rapid follow-up shots",
  "depth_focus": "7.5 vs 5.5 ft-lbs — 36% more impulse, but different physics",
  "unique_selling_point": null,
  "ranking_reason": null,
  "target_user": "Self-defense shooters who need sub-0.3s split times",
  "cons_to_mention": ".45 gives slower split times for most shooters",
  "techniques_to_use": ["physical_translation", "scenario_painting"],
  "tone_category": "nerd_out",
  "emotional_beat": "Understanding — recoil isn't just about force, it's about direction",
  "ends_with": "Round winner declared. Transition: 'But recoil is irrelevant if the bullet can't stop the threat. Terminal performance — round 3.'",
  "debate_seed": "Does manageable recoil matter more than stopping power?"
}
```

### Bước 3: Filtered blueprint (cho CẢ 2 sản phẩm)

```json
{
  "product_evaluation": [
    {
      "product_name": ".45 ACP",
      "product_type": "ammunition",
      "key_specs": {"caliber": ".45", "bullet_weight": "230 gr"},
      "recoil_profile": {
        "recoil_impulse_ftlb": "7.5 ft-lbs",
        "felt_recoil_description": "Smooth, straight-back push",
        "physical_translation": "More of a shove than a snap"
      }
    },
    {
      "product_name": "9mm Parabellum",
      "product_type": "ammunition",
      "key_specs": {"caliber": "9mm", "bullet_weight": "124 gr"},
      "recoil_profile": {
        "recoil_impulse_ftlb": "5.5 ft-lbs",
        "felt_recoil_description": "Sharp, snappy impulse",
        "physical_translation": "Fast upward snap that pulls muzzle"
      }
    }
  ]
}
```

### Bước 4: Writer output (kỳ vọng) — criterion pattern

```
── Elements bắt buộc ──

1. CRITERION DECLARATION:
   "Recoil. Not because it's scary — because it dictates how fast
    your sights come back on target. In a self-defense scenario,
    split time IS survival time."

2. PRODUCT A DATA (.45 ACP):
   "7.5 ft-lbs of recoil impulse. But here's what that number hides:
    .45 ACP operates at 21,000 PSI, pushing a 230-grain bullet at
    barely 830 fps. The result is a long, smooth push — like someone
    pressing a palm against your chest. Your muzzle rises, but it
    rises SLOWLY."

3. PRODUCT B DATA (9mm):
   "5.5 ft-lbs. 27% less raw impulse. But 9mm generates that impulse
    at 35,000 PSI, launching a 124-grain bullet at 1,150 fps.
    The physics: lighter bullet + higher pressure = a sharp, fast SNAP
    that yanks the muzzle upward before you can react."

4. THE GAP:
   "The gap is 2 ft-lbs — 36% more impulse for .45. But impulse alone
    is misleading. What matters is IMPULSE DURATION. .45's push lasts
    longer, giving your hands time to absorb. 9mm's snap comes and goes
    before your grip muscles can react. Translation: .45 feels heavier
    but more controllable per shot. 9mm feels lighter but snappier —
    and for rapid strings, that snap compounds."

5. ROUND WINNER:
   "9mm takes this round. Not because 5.5 ft-lbs is magic — but because
    competitive and defensive shooters consistently clock 0.18-0.22s splits
    with 9mm vs 0.25-0.30s with .45. For a 3-shot string, that's 0.24
    seconds faster back on target. In a fight, 0.24 seconds is an eternity."

── Transition (ends_with from outline): ──
   "But recoil is irrelevant if the bullet can't stop the threat.
    Terminal performance — round 3."
```

---

## So sánh 3 chapter types

| Yếu tố | `body` (Ranking/Catalog) | `topic_block` (Deep Dive) | `criterion` (H2H) |
|---------|--------------------------|---------------------------|-------------------|
| **Số SP** | 1 | 1 | 2 |
| **Cấu trúc** | Intro → Criterion → Support → Weakness → Verdict | Anchor → Data → Physical → Proof → Implication | Declaration → A data → B data → Gap → Winner |
| **data_focus** | Fields theo ranking criterion + angle | 1-2 field groups = 1 topic | 1 field group áp dụng cho 2 SP |
| **Bắt buộc** | 1 weakness/con | Physical Translation mọi số | Round winner dứt khoát |
| **Kết thúc** | Tease next product | Practical implication → next topic | Round verdict → next criterion |

## Physical Translation — Quy tắc vàng

Mọi con số ĐỀU phải được chuyển thành cảm giác vật lý:

| Con số thô | ❌ Sai | ✅ Đúng |
|----------|--------|---------|
| 21,000 PSI | "Low pressure" | "Barely half what 9mm generates — less stress on every component, every trigger pull" |
| 7.5 ft-lbs | "Moderate recoil" | "A smooth palm-press against your chest — your muzzle rises slowly, not snaps" |
| 830 fps | "Subsonic velocity" | "Slow enough to suppress without cracking the sound barrier — but at 25 yards, gravity starts winning" |
| $0.45/round | "Expensive ammo" | "Every magazine costs $6.30 to fill — 3x what 9mm shooters pay for the same 14 rounds" |

## Tóm tắt cơ chế chọn nội dung

```
angle_preset.required_fields → outline chọn data_focus →
  code filter blueprint → writer CHỈ thấy data cần thiết →
    viết theo chapter_type pattern → physical translation mọi số
```

**Outline quyết định "viết gì". Writer quyết định "viết như thế nào".**
