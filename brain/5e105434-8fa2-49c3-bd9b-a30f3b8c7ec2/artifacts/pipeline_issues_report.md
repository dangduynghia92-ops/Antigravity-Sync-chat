# Báo Cáo Phân Tích: Đứt Gãy Mạch Truyện Trong Pipeline (Chuyên Đề: Tàu Hải Tặc / Chiến Hạm)

Qua quá trình mổ xẻ các file prompt lõi của hệ thống, đặc biệt là ngách Pirate/Ship (`system_narrative_phase_plan_pirate.txt`), tôi đã xác định được nguyên nhân cốt lõi dẫn đến việc kịch bản được tạo ra bị cứng nhắc, thiếu sự liên kết và xáo trộn hoàn toàn về dòng thời gian (như bạn đã thấy ở các Chapter 4 đến 9 trong *Queen Anne's Revenge*).

Dưới đây là chi tiết và đề xuất giải pháp.

---

## Vấn Đề Trọng Tâm: Lỗi Xáo Trộn Dòng Thời Gian (Chronological Fragmentation)

### Biểu Hiện Thực Tế
Trong kịch bản *Queen Anne's Revenge*:
- Phase **Bánh Răng Sinh Học** (Chap 4, 5) mô tả hoàn toàn về đời sống ngột ngạt và y tế của hải tặc. Ở cuối Chap 5 có gieo điểm yếu (mớn nước sâu).
- Phase **Thử Lửa** (Chap 6, 7) đùng một cái quay lại kể trận đấu súng hào hùng với HMS Scarborough.
- Phase **Cái Chết Vật Lý** (Chap 8, 9) lại quay về mô tả vụ mắc cạn do mớn nước sâu.
- Các chi tiết bị cưỡng ép, đứt gãy trình tự thời gian (ví dụ: tàu bị cướp từ tháng 11/1717, đánh Scarborough đầu năm 1718, phong tỏa Charleston tháng 5/1718, rồi mắc cạn tháng 6/1718). Thay vì diễn biến tự nhiên, mọi sinh hoạt bị dồn hết vào Chap 4,5, còn đánh nhau dồn hết vào Chap 6,7.

### Nguyên Nhân Gốc Rễ
- Sự khác biệt về quy định (Rules) khi gán sự kiện vào Phase. Trong nhóm Biography (`system_narrative_phase_plan_biography.txt`), rule là **CHRONOLOGICAL MAPPING** (Nhóm theo thời gian, không bao giờ được xáo trộn).
- Nhưng trong file của Pirate (`system_narrative_phase_plan_pirate.txt`), rule lại đang là **THEMATIC MAPPING** (Nhóm Cứng theo Chủ Đề):
  - AI bị trói buộc: Tất cả những sự kiện là `ship_life_and_crew`, `economics` phải tống hết vào phase `Bánh Răng`.
  - Tất cả những sự kiện là `combat_events` phải tống hết vào phase `Thử Lửa`.
- **Hệ quả:** Mặc dù Vòng Đời Tàu (Chiếm đoạt -> Vận Hành -> Suy Tàn) rất logic, nhưng AI lại phải "bóc" toàn bộ các trận đánh ra khỏi mốc thời gian của nó để nhét riêng vào một chỗ. Điều này phá nát trải nghiệm "vòng đời tự nhiên" của một sự vật.

### Đề Xuất Nâng Cấp Tận Gốc
- **Cập nhật File Prompt Phiên Bản Mới:** Thay đổi toàn bộ rule trong `system_narrative_phase_plan_pirate.txt` từ `THEMATIC MAPPING` thành **CHRONOLOGICAL LIFE-CYCLE MAPPING**.
- **Luật Cốt Lõi Mới:** Vẫn giữ nguyên các Phase theo vòng đời (Sinh ra -> Vận hành -> Đỉnh cao/Kinh hoàng -> Suy tàn), nhưng **BUỘC AI phải rải sự kiện tiến lên theo dòng thời gian lịch sử**. 
  - Nghĩa là: Không xé lẻ mảng đời sống và chiến đấu. Nếu một trận chiến diễn ra ở giai đoạn sớm, nó sẽ nằm trong Phase rèn luyện (Bánh Răng); nếu một sự kiện đời sống mang tính bước ngoặt xảy ra giữa trận đánh lớn, nó sẽ nằm ở Phase Đỉnh cao (Thử Lửa).
  - Đời sống và chiến đấu phải đan xen vào nhau tự nhiên theo dòng thời gian nhằm thúc đẩy tuyến quan hệ Nguyên Nhân - Kết Quả (Cause & Effect).

---
**Kết Luận:** Điều chỉnh trên sẽ giải phóng AI khỏi sự gò bó của chủ đề cứng nhắc. Trả lại một kịch bản có tính "người kể chuyện" tự nhiên, tuần tự và theo đúng nhịp đập vòng đời thăng trầm của một chiến hạm.
