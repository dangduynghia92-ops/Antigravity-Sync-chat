# Nghiên Cứu: Biến Data Thô → Kịch Bản Sống Động

> Tổng hợp từ: documentary scriptwriting, creative nonfiction, YouTube retention, LLM prompt engineering

---

## 1. Micro-Tension — Căng thẳng trong từng dòng

**Nguồn**: Narrative nonfiction theory (Donald Maass, lindasclare.com)

> "Micro-tension is the technique of creating small, line-by-line moments of curiosity that compel the reader to keep reading NOW."

### Kỹ thuật:

| Kỹ thuật | Mô tả | Prompt hiện tại có? |
|---|---|---|
| **Contradiction** | Đặt 2 sự thật mâu thuẫn cạnh nhau → tạo tension | ❌ Không |
| **Withholding** | Gợi mở nhưng chưa giải đáp → buộc phải đọc tiếp | ❌ Không |
| **Gap between desire and reality** | Nhân vật muốn X nhưng thực tế là Y | ❌ Không |
| **Internal conflict** | Highlight mâu thuẫn nội tâm, không chỉ sự kiện bên ngoài | ❌ Không |

**Ví dụ áp dụng:**
```
Khô:  "Einstein supported pacifism but signed the letter to Roosevelt 
       recommending the atomic bomb."

Micro-tension: "Einstein had spent 30 years preaching peace. He had 
       written essays on it. He had given speeches. He believed it with 
       every fiber of his being. And then, on August 2, 1939, he signed 
       a letter asking the President of the United States to build the 
       most destructive weapon in human history. He signed it in his 
       own handwriting."
```

> [!IMPORTANT]
> **Thiếu trong prompt**: Không có rule nào yêu cầu AI tạo tension ở level câu/đoạn. Prompt chỉ yêu cầu structure (DARK_REVELATION, CONTRAST_CLIFF) ở level chapter — nhưng **tension cần xảy ra ở MỌI đoạn văn**, không chỉ ở chapter endings.

---

## 2. Information Disguised as Story — Giấu thông tin vào câu chuyện

**Nguồn**: Creative nonfiction (bookbutchers.com, firstediting.com)

> "The goal is to integrate facts so seamlessly that the reader remains immersed in the narrative rather than feeling they are being taught."

### Kỹ thuật:

| Kỹ thuật | Mô tả | Prompt hiện tại có? |
|---|---|---|
| **Anecdotes over data dumps** | Dùng 1 scene cụ thể thay vì liệt kê nhiều facts | ⚠️ Có trong structure examples nhưng không phải rule |
| **Integrate quotes organically** | Quote + bối cảnh hành động, không phải trích dẫn rời | ✅ Rule 5 (vừa thêm) |
| **The human element** | Mọi thông tin phải qua lăng kính 1 CON NGƯỜI cụ thể | ❌ Không |
| **Sensory anchoring** | Mỗi scene có ít nhất 1 chi tiết giác quan | ❌ Không |

**Ví dụ áp dụng:**
```
Data dump: "Einstein published 4 papers in 1905 covering the 
           photoelectric effect, Brownian motion, special relativity, 
           and mass-energy equivalence."

Disguised: "In 1905, an unknown patent clerk in a rented apartment 
           in Bern sat down with a pencil and a stack of paper. 
           In the span of 8 months, he wrote 4 papers. Each one, 
           by itself, would have been enough for a Nobel Prize. 
           Together, they demolished 200 years of physics. 
           The journal editor who received them had never heard 
           his name."
```

> [!IMPORTANT]
> **Thiếu trong prompt**: Không có quy tắc "NEVER deliver facts as a list — always embed them in a specific moment with a specific person in a specific place."

---

## 3. Pattern Interrupts — Phá vỡ nhịp điệu

**Nguồn**: YouTube retention research (murphy.inc, socialmediaexaminer.com)

> "Plan pattern interrupts every 30-60 seconds: shifts in tone, sudden questions, unexpected facts, or changes in pacing."

### Kỹ thuật:

| Kỹ thuật | Mô tả | Prompt hiện tại có? |
|---|---|---|
| **Tonal shifts** | Chuyển đột ngột: nghiêm túc → châm biếm → buồn | ❌ Không |
| **Direct address** | Nói thẳng vào listener: "Think about that." | ❌ Không |
| **Counter-intuitive facts** | Đưa ra sự thật ngược với kỳ vọng | ❌ Không |
| **Rhetorical questions** | "But here's what no one asks: WHY?" | ❌ Không |

**Ví dụ áp dụng:**
```
Monotone: "He won the Nobel Prize in 1921 for the photoelectric effect. 
          This was a significant achievement in physics."

With interrupts: "He won the Nobel Prize in 1921. Not for relativity — 
          the thing that made him the most famous scientist alive. 
          The committee didn't understand it. They gave him the prize 
          for the photoelectric effect instead. Think about that. 
          The greatest theory of the 20th century, and the Nobel 
          committee said: 'We'll pass.'"
```

> [!IMPORTANT]
> **Thiếu trong prompt**: Không có "address the audience directly at least once per chapter" hoặc "include at least 1 counter-intuitive revelation per chapter."

---

## 4. Perspective Filtering — Lọc qua góc nhìn nhân vật

**Nguồn**: Creative nonfiction biography (writers.com, danieljtortora.com)

> "Filter observations through the subject's point of view. Don't just explain history; describe how it impacted THEM personally."

### Kỹ thuật:

| Kỹ thuật | Mô tả | Prompt hiện tại có? |
|---|---|---|
| **POV anchoring** | Kể qua mắt nhân vật, không phải narrator toàn tri | ❌ Không rõ ràng |
| **Interior world** | Suy nghĩ, nỗi sợ, hy vọng — không chỉ hành động | ❌ Không |
| **Physical environment** | Mô tả nơi họ sống/làm việc → hiểu tính cách | ❌ Không |

**Ví dụ áp dụng:**
```
External: "Einstein moved to Princeton in 1933 and worked at the 
          Institute for Advanced Study."

Filtered: "Princeton was quiet. Too quiet. After Berlin — its cafes, 
          its arguments, its brilliant enemies — this small American 
          town felt like exile disguised as a compliment. He walked 
          to the Institute every morning in worn leather sandals 
          and no socks. A colleague asked why. 'When you are thinking 
          about the nature of light,' Einstein said, 'socks are an 
          unnecessary complication.'"
```

---

## 5. Few-Shot Anchoring — Cho AI "thấy" output mong muốn

**Nguồn**: LLM prompt engineering (chatlyai.app, medium.com)

> "Provide the LLM with an example of raw data followed by the high-quality cinematic version. This is often the most effective way to calibrate the model's tone."

### Kỹ thuật trong prompt:

| Kỹ thuật | Mô tả | Prompt hiện tại có? |
|---|---|---|
| **BAD/GOOD examples per structure** | Có ví dụ xấu/tốt | ✅ Có (8 cặp) |
| **BAD/GOOD examples tổng quát** | Ví dụ xấu/tốt cho TONE chung | ⚠️ Vừa thêm (Show Don't Tell) |
| **Extended example** | 1 đoạn văn hoàn chỉnh mẫu (100-200 từ) | ❌ Không có |
| **Anti-pattern gallery** | Liệt kê 5-10 lỗi phổ biến nhất | ❌ Chỉ có rải rác |

> [!TIP]
> **Suggestion**: Thêm 1 đoạn **GOLDEN SAMPLE** (~150 từ) cuối prompt — mẫu hoàn chỉnh thể hiện TẤT CẢ các rules: show don't tell + micro-tension + perspective filtering + pattern interrupt + dialogue + sensory detail. AI sẽ "mô phỏng" tone này cho toàn bộ output.

---

## 6. Balance Show/Tell — Biết khi nào KỂ

**Nguồn**: writingforchildren.com, reddit creative writing

> "Use TELLING to bridge time and establish context. Use SHOWING for emotionally charged, pivotal moments."

### Prompt hiện tại: **100% SHOW** — không nói khi nào TELL là OK

Quy tắc cần thêm:
```
WHEN TO TELL (brief summary is OK):
- Bridging years between events: "Three years passed. Nothing changed."
- Establishing era context: "In 1905, quantum physics did not exist."
- Moving between locations: "He left Munich. Berlin was next."

WHEN TO SHOW (always expand into scene):
- Turning points
- First/last meetings
- Moments of failure or triumph
- Any event tagged as emotional_beat in the outline
```

> [!IMPORTANT]
> **Thiếu trong prompt**: Không có hướng dẫn khi nào nên TÓM TẮT vs khi nào phải MỞ RỘNG thành scene. Kết quả: AI có thể show everything (quá dài) hoặc tell everything (quá khô).

---

## Tóm Tắt: 8 Thứ Prompt Writer Đang Thiếu

| # | Thiếu | Mức độ ảnh hưởng |
|---|---|---|
| 1 | **Micro-tension** rules (tension ở level câu/đoạn) | 🔴 Critical |
| 2 | **Information disguised as story** (never list facts) | 🔴 Critical |
| 3 | **Pattern interrupts** (rhetorical questions, tonal shifts) | 🟡 High |
| 4 | **Perspective filtering** (filter through character's POV) | 🟡 High |
| 5 | **Golden sample** paragraph mẫu (few-shot anchoring) | 🟡 High |
| 6 | **Show/Tell balance** (when to summarize vs expand) | 🟡 High |
| 7 | **Sensory anchoring** (≥1 sensory detail per key scene) | 🟠 Medium |
| 8 | **Direct audience address** (at least once per chapter) | 🟠 Medium |
