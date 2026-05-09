# Crowd Pipeline — Bug Fix Log

## Tổng kết: 7 bugs đã fix

Nguyên nhân gốc: tôi chỉ thêm crowd data vào **internal pipeline steps** mà không trace đến **output cuối cùng** (Excel, flat_prompt).

### Bug #1: Step 3.2 input thiếu crowd_labels
- **Triệu chứng**: `crowd_labels: []` ở mọi scene
- **Root cause**: `seq_for_llm` không có field `crowd_labels`
- **Fix**: Thêm `crowd_labels` vào `seq_for_llm`

### Bug #2: Post-Step3 không propagate crowd  
- **Triệu chứng**: Scene có crowd nhưng `crowd_labels` rỗng
- **Root cause**: Audio_sync loop không copy `crowd_labels` từ filmable_scenes
- **Fix**: Thêm fallback propagation

### Bug #3: Step 3.2 Rule 6 thiếu hướng dẫn crowd_labels
- **Triệu chứng**: LLM không biết cần fill `crowd_labels` nào
- **Root cause**: Rule 6 chỉ nói `has_crowd = true/false`, không hướng dẫn chọn EXT-* labels
- **Fix**: Mở rộng Rule 6

### Bug #4: Step 4 template dùng sai tên reference
- **Triệu chứng**: flat_prompt không mention EXT-* labels
- **Root cause**: Prompt nói `crowd_archetypes` thay vì `[EXT-*]`
- **Fix**: Sửa rule + extras field description

### Bug #5: Step 2d thiếu sheet_prompt
- **Triệu chứng**: Không thể gen ảnh tham chiếu cho crowd
- **Root cause**: Output format không có field `sheet_prompt`
- **Fix**: Thêm vào JSON template

### Bug #6: Excel Sheet 1 thiếu cột Crowd
- **Triệu chứng**: User không thấy crowd nào ở mỗi scene
- **Root cause**: Sheet 1 chỉ có 9 cột, không có Crowd
- **Fix**: Thêm cột "Crowd" (cột G)

### Bug #7: Excel Sheet 2 thiếu crowd reference images
- **Triệu chứng**: Chỉ có 4 character + locations, không có crowd
- **Root cause**: `_export_excel` chỉ loop `self.characters_data`, bỏ qua `self.crowd_data`
- **Fix**: Thêm crowd block với Type="Crowd"
