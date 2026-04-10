# Tóm tắt Frameworks — Battle Narrative Style Guide

## Nguồn 1: Style Guide (`narrative_phân_tích_trận_đánh.json`) — **4 frameworks**

| # | Framework | Dùng khi | Cấu trúc | Ví dụ phù hợp |
|---|---|---|---|---|
| 1 | **The Investigative Deep-Dive** | Kết quả sốc cần giải thích ngược | Kết quả → Tua lại → Phân tích → Cao trào → Di sản | Trận Thermopylae, Trận Điện Biên Phủ |
| 2 | **The Domino Chain** | Chuỗi nhân-quả, 1 sự kiện nhỏ → thảm họa | Trigger nhỏ → Ripple → Khuếch đại → Tipping point → Sụp đổ | WWI (ám sát → chiến tranh), Sự sụp đổ Constantinople |
| 3 | **The Zoom Lens** | Sự kiện cần bối cảnh rộng (thế kỷ → 1 khoảnh khắc) | Satellite → Map → Street → Kính hiển vi → Pull back | Lepanto (2000 năm xung đột → 1 buổi chiều), Fall of Rome |
| 4 | **The Trial** | Nhiều góc nhìn đối lập, "ai đúng?" | Câu chuyện phổ biến → Phản biện → Bằng chứng ẩn → Bức tranh đầy đủ | Hiroshima (cần thiết hay tội ác?), Alexander the Great |
| ❌ | **The Pendulum** | ~~Vinh quang xen bi kịch~~ | ~~Triumph ↔ Cost xen kẽ, mỗi vòng rộng hơn~~ | — |

> [!NOTE]
> Style guide có **4 frameworks**. Pendulum đã bị loại khỏi file JSON này.

---

## Nguồn 2: Detect Prompt (`system_detect_framework.txt`) — **5 frameworks hardcoded**

| # | Framework | Mô tả ngắn |
|---|---|---|
| 1 | The Investigative Deep-Dive | Reveal → Rewind → Build → Climax → Legacy |
| 2 | The Domino Chain | Small trigger → cascading consequences |
| 3 | The Zoom Lens | Satellite → Map → Street → Intimate → Pull Back |
| 4 | The Trial | Popular Story → Challenge → Hidden Evidence → Full Picture |
| 5 | **The Pendulum** | Glory ↔ Shadow alternating, each wider |

> [!WARNING]
> **Mismatch**: Detect prompt có **5** frameworks (bao gồm Pendulum), nhưng style guide JSON chỉ có **4** (không có Pendulum). Nếu AI detect original script là Pendulum → user chọn Pendulum → **không tìm thấy trong style guide** → lỗi hoặc output kém.

---

## So sánh 2 nguồn

| Framework | Trong Detect Prompt? | Trong Style Guide? | Tình trạng |
|---|---|---|---|
| Investigative Deep-Dive | ✅ | ✅ | ✅ OK |
| Domino Chain | ✅ | ✅ | ✅ OK |
| Zoom Lens | ✅ | ✅ | ✅ OK |
| Trial | ✅ | ✅ | ✅ OK |
| Pendulum | ✅ | ❌ | ⚠️ Mismatch |
