# Kiến trúc Tổng thể: Pipeline tự động hóa Video Prompt từ Script

Để xây dựng một Tool/Module bằng Python giải quyết triệt để bài toán đồng bộ khung hình, khớp thời gian và hợp logic chuyển cảnh, chúng ta cần một Pipeline (đường ống) dữ liệu chạy qua **4 Module cốt lõi**. 

Mục tiêu cốt lõi: Mọi dữ liệu luân chuyển giữa các bước đều phải được format chuẩn **JSON** để code dễ dàng đọc, parse và validation (kiểm chứng) trước khi đẩy vào API tạo video.

---

## Bước 1: Module Phân rã Kịch bản (Script Chunking & Timing)
**Mục tiêu:** Cắt kịch bản dài thành các mảng lớn (Sequence) mang trọn vẹn ngữ cảnh.

*   **Input:** File text kịch bản (`.txt`) hoặc Tệp sub (`.srt`). Kèm tham số `MIN_DURATION` (vd: 10s) và `MAX_DURATION` (vd: 25s).
*   **Logic xử lý (Thuật toán Python):** 
    * Thuật toán phân rã theo Đoạn văn (Paragraphs) hoặc Mạch ý.
    * Ước tính thời gian âm thanh (~2.5 - 3 từ/giây).
    * Gộp/Cắt đoạn thông minh bằng dấu câu sao cho mỗi Block (Sequence) luôn nằm trong khoảng 10-25s.
*   **Output (JSON List):** Danh sách các "Phân đoạn Macro" (Sequences) hoàn hảo về cả logic chữ và thời lượng.

---

## Bước 2: Module Phân tích Siêu Dữ Liệu (Global Context Analysis)
**Mục tiêu:** Quét toàn bộ kịch bản một lần để gom nhóm tài nguyên tĩnh (Nhân vật, Không gian, Thẩm mỹ).

*   **Input:** Toàn bộ Sequences từ Bước 1 + File Style (Ví dụ: `styles/Dark Gouache Drama.txt`).
*   **Logic xử lý (LLM Task):** Dùng AI đọc lướt để trích xuất Danh sách nhân vật (Đặc điểm nhận dạng) và Danh sách địa điểm (Locations xuất hiện trong bài).
*   **Output (JSON Object):** Bộ `Global Context` khoá chặt quy chuẩn thiết kế.

---

## Bước 3: Module Đạo diễn Hình ảnh (Scene Breakdown - Micro)
**Mục tiêu:** "Trái tim" của hệ thống. Biến một Phân đoạn chữ tĩnh (15s) thành các đoạn lệnh quay video ngắn (3-5s).

*   **Input:** Từng `Sequence` (từ Bước 1) + Bộ `Global Context` (từ Bước 2).
*   **Logic xử lý (LLM Task + Python Validation):**
    * LLM tự động gán một Không gian (Location) lấy từ Bước 2 áp vào cho Sequence này.
    * LLM đập vỡ cái Sequence 15s đó ra thành 3-4 Scenes nhỏ hơn (áp dụng luật 70/30 B-roll, và dịch ý niệm trừu tượng thành hành động vật lý).
    * Python validation: `Sum(scene_duration)` phải bằng giới hạn của Sequence. Vượt quá -> Hủy -> Bắt LLM gọi lại.
*   **Output (JSON List):** Danh sách chi tiết các "Scene" quay.

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
