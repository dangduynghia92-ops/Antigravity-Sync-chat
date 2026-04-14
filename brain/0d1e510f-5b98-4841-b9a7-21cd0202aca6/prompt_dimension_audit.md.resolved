# Audit: Các Khía Cạnh Narrative Đã Cover vs Thiếu

## Tổng quan

Đánh giá 3 file prompt chính:
- [system_research_blueprint_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_research_blueprint_pirate.txt) — trích xuất data
- [system_narrative_write_pirate.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pirate.txt) — viết (Ship)
- [system_narrative_write_pirate_haven.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_narrative_write_pirate_haven.txt) — viết (Haven)

---

## ✅ ĐÃ CÓ (tốt)

| Khía cạnh | Blueprint (Research) | Writer Prompt | Ghi chú |
|-----------|---------------------|---------------|---------|
| **Trận chiến** (battles) | ✅ `climactic_events` — blow-by-blow, tactics | ✅ HEIST_SEQUENCE structure | Rất chi tiết — before/during/after |
| **Kinh tế** (economy) | ✅ `economic_data` — USD conversion, loot, trade | ✅ MONEY ANGLE rule | Mạnh nhất trong toàn bộ pipeline |
| **Y tế / bệnh tật** | ✅ `dark_reality.medical_practices`, `specific_diseases` | ✅ PIRATE MEDICINE, SURVIVAL_LENS | Rất chi tiết — step-by-step |
| **Xã hội** (governance) | ✅ `anatomy_specs.governance_system` (location only) | ✅ MECHANICAL_AUTOPSY | Tốt cho Location; Ship ít hơn |
| **Tâm lý nhân vật** | ⚠️ `key_figures.psychological_profile` (1 dòng) | ⚠️ POWER_PLAY structure mentions "psychology" | Có nhưng **sơ sài** |
| **Bối cảnh chính trị** | ✅ `era_context` — world_state, power_vacuum, naval_powers | ✅ Bối Cảnh phase | Tốt nhưng thiếu chiều sâu |
| **Myth vs Reality** | ✅ `myths_vs_reality` — belief/evidence/why | ✅ WOVEN TECHNIQUE section | Rất tốt |
| **Sensory** (giác quan) | ⚠️ `narrative_moments.physical_details` | ⚠️ Writer yêu cầu "sensory" nhưng mơ hồ | Có framework nhưng thiếu hướng dẫn cụ thể |

---

## ❌ THIẾU HOẶC YẾU

### 1. 🌊 Thiên Nhiên / Môi Trường (THIẾU HOÀN TOÀN)

**Blueprint**: Không có section nào yêu cầu trích xuất:
- Khí hậu, thời tiết, mùa bão Caribbean
- Địa lý cụ thể — vịnh, rạn san hô, dòng hải lưu, gió mùa
- Hệ sinh thái — rừng ngập mặn, động vật, thực vật
- Tác động thiên nhiên lên cuộc sống (bão phá hủy, dịch bệnh theo mùa)

**Writer**: Chỉ có 1 dòng gián tiếp: "weather" trong `sub_key_data` texture — không hề hướng dẫn MÔ TẢ thiên nhiên như thế nào.

> [!CAUTION]
> Đây là lỗ hổng lớn nhất. Thiên nhiên Caribbean là "nhân vật thứ ba" — bão, nắng, biển, muỗi, sốt rét. Thiếu nó = script khô khan như Wikipedia.

### 2. 🏚️ Cuộc Sống Hàng Ngày (YẾU)

**Blueprint**: `dark_reality.daily_horrors` cover phần "kinh hoàng" nhưng THIẾU:
- Sinh hoạt thường ngày — ăn gì, ngủ đâu, giải trí gì, mối quan hệ
- Cấu trúc ngày — ca trực, phân công, thời gian rảnh
- Đời sống xã hội trên tàu/đảo — nhậu, đánh bạc, hát, kể chuyện
- Ẩm thực — thực phẩm cụ thể, thiếu nước ngọt, rượu rum thay nước
- Trang phục — mặc gì, vũ khí cá nhân, trang sức cướp được

**Writer**: SURVIVAL_LENS có "daily reality (escalating)" nhưng chỉ focus vào khía cạnh "kinh hoàng" — không có hướng dẫn viết cuộc sống BÌNH THƯỜNG (texture cho các chapter khác).

### 3. 🧠 Tâm Lý Chiều Sâu (SƠ SÀI)

**Blueprint**: `psychological_profile` chỉ là 1 field text trong `key_figures` — không cấu trúc.

**Thiếu**:
- Motivation matrix: revenge? freedom? greed? ideology?
- Moral evolution: nhân vật thay đổi thế nào qua thời gian?
- Relationship dynamics: ai trung thành, ai phản bội, vì sao?
- Fear/vulnerability: sợ gì, điểm yếu gì?
- Decision moments: 2-3 quyết định quan trọng nhất VÀ logic đằng sau

### 4. 🏛️ Chính Trị Sâu (CÓ NHƯNG HỜI HỢT)

**Blueprint**: `era_context` cover bối cảnh nhưng THIẾU:
- Chính trị NỘI BỘ — phe phái trên tàu/đảo, tranh chấp quyền lực
- Quan hệ với thuộc địa — ngoại giao ngầm, thoả thuận, phản bội
- Vai trò của privateering — ranh giới cướp biển hợp pháp vs bất hợp pháp
- Tác động lên chính sách đế quốc — piracy thay đổi luật biển thế nào?

### 5. 🌬️ Bầu Không Khí / Atmosphere (CÓ NHƯNG MƠ HỒ)

**Blueprint**: `narrative_moments` yêu cầu "physical_details" nhưng không hướng dẫn CỤ THỂ:
- Âm thanh đặc trưng — sóng, gió trong buồm, kẽo kẹt gỗ, tiếng chuông
- Mùi — muối biển, gỗ mục, thuốc súng, rum, cơ thể người
- Ánh sáng — bình minh trên biển, đèn dầu trong khoang, sương mù
- Cảm giác — lắc lư tàu, nắng cháy da, gió muối, ẩm ướt

---

## 📋 ĐỀ XUẤT BỔ SUNG

### A. Thêm vào Blueprint Research Prompt (trích xuất data)

```
16. **ENVIRONMENT & NATURE**: The physical world:
    - climate: Typical weather, hurricane season, temperature, humidity
    - geography: Specific bays, reefs, currents, winds, strategic features
    - ecosystem: Vegetation, animals, insects, disease vectors (mosquitoes)
    - natural_events: Storms, earthquakes, droughts that affected the subject
    - nature_as_character: How did the environment HELP or HINDER pirates?

17. **DAILY LIFE**: Life beyond battles and horror:
    - daily_routine: Watches, duties, meals, leisure time
    - food_and_drink: Specific foods (hardtack, salted meat, rum rations), water supply
    - entertainment: Gambling, music, storytelling, competitions
    - clothing_and_gear: What they wore, personal weapons, stolen luxury items
    - social_structure: Hierarchy, friendships, rivalry, democratic practices
    - relationships: Crew bonds, prostitution, rare families

18. **POLITICAL DEPTH**: Internal and external politics:
    - internal_politics: Factions, power struggles, mutiny causes
    - external_diplomacy: Deals with governors, letters of marque, betrayals
    - privateering_line: When were they "legal"? When did status change?
    - policy_impact: How piracy changed maritime law, insurance, naval strategy

19. **ATMOSPHERE PALETTE**: Specific sensory signatures:
    - sounds: Ship creaking, waves, cannon thunder, crew shanties, silence
    - smells: Salt, gunpowder, rot, rum, tropical flowers, unwashed bodies
    - light: Dawn at sea, candlelight below deck, tropical sunsets, storm darkness
    - tactile: Ship rocking, heat, wind, wet wood, rope burns
```

### B. Thêm vào Writer Prompt (hướng dẫn viết)

Thêm section mới vào cả 2 writer prompt (ship + haven):

```
═══════════════════════════════════════
ATMOSPHERE LAYER (ENVIRONMENT AS CHARACTER)
═══════════════════════════════════════

The Caribbean is not a backdrop. It is the THIRD CHARACTER.

EVERY chapter must have at least ONE environmental anchor:
- Weather/sea state that AFFECTS the action (not decoration)
- A sensory detail that places the audience PHYSICALLY in the scene

✓ "Gió mùa đông bắc thổi 25 hải lý — lợi thế tốc độ nghiêng hẳn về tàu sloop nhẹ.
   Queen Anne's Revenge, nặng 300 tấn, phải mất 40 phút mới quay mũi."
   (→ weather drives tactical decision)

✓ "Mùi thuốc súng trộn lẫn mùi máu khô trong gió biển. Thuyền trưởng Hornigold
   đứng trên cầu tàu Nassau, đếm xác — ba cái sáng nay."
   (→ smell anchors the location)

✗ "Biển xanh ngắt và trời trong vắt." (→ decoration, no function)
✗ "Gió thổi." (→ vague, no detail)

DAILY LIFE TEXTURE (1-2 sentences per chapter):
When NOT in action, show what daily life FEELS like:
- What did they eat? (hardtack crawling with weevils, rum instead of clean water)
- How did they sleep? (hammocks 18 inches apart, rats running over legs)
- What did they do for fun? (dice, music, storytelling, target practice)
Use as BRIDGE material between scenes — not as standalone paragraphs.
```
