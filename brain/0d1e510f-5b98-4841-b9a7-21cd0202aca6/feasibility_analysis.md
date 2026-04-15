# Đánh Giá Tính Khả Thi: 15 Quy Tắc Key_Data

## Tóm Tắt Nhanh

| Đánh giá | Số rules |
|----------|----------|
| ✅ Khả thi ngay (không xung đột) | 7 |
| ⚠️ Khả thi, cần sửa prompt | 6 |
| 🔴 Xung đột cần giải quyết | 2 |

---

## NHÓM 1: PHÂN LOẠI KEY_DATA (D1-D4)

### D1: EVENT = main, gom cluster
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **Không xung đột** — rule hiện tại L159-175 (EVENT CLUSTER RULE) đã nói y hệt |
| Data field? | ✅ `main_key_data`, `sub_key_data` đã có |
| AI thực hiện? | ✅ Đã hoạt động tốt |
| **Kết luận** | **Giữ nguyên, không cần thay đổi** |

### D2: CONDITION = main (nếu scene) hoặc sub (nếu background)
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **Không xung đột** — tương thích với L14 outline: "main_key_data = build into SCENES, sub = texture" |
| Data field? | ✅ Đã có |
| AI thực hiện? | ✅ Đã hoạt động |
| **Kết luận** | **Giữ nguyên** |

### D3: SEED — plant observation ở phase sớm, harvest ở phase sau
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ⚠️ **Tương thích một phần.** L177-183 (COLLAPSE SEEDS RULE) đã yêu cầu gieo seeds ở Bánh Răng. Nhưng rule mới thêm phần "harvest ở phase sau" — cái này chưa có |
| Data field? | ✅ `collapse_seeds` trong blueprint, `callback_to` + `foreshadow` trong outline |
| AI thực hiện? | ⚠️ AI CÓ data (`callback_to`) nhưng **chưa được hướng dẫn dùng** ở write prompt |
| **Kết luận** | **Khả thi. Cần: (1) Thêm harvest rule vào phase plan, (2) Thêm callback enforcement vào write prompt** |

### D4: MOTIVATION thuộc về EVENT, không tách riêng
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | 🔴 **XUNG ĐỘT TRỰC TIẾP** với **3 vị trí**: |
| | 1. Phase Plan L144-148: `Bánh Răng → ship_life_and_crew, economics, collapse_seeds` — rule hiện tại ép MỌI crew data (kể cả motivation) vào Bánh Răng |
| | 2. Phase Plan L149: `Thử Lửa → combat_events (PEAK only)` — không cho phép đưa motivation vào đây |
| | 3. Phase Plan L152: `NEVER assign a birth event to a combat phase or vice versa` — rule này OK cho birth↔combat, nhưng AI có thể hiểu rộng thành "không mix data giữa phases" |
| Data field? | ✅ Không cần field mới |
| AI thực hiện? | ✅ AI có thể thực hiện nếu rule clear — AI chỉ cần biết "motivation của event X đi cùng event X" |
| **Kết luận** | **Khả thi nhưng PHẢI sửa 3 dòng trong phase plan prompt.** Câu hiện tại quá rigid. |

---

## NHÓM 2: SẮP XẾP CHAPTERS (O1-O5)

### O1: Lifecycle progression
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | 🔴 **XUNG ĐỘT TRỰC TIẾP** với **3 vị trí**: |
| | 1. Outline L270: `THEMATIC ORDER IS MANDATORY (Context → Anatomy → Characters → Dark → Legacy)` |
| | 2. Outline L183: `THEMATIC ORDER: Chapters follow phase order` |
| | 3. Framework JSON L59: `chapter_design: "THEMATIC body"` |
| Data field? | ✅ Phase order trong framework steps đã là roughly lifecycle (Birth → Mutation → Engine → Apex → Death → Archaeology) |
| AI thực hiện? | ✅ Lifecycle order TỰ NHIÊN hơn cho AI vì nó khớp với chronological timeline trong blueprint |
| **Kết luận** | **Khả thi nhưng PHẢI sửa 3 vị trí: Outline L270, L183, và Framework JSON L59.** Đổi "THEMATIC" → "LIFECYCLE". |

> [!IMPORTANT]
> Framework JSON `chapter_design` (L59) là phần AI đọc qua `style_json` — nếu không sửa ở đây, AI vẫn nhận lệnh "THEMATIC body" dù prompts nói "LIFECYCLE". **Phải sửa cả JSON.**

### O2: Freeze-frame sau mutation, trước first battle
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **Không xung đột** — framework steps đã đặt Bánh Răng SAU Đột Biến và TRƯỚC Thử Lửa. Đây là thứ tự hiện tại |
| AI thực hiện? | ✅ Framework steps order enforces này tự động |
| **Kết luận** | **Đã đúng sẵn. Chỉ cần label "freeze-frame" trong prompt.** |

### O3: Event escalation (nhỏ → lớn)
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **Không xung đột** — hiện tại không có rule nào chỉ định thứ tự events trong cùng 1 phase |
| Data field? | ✅ Outline đã có `time_anchor` → AI có thể sắp chronological. Các combat_events trong blueprint có dates |
| AI thực hiện? | ⚠️ AI CÓ THỂ sắp nhưng cần hướng dẫn rõ. Hiện tại AI tự chọn order |
| **Kết luận** | **Khả thi. Thêm rule escalation vào outline prompt.** |

### O4: Causal proximity (seed-harvest ≤ 2 chapters)
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ⚠️ **Xung đột gián tiếp** — THEMATIC mapping hiện tại forced seeds vào Bánh Răng (Ch4-5) và harvest vào Cái Chết (Ch8-9) = 3-4 chapters cách nhau. Nhưng nếu O1 (lifecycle) được áp dụng, khoảng cách sẽ giảm tự nhiên |
| Data field? | ✅ `foreshadow` + `callback_to` fields track liên kết xuyên chapters |
| AI thực hiện? | ⚠️ Khó cho AI đếm "≤ 2 chapters" nếu nó không biết tổng chapters. Cần rule mềm hơn: "gần nhau nhất có thể" |
| **Kết luận** | **Khả thi nếu O1 áp dụng. Nên dùng "gần nhau nhất có thể" thay vì "≤ 2 chapters" cứng.** |

### O5: Phase transition bridge (ends_with tease + callback_to recall)
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **Không xung đột** — `ends_with` rule đã có (L120-126 write prompt). `callback_to` field đã có (L248 outline). Chỉ thiếu rule nối 2 thứ lại |
| Data field? | ✅ Cả 2 fields đã tồn tại |
| AI thực hiện? | ⚠️ Outline AI tạo `callback_to` tốt (QAR data xác nhận). Writer AI nhận field qua template L36. **Nhưng không có rule nói "dùng callback_to"** |
| **Kết luận** | **Khả thi. Chỉ cần thêm 1 rule vào write prompt: "Use callback_to in scene anchor".** |

---

## NHÓM 3: VIẾT NỘI DUNG (W1-W5)

### W1: Scene Anchor bắt buộc
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **ĐÃ IMPLEMENT** ở phiên trước (L88-119 write prompt) |
| **Kết luận** | **Đã có. Không cần thay đổi.** |

### W2: Callback Integration trong 3 câu đầu
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **Không xung đột** — bổ sung cho W1 (Scene Anchor) |
| Data field? | ✅ `callback_to` gửi qua template L36 |
| Thực hiện? | ✅ Chỉ cần thêm 2-3 dòng vào SCENE ANCHOR section |
| **Kết luận** | **Khả thi. Thêm vào L89-97.** |

### W3: Motivation-First
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **ĐÃ CÓ** ở L130-147 (`TIMELINE FLOW — CAUSE BEFORE EFFECT` + `MICRO-CALLBACK`). Rule hiện tại nói "state motive/cause FIRST" |
| **Kết luận** | **Đã có. Không cần thay đổi.** |

### W4: Escalation Transition giữa events cùng phase
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ Không xung đột. Hiện tại `ends_with` rule đã có cho cross-chapter transitions |
| Data field? | ✅ Outline đã có `ends_with` cho mỗi chapter |
| Thực hiện? | ⚠️ Cần thêm sub-rule cho intra-phase events. Hiện tại chỉ focused cross-phase |
| **Kết luận** | **Khả thi. Thêm rule cho escalation pattern.** |

### W5: Micro-callback ≤ 2 câu
| Kiểm tra | Kết quả |
|----------|---------|
| Xung đột? | ✅ **ĐÃ CÓ** ở L142-146. Rule hiện tại nói "keep it to 1-4 sentences" |
| Điều chỉnh? | Có thể siết từ "1-4 sentences" → "1-2 sentences" để nhẹ hơn |
| **Kết luận** | **Đã có. Có thể siết nhẹ.** |

---

## TỔNG KẾT: NHỮNG GÌ PHẢI THAY ĐỔI

### Cần sửa (XUNG ĐỘT TRỰC TIẾP)
| Vị trí | Hiện tại | Cần đổi thành |
|--------|----------|---------------|
| Phase Plan L66 | `THEMATIC order` | `LIFECYCLE order` |
| Phase Plan L144 | `THEMATIC MAPPING` | `LIFECYCLE MAPPING` |
| Phase Plan L148-149 | Rigid data silos (Bánh Răng giữ all crew, Thử Lửa chỉ combat) | Cho phép motivation bundling |
| Outline L183 | `THEMATIC ORDER` | `LIFECYCLE ORDER` |
| Outline L270 | `THEMATIC ORDER IS MANDATORY` | `LIFECYCLE ORDER IS MANDATORY` |
| **JSON L59** | `THEMATIC body` | `LIFECYCLE body` ← **DỄ BỎ QUA** |

### Cần thêm (LỖ HỔNG)
| Vị trí | Thiếu gì | Thêm gì |
|--------|----------|---------|
| Write prompt (sau L97) | Callback enforcement | "If callback_to exists, integrate into scene anchor" |
| Phase Plan (sau L183) | Seed-harvest proximity | "Seeds and their consequences should be as close as possible" |
| Outline prompt (body rules) | Escalation order for combat events | "Events in Thử Lửa: order by escalation (smaller → largest)" |

### Không cần thay đổi (ĐÃ CÓ / TƯƠNG THÍCH)
Rules D1, D2, O2, W1, W3, W5 — đã OK với hệ thống hiện tại.

---

## RỦI RO

1. **Pirate Haven** dùng chung `system_narrative_phase_plan_pirate.txt` → thay đổi sẽ ảnh hưởng → cần verify
2. **Blueprint filter** (`rewriter.py`) dùng `pirate_phase` field matching → nếu outline vẫn giữ `pirate_phase` field thì code KHÔNG cần sửa
3. **Framework JSON `chapter_design`** dễ bị bỏ quên vì AI đọc nó qua `style_json` — nếu không sửa, AI nhận tín hiệu mâu thuẫn ("prompt nói LIFECYCLE, style nói THEMATIC")
