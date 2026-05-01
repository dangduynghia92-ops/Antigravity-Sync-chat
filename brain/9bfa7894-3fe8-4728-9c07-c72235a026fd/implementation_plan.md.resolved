# Implementation Plan: New Niche "POV Biography"

*Kế hoạch này được chia nhỏ và thực hiện theo từng bước. Hiện tại chỉ tập trung vào **Bước 1: Research Blueprint**.*

## Mục tiêu Bước 1
Xây dựng bộ công cụ trích xuất dữ liệu (Blueprint) riêng cho Niche POV Biography. Dựa trên Blueprint của "Tiểu sử", chúng ta sẽ giữ lại gần như toàn bộ sự đồ sộ của dữ liệu để AI có nguyên liệu "Show, Don't Tell", **chỉ loại bỏ 2 trường thừa thãi** theo yêu cầu: `myths_vs_reality` và `legacy_and_historiography`.

---

## Proposed Changes (Step 1 Only)

### Phase A: Cấu hình Prompts (Tạo file mới)

#### 1. Tạo `system_research_blueprint_pov_biography.txt`
- **Nguồn:** Clone từ `system_research_blueprint_biography.txt`.
- **Hành động:** 
  - Xóa bỏ Field: `myths_vs_reality`.
  - Xóa bỏ Field: `legacy_and_historiography`.
  - **Bổ sung luật:** Ép buộc AI phải tìm kiếm và đính kèm **Độ tuổi (Age)** và các **Chi tiết giác quan/tả thực (Sensory details)** vào các sự kiện trong `life_phases` và `conflicts` để phục vụ cho văn phong Cinematic của POV sau này.

#### 2. Tạo `system_audit_pov_biography_blueprint.txt`
- **Nguồn:** Clone từ `system_audit_biography_blueprint.txt`.
- **Hành động:** 
  - Điều chỉnh file schema để khớp với Blueprint mới (không còn 2 trường đã xóa).
  - Nghiêm cấm AI nhét dữ liệu rác vào trường `additional_findings` (đưa các chi tiết thừa vào `texture_and_hooks` hoặc loại bỏ).

#### 3. Tạo `system_crossref_pov_biography_blueprint.txt`
- **Nguồn:** Clone từ `system_crossref_biography_blueprint.txt`.
- **Hành động:** Chỉnh sửa tương tự Audit, loại bỏ 2 trường không cần thiết và đảm bảo việc gộp dữ liệu từ 3 luồng Research diễn ra trơn tru.

*(Tùy chọn: `system_enrich_blueprint_pov_biography.txt` nếu cần đào sâu thêm các yếu tố dark_psychology).*

### Phase B: Code Wiring (`core/rewriter.py`)

#### 1. Khai báo Research Sections
Tạo 3 hằng số section mới dành riêng cho POV (dựa trên các trường của Blueprint mới) để chia tải cho AI khi gọi API:
- `_POV_BIO_RESEARCH_SECTION_A`: Tập trung vào Tuổi thơ, Bản ngã, Ngoại hình, Vices & Obsessions, Bệnh lý.
- `_POV_BIO_RESEARCH_SECTION_B`: Tập trung vào Hành trình (Life Phases), Thành tựu, Sự kiện bước ngoặt (Turning Points).
- `_POV_BIO_RESEARCH_SECTION_C`: Tập trung vào Xung đột (Conflicts), Các mối quan hệ (Key relationships), và Cái chết (Death & Funeral).

#### 2. Cập nhật hàm `_get_research_sections()`
- Thêm logic rẽ nhánh để hệ thống nhận diện Niche:
```python
elif "pov_biography" in niche_lower or "pov" in niche_lower:
    return [_POV_BIO_RESEARCH_SECTION_A, _POV_BIO_RESEARCH_SECTION_B, _POV_BIO_RESEARCH_SECTION_C]
```

---

## User Review Required

> [!IMPORTANT]
> Đây là bản kế hoạch CHỈ dành cho **Bước 1 (Research)**. 
> - Việc loại bỏ 2 trường `myths_vs_reality` và `legacy_and_historiography` đã được cập nhật.
> - Việc ép AI tìm "Độ tuổi" và "Chi tiết tả thực" vào các sự kiện có phù hợp với mong muốn của bạn không?
> 
> Xin hãy xem xét và phê duyệt để tôi bắt đầu viết Prompt và Code cho riêng Bước 1 này. Sau khi hoàn thành và test xong Bước 1, chúng ta mới lên kế hoạch cho Bước 2.
