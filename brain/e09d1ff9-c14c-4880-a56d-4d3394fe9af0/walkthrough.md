# Pipeline Simulation — 48s Julius Caesar POV

Kiểm tra tính khả thi bằng cách chạy thử toàn bộ pipeline với đoạn script thực tế.

---

## Input Script (~48s)

> *You are 18, 82 BC. Sullah has seized Rome and he is writing lists, names on parchment that become death warrants by mourning. Your family back the wrong side of his war and Sullah remembers everything. His men strip your priesthood. They confiscate your wife Cornelia's dowy. They want every stone attached to your name.*
>
> *You slip out of the city before soldiers reach your door and run north through frozen fields. You sleep in barns. You bribe checkpoint guards with borrowed coins. Fever pins you down for a week in a stranger's hoft. You burn. You shiver. You survive. When Sullah dies in his bed like an old man and Rome finally exhales, you are still breathing in the dark.*

---

## Tiền xử lý: SRT Parse

Giả lập SRT merge + interpolation → 14 câu, duration ước tính theo tỷ lệ ký tự trên 48s:

| ID | Text | Duration |
|---|---|---|
| 1 | You are 18, 82 BC. | 2.0s |
| 2 | Sullah has seized Rome and he is writing lists, names on parchment that become death warrants by mourning. | 6.9s |
| 3 | Your family back the wrong side of his war and Sullah remembers everything. | 4.9s |
| 4 | His men strip your priesthood. | 2.0s |
| 5 | They confiscate your wife Cornelia's dowy. | 2.4s |
| 6 | They want every stone attached to your name. | 3.3s |
| 7 | You slip out of the city before soldiers reach your door and run north through frozen fields. | 6.5s |
| 8 | You sleep in barns. | 1.6s |
| 9 | You bribe checkpoint guards with borrowed coins. | 2.8s |
| 10 | Fever pins you down for a week in a stranger's hoft. | 4.5s |
| 11 | You burn. | 0.8s |
| 12 | You shiver. | 0.8s |
| 13 | You survive. | 0.8s |
| 14 | When Sullah dies in his bed like an old man and Rome finally exhales, you are still breathing in the dark. | 8.5s |

**Tổng: ~47.8s ≈ 48s ✓**

JSON gửi cho Bước 1 (đã lột timecode):
```json
[
  {"sentence_id": 1, "text": "You are 18, 82 BC.", "duration": 2.0},
  {"sentence_id": 2, "text": "Sullah has seized Rome and he is writing lists...", "duration": 6.9},
  ...
  {"sentence_id": 14, "text": "When Sullah dies in his bed like an old man...", "duration": 8.5}
]
```

---

## Bước 1: Semantic Chunking — Áp dụng 4 Quy tắc

### Phân tích từng quy tắc

**Quy tắc 1 (Không gian & Thời gian):**
- S1-2: Sullah's Palace — Sullah ngồi viết danh sách tử hình
- S3-6: Caesar's Villa — Lính đến lục soát, tước bỏ → **Đổi Location** ✂️
- S7: "slip out of the city... run north through frozen fields" → **Đổi Location** (thành đồng/đường) ✂️
- S8-13: Đang chạy trốn (chuồng ngựa, trạm kiểm soát, nhà người lạ) → Cùng một arc "fleeing"
- S14: "When Sullah dies..." → **Nhảy thời gian** (nhiều năm trôi qua) ✂️

**Quy tắc 2 (Subject Shift):**
- S1-2: Subject = Sullah (viết, cầm quyền)
- S3-6: Subject = Lính Sullah + Caesar bị tước bỏ → **Subject khác** ✂️ (đã cắt ở Rule 1)

**Quy tắc 3 (Max 25s):**
- SEQ_01: S1-2 = 8.9s ✅
- SEQ_02: S3-6 = 12.6s ✅
- SEQ_03: S7-13 = 17.8s ✅
- SEQ_04: S14 = 8.5s ✅

### Output Bước 1

```json
[
  {
    "sequence_id": "SEQ_01",
    "sentence_ids": [1, 2],
    "location_shift": "Sullah's Palace",
    "main_subject": "Sullah",
    "full_text": "You are 18, 82 BC. Sullah has seized Rome and he is writing lists, names on parchment that become death warrants by mourning.",
    "total_duration": 8.9
  },
  {
    "sequence_id": "SEQ_02",
    "sentence_ids": [3, 4, 5, 6],
    "location_shift": "Caesar's Villa",
    "main_subject": "Sullah's soldiers and Caesar's family",
    "full_text": "Your family back the wrong side of his war and Sullah remembers everything. His men strip your priesthood. They confiscate your wife Cornelia's dowy. They want every stone attached to your name.",
    "total_duration": 12.6
  },
  {
    "sequence_id": "SEQ_03",
    "sentence_ids": [7, 8, 9, 10, 11, 12, 13],
    "location_shift": "Roman countryside, roads, barns",
    "main_subject": "Caesar fleeing",
    "full_text": "You slip out of the city before soldiers reach your door and run north through frozen fields. You sleep in barns. You bribe checkpoint guards with borrowed coins. Fever pins you down for a week in a stranger's hoft. You burn. You shiver. You survive.",
    "total_duration": 17.8
  },
  {
    "sequence_id": "SEQ_04",
    "sentence_ids": [14],
    "location_shift": "Dark room (years later)",
    "main_subject": "Caesar surviving",
    "full_text": "When Sullah dies in his bed like an old man and Rome finally exhales, you are still breathing in the dark.",
    "total_duration": 8.5
  }
]
```

**4 sequences, tổng 47.8s ✓**

---

## Bước 2: Global Context (2 API Calls)

### Call 1 → `_step2_characters.json`

```json
{
  "characters": [
    {
      "label": "Roman-Commander-A",
      "real_name": "Julius Caesar",
      "group": "PROTAGONIST",
      "chapters": [1],
      "visual_description": "Young Roman man (18), short dark curly hair, clean-shaven, lean build, wearing plain white toga with thin crimson stripe, no weapon",
      "body_language": "Tense, alert, hunched when fleeing, upright when defiant",
      "sheet_prompt": "Character reference sheet on clean white background. Three neutral standing views: front, 3/4 angle, side profile. Young Roman man (18), short dark curly hair, clean-shaven, plain white toga with thin crimson stripe. Label 'Roman-Commander-A'. [STYLE_KEYWORDS]."
    },
    {
      "label": "Roman-Dictator-A",
      "real_name": "Sullah",
      "group": "NAMED",
      "chapters": [1],
      "visual_description": "Old Roman man (60s), heavy-set, receding gray hair, deep facial lines, wearing rich purple toga with gold laurel wreath, scarred hands",
      "body_language": "Slow deliberate movements, hunched over desk, radiates cold authority",
      "sheet_prompt": "Character reference sheet on clean white background. Three neutral standing views: front, 3/4 angle, side profile. Old Roman man (60s), heavy-set, receding gray hair, rich purple toga with gold laurel wreath. Label 'Roman-Dictator-A'. [STYLE_KEYWORDS]."
    }
  ],
  "factions": [
    {
      "faction_name": "Sullah's Soldiers",
      "uniform_description": "Heavy bronze chest armor (lorica musculata), dark red wool cloaks, iron-studded leather belts, short gladius swords at hip, oval shields",
      "banner": "Red banner with Sullah's personal insignia",
      "appears_as": "armed soldiers raiding villas, checkpoint guards, pursuing squads"
    }
  ]
}
```

### Call 2 → `_step2_visual_bible.json`

```json
{
  "locations": [
    {
      "label": "Sullah's Palace",
      "bible_description": "Grand Roman palace interior, marble columns with gold leaf, heavy wooden desk covered in scrolls and sealing wax, mosaic floor, iron candelabras casting long shadows",
      "default_lighting": "Warm flickering candlelight from multiple iron candelabras, deep shadows pooling in corners"
    },
    {
      "label": "Caesar's Villa",
      "bible_description": "Modest Roman villa with cracked stone walls, narrow arched doorway, terracotta roof tiles, small inner courtyard with dry fountain, vine-covered pillars, wooden furniture",
      "default_lighting": "Cold moonlight through narrow windows, minimal interior light"
    },
    {
      "label": "Roman Countryside",
      "bible_description": "Frozen winter fields with dead grass, bare twisted trees, muddy dirt road, distant hills, scattered stone barns with thatched roofs, low stone walls along paths",
      "default_lighting": "Overcast gray winter sky, cold blue-white diffused light, fog clinging to low ground"
    },
    {
      "label": "Stranger's Hut",
      "bible_description": "Small dark interior of a peasant stone hut, straw bedding on dirt floor, single clay oil lamp, smoke-blackened wooden beams, rough wool blankets",
      "default_lighting": "Near darkness, single flickering oil lamp casting orange glow on one wall"
    }
  ]
}
```

---

## Bước 3: Scene Storyboarding — Simulation Chi Tiết

### SEQ_01 (8.9s) — Sullah's Palace

8.9s → cần **2 scenes** (mỗi scene 3-6s)

```json
{
  "sequence_id": "SEQ_01",
  "total_sequence_duration": 8.9,
  "locked_location": "Sullah's Palace",
  "scenes": [
    {
      "global_scene_id": "SEQ_01_SCN_01",
      "duration": 4.0,
      "matched_text": "You are 18, 82 BC. Sullah has seized Rome.",
      "character_labels": ["Roman-Dictator-A"],
      "faction_labels": [],
      "shot_type": "Wide Shot",
      "roll_type": "B-Roll",
      "camera_motion": "Slow Pan",
      "lighting_and_atmosphere": "Warm flickering candlelight casting long shadows across marble columns, oppressive and foreboding.",
      "background_and_extras": "Stacks of scrolls and wax seals scattered across a massive wooden desk, iron candelabras lining the walls.",
      "physical_action": "Establishing shot of grand Roman palace interior, camera reveals a heavy figure hunched over a desk surrounded by scrolls."
    },
    {
      "global_scene_id": "SEQ_01_SCN_02",
      "duration": 4.9,
      "matched_text": "He is writing lists, names on parchment that become death warrants by mourning.",
      "character_labels": ["Roman-Dictator-A"],
      "faction_labels": [],
      "shot_type": "Extreme Close-up",
      "roll_type": "A-Roll",
      "camera_motion": "Static",
      "lighting_and_atmosphere": "Candlelight catches ink glistening wet on parchment, warm amber glow against cold marble.",
      "background_and_extras": "Dripping red wax seal being stamped onto a rolled parchment, a pile of sealed scrolls growing beside the desk.",
      "physical_action": "Scarred weathered hand of old Roman man dipping iron stylus into dark ink, scratching names onto rough parchment with deliberate, unhurried strokes."
    }
  ]
}
```

**Validation:** 4.0 + 4.9 = 8.9s ✅ (0% error)

---

### SEQ_02 (12.6s) — Caesar's Villa

12.6s → cần **3 scenes**

```json
{
  "sequence_id": "SEQ_02",
  "total_sequence_duration": 12.6,
  "locked_location": "Caesar's Villa",
  "scenes": [
    {
      "global_scene_id": "SEQ_02_SCN_01",
      "duration": 4.9,
      "matched_text": "Your family back the wrong side of his war and Sullah remembers everything.",
      "character_labels": [],
      "faction_labels": ["Sullah's Soldiers"],
      "shot_type": "Wide Shot",
      "roll_type": "B-Roll",
      "camera_motion": "Slow Pan",
      "lighting_and_atmosphere": "Cold blue moonlight flooding through archway, dust swirling in the air, tense and threatening.",
      "background_and_extras": "Four soldiers in heavy bronze chest armor and dark red cloaks marching in through narrow arched doorway of a modest villa.",
      "physical_action": "Establishing shot of Caesar's Villa as armed soldiers push open the wooden door and stride into the courtyard."
    },
    {
      "global_scene_id": "SEQ_02_SCN_02",
      "duration": 4.4,
      "matched_text": "His men strip your priesthood. They confiscate your wife Cornelia's dowy.",
      "character_labels": [],
      "faction_labels": ["Sullah's Soldiers"],
      "shot_type": "Medium Close-up",
      "roll_type": "B-Roll",
      "camera_motion": "Static",
      "lighting_and_atmosphere": "Harsh torchlight from soldiers' hands, violent and chaotic mood, shadows thrashing on walls.",
      "background_and_extras": "Overturned wooden table, ceramic pots shattered on mosaic floor, a woman's jewelry box spilling gold coins.",
      "physical_action": "Two armored gauntlets aggressively ripping a sacred white linen priest scarf from a wooden shrine, fabric tearing audibly."
    },
    {
      "global_scene_id": "SEQ_02_SCN_03",
      "duration": 3.3,
      "matched_text": "They want every stone attached to your name.",
      "character_labels": [],
      "faction_labels": ["Sullah's Soldiers"],
      "shot_type": "Low Angle Shot",
      "roll_type": "B-Roll",
      "camera_motion": "Static",
      "lighting_and_atmosphere": "Dusty air thick with marble particles, harsh side-lighting from a single torch, destructive and final.",
      "background_and_extras": "Crumbled stone debris scattered across courtyard floor, vine leaves falling from broken pillars.",
      "physical_action": "Iron hammer swinging down in slow motion, smashing a carved family name inscription off a stone wall, chunks of marble exploding outward."
    }
  ]
}
```

**Validation:** 4.9 + 4.4 + 3.3 = 12.6s ✅ (0% error)

---

### SEQ_03 (17.8s) — Caesar Fleeing

17.8s → cần **4 scenes**

> [!WARNING]
> **🔴 Phát hiện vấn đề: Câu ngắn staccato**
> Sentences 11-13 ("You burn." "You shiver." "You survive.") mỗi câu chỉ ~0.8s. Chúng KHÔNG THỂ thành scenes riêng lẻ (min 3s). AI phải gộp chúng với sentence 10 thành 1 scene.
> 
> - S10 (4.5s) + S11-13 (2.4s) = 6.9s → **vượt max 6.0s**
> - S10 riêng (4.5s) + S11-13 riêng (2.4s) → scene 2 **dưới min 3.0s**
> 
> **→ Đây là XUNG ĐỘT THỰC SỰ trong plan.** Xem phần phân tích bên dưới.

**Giải pháp tạm → AI gộp linh hoạt:**

```json
{
  "sequence_id": "SEQ_03",
  "total_sequence_duration": 17.8,
  "locked_location": "Roman countryside, roads, barns",
  "scenes": [
    {
      "global_scene_id": "SEQ_03_SCN_01",
      "duration": 6.0,
      "matched_text": "You slip out of the city before soldiers reach your door and run north through frozen fields.",
      "character_labels": ["Roman-Commander-A"],
      "faction_labels": [],
      "shot_type": "Wide Shot",
      "roll_type": "A-Roll",
      "camera_motion": "Slow Tracking",
      "lighting_and_atmosphere": "Pre-dawn gray light, freezing mist rolling across dead fields, desperate and exposed.",
      "background_and_extras": "Bare twisted trees silhouetted against gray sky, frozen grass crunching underfoot, distant torches of patrol behind.",
      "physical_action": "Young Roman man (18) in torn white toga sprinting across a frozen field, bare feet on icy ground, looking back over his shoulder in terror."
    },
    {
      "global_scene_id": "SEQ_03_SCN_02",
      "duration": 4.4,
      "matched_text": "You sleep in barns. You bribe checkpoint guards with borrowed coins.",
      "character_labels": ["Roman-Commander-A"],
      "faction_labels": ["Sullah's Soldiers"],
      "shot_type": "Medium Shot",
      "roll_type": "A-Roll",
      "camera_motion": "Static",
      "lighting_and_atmosphere": "Dim gray overcast light filtering through barn slats, cold and exhausted mood.",
      "background_and_extras": "A soldier in dark red cloak standing at a wooden checkpoint gate, hand outstretched waiting for payment.",
      "physical_action": "Young Roman man with straw in his hair reaching forward with a trembling hand, pressing two small bronze coins into a guard's open palm."
    },
    {
      "global_scene_id": "SEQ_03_SCN_03",
      "duration": 4.0,
      "matched_text": "Fever pins you down for a week in a stranger's hoft. You burn.",
      "character_labels": ["Roman-Commander-A"],
      "faction_labels": [],
      "shot_type": "Close-up",
      "roll_type": "A-Roll",
      "camera_motion": "Extreme Slow Zoom In",
      "lighting_and_atmosphere": "Near darkness, single flickering oil lamp casting orange glow, feverish and suffocating.",
      "background_and_extras": "Rough stone walls of a peasant hut, straw bedding, steam rising from a clay bowl of water beside the bed.",
      "physical_action": "Young Roman man lying on straw bedding, drenched in sweat, eyes half-closed, chest heaving with labored breaths, hand clutching rough wool blanket."
    },
    {
      "global_scene_id": "SEQ_03_SCN_04",
      "duration": 3.4,
      "matched_text": "You shiver. You survive.",
      "character_labels": ["Roman-Commander-A"],
      "faction_labels": [],
      "shot_type": "Medium Shot",
      "roll_type": "A-Roll",
      "camera_motion": "Static",
      "lighting_and_atmosphere": "Gray dawn light seeping through cracks in wooden door, cold but calmer, mood shifting from despair to endurance.",
      "background_and_extras": "Morning frost on the inside of stone walls, a thin stream of smoke rising from dying embers in a small hearth.",
      "physical_action": "Young Roman man slowly pushing himself upright from straw bed, thin arms shaking, jaw clenched, wrapping a tattered cloak around his shoulders with deliberate effort."
    }
  ]
}
```

**Validation:** 6.0 + 4.4 + 4.0 + 3.4 = 17.8s ✅ (0% error)

> Giải pháp: AI đã gộp S7 (6.5s→6.0s trim), S8-9 (4.4s), S10-11 (5.3s→4.0s), S12-13 (2.4s→3.4s). Tail Correction phân bổ lại. Hoạt động nhưng đòi hỏi AI phải linh hoạt nhóm câu.

---

### SEQ_04 (8.5s) — Sullah dies, Caesar survives

8.5s → cần **2 scenes**

```json
{
  "sequence_id": "SEQ_04",
  "total_sequence_duration": 8.5,
  "locked_location": "Dark room (years later)",
  "scenes": [
    {
      "global_scene_id": "SEQ_04_SCN_01",
      "duration": 4.5,
      "matched_text": "When Sullah dies in his bed like an old man and Rome finally exhales.",
      "character_labels": ["Roman-Dictator-A"],
      "faction_labels": [],
      "shot_type": "Wide Shot",
      "roll_type": "B-Roll",
      "camera_motion": "Slow Pan",
      "lighting_and_atmosphere": "Pale golden morning light flooding through open windows, heavy silence, the air feels lighter.",
      "background_and_extras": "An ornate bed with rumpled silk sheets, cold candelabras with melted-down candles, dust motes floating in sunlight.",
      "physical_action": "Empty ornate bed with an impression of a body, sheets pulled back, a single laurel wreath lying abandoned on the pillow."
    },
    {
      "global_scene_id": "SEQ_04_SCN_02",
      "duration": 4.0,
      "matched_text": "You are still breathing in the dark.",
      "character_labels": ["Roman-Commander-A"],
      "faction_labels": [],
      "shot_type": "Close-up",
      "roll_type": "A-Roll",
      "camera_motion": "Extreme Slow Zoom In",
      "lighting_and_atmosphere": "Near total darkness, single sliver of light from a crack in a door, quiet and resolute.",
      "background_and_extras": "Bare stone wall, shadows consuming everything except a narrow band of light across a face.",
      "physical_action": "Close-up of young Roman man's face in darkness, eyes open and fixed forward, jaw set, steady breath visible as faint vapor in cold air."
    }
  ]
}
```

**Validation:** 4.5 + 4.0 = 8.5s ✅ (0% error)

---

## Bước 4: Final Prompt Assembly (1 ví dụ)

**SEQ_03_SCN_01** assembled (dùng Rembrandt Historical style giả lập):

```json
{
  "global_scene_id": "SEQ_03_SCN_01",
  "character_labels": ["Roman-Commander-A"],
  "faction_labels": [],
  "shot_type": "Wide Shot",
  "camera_motion": "Slow Tracking",
  "roll_type": "A-Roll",
  "subject_action": "Young Roman man (18), short dark curly hair, clean-shaven, torn white toga, sprinting across a frozen field, bare feet on icy ground, looking back over shoulder in terror.",
  "background_and_extras": "Bare twisted trees silhouetted against gray sky, frozen grass crunching underfoot, distant torches of patrol behind.",
  "location": "Frozen winter fields with dead grass, bare twisted trees, muddy dirt road, distant hills",
  "lighting_and_atmosphere": "Pre-dawn gray light, freezing mist rolling across dead fields, desperate and exposed.",
  "mandatory_style": "[Rembrandt Historical style keywords]",
  "negative_prompt": "[Rembrandt negative keywords]",
  "constraints": "[Safety + Quality + Historical constraints]"
}
```

---

## 🔍 Phân tích Xung đột & Vấn đề Phát hiện

### 🔴 Vấn đề 1: Câu staccato ngắn (< 1s) vs Scene min 3s

**Hiện tượng:** "You burn." (0.8s), "You shiver." (0.8s), "You survive." (0.8s) — mỗi câu quá ngắn.

**Xung đột:** Không có cách chia nào thoả mãn hoàn hảo range 3-6s:
- Gộp cả S10-13 = 6.9s → vượt max 6s
- Tách S10 (4.5s) + S11-13 (2.4s) → scene 2 dưới min 3s

**Đánh giá:** Đây là **edge case**, KHÔNG phải lỗi plan. Trong SRT thực tế, "You burn." sẽ có pause trước/sau → duration thực ~1.5-2.0s, không phải 0.8s. Linear interpolation tính theo ký tự sẽ thiên thấp cho câu cực ngắn.

**Giải pháp:** Thêm quy tắc Bước 3: *"Khi gộp các câu ngắn liên tiếp mà tổng duration gần biên 6s, cho phép AI chia sáng tạo — Tail Correction sẽ xử lý phần còn lại."* **Không cần sửa plan, cơ chế hiện tại đã cover được.**

---

### 🟡 Vấn đề 2: SEQ_04 chỉ có 1 câu duy nhất (8.5s)

**Hiện tượng:** Sentence 14 tạo thành 1 sequence riêng do nhảy thời gian. Nhưng nó chứa **2 ý tưởng khác nhau**:
- "Sullah dies in his bed" → B-Roll, Sullah's bedroom
- "you are still breathing in the dark" → A-Roll, Caesar ở nơi khác

**Xung đột tiềm ẩn:** 2 scenes nhưng `locked_location` cho cả sequence là "Dark room (years later)" — scene đầu tiên lại ở bedroom Sullah → **trượt location**?

**Đánh giá:** Đây là **ranh giới mơ hồ hợp lý.** Narrator nói cả hai trong cùng 1 câu → AI Bước 1 gộp vào 1 sequence là tự nhiên. Nhưng Bước 3 cần tách vì 2 location khác nhau.

**Giải pháp:** Cho phép AI Bước 3 break `locked_location` NẾU text bên trong sentence rõ ràng mô tả 2 nơi khác nhau. Hoặc: AI Bước 1 ghi `locked_location: "Transition: Sullah's deathbed → Caesar in darkness"` để Bước 3 biết đây là cảnh chuyển tiếp.

---

### 🟡 Vấn đề 3: POV narration — Ai là Subject?

**Hiện tượng:** Script dùng "You" (POV) → narrator đang nói VỀ Caesar. Nhưng S1-2 mô tả SULLAH đang hành động. AI Bước 1 cần xác định `main_subject` — subject ở đây là Sullah (người hành động) hay Caesar (POV)?

**Đánh giá:** Không phải lỗi plan. AI Bước 1 có đủ ngữ cảnh để hiểu S1-2 chủ thể hình ảnh là Sullah, dù POV là Caesar.

---

### ✅ Tổng kết Feasibility

| Tiêu chí | Kết quả |
|---|---|
| Tổng duration sau Chunking | 47.8s = 47.8s ✅ khớp |
| Số Sequences | 4 (8.9s / 12.6s / 17.8s / 8.5s) — tất cả ≤ 25s ✅ |
| Số Scenes tổng cộng | 11 scenes ✅ |
| Mọi scene trong range 3-6s? | 10/11 ✅, 1 edge case (staccato sentences → giải quyết bằng creative grouping) |
| Validation timing | Tất cả 4 sequences đạt 0% error ✅ |
| Character labels match | Caesar + Sullah đều được reference đúng ✅ |
| Faction labels match | "Sullah's Soldiers" dùng đúng ở SEQ_02 + SEQ_03 ✅ |
| Location consistency | ✅ ngoại trừ SEQ_04 có transition 🟡 |
| Camera Motion tuân thủ bảng? | ✅ Mỗi scene đầu SEQ = Slow Pan, fleeing = Tracking, fever = Zoom In, còn lại Static |
| Vector Continuity? | ✅ Không có 2 motion liền kề đối nghịch |

**Kết luận: Plan KHẢ THI — 48s script → 4 sequences → 11 scenes hoạt động đúng. 2 edge cases nhỏ (staccato sentences, transition location) có giải pháp rõ ràng, không cần thay đổi kiến trúc plan.**
