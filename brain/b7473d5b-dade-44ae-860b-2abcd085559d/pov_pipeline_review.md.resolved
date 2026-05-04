# Review: Pipeline POV Tiểu Sử (Narrative Mode)

Dưới đây là review chi tiết về luồng xử lý (pipeline) của tab **Script Creation** khi chạy ở chế độ **Narrative** với style **POV Tiểu sử** (POV Biography / Góc nhìn nhập vai).

Pipeline này được thiết kế cực kỳ chặt chẽ, tập trung vào **tính điện ảnh (cinematic)**, **hành động vật lý (physical action)** và **dòng thời gian tuyến tính (chronological timeline)**, thay vì liệt kê tiểu sử truyền thống.

---

## 1. Phase Plan (Lập kế hoạch sự kiện)
**File Prompt:** `system_narrative_phase_plan_pov.txt`

Khác với biography thông thường (gom sự kiện vào các phase cố định của framework), POV Biography sử dụng cấu trúc **phẳng (flat list)** dựa trên dòng thời gian:
*   **Đầu ra:** Một `event_timeline` (danh sách các sự kiện được sắp xếp nghiêm ngặt theo độ tuổi tăng dần).
*   **SCENE TEST (Bộ lọc Scene):** Đây là cốt lõi của POV. Một sự kiện chỉ được làm sự kiện chính (main_key_data) nếu nó có đủ 3 yếu tố:
    1.  **PLACE:** Có bối cảnh vật lý cụ thể (ví dụ: chiến trường, phòng ngai vàng).
    2.  **ACTION:** Nhân vật có hành động hoặc lựa chọn cụ thể.
    3.  **CONSEQUENCE:** Có hậu quả/thay đổi ngay lập tức sau hành động đó.
*   **Xử lý Body State (Thể trạng):** Những thay đổi vật lý dần dần (mù lòa, liệt, giọng yếu...) *không bao giờ* đứng độc lập thành sự kiện chính. Chúng bị ép xuống thành `sub_key_data` để writer "dệt" (weave) vào các hành động cụ thể.
*   **Independence Test:** Nếu nhiều sự kiện xảy ra cùng một độ tuổi, AI phải kiểm tra xem chúng có độc lập không (dựa trên địa điểm, quan hệ nhân quả, và người tham gia). Nếu có liên quan nhân quả, chúng sẽ bị merge (gộp) lại.
*   **Phase Labels:** Các nhãn (Nguồn Gốc, Thử Lửa, Trỗi Dậy, Đỉnh Cao, Suy Tàn, Kết Thúc) chỉ đóng vai trò là **tag định hướng nhịp độ**, không dùng để gom nhóm cấu trúc như các framework khác.

## 2. Outline Generation (Lên dàn ý chương)
**File Prompt:** `system_narrative_outline_pov.txt`

Dựa trên `event_timeline`, Outline AI sẽ phân bổ sự kiện vào các chương (chapter).
*   Đảm bảo duy trì luồng thời gian liên tục.
*   Bảo vệ tính nhất quán của các mối quan hệ (key_relationships) và quá trình chuyển biến tâm lý/thể chất.

## 3. Writing Phase (Viết kịch bản)
**File Prompt:** `system_narrative_write_pov.txt`
**Core Logic:** `core/rewriter.py`

Khi AI bắt đầu viết, pipeline can thiệp mạnh mẽ bằng code Python để đảm bảo đúng format POV:
*   **Auto-Injection Level Anchor:** Hàm `_inject_level_anchor()` trong `rewriter.py` tự động chèn dòng *“Level [Number], [Label]. You are [Age].”* vào đầu mỗi chương. Điều này ngăn AI tự chế ra các format mở bài sai lệch hoặc làm loạn luật prompt.
*   **Body Structures (Cấu trúc chương):** Pipeline tiêm (inject) các cấu trúc chuyên biệt cho POV dựa trên dict `_BODY_STRUCTURES["pov tiểu sử"]`:
    *   **`action_scene`**: Mở đầu bằng bối cảnh vật lý -> Hành động chi tiết từng cú đánh/bước đi -> Hậu quả trực tiếp. (Dành cho chiến đấu, đối đầu).
    *   **`transformation_scene`**: Trạng thái trước -> Khoảnh khắc xúc tác -> Trạng thái sau. (Dành cho việc nhận tước hiệu, thay đổi quyền lực).
    *   **`legacy_close`**: Chỉ dùng cho chương cuối. Miêu tả cái chết vật lý (nếu chưa có) -> Bảng điểm di sản (số liệu) -> Vòng lặp callback về chi tiết ở Level 1 -> Dòng chốt (im lặng/sức nặng).

## 4. Audit & Review (Hậu kiểm & Duyệt lại)
**File Prompts:** `system_validate_sub_key_pov.txt`, `system_narrative_audit_pov.txt`, `system_narrative_review_pov.txt`

*   **Sub-key Validation:** Kiểm tra xem writer có vô tình bỏ sót các `sub_key_data` (đặc biệt là các chi tiết body state/môi trường) hay không.
*   **Audit Logic:** Loại bỏ các ngôn từ hoa mỹ, phép ẩn dụ bay bổng (poetic metaphors). Ép AI phải sử dụng ngôn ngữ trực diện, vật lý, tập trung vào 5 giác quan và hành động thực tế.

---

### Nhận xét tổng quan
1. **Điểm mạnh:** Flow POV hiện tại là một trong những pipeline được "hardened" (làm cứng) tốt nhất. Khái niệm **Scene Test** và **Auto-Injection Level** giải quyết triệt để vấn đề AI hay "kể lể" lê thê hoặc sai format độ tuổi. 
2. **Kiểm soát tính nhất quán:** Nhờ việc tách biệt lập kế hoạch dòng thời gian (`event_timeline`) và tạo chương (`outline`), việc đảm bảo tính logic và phát triển nhân vật được duy trì qua hàng chục chapter một cách ổn định.

Bạn có muốn tôi đi sâu vào phân tích file logic cụ thể nào (như `rewriter.py` logic) hay tối ưu lại prompt nào trong pipeline này không?
