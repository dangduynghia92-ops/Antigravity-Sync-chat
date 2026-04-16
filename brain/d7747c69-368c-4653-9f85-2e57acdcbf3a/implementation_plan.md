# Chẩn Đoán & Kế Hoạch Sửa: Framework Cho Nội Dung Dạng Caliber/Đạn Dược

## Bản chất vấn đề (Đã hiệu chỉnh)

Súng hay đạn **đều là sản phẩm** → Không cần tạo hệ thống framework hoàn toàn riêng biệt. Vấn đề thực sự nằm ở **3 lớp cụ thể** trong pipeline:

---

## Lớp 1: Blueprint Extraction — Trích xuất data chưa đủ

**Hiện tại:** Prompt `system_extract_blueprint_firearms.txt` được thiết kế bóc data của **khẩu súng** (giá, cân nặng, barrel length, trigger pull, capacity...).

**Thiếu gì:** Khi đầu vào là kịch bản về **cỡ đạn** (.45 ACP, .22 LR), cần bóc được các data points hoàn toàn khác:

| Data point cần bóc | Ví dụ từ kịch bản mẫu |
|---|---|
| Chamber pressure (PSI) | 21,000 PSI (.45 ACP) vs 35,000 PSI (9mm) |
| Bullet weight range (grains) | 155gr → 230gr |
| Muzzle velocity (fps) | 830 fps (230gr .45 ACP chuẩn) |
| Ballistic coefficient | 0.206 (.357) vs 0.205 (.44 Mag) |
| Trajectory drop (inches at distance) | -11.92 in tại 100 yards |
| Recoil energy (ft-lb) | 7.77 ft-lb (.357) vs 14.96 ft-lb (.44) |
| Wound channel / terminal ballistics | Case study Dearborn Heights, 1-shot stop data |
| Historical origin & adoption | Chiến tranh Moro 1899, FBI load 158-grain |
| Platform versatility | 1911, PCC, revolver, lever-action, suppressed |
| Handloading data | Case volume, primer type, powder flexibility |
| Ammo cost per round | $0.23/rd (9mm) vs $0.39/rd (.45 ACP) |
| Subsonic capability | Tự nhiên subsonic (850 fps) vs cần đạn chuyên biệt |

> [!IMPORTANT]
> **Quyết định cần:** Bổ sung schema caliber data VÀO prompt extraction hiện tại (thêm nhánh if/else), hay tạo prompt extraction phụ riêng?

---

## Lớp 2: Chapter Structure (Body) — Cấu trúc kể chuyện sai kiểu

Đây là **vấn đề lớn nhất**. Tất cả `chapter_template` hiện tại đều theo mô hình:

```
1 Chapter = 1 SẢN PHẨM (hoặc 1 ROUND so sánh sản phẩm)
```

Nhưng kịch bản đối thủ dạng caliber dùng mô hình hoàn toàn khác:

```
1 Chapter = 1 KHÍA CẠNH / TOPIC BLOCK của cỡ đạn
```

**Ví dụ cụ thể từ kịch bản .45 ACP (Video 1):**

| Chapter | Nội dung | Kỹ thuật chính |
|---------|----------|----------------|
| Block 1 | Cội nguồn: Chiến tranh Moro, .38 Long Colt thất bại | Historical Case Study |
| Block 2 | M1917 Revolver, Half-moon clips | Platform Versatility |
| Block 3 | Đập tan lầm tưởng giật mạnh (21,000 PSI) | Physical Translation + Myth Bust |
| Block 4 | Biến thể: .45 Super, .460 Rowland, .45 GAP | Evolution / Variants |
| Block 5 | Thực chiến: Tunnel Rats Việt Nam, Sub-guns | Scenario Painting + History |
| Block 6 | Handloading + Suppressor | Technical Deep-Dive |
| Block 7 | Long guns: Marlin Camp Carbine, Kriss Vector | Platform Expansion |

**Ví dụ từ kịch bản .357 vs .44 (Video 5, dạng Duel):**

| Chapter | Nội dung | Kết quả round |
|---------|----------|---------------|
| Ch 1 | Cartridge Architecture (kích thước, dung tích vỏ) | .44 thắng (40% volume) |
| Ch 2 | Exterior Ballistics (velocity, drop, energy) | .44 thắng nhẹ |
| Ch 3 | Terminal Performance (sức phá hủy mô) | .44 thắng nhưng over-penetrate |
| Ch 4 | Physics of Recoil (ft-lb đá vào cổ tay) | .357 thắng (7.7 vs 14.9) |
| Ch 5 | Final Verdict | .357 thắng tổng thể cho 90% người dùng |

> [!IMPORTANT]
> **Cần tạo `chapter_template` mới** theo dạng Topic Block cho 2 loại kịch bản:
> - **Single-caliber:** Mỗi chapter = 1 topic (History, Ballistics, Recoil, Application, Limitation)
> - **Caliber-vs-caliber:** Mỗi chapter = 1 tiêu chí ballistic so sánh (giống Head-to-Head nhưng với tiêu chí cỡ đạn thay vì tiêu chí súng)

---

## Lớp 3: Hook & End — Cần điều chỉnh

**Hook hiện tại** được xây cho review sản phẩm:
- `damning_verdict_first` → Phán xét 1 khẩu súng cụ thể
- `stress_test_cold_open` → Test thực tế 1 khẩu súng
- `provocative_caliber_question` → ✅ Cái này gần đúng nhưng vẫn focus sản phẩm

**Hook cần cho kịch bản caliber:**
- **Nostalgia/Legacy opener:** "The .45 ACP has been dropping hammers since 1911..."
- **Mythical claim opener:** ".38 Special is dead — or is it?"
- **Controversy/War opener:** "9mm vs .45: the debate that never dies"

**End chapter cần:**
- Chốt verdict **theo tình huống sử dụng** (tủ đầu giường dùng .45, ra đường dùng 9mm) thay vì chốt "khẩu súng nào thắng"
- Case study punchline (vụ cưa chân Dearborn Heights) thay vì spec summary

---

## Proposed Changes

### [MODIFY] [Review_súng_đạn.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/Review_s%C3%BAng_%C4%91%E1%BA%A1n.json)
- Thêm **2 frameworks mới** vào mảng `frameworks[]`:
  - **"The Caliber Anatomy":** Single-caliber deep-dive, chapter_template theo Topic Block
  - **"The Caliber Duel":** Caliber-vs-Caliber head-to-head, chapter_template theo tiêu chí ballistic
- Bổ sung `hook_methods` mới: `nostalgia_legacy_opener`, `controversy_war_opener`
- Cập nhật `technique_emphasis`: đẩy `Scenario Painting`, `Visceral Analogy`, `Appeal to Authority` lên `use_heavily`

### [MODIFY] [system_extract_blueprint_firearms.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_extract_blueprint_firearms.txt)
- Bổ sung schema trích xuất cho dữ liệu caliber/ammo (PSI, grain, fps, ballistic coefficient, trajectory, recoil energy, adoption history, cost-per-round)

### [MODIFY] [system_review_outline_firearms.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_review_outline_firearms.txt)
- Bổ sung quy tắc outline cho Topic Block chapter (thay vì product-per-chapter)

### [MODIFY] [system_write_review_firearms.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_write_review_firearms.txt)
- Bổ sung body chapter elements cho dạng caliber (Physical Translation, Case Study, Historical Anchoring)

---

## Câu Hỏi Cần Bạn Xác Nhận

1. Bạn muốn đặt tên 2 framework mới là gì? Tôi đề xuất: **"The Caliber Anatomy"** (mổ xẻ 1 cỡ đạn) và **"The Caliber Duel"** (so sánh 2 cỡ đạn). Có OK không?
2. Schema blueprint cho caliber data nên **bổ sung vào prompt extraction hiện tại** hay **tạo extraction prompt riêng**?
3. Ngoài 5 kịch bản mẫu, bạn còn dạng kịch bản nào khác liên quan tới đạn dược mà tôi cần tham khảo thêm trước khi viết framework không?
