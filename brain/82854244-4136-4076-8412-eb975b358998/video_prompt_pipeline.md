# Kiến trúc Tổng thể: Pipeline tự động hóa Video Prompt từ Script

Để xây dựng một Tool/Module bằng Python giải quyết triệt để bài toán đồng bộ khung hình, khớp thời gian và hợp logic chuyển cảnh, chúng ta cần một Pipeline (đường ống) dữ liệu chạy qua **4 Module cốt lõi**. 

Mục tiêu cốt lõi: Mọi dữ liệu luân chuyển giữa các bước đều phải được format chuẩn **JSON** để code dễ dàng đọc, parse và validation (kiểm chứng) trước khi đẩy vào API tạo video.

---

## Bước 1: Module Phân rã Kịch bản (Macro Semantic Chunking)
**Mục tiêu:** Cắt kịch bản dài thành các mảng lớn (Sequence) mang trọn vẹn mạch ngữ cảnh chữ, đồng thời phân lập cực kỳ rõ ràng về Không gian và Nhân vật để nhồi cho AI.

*   **Input:** File Bản Script Sạch đã lột bỏ timecode (Kèm tham số sức chứa tối đa của 1 Sequence: vd 60-80 từ ~ 20-30s).
*   **Logic xử lý (LLM + Python Rules):** Cỗ máy áp dụng 4 BỘ QUY TẮC CỐT LÕI để chặt Sequence:
    * **Quy tắc 1 (Không gian & Thời gian - Ưu tiên #1):** Cắt thành Sequence mới ngay khi kịch bản phát hiện sự thay đổi về Setting. (Vd: Từ phòng khách ra ngõ, từ ban ngày sang "3 năm sau" đêm tối). Ánh sáng/Môi trường đổi -> Phải ngắt đoạn.
    * **Quy tắc 2 (Chủ thể trọng tâm - Subject Shift):** Dù cùng 1 không gian, nhưng nếu tiêu điểm đổi từ Nhóm Tướng Địch (Đám đông) sang Gương mặt Nhân vật chính (Cá nhân) -> Phải ngắt đoạn để module Gen ảnh không tải nhầm Asset.
    * **Quy tắc 3 (Giới hạn dung lượng - Max Duration):** Nếu 1 cảnh chém nhau ngoài bãi cỏ kéo dài quá lâu (vd 200 từ), hệ thống buộc phải chặt đôi nó ra. Chốt chặn này ngăn AI/RAM không bị tràn bộ nhớ khi xử lý lệnh.
    * **Quy tắc 4 (Ranh giới Ngữ nghĩa - Semantic Boundary):** Ngay cả khi bị chặt bởi Quy tắc 3, Python tuyệt đối cấm việc "cắt ngang một câu đang nói dở". Lưỡi dao cắt bắt buộc phải rơi trúng dấu chấm hoặc dấu xuống dòng (`.`, `\n`). 
*   **Output (JSON List Example):** Định dạng chuẩn mực trọn vẹn ngữ nghĩa để đẩy cho Con AI ở Bước 3 làm nhiệm vụ chia Scene:
```json
[
  {
    "sequence_id": "SEQ_01",
    "location_shift": "Sullah's Palace",
    "main_subject": "Sullah and soldiers",
    "full_text": "You are 18, 82 BC. Sullah has seized Rome and he is writing lists, names on parchment that become death warrants by mourning.",
    "total_duration": 9.0
  },
  {
    "sequence_id": "SEQ_02",
    "location_shift": "Caesar's Villa",
    "main_subject": "Julius Caesar and Guards",
    "full_text": "Your family back the wrong side of his war and Sullah remembers everything. His men strip your priesthood. They confiscate your wife Cornelia's dowy. They want every stone attached to your name.",
    "total_duration": 14.0
  }
]
```

---

## Bước 2: Module Phân tích Siêu Dữ Liệu (Global Context Analysis)
**Mục tiêu:** Quét toàn bộ kịch bản một lần duy nhất để "Khóa" (Lock) thiết kế mĩ thuật cho toàn bộ dự án bằng cách tạo ra các bộ Tham chiếu tĩnh (Character Sheet & Visual Bible).

*   **Input (Tuyệt chiêu Plain Text):** 
    * **Bản Script Sạch (Cleaned Text):** Code Python ngầm lấy toàn bộ các chuỗi `full_text` ở Bước 1 nối lại, **lột sạch sành sanh mọi con số Timecode hầm bà lằng (00:00:xx)** để đúc thành một File Văn Bản Tiểu Thuyết liền mạch trơn tru.
    * Gửi nguyên cái Bản Văn Bản Sạch đó cho AI cùng các Tệp Phong cách (`.txt` style) và Tệp Mẫu Prompt (`character_group_prompt.txt`).
    * *(Lý do phải làm Sạch: Tránh việc nhồi nhét timecode vào não AI làm nó bị ngộ độc số liệu, mất khả năng gom ngữ cảnh, đồng thời tiết kiệm 50% chi phí Token API)*.
*   **Logic xử lý (LLM Task):**
    * **Khóa Nhân vật (Character Design):** LLM đọc cái "Tiểu thuyết" mượt mà đó, trích xuất tất cả tên các nhân vật/phe phái. Định nghĩa 4 thuộc tính (Mũ, Tóc, Quần áo, Vũ khí) và sinh ra câu lệnh (Prompt) chuẩn form: *"Bảng tham chiếu 3 góc độ, nền trắng, có Label tên ở dưới"*.
    * **Khóa Không gian (Visual Bible):** LLM lọc ra danh sách các bối cảnh chính (Locations) và sinh câu lệnh mô tả chi tiết không gian rộng.
*   **Output (JSON Object Example):** Kho lưu trữ Context dùng làm "Sườn" để Module 3 lấy thông tin:
```json
{
  "global_style": "Classical Oil Painting Historical, cinematic...",
  "characters": [
    {
      "label": "Constantino el Grande",
      "sheet_prompt": "Character reference sheet on clean white background. Three neutral standing views... [Roman Emperor armor]. Bold label text 'Constantino'."
    }
  ],
  "locations": [
    {
      "label": "Constantinopla City",
      "bible_prompt": "A majestic establishing shot of Constantinopla, classical Roman architecture... Classical Oil Painting Historical."
    }
  ]
}
```

---

## Bước 3: Module Đạo diễn Hình ảnh (Micro Scene Storyboarding)
**Mục tiêu:** Kế thừa "Cỗ được dọn sẵn" là mảng Segment đã nội suy Không gian của Bước 1. Đóng vai trò Đạo diễn, đập vỡ Sequence đó thành các Shot quay ngắn (3-5s) chuẩn ngôn ngữ điện ảnh.

*   **Data Gửi Đi (Input Payload):** Mảng Data nguyên khối tống vào não LLM:
    1. `Sequence Context`: Trọn bộ Output JSON của Bước 1 chuyển sang (đặc biệt là 2 tham số vàng `location_shift` và `main_subject`, cùng `total_duration`).
    2. `Visual Assets`: Bảng Nhân vật và Không gian được bọc sẵn từ Bước 2.
    3. `System Prompt`: Lệnh Đạo diễn bắt ép LLM tuân thủ 4 Luật.
*   **Hướng dẫn AI chia cảnh (System Prompt Rules):**
    * **Quy tắc Khóa Cảnh (Location & Subject Lock):** Bất kể Lời đọc (Voiceover) đang lan man chém gió ở đâu, **Mọi hành động điện ảnh đều PHẢI diễn ra tại đúng Không gian và xoay quanh Chủ thể đã được khai báo ở Bước 1**. 
    * **Quy tắc Toán (Time Math):** Tổng các `scene_duration` chạy ra phải BẰNG CHÍNH XÁC `total_duration` của Sequence khởi thủy. Mỗi shot dao động từ 3s - 5s.
    * **Quy tắc Điện ảnh (A-Roll & B-Roll):** Không được quay bám sát mặt nhân vật mãi. Bắt buộc trộn nhịp điệu máy quay: Cảnh Rộng Toàn Cảnh (Wide Establishing), Cảnh Trung (Medium), và Cận Cảnh Đặc Tả bàn tay/vật thể/đôi mắt (Extreme Close-up).
    * **Quy tắc Dịch Vật Lý (Physical Action Only):** CẤM sinh từ ngữ trừu tượng (Thua trận, buồn bã). Bắt buộc dịch ra sự kiện vật lý nhìn thấy được (đầu gối gục xuống bùn, gươm rơi loảng xoảng).
*   **Output (JSON List Example):**
```json
{
  "total_sequence_duration": 14.0,
  "locked_location": "Caesar's Villa",
  "scenes": [
    {
      "scene_id": 1,
      "duration": 4.0,
      "matched_text": "Your family back the wrong side of his war...",
      "shot_type": "Medium Shot",
      "roll_type": "A-Roll",
      "physical_action": "Young Julius Caesar (18 years old) standing in the dark shadows of his room, body tense with fear."
    },
    {
      "scene_id": 2,
      "duration": 5.0,
      "matched_text": "His men strip your priesthood. They confiscate your wife Cornelia's dowy.",
      "shot_type": "Medium Close-up",
      "roll_type": "B-Roll",
      "physical_action": "Two heavy, armored arms of Roman soldiers aggressively ripping a sacred white priest scarf off."
    },
    {
      "scene_id": 3,
      "duration": 5.0,
      "matched_text": "They want every stone attached to your name.",
      "shot_type": "Low Angle Shot",
      "roll_type": "B-Roll",
      "physical_action": "Roman soldiers swinging heavy metal hammers, smashing a white marble family statue to pieces."
    }
  ]
}
```
*   **Python Validation:** Code Python sẽ móc vào cục JSON trên, cộng nhẩm `4 + 5 + 5 = 14`. Nếu khớp thời lượng gốc Bước 1 ném sang -> Bấm duyệt cái rụp sang Bước 4 (Ráp Prompt Tiếng Anh). Không khớp -> Báo lỗi API, gọi lại.

---

## Bước 4: Module Lắp ráp và Đóng gói (Prompt Assembly)
**Mục tiêu:** Ráp các biến số để chốt hạ câu lệnh Tiếng Anh cuối cùng dùng để gọi API.

*   **Input:** Từng phần data `Scene` (Bước 3) + `Global Context` (Bước 2) + Đường dẫn ảnh tham chiếu dưới Local nếu có.
*   **Logic xử lý (Python String Builder):** Ráp nối theo công thức cố định: 
    `[Shot Type]. [Physical Action] at [Location]. [Global Style]. Constraints.`
*   **Output (JSON Data):** Tệp lệnh hoàn chỉnh sẵn sàng gọi Veo/Runway.

---

### Tổng kết Đường đi Dữ liệu (Data Flow)
**Full Script Text** ---> (B1) ---> **Sequences (10-25s)** ---> (B3) ---> **Scenes (3-5s)** ---> (B4) ---> **Final API Prompts**

*(Module 2 chạy một lần ở đầu để lấy data tổng quan làm tài nguyên cho Bước 3 và Bước 4).*
