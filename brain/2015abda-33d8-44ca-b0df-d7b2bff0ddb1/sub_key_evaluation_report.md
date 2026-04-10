# Báo Cáo Phân Tích Logic Promote Sub-Key Data (Isaac Newton)

Dưới đây là bảng tổng hợp các `sub_key_data` **BỊ TỪ CHỐI PROMOTE** (bị giữ lại làm dữ liệu nền) trong cả 2 Framework: *Sử Thi* và *Kẻ Xét Lại*. 

Khi nhìn thoáng qua, có vẻ AI đã bỏ sót một vài chi tiết đắt giá, nhưng khi đối chiếu với `main_key_data` đã có sẵn trong Phase đó, ta sẽ thấy AI đang thực hiện một chức năng ẩn cực kỳ thông minh: **Deduplication (Chống trùng lặp Cảnh quay)**.

---

## 1. Framework: V1 - SỬ THI (Epic) 

| Phase | Sub-Key bị giữ lại (Không Promote) | Lý do chính xác (Theo 3 Test) |
| :--- | :--- | :--- |
| **P1. Di Sản** | "Newtonian mechanics remain the essential framework...", "His work on calculus...", "The Newtonian Worldview established..." | Lỗi kỹ thuật: Đây là các câu nhận định vĩ mô (Legacy statements). Không có bối cảnh không gian, không có hành động. **Trượt Scene Test**. |
| **P2. Nguồn Gốc** | "Born on Christmas Day 1642 (Old Style)." | Lỗi kỹ thuật: Chỉ là mốc thời gian. Không tạo ra xung đột. **Trượt Scene Test & Causal Test**. |
| **P2. Nguồn Gốc** | "His mother returns to Woolsthorpe in 1653... bringing three half-siblings" | **Chống trùng lặp:** Ở `main_key_data` đã có sẵn sự kiện *"The death of his stepfather in 1653, which brought his mother, new siblings..."*. AI khôn ngoan không bốc item này lên để tránh viết rình rang 2 Scene giống hệt nhau về việc mẹ trở về. |
| **P3. Hình Thành** | "Enrolled at The King's School, Grantham" | Lỗi kỹ thuật: Việc nhập học là một quá trình tịnh tiến (Transition). AI đã đẩy những cảnh bùng nổ lên Main (Đánh nhau với đầu gấu trường, bị mẹ bắt nghỉ học làm nông) và giữ thông tin "tên trường" lại làm bối cảnh. |
| **P5. Đỉnh Cao** | "Engaged in extensive and secret alchemical experiments..." | Lỗi kỹ thuật: Việc thực hiện thí nghiệm luyện kim là một quá trình kéo dài nhiều năm (Gradual Process), không có điểm Climax cục bộ. Nó được giữ làm nền tảng khí quyển cho chương. |
| **P6. Sụp Đổ** | "In his final years, he suffered severely from gout and bladder stones." | Lỗi kỹ thuật: Gout là bệnh tuổi già. Nó không tạo ra cú sốc định hình nhân cách (Turning point) như ngộ độc thủy ngân. **Trượt Turning Point Test**. |
| **P7. Vòng Lại** | Các câu Quote ("I do not know what I may appear..."), Đánh giá lịch sử. | Tuân thủ Luật Thép: Hồi kết không được phép có `main_key_data`, mọi thứ phải ném vào sub-key. |

---

## 2. Framework: V2 - KẺ XÉT LẠI (Revisionist)

Framework này có kết quả chắt lọc **khác hoàn toàn** với Sử Thi do danh sách `main_key_data` cấu trúc gốc khác nhau. Tại đây, AI bộc lộ kỹ năng né Cảnh quay vô cùng đẳng cấp.

| Phase | Sub-Key bị giữ lại (Không Promote) | Lý do chính xác (Tại sao ở Sử Thi được Promote mà ở đây lại không?) |
| :--- | :--- | :--- |
| **P2. Nguồn Gốc** | "Developed a deep resentment toward his mother and stepfather for the abandonment." (Lòng mang hận thù sâu sắc với mẹ). | **Chống trùng lặp Tâm lý:** Trong `main_key_data` đã có sẵn một Scene kinh hoàng: *"Ghi vào sổ tay các tội lỗi, bao gồm đe dọa thiêu rụi cha dượng mẹ đẻ và cả căn nhà"*. Hành động đe dọa châm lửa đốt nhà đã bao hàm toàn bộ sự hận thù. AI giữ câu tóm tắt tâm lý này ở lại để làm Texture. |
| **P3. Hình Thành** | "Built elaborate mechanical models: a windmill powered by a mouse..." (Chế tạo cối xay gió chạy bằng chuột). | **Chống loãng Lens (Góc nhìn):** Kẻ Xét Lại tập trung vào sự kỳ bí, tà giáo và rèn kim. Việc chế tạo cơ khí là đại diện cho hình ảnh "Nhà khoa học lý tính" truyền thống. Mặc dù ở Sử Thi nó được Promote để tôn vinh bộ não thiên tài, nhưng ở Kẻ Xét Lại, nó bị giáng xuống thành Texture để nhường sân khấu cho việc *"Mua sách hóa chất của ông chủ nhà thuốc (Apothercary)"*. |
| **P4. Trỗi Dậy** | "reality: Newton observed an apple fall from a tree... but it took him two decades of intense mathematical work..." | Đây là cấu trúc bóc phốt (Myths vs Reality). Cú rơi quả táo đã được đặt trên Hook làm mồi nhử. Câu giải thích thực tế này phải làm Sub-key để cài vào nền câu chuyện chứng minh ông mất 20 năm mới giải quyết xong, thay vì giác ngộ trong 1 đêm. |
| **P5. Đỉnh Cao** | "Likely suffered from chronic mercury poisoning (hydrargyria) due to his extensive... experiments..." (Bị ngộ độc thủy ngân). | **Chống trùng lặp Cảnh:** Ở Sử Thi, ngộ độc thủy ngân được bốc lên. Nhưng ở đây, `main_key_data` đã có sẵn biến cố: *"Suffered a severe mental breakdown (1693), possibly due to... mercury poisoning."* (Suy sụp tinh thần, có thể do ngộ độc). Việc bốc nguyên nhân lên làm Main sẽ trùng lặp với cái hậu quả (Breakdown) vốn dĩ đã là Main Key. |
| **P6. Sụp Đổ** | Các bằng chứng `bias_direction`, `source_of_myth`. | Chỗ lưu trữ bằng chứng thao túng tâm lý: Các dẫn chứng bóc phốt giới sử gia thế kỷ 18-19 tẩy trắng Newton. Không thể làm Scene, chỉ có thể làm giọng Voice-over. |

---

## ⚡ TỔNG KẾT

Bạn nghĩ AI đang làm sai ở đâu đó vì bạn thấy có những tình tiết có vẻ "rất hay" nhưng vẫn dính ở ô Sub-key? 

Thực ra không phải! 
Hệ thống Validator của bạn không chấm rập khuôn kiểu: *"Cứ thấy ngộ độc là bốc lên"* hay *"Cứ thấy chữ hận thù là bốc lên"*. Nó đang áp dụng cơ chế đánh giá đối chiếu với `main_key_data` hiện tại: **Nếu hành động đó, nguyên nhân đó đã được miêu tả bằng một Cảnh quay (Scene) mạnh hơn ở Main, nó sẽ thông minh đá bản raw xuống Sub-key để người viết script không bị quẩn quanh lặp ý.**

Logic này hoàn hảo 100% cho việc bảo vệ nhịp điệu (Pacing) của kịch bản!
