# POV Biography Niche — Implementation Plan v7

> **Cập nhật v7:** Định nghĩa rõ 6 phases.

---

## Phase Plan — 6 Phases: Định Nghĩa Chi Tiết

---

### Phase 1: NGUỒN GỐC

**Định nghĩa:** Nhân vật CHƯA chọn gì — thế giới chọn cho họ. Những thứ họ KHÔNG kiểm soát: nơi sinh, gia đình, bệnh tật bẩm sinh, hoàn cảnh xã hội.

**Litmus Test:** *"Event này xảy ra VỚI nhân vật, hay DO nhân vật?"*
- Xảy ra VỚI họ → Nguồn Gốc
- DO họ → chuyển sang Thử Lửa

**Dữ liệu ưu tiên từ blueprint:** `life_phases` (childhood), `core_identity.birth`, `health_conditions`, `physical_traits`

**Viewer cảm thấy:** Empathy + "Đời bất công" + muốn biết nhân vật sẽ phản ứng thế nào

**Ví dụ:**
| Nhân vật | Events Nguồn Gốc |
|---|---|
| Genghis | Born with blood clot omen, father is minor chieftain, mother kidnapped from another man |
| Genghis | Father poisoned by Tatars, clan abandons family, eat roots/rats |
| Baldwin | Numb arm at age 9, candle test — no pain |
| Baldwin | Leprosy diagnosis at 11 — terminal, no cure |
| Caesar | Born in Subura slums despite ancient family name, surrounded by debt |

**Anti-patterns (KHÔNG thuộc Nguồn Gốc):**
- ❌ "Kills half-brother" → nhân vật CHỦ ĐỘNG → Thử Lửa
- ❌ "Forms alliance" → nhân vật QUYẾT ĐỊNH → Trỗi Dậy
- ❌ "Proclaimed king" → kết quả hành động → Trỗi Dậy hoặc Đỉnh Cao

---

### Phase 2: THỬ LỬA

**Định nghĩa:** Lần ĐẦU TIÊN nhân vật tự chọn, tự hành động, tự đối mặt. Những "first" quyết định tính cách: first kill, first escape, first stand, first survival test.

**Litmus Test:** *"Đây có phải LẦN ĐẦU nhân vật đối mặt và PHẢN ỨNG bằng hành động không?"*
- Lần đầu → Thử Lửa
- Đã quen, đã có kinh nghiệm → Trỗi Dậy

**Dữ liệu ưu tiên từ blueprint:** `life_phases` (adolescence/youth), `turning_points` sớm, `conflicts` đầu tiên

**Viewer cảm thấy:** Shock + "Wow, nhân vật dám làm thế" + respect bắt đầu hình thành

**Ví dụ:**
| Nhân vật | Events Thử Lửa |
|---|---|
| Genghis | **First kill** — kills half-brother over stolen fish (age 12) |
| Genghis | **First escape** — captured, wooden cage, slams plank into guard, escapes (age 15) |
| Baldwin | **First throne** — crowned at 13, barons calculating, Saladin emerging |
| Caesar | **First survival** — Sulla's purge, hiding in countryside, nearly dies of illness (age 18) |
| Caesar | **First defiance** — captured by pirates, demands higher ransom, crucifies them (age 25) |

**Anti-patterns:**
- ❌ "Conquers Jin Dynasty" → đã có quân đội, kinh nghiệm → Đỉnh Cao
- ❌ "Forms political alliance" → strategic, not survival → Trỗi Dậy
- ❌ "Issues new law" → system building → Đỉnh Cao

---

### Phase 3: TRỖI DẬY

**Định nghĩa:** Từ survivor → leader. Nhân vật bắt đầu XÂY DỰNG: liên minh, followers, quyền lực, uy tín. Có cả thắng lợi VÀ phản bội — vì khi lên cao, mối quan hệ phức tạp hơn.

**Litmus Test:** *"Nhân vật đang TÍCH LŨY power hay đang DÙNG power?"*
- Tích lũy → Trỗi Dậy
- Đã có power và dùng nó → Đỉnh Cao

**Dữ liệu ưu tiên từ blueprint:** `key_relationships` (allies, betrayers), `conflicts` (power struggles), `achievements` sớm, `turning_points` giữa cuộc đời

**Viewer cảm thấy:** Momentum + rooting for nhân vật + lo lắng khi có phản bội

**Ví dụ:**
| Nhân vật | Events Trỗi Dậy |
|---|---|
| Genghis | Wife kidnapped → forms 3-army alliance → rescue → "United, you are something" |
| Genghis | Sworn brother raises army → 3-day battle → betrayal destroyed |
| Genghis | 200,000 people kneel → proclaimed Genghis Khan → sworn brother asks noble death |
| Caesar | Weeps at Alexander's statue → resigns → returns to Rome with ambition |
| Caesar | Borrows from Crassus → sponsors games → wins Pontifex Maximus |
| Caesar | Forms First Triumvirate → divides Republic's resources |

**Anti-patterns:**
- ❌ "Born into poverty" → passive, no agency → Nguồn Gốc
- ❌ "Conquers Gaul for 8 years" → already HAS power → Đỉnh Cao
- ❌ "Body failing, generals watching" → declining → Suy Tàn

---

### Phase 4: ĐỈNH CAO

**Định nghĩa:** Maximum power. Nhân vật ĐÃ CÓ quyền lực và DÙNG nó ở quy mô lớn nhất. Chinh phục, xây hệ thống, thay đổi thế giới. **Nhưng:** hạt giống suy tàn bắt đầu xuất hiện (cơ thể yếu, kẻ thù âm mưu, kiêu ngạo).

**Litmus Test:** *"Nhân vật đang ở ĐỈNH quyền lực chưa? Hành động này có quy mô LỚN NHẤT không?"*
- Quy mô lớn nhất, power cao nhất → Đỉnh Cao
- Power đang giảm, cơ thể/tâm lý suy → Suy Tàn

**Dữ liệu ưu tiên từ blueprint:** `achievements` lớn nhất, `military_campaigns`, `governance`, `conflicts` quy mô lớn, `dark_impact`

**Viewer cảm thấy:** Awe + "Incredible" + nhưng bắt đầu thấy cái giá ("No satisfaction, only distance")

**Ví dụ:**
| Nhân vật | Events Đỉnh Cao |
|---|---|
| Genghis | Builds written law — meritocracy, tolerance, courier network |
| Genghis | Conquers Jin Dynasty — makes Great Wall irrelevant |
| Genghis | Ambassador executed → 3 days silence → decides total war |
| Genghis | Erases Khwarezm Empire — river diverted over ruins |
| Baldwin | Montgisard — 375 knights defeat 26,000 (his only peak moment) |
| Caesar | 8-year Gaul conquest — millions dead, Vercingetorix surrenders |
| Caesar | Crosses Rubicon — "The die is cast" |
| Caesar | Defeats Pompey, places Cleopatra, "Veni Vidi Vici" |

**Anti-patterns:**
- ❌ "First alliance formed" → still building power → Trỗi Dậy
- ❌ "Body failing, can't ride" → declining → Suy Tàn
- ❌ "Dies at 65" → death → Kết Thúc

---

### Phase 5: SUY TÀN

**Định nghĩa:** Cơ thể, quyền lực, hoặc mối quan hệ đang SỤP ĐỔ. Nhân vật vẫn chiến đấu nhưng viewer BIẾT kết cục đang đến. Body-as-clock tăng tốc ở phase này.

**Litmus Test:** *"Nhân vật đang MẠNH LÊN hay YẾUĐI? Viewer có cảm giác 'hết rồi' chưa?"*
- Yếu đi, mất kiểm soát → Suy Tàn
- Vẫn mạnh, vẫn chinh phục → Đỉnh Cao

**Dữ liệu ưu tiên từ blueprint:** `health_conditions` (progression), `conflicts` cuối, `key_relationships` tan vỡ, `physical_state_arc`

**Viewer cảm thấy:** Dread + sadness + respect cho nhân vật vẫn chiến đấu dù biết thua

**Ví dụ:**
| Nhân vật | Events Suy Tàn |
|---|---|
| Genghis | Last campaign through winter — body failing, "not what it was", generals watch like men watching a fire running low |
| Baldwin | Rotting throne — skin cracking, can't grip, someone lifts him onto horse |
| Baldwin | Iron will — legs giving out, silver mask, strips brother-in-law of power |
| Baldwin | Last ride — nearly blind, carried on litter, but Saladin withdraws at sight of banners |
| Baldwin | Blind king — totally blind, bedridden, still issues orders |
| Baldwin | Sand castle — crowns nephew, "my reign has been buying time" |
| Caesar | Dictator for Life — arrogance, refuses to stand for senators, "falling sickness" |
| Caesar | Ides of March — 23 stab wounds, pulls toga over face |

> [!NOTE]
> **Baldwin đặc biệt:** Suy Tàn chiếm 5/11 chapters (Lv5-9) vì leprosy = slow, visible decline kéo dài. Đỉnh Cao chỉ 1 chapter (Montgisard). → Phase plan linh hoạt theo nhân vật.
> 
> **Caesar đặc biệt:** Assassination (Ides) nằm ở Suy Tàn (không phải Kết Thúc) vì đó là HẬU QUẢ của kiêu ngạo — climax của sự sụp đổ.

**Anti-patterns:**
- ❌ "Builds courier network" → system building at power → Đỉnh Cao
- ❌ "Born with disease" → passive, childhood → Nguồn Gốc
- ❌ "Legacy reflection" → no new events → Kết Thúc

---

### Phase 6: KẾT THÚC

**Định nghĩa:** Chapter cuối cùng. Death scene (nếu chưa ở Suy Tàn) + legacy scorecard + circular callback + what happened AFTER them.

**Litmus Test:** *"Nhân vật đã CHẾT hoặc cuộc đời đã KẾT THÚC chưa? Phần này có nói về THẾ GIỚI SAU HỌ không?"*
- Vẫn sống, vẫn hành động → Suy Tàn
- Đã chết hoặc cuộc đời kết thúc → Kết Thúc

**Dữ liệu ưu tiên từ blueprint:** `death_and_funeral`, `legacy_and_historiography`, `key_quotes` cuối đời

**Viewer cảm thấy:** Weight + silence + reflection + "đã sống cùng toàn bộ cuộc đời"

**main_key_data:**
- **CÓ** death scene nếu chưa cover ở Suy Tàn (Genghis: death at 65)
- **= []** nếu death đã cover ở Suy Tàn (Caesar: assassination was Lv11)

**sub_key_data luôn chứa:**
- Legacy scorecard (numbers, achievements, territory)
- Aftermath (what happened to the world after them)
- Circular callback (connect back to Nguồn Gốc)
- Burial/funeral details (if applicable)

**Ví dụ:**
| Nhân vật | Kết Thúc |
|---|---|
| Genghis | Death: horse accident → fever → dies at 65. Legacy: "a fifth of earth's land mass." Burial: no grave, horses over site. Callback: "You came from nothing. You returned to nothing. And now you are history." |
| Baldwin | Death: dies at 24, leprosy. Aftermath: "2 years later, the French knight loses Jerusalem." Callback: numb arm from Lv1 → entire body numb at death |
| Caesar | (death covered in Suy Tàn). Legacy: "dismantled the Republic, destroyed by men he empowered." Callback: "from observant boy in slums → architect of world order" |

**Anti-patterns:**
- ❌ New character development → should be in earlier phases
- ❌ New conflict/enemy → should be in Suy Tàn
- ❌ Analysis/interpretation → POV doesn't analyze, just SHOWS

---

## Bảng Ranh Giới: Phân Biệt 2 Phase Liền Kề

| Ranh giới | Câu hỏi | Nếu A → | Nếu B → |
|---|---|---|---|
| **Nguồn Gốc ↔ Thử Lửa** | "Nhân vật CHỦ ĐỘNG hành động chưa?" | Chưa → Nguồn Gốc | Rồi → Thử Lửa |
| **Thử Lửa ↔ Trỗi Dậy** | "Lần ĐẦU hay đã có kinh nghiệm?" | Lần đầu → Thử Lửa | Có nền tảng → Trỗi Dậy |
| **Trỗi Dậy ↔ Đỉnh Cao** | "Đang TÍCH LŨY power hay DÙNG power?" | Tích lũy → Trỗi Dậy | Dùng ở quy mô lớn → Đỉnh Cao |
| **Đỉnh Cao ↔ Suy Tàn** | "Đang MẠNH LÊN hay YẾU ĐI?" | Mạnh/stable → Đỉnh Cao | Yếu đi, mất control → Suy Tàn |
| **Suy Tàn ↔ Kết Thúc** | "Vẫn SỐNG/hành động hay đã KẾT THÚC?" | Vẫn chiến đấu → Suy Tàn | Chết/legacy only → Kết Thúc |

---

## Đặc Biệt: Nhân Vật Suy Tàn Sớm vs Muộn

| Pattern | Ví dụ | Phase distribution |
|---|---|---|
| **Suy Tàn dài** (bệnh/decline chậm) | Baldwin IV | Nguồn Gốc 2ch, Thử Lửa 1ch, Đỉnh Cao 1ch, **Suy Tàn 5ch**, Kết Thúc 2ch |
| **Đỉnh Cao dài** (nhiều chinh phục) | Genghis Khan | Nguồn Gốc 2ch, Thử Lửa 2ch, Trỗi Dậy 3ch, **Đỉnh Cao 4ch**, Suy Tàn 1ch, Kết Thúc 1ch |
| **Trỗi Dậy dài** (political rise) | Julius Caesar | Nguồn Gốc 1ch, Thử Lửa 2ch, **Trỗi Dậy 3ch**, Đỉnh Cao 3ch, Suy Tàn 2ch, Kết Thúc 1ch |

→ AI phase plan KHÔNG cần chia đều — phase nào có nhiều events quan trọng nhất thì dài nhất.

---

## Phần Giữ Nguyên (Đã Duyệt)

- **Blueprint Fields**: Bỏ 6 fields (LENS), giữ 15 fields (DATA), thêm 2 fields mới
- **Tiêu chí main/sub**: Visual Moment Test, 3 loại (anchor, texture, bridge)
- **Validate Sub-Key**: GIỮ, 3 Tests mới (Physical Moment, Agency, Consequence)
- **Chia Chapter**: 1 anchor ≈ 1 Level, split_threshold [2,3]
- **Chapter Flow**: 5 kiểu opening, 4 sentence patterns, menu-based
- **Writer Prompt**: ~150-200 dòng, viết mới hoàn toàn
- **Pipeline**: Code chung giữ nguyên, thêm niche branches
- **Ngôn ngữ/Blueprint/Length**: Theo UI
