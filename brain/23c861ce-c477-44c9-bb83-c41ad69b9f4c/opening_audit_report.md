# Tổng hợp: Tất cả cách mở đầu chapter — Niche Bí Ẩn Lịch Sử

## Tóm tắt vấn đề

Mở đầu chapter **giống báo cáo khoa học**: an toàn, uy tín, nghiêm túc quá mức → **mất kịch tính**, mất hook.

---

## 4 Lớp Prompt Ảnh Hưởng Đến Cách Mở Đầu

### Lớp 1: Style JSON (`identity` + `tone`) ⚠️ NGHI VẤN CHÍNH

```json
"identity": "Nhà phân tích lịch sử — trình bày bằng chứng một cách KHÁCH QUAN,
             đặt câu hỏi sắc bén, và để khán giả tự rút kết luận."

"tone": "Phân tích — NGHIÊM TÚC nhưng không khô khan. Xen kẽ giữa giọng PHÂN TÍCH
        (khi trình bày data) và giọng immersive (khi dựng bối cảnh)."
```

> [!WARNING]
> **Vấn đề**: AI đọc "khách quan", "phân tích", "nghiêm túc" → default sang giọng academic cho MỌI phần, kể cả opening. Chỉ dẫn "xen kẽ giọng immersive" quá yếu — AI không biết KHI NÀO chuyển.

---

### Lớp 2: 7 Structure Prompts (COLD OPEN rules) ✅ TỐT

Mỗi structure có COLD OPEN riêng — **đều yêu cầu mystery + stakes trong 15 giây**:

| Structure | COLD OPEN yêu cầu | Ví dụ good |
|---|---|---|
| **Mythbuster** | `ACCEPTED BELIEF` + `FACT shatters it` | "We know how pyramids were built... one block took three weeks. The Great Pyramid has 2.3 million." |
| **Detective Trail** | `MYSTERY` + `ANOMALY` immediately | "Roman concrete survived 2,000 years. Modern concrete crumbles in decades." |
| **Bureaucratic Anomaly** | `SYSTEM` + `ONE THING missing` | "Allies convicted dozens of war criminals. They deliberately exempted one." |
| **Human Anchor** | `WHO` + `WHAT HAPPENED` + `WHY it matters` | "First casualty of WWII was not a soldier. He was a farmer, drugged by his own government..." |
| **Conflicting Accounts** | `PARADOX` — two truths that can't both be right | "Churchill offered to merge Britain and France. British called it solidarity. French called it takeover." |
| **Ticking Clock** | `WHAT was lost` + `WHY it matters` | "Greek Fire could burn on water. When Constantinople fell, the formula vanished forever." |
| **Innocent Facade** | `Dark truth revealed up front` (dramatic irony) | "The most successful assassination weapon was sold as a beauty cream." |

> [!NOTE]
> Các COLD OPEN rules **đã tốt** — vấn đề là AI không tuân thủ vì bị `identity`+`tone` override.

---

### Lớp 3: Bridge Formats (body chapter transitions)

Sau COLD OPEN, chapter 2+ mở bằng bridge → cấu trúc writing hiện tại:

```
Bridge (1-2 câu) → COLD OPEN → Body content
```

6 bridge formats: CONTRAST, THEMATIC LINK, QUESTION BRIDGE, COLD OPEN (jump in), CALLBACK, TEMPORAL.

> [!NOTE]
> Bridge formats phong phú nhưng AI có thể viết bridge quá formal vì `tone` = "phân tích nghiêm túc".

---

### Lớp 4: 5 Opening Methods (Style JSON — chỉ dùng cho HOOK chapter)

| Opening | Technique |
|---|---|
| Immersive Narrative Hook | Ngôi 2, dựng bối cảnh sensory |
| Phá Vỡ Niềm Tin Quen Thuộc | Sharp reversal |
| Khung Bí Ẩn Hấp Dẫn | Information gap |
| Artifact-First Hook | Mô tả vật thể cụ thể |
| Câu Hỏi Khiêu Khích | Challenge trực tiếp |

> [!IMPORTANT]
> Các openings này **CHỈ dùng cho HOOK chapter** (chapter 1), **KHÔNG ảnh hưởng đến body chapters**. Body chapters dùng COLD OPEN từ structure prompts (Lớp 2).

---

## Chẩn Đoán: Tại Sao Mở Đầu Giống Báo Cáo Khoa Học?

### Nguyên nhân gốc: `identity` + `tone` quá "an toàn"

```
AI hiểu:
  "Nhà phân tích lịch sử" + "nghiêm túc" + "khách quan"
  → Viết mở đầu kiểu: "The history of X reveals fascinating insights..."
  → Thay vì: "The first casualty of WWII was not a soldier."
```

### Chuỗi nguyên nhân:

1. **`identity`** nói "nhà phân tích" → AI mặc định giọng phân tích cho tất cả
2. **`tone`** nói "nghiêm túc" → AI không dám viết dramatic
3. **`data_density`** nói "Cao, 2-3 citations" → AI nhồi citation ngay mở đầu
4. **`vocabulary`** nói "academic hybrid cho evidence/analysis" → AI dùng academic voice cho cả opening
5. **COLD OPEN rules tốt** nhưng bị override bởi identity/tone → AI viết COLD OPEN kiểu phân tích thay vì kiểu hook

### Bằng chứng: So sánh

| Prompt yêu cầu | AI viết ra |
|---|---|
| "State the MYSTERY and ANOMALY immediately" | "Historical records reveal that..." |
| "The viewer must know within 15 seconds" | "Scholars have long debated the origins of..." |
| "Stakes clear. Mystery clear." | "According to researchers at the University of..." |

---

## Đề xuất sửa

Bạn muốn tôi sửa ngay không? Hướng sửa:

1. **`identity`**: Đổi từ "nhà phân tích" → "narrator who hooks first, analyzes second"
2. **`tone`**: Thêm rule rõ ràng: "OPENINGS phải dramatic/cinematic. Giọng phân tích CHỈ bắt đầu SAU evidence section"
3. **`sentence_rhythm`**: Thêm: "COLD OPEN = short punchy sentences ONLY. NO citations in first 3 sentences"
4. **Thêm rule vào style JSON**: "The first 2-3 sentences of EVERY body chapter must read like a movie trailer, NOT a research paper"
