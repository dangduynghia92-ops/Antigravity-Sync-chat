# Fix Blueprint Data Loss & Improve Content Quality

## Mô tả vấn đề

Pipeline Review Súng Đạn mất toàn bộ `detailed_facts` (26 items → string "NP3 coating") do **3 bugs kết hợp**, dẫn đến kịch bản output spam NP3 ở 7/8 chapters trong khi video gốc chỉ nhắc 1 lần.

## Các lỗi cần fix

### Bug 1: `_strip_source_tags()` không nhận đúng format của `detailed_facts`

> [!CAUTION]
> Bug này khiến source tags **không bị strip** khỏi `detailed_facts`, gây hỗn loạn cho các step downstream.

**File**: [script_creation_tab.py#L3296-3305](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py#L3296-L3305)

**Vấn đề**: Hàm tìm pattern `{"value": X, "source": Y}` (2 keys), nhưng extraction prompt sinh format `{"fact": X, "source": Y}` (cũng 2 keys, nhưng key khác). Kết quả: source tags tồn tại trong blueprint qua tất cả steps downstream.

**Fix**: Mở rộng `_strip_source_tags` để nhận cả pattern `{"fact", "source"}`:
```diff
 if isinstance(obj, dict):
     if "value" in obj and "source" in obj and len(obj) == 2:
         return obj["value"]
+    if "fact" in obj and "source" in obj and len(obj) == 2:
+        return obj["fact"]
     return {k: ScriptCreationTab._strip_source_tags(v) for k, v in obj.items()}
```

---

### Bug 2 (CRITICAL): Correction code ghi đè array bằng scalar

> [!CAUTION]
> Đây là bug phá hủy dữ liệu chính, xóa sạch 26 data points.

**File**: [script_creation_tab.py#L4411-4416](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py#L4411-L4416)

**Vấn đề**: Reality Check AI trả `field: "detailed_facts"` với `correct_value: "NP3 coating"`. Code dòng 4416 `bp_prod[field] = correct` ghi đè mù quáng — array 26 items → string "NP3 coating".

**Fix**: Thêm type guard — khi target field là `list`, tìm & sửa element bên trong thay vì ghi đè toàn bộ:

```python
# Apply corrections
for chk in vp.get("ai_knowledge_checks", []):
    if chk.get("verified") is False and chk.get("correct_value"):
        field = chk.get("field", "")
        correct = chk["correct_value"]
        ai_val = chk.get("ai_value", "")
        if field and field in bp_prod:
            existing = bp_prod[field]
            if isinstance(existing, list):
                # Field is an array (e.g. detailed_facts) — find & fix
                # the specific element containing ai_value, don't overwrite all
                _patched = False
                for item in existing:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            if isinstance(v, str) and ai_val and ai_val in v:
                                item[k] = v.replace(ai_val, correct)
                                _patched = True
                                break
                    elif isinstance(item, str) and ai_val and ai_val in item:
                        idx = existing.index(item)
                        existing[idx] = item.replace(ai_val, correct)
                        _patched = True
                    if _patched:
                        break
                if _patched:
                    n_corrections += 1
            else:
                bp_prod[field] = correct
                n_corrections += 1
        else:
            # ... existing nested dot-notation logic ...
```

---

### Bug 3: Reality Check prompt không hướng dẫn AI trả `field` chính xác cho array elements

**File**: [system_reality_check_firearms.txt](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_reality_check_firearms.txt)

**Vấn đề**: Prompt không có rule cho trường hợp correction nằm bên trong array. AI trả `field: "detailed_facts"` thay vì chỉ rõ element nào.

**Fix**: Thêm rule mới vào prompt:

```
ARRAY FIELD CORRECTION RULE:
If the incorrect value is INSIDE an array field (e.g., one item in `detailed_facts`),
set `field` to the array field name (e.g., "detailed_facts") and set `ai_value` to the
EXACT incorrect text from the specific array item. The downstream code will use `ai_value`
to locate and patch the correct element. Do NOT set `correct_value` to the full corrected
array — only provide the corrected TEXT for that single item.
```

---

## Proposed Changes

### Component 1: Source Tag Stripping

#### [MODIFY] [script_creation_tab.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

**`_strip_source_tags()`** (L3296-3305): Thêm pattern `{"fact", "source"}` để strip đúng format extraction prompt.

---

### Component 2: Array-Safe Correction Application

#### [MODIFY] [script_creation_tab.py](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

**Correction loop** (L4411-4430): Thêm `isinstance(existing, list)` guard. Khi field trỏ vào array, dùng `ai_value` để tìm element chứa lỗi và patch in-place thay vì ghi đè array.

---

### Component 3: Prompt Hardening

#### [MODIFY] [system_reality_check_firearms.txt](file:///F:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_reality_check_firearms.txt)

Thêm explicit rule hướng dẫn AI cách correction cho array fields.

---

## Verification Plan

### Manual Verification

1. **Re-run pipeline trên video Barrett M107A1 50 BMG**: Chạy lại pipeline Review với sample video đã có. So sánh `_blueprint.json` mới vs cũ:
   - `detailed_facts` phải giữ nguyên array 26 items (không bị overwrite thành string)
   - Source tags `{"fact": ..., "source": ...}` phải được strip thành string thuần (chỉ giữ fact value)
   - "MP3" phải được sửa thành "NP3" **bên trong** array element, không phải thay thế toàn bộ array

2. **Kiểm tra output chapters**: Đếm số lần "NP3" xuất hiện. Phải giảm từ 7/8 chapters xuống mức hợp lý (1-2 chapters liên quan trực tiếp tới coating/surface).

> [!IMPORTANT]
> Anh có thể verify bằng cách chạy lại pipeline trên cùng video sample và so sánh kết quả `_blueprint.json`. Nếu anh không muốn re-run pipeline (tốn API calls), tôi có thể viết 1 script test nhỏ chạy offline để simulate `_strip_source_tags` + correction flow trên data thực từ `_blueprint_raw.json` + `_reality_check.json` đã có sẵn.
