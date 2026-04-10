# Cẩm nang Viết Hook Kịch bản Lịch Sử (Youtube Documentary)

Bản tổng hợp này đúc kết triết lý kịch bản Cinematic và cách ép AI (Writer) từ bỏ thói quen viết tiểu sử "Wikipedia" tẻ nhạt, chuyển sang cấu trúc "Giữ chân người xem" (Retention) trong 30 giây đầu của video.

---

## 1. PHƯƠNG PHÁP & KỸ THUẬT KỂ CHUYỆN (Methodology)

Youtube Documentaries không phải là thư viện. Khán giả không quan tâm nhân vật sinh năm bao nhiêu ở làng quê nào. Kỹ thuật bắt buộc cho Hook là **"In Medias Res" (Bắt đầu từ giữa nhịp)** hoặc **Nịch lý (Paradox)**.

### 3 Nguyên tắc Vàng của một Hook Triệu View:
1. **Cold Open (Vào đề lạnh lùng):** Không chào hỏi (Xin chào các bạn đã đến với kênh...). Vứt thẳng khán giả vào khoảnh khắc tăm tối nhất, vinh quang nhất, hoặc tàn bạo nhất của nhân vật.
2. **The Paradox (Nghịch lý):** Đưa ra hai mảng lắp ghép không tưởng về cùng một người. (Ví dụ: "Hắn cứu 10.000 người Hồi Giáo, nhưng lại đích thân ra lệnh xích 20.000 người Công Giáo vào khoang mái chèo"). Sự mâu thuẫn ép não bộ khán giả phải tò mò.
3. **The Anchor Question (Câu hỏi Mỏ neo):** Sau khi làm khán giả choáng ngợp ở đỉnh cao/đáy vực, phải khóa họ lại bằng câu dắt cung thời gian: *"Làm thế nào mà một [KẺ YẾU HÈN] lại trở thành [BẠO CHÚA] như vậy? Để hiểu được cái đêm định mệnh này, chúng ta phải tua ngược thời gian..."*

---

## 2. CHUYỂN HÓA THÀNH PROMPT (Prompt Injection)

Để con AI (Gemini/Claude) hiểu được phương pháp trên, bạn KHÔNG ĐƯỢC để Hook trôi nổi tự do dựa vào cái Tóm tắt (Summary). Bạn phải kẹp đoạn Prompt dưới đây vào **`system_narrative_write_biography.txt`** (Ưu tiên đặt ở mục `CHAPTER FLOW` hoặc tạo hẳn một mục `IF CHAPTER IS HOOK`).

> [!TIP]
> Bạn có thể bôi đen copy nguyên đoạn Prompt tiếng Anh dưới đây ném vào file cấu hình của bạn.

```text
═══════════════════════════════════════
SPECIAL RULE: IF THIS IS A HOOK CHAPTER (CHAPTER 1)
═══════════════════════════════════════

If generating Chapter 1, YOU MUST IGNORE chronological storytelling. 
Do NOT start with birth, childhood, or basic Wikipedia introductions. 

Follow this strict 3-Beat Hook Formula:

1. THE FREEZE FRAME (IN MEDIAS RES):
   Start the video at the absolute CLIMAX or the lowest ROCK BOTTOM of the subject's life. Place the listener directly in the room/battlefield using 3rd person limits. 
   - Rule: Use vivid, stark imagery. No adjectives. Just the cold truth. 
   - Example: "The yellow walls of the studio were rotting. His friend had just walked out the door. On the table, the razor blade caught the gaslight." 

2. THE PARADOX (THE WHY):
   Deliver the ultimate contradiction about this person. Demolish what the audience thinks they know.
   - Rule: Frame their legacy as a shocking contradiction.
   - Example: "He is known today as a madman who painted stars. But on this night, he was a calculated, hyper-literate philosopher driven to the edge by perfection."

3. THE REWIND ANCHOR:
   Force the narrative to pause and hit the rewind button. State the central thesis question of the video.
   - Rule: End the hook by dragging the audience back to the beginning.
   - Example: "But how does a man chasing the sun end up in the dark with a razor? To understand the breaking of a genius, we cannot look at the blood. We must rewind 35 years... to a child named after a ghost."
```

---

## 3. CÁCH LẮP ĐẶT VÀO HỆ THỐNG FRAMEWORK (JSON)

Nếu bạn muốn mỗi Framework kể Hook theo một phong cách khác nhau, hãy giữ nguyên cấu trúc `styles/narrative_tiểu_sử_nhân_vật.json` mà bạn đang làm, nhưng **siết chặt văn phong (Prose) bằng các lệnh cấm**:

Ví dụ trong Framework **Kẻ Xét Lại (Revisionist)**:
```json
"hook": {
    "method": "Bắt đầu bằng lời nói dối lớn nhất mà Lịch sử ghi chép về họ. Sau đó dùng 1 câu đập nát lời nói dối đó.",
    "anti_pattern": "Tuyệt đối không dùng những từ ngữ Cải lương/Sến súa (Ví dụ: The pages of history, Destined for greatness, Written in blood). Viết câu ngắn, đanh thép.",
    "example_approach": "History books call him a bloodthirsty pirate. They lied. He was a state-sponsored geopolitical mastermind who just happened to operate on the sea."
}
```

> [!IMPORTANT]
> **Tâm pháp cốt lõi:** Lỗi "Câu văn lủng củng" của AI thường xuyên xảy ra ở đoạn Hook vì AI có xu hướng *Cố gắng tỏ ra triết lý và nguy hiểm*. Bằng cách ép nó tuân theo "Công thức 3 nhịp" (Freeze Frame -> Paradox -> Rewind Anchor) bằng các câu ngắn, nó sẽ bị khóa chặt vào Hành Động thay vì miêu tả cảm xúc.
