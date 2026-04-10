# So sánh Prompt Generic vs Battle

## Triết lý thiết kế

| | **Generic** (`system_extract_blueprint.txt`) | **Battle** (`system_extract_blueprint_battle.txt`) |
|---|---|---|
| Role | "content extraction specialist" | "military history DATA EXTRACTION specialist" |
| Mục tiêu | "WHAT the script is about" | "WHAT the script SAYS" |
| Anti-copy | "Do NOT copy complete sentences" | + "Do NOT preserve narrative sequence/structure" |
| Missing data | Không đề cập | Rule #5: "If not in script → OMIT, do NOT invent" |
| Coverage | "enough to create a NEW script" | "OVER-EXTRACT from script, comprehensive > concise" |

---

## So sánh Sections

| Section | **Generic** | **Battle** | Khác biệt |
|---|---|---|---|
| `core_topic` | ✅ | ✅ | Battle yêu cầu "who vs whom, when, where, why" |
| `key_facts` | ✅ | ✅ | Tương tự |
| `key_events` | ✅ structured (event, actors, outcome, significance) | ❌ Thay bằng `battle_phases` | Battle tách theo front/phase, không chỉ "events" |
| `key_characters` | ✅ (name, role, personality, decisions, fate) | ❌ Thay bằng `commanders` | Battle gắn commander với front + faction |
| `arguments` | ✅ (claim, evidence, counter) | ✅ `arguments_and_legacy` | Tương tự |
| `technical_details` | ✅ (element, mechanism, tactical_impact) | ✅ `technology_and_weapons` | Battle thêm strengths + weaknesses |
| `geography` | ✅ nhưng 1 string duy nhất | ✅ **structured dict** | Battle: terrain[], weather_events[], strategic_positions[], distances[] |
| `emotional_core` | ✅ 1 string | ✅ `emotional_drivers[]` | Battle: structured list với cause + manifestation |
| `narrative_moments` | ✅ (event, scene, vivid_details, scale_and_contrast) | ✅ (phase, scene, physical_details, scale_indicator) | Battle: gắn moment với battle phase |
| `must_include` | ✅ | ✅ | Tương tự |
| `product_evaluation` | ✅ (có schema) | ❌ **Bỏ hoàn toàn** | Không liên quan battle |
| `ranking_criteria` | ✅ | ❌ **Bỏ** | Product review field |
| `original_order` | ✅ | ❌ **Bỏ** | Product review field |
| `thesis_angle` | ✅ | ❌ **Bỏ** | Product review field |

---

## Sections MỚI chỉ có trong Battle

| Section | Mô tả | Tại sao cần |
|---|---|---|
| `battle_phases[]` | Tách trận đánh theo front/phase, bắt buộc cover TẤT CẢ | Generic chỉ có "key_events" → AI bỏ sót flanks |
| `political_context{}` | Factions, interests, rivalries, funding, catalyst | Generic chỉ gom vào `key_facts` → thiếu depth |
| `weapon_asymmetry[]` | So sánh trực tiếp vũ khí 2 bên | Generic chỉ list riêng → không so sánh |
| `emotional_drivers[]` | Structured: emotion + cause + manifestation | Generic chỉ 1 paragraph → không actionable |

---

## Ước tính Token & Cost

| | **Generic** | **Battle** |
|---|---|---|
| Prompt length | ~2,700 tokens | ~4,200 tokens |
| Output length | ~3,000–5,000 tokens | ~5,000–10,000 tokens |
| Tổng/call | ~6–8K tokens | ~9–14K tokens |
| Tăng cost | — | ~1.5–2× |

> [!NOTE]
> Battle prompt dài hơn ~55% và output dày hơn vì structured fields nhiều hơn. Đổi lại: coverage tốt hơn, ít cần retry, và writer prompt nhận được data đầy đủ hơn → giảm hallucination ở bước viết.
