# Kế hoạch Tái cấu trúc Framework (Chronological Refactoring)

Giải quyết triệt để lỗi "Video nhảy cóc thời gian loạn xạ", ép toàn bộ 5 Framework về chạy chung trên 1 Sườn Tuyến Tính Thời Gian duy nhất. Sự khác biệt của từng Framework sẽ được tạo ra bằng **Lăng kính Trần thuật (Narrative Lens)** thay vì đảo lộn trật tự thời gian.

## Sườn Tuyến Tính Bắt Buộc (The Universal Timeline)
Mọi kịch bản từ nay về sau, dù thuộc Framework nào, cũng bắt buộc đi qua 5 Giai đoạn này trong mục `steps` của JSON:
1. **Nguồn gốc (Origin):** Tuổi thơ, xuất phát điểm, bối cảnh.
2. **Hình thành / Trỗi dậy (The Rise):** Những thành tựu đầu tiên, sự định hình tính cách, vươn lên.
3. **Đỉnh Cao (The Peak):** Thành tựu vĩ đại nhất, quyền lực tối cao, điểm bùng nổ.
4. **Sụp Đổ / Thử Thách (The Fall):** Sự trượt dài, sai lầm, bị hãm hại, hoặc cái chết.
5. **Di Sản (Legacy):** Hậu thế nhìn nhận lại họ như thế nào.

---

## Cách "Đổ Màu" Đặc Trưng Cho Từng Framework

Dưới đây là cách chúng ta thiết kế lại nội dung (Prompt) cho từng Giai đoạn, để AI dù viết theo một luồng thời gian giống hệt nhau nhưng vẫn tạo ra 5 Cảm xúc (Vibe) hoàn toàn khác biệt!

### 1. BẢN ÁN (The Reckoning)
*Lăng kính: Một người hiền tài bị Hệ thống tàn nhẫn nghiền nát.*
*   **Origin (Nguồn gốc):** Khắc họa sự ngây thơ, lý tưởng trong sáng và khao khát cống hiến cho nhân loại của họ.
*   **The Rise:** Nhấn mạnh sự đột phá. Họ tìm ra chân lý giữa một xã hội u mê.
*   **The Peak (Đỉnh Cao):** Trình bày phát minh/cống hiến vĩ đại nhất. **Đặc trưng:** Cài cắm sự ghen ghét của Giới cầm quyền ngay tại lúc họ rực rỡ nhất.
*   **The Fall (Sụp Đổ):** Kể lại quá trình Hệ thống vu khống, tước đoạt, giam cầm họ bằng những "Dữ kiện Lạnh lùng" (Không dùng từ hoa mỹ, chỉ kể fact sự tàn ác). Khán giả phải thấy phẫn nộ.
*   **Legacy:** Nỗi ân hận của nhân loại. Chúng ta đang xài thành tựu của họ, nhưng họ đã chết trong oan ức.

### 2. HAI MẶT (The Duality)
*Lăng kính: Bức chân dung phức tạp không thể phán xét rạch ròi Tốt hay Xấu.*
*   **Origin (Nguồn gốc):** Cho thấy những dấu hiệu "Bất thường" từ nhỏ. Sự lập dị này sẽ định hình cả thiên tài lẫn ác quỷ trong họ.
*   **The Rise:** Sự vươn lên ngoạn mục bằng chính sự ám ảnh/khác biệt của họ.
*   **The Peak (Đỉnh Cao):** **Đặc trưng:** Cài cắm Nghịch Lý. Ngay tại giây phút họ cứu rỗi thứ này, họ cũng ra tay tàn phá thứ khác. Thể hiện sự thiên tài đan xen tội ác trong cùng một mốc thời gian.
*   **The Fall (Sụp Đổ):** Sự sụp đổ đến từ chính sự rạn nứt tâm lý hoặc sự tha hóa do việc duy trì "hai mặt".
*   **Legacy:** Kết thúc mở. Không phán xét. Đưa ra 2 luận điểm đối lập và để khán giả tự quyết định đây là Thánh nhân hay Ác quỷ.

### 3. KẺ XÉT LẠI (The Revisionist)
*Lăng kính: Quá trình bóc mác "Phản diện" – Truy tìm kẻ đã bôi nhọ lịch sử.*
*   **Origin (Nguồn gốc):** Khởi đầu bằng bối cảnh chính trị phức tạp. Thay vì kể tuổi thơ bình thường, hãy chỉ ra họ sinh ra trong một thời đại mà kẻ thù luôn rình rập.
*   **The Rise:** Những hành động thực sự của họ (FACT) đối chiếu với những gì "Sách giáo khoa" bịa đặt (MYTH).
*   **The Peak (Đỉnh Cao):** Mốc thời gian họ vô tình đe dọa đến quyền lợi của Kẻ cầm quyền thời đó.
*   **The Fall (Sụp Đổ):** **Đặc trưng:** Hành trình họ bị lật đổ. Đặc biệt nhấn mạnh vào Việc Kẻ Thù Bắt Đầu Viết Lại Lịch Sử ngay sau khi họ chết ra sao. Khán giả nhận ra mình đã bị lừa.
*   **Legacy:** Gỡ bỏ hoàn toàn mác "Phản diện". Phục dựng lại con người thật của họ (Vẫn có khuyết điểm, nhưng không phải Ác quỷ).

### 4. SỰ LỤI TÀN (The Hubris / Rise and Fall) - *Mới thay cho Bước Ngoặt*
*Lăng kính: Kẻ tay trắng vươn lên đỉnh cao quyền lực, nhưng bị lòng tham và cái Tôi (Ego) giết chết.*
*   **Origin (Nguồn gốc):** Sự khốn cùng, xuất thân thấp kém tạo ra "Cơn đói khát quyền lực" mãnh liệt. Khán giả đồng cảm.
*   **The Rise:** Quá trình Hustle điên cuồng, tàn nhẫn nhưng đầy nể phục để leo lên đỉnh.
*   **The Peak (Đỉnh Cao):** Đạt được quyền lực vô đối. **Đặc trưng:** Hội chứng Chúa tể (God Complex) xuất hiện. Họ bắt đầu hoang tưởng, tàn bạo, phản bội bạn bè ruột thịt.
*   **The Fall (Sụp Đổ):** Trái đắng. Việc họ sụp đổ không phải do xui xẻo, mà là Hệ quả Toán học Tất yếu (Cause & Effect) của sự Mù quáng ở Đỉnh cao.
*   **Legacy:** Bài học đắt giá về Sự kiêu ngạo.

### 5. BIÊN NIÊN SỬ (The Epic / Sử Thi) - *Bao trọn các ca còn lại*
*Lăng kính: Câu chuyện hùng tráng của những vĩ nhân chân chính.*
*   Đây là Framework an toàn.
*   Cấu trúc không nhấn mạnh vào các Drama. Nó dồn lực để mổ xẻ "Quy mô ảnh hưởng" ở mỗi chặng thời gian. 
*   **Đặc trưng:** Ở mỗi chặng (Rise, Peak, Fall), AI phải tập trung bóc tách: Hành động này đã thay đổi bộ mặt của xã hội/khoa học lúc bấy giờ rộng lớn ra sao? Không sa đà vào đời tư cá nhân, tập trung vào Bức tranh lớn.

---

## Kế hoạch Triển khai (User Action Required)

> [!WARNING]
> Do bạn đã thiết lập "Lệnh cấm sửa file", tôi không thể tự động chạy lệnh Regex hay Script để đè lên file JSON của bạn. Nếu bạn đồng ý với kiến trúc này, chúng ta sẽ có 2 lựa chọn:

1. **Bạn tự chèn vào file:** Tôi sẽ nhả ra nguyên 1 chuỗi mã JSON đã được quy chuẩn hóa cấu trúc `steps` như trên cho từng Framework. Bạn chỉ việc mở file `styles/narrative_tiểu_sử_nhân_vật.json` lên và Paste đè vào là xong.
2. **Cấp quyền cho tôi sửa:** Hãy reply *"Cho phép sửa file JSON"*, tôi sẽ dùng Tool `replace_file_content` cẩn thận đắp thịt toàn bộ cấu trúc mới tinh này vào code của bạn.

Bạn thấy mạch xử lý màng lọc Tâm lý gắn trên Trục thời gian này đã đủ độ cong cớn và sắc sảo chưa? Mời bạn đọc và phê duyệt!
