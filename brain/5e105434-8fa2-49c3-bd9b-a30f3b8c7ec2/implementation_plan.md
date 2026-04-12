# Thống Nhất Kiến Trúc Pipeline 3 Bước Phân Chương (Phase Planning) Cho Niche Trận Đánh

Mục tiêu: Loại bỏ hoàn toàn sự rẽ nhánh hardcode (chỉ ưu tiên Tiểu sử nhân vật) trong `script_creation_tab.py`. Thay vào đó, thiết kế hệ thống theo hướng rẽ nhánh động (Data-driven): Bất kỳ Niche nào khai báo file Prompt `_phase_plan` trong bảng Map sẽ tự động được hưởng cơ chế cắt chương 3 bước (A1: Phase Plan → A2: Validate Sub-keys đa luồng → A3: Chia chương ngẫu nhiên Toán học). 
Đồng thời, bổ sung bộ Prompts 3 bước này cho Niche "Phân tích trận đánh" (Battle).

## User Review Required

> [!IMPORTANT]
> Việc gỡ bỏ Hardcode `_is_biography` và chuyển sang check tự động `_has_phase_plan` sẽ giúp hệ thống của bạn mở rộng dễ dàng sau này. Niche `mystery` (Bí ẩn) hiện vẫn tự động dùng cơ chế Single-shot cũ do không khai báo `_phase_plan`, không bị ảnh hưởng. Nếu bạn duyệt, tôi sẽ tiến hành refactor hệ thống.

## Proposed Changes

### Core Logic & UI

#### [MODIFY] `core/rewriter.py`
- Bổ sung key `narrative_phase_plan` và `validate_sub_key` vào `_NICHE_PROMPT_MAP` dành cho tập khóa của Battle (battle, war, military, trận, chiến...).
- Cập nhật hàm `validate_phase_plan_sub_keys`:
  - Thêm tham số `niche` để gọi hàm `_require_niche_prompt("validate_sub_key", niche)`.
  - Thay vì lấy cứng `bp_life_phases`, sẽ làm vòng lặp linh hoạt lấy ra các keys trọng tâm của Blueprint (như `battle_phases`, `turning_points`, v.v) tùy theo Blueprint nào có chứa để nạp vào Context cho AI tham chiếu.

#### [MODIFY] `ui/script_creation_tab.py`
- Thay thế hoàn toàn cờ `_is_biography` bằng `_has_phase_plan` sử dụng try-catch lệnh `_get_niche_prompt("narrative_phase_plan", niche)`. Niche nào có đăng ký Prompt Phase Plan sẽ mặc định chạy luồng 3 bước, Niche nào không có sẽ chạy Single-shot. Nhờ vậy, không cần động vào file giao diện nữa mỗi khi thêm Niche hạng nặng.

---

### Battle Phase Prompts

Cần khởi tạo và điều chỉnh các file Prompt dành riêng cho Battle mô phỏng theo tiến trình của Tiểu sử:

#### [NEW] `prompts/system_narrative_phase_plan_battle.txt`
- Prompt chuyên làm nhiệm vụ Bước A1: Đọc Blueprint Trận đánh (được tổng hợp từ extract) và Framework, chia nhỏ toàn bộ diễn biến thành các Phase hành động theo Framework.
- Ép AI phân loại Data thành `main_key_data` (Biến cố/Bước ngoặt quân sự) và `sub_key_data` (Chi tiết nhỏ lẻ, tiểu cảnh).

#### [NEW] `prompts/system_validate_sub_key_battle.txt`
- Prompt dùng ở Bước A2 (Validate đa luồng): Chuyên dùng để AI cân nhắc lại liệu 1 sự kiện `sub_key_data` có đáng bị giáng cấp không?
- Đặt ra 3 bài test quân sự:
  1. *Test Chuyển Biến (Turning Point Test)*: Sự kiện này có thay đổi cán cân chiến thắng không?
  2. *Test Góc Cận (Scene Test)*: Sự kiện này có đủ dữ kiện thị giác đẫm máu/choáng ngợp để đạo diễn tua chậm làm 1 pha action không?
  3. *Test Độc Lập (Causal Independence)*: Nếu cắt bỏ sự kiện này, chiến thắng/thất bại tổng thể có trở nên vô lý không?
- Nếu thỏa mãn, AI trả về lệnh `PROMOTE`.

#### [MODIFY] `prompts/system_narrative_outline_battle.txt`
- Loại bỏ toàn bộ phần ép AI tự làm Chain-of-Thought (CoT) phân rã `phase_chapter_plan`.
- Sửa lại mô tả Output để nó nhận trực tiếp cụm JSON `phase_chapter_plan` do Code truyền từ hàm A3 vào, AI chỉ việc sinh ra chi tiết cho biến `chapters[]`.

## Verification Plan

### Manual Verification
1. Chọn 1 Niche Tiểu Sử và 1 Niche Trận Đánh, chạy lại chế độ Rewrite:
   - Dò log thấy Niche Tiểu Sử vẫn chạy qua 3 Bước "Phase planning..." -> "Validating sub_key_data..." -> "Apply chapter splits".
   - Dò log thấy Niche Trận Đánh ĐÃ CHẠY qua 3 Bước y hệt như trên thay vì gọi 1 api "planning phases".
   - Chọn Niche Mystery, thấy nó vẫn nhảy qua luồng Single-shot an toàn.
2. Kiểm tra chất lượng Outline gốc `chapters[]` sinh ra từ Trận đánh để đảm bảo không bị thừa/thiếu tham số so với version cũ.
