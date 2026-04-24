# Anti-Plagiarism Fix — Content Originality

## Root Cause Analysis

### Bug 1: `alternative_rhetoric` bị mất (Race Condition)

`transform_rhetoric()` chạy **song song** với enrichment trong `ThreadPoolExecutor` (Step 5). Cả hai đều ghi vào `blueprint` object rồi save `_blueprint.json`.

```
Thread A (enrichment):  blueprint["detailed_facts"] = ... → save _blueprint.json  ✓
Thread B (rhetoric):    blueprint["alternative_rhetoric"] = ... → save _blueprint.json  ✓ (nhưng ghi sau)
```

**Nhưng thực tế:** `_bp_write_lock` chỉ lock file write, không lock blueprint object. Enrichment ghi `_blueprint.json` SAU rhetoric → **đè mất `alternative_rhetoric`** vì enrichment copy KHÔNG có field mới.

**Bằng chứng:** `_blueprint.json` không chứa `alternative_rhetoric` hay `author_rhetoric`. `_rhetoric_transform.json` chứa alternatives nhưng KHÔNG ai đọc lại nó.

### Bug 2: Ranking order bị copy (Subjective data leak)

Code ĐÚNG LÀ ĐÃ shuffle products + strip `source_parts`, `comparisons`. Nhưng AI vẫn thấy:

| Field | Chứa gì | Ảnh hưởng |
|-------|--------|-----------|
| `author_rhetoric` | "Número uno indiscutible" (DDM4) | AI biết DDM4 = #1 |
| `myths_misconceptions` | PSA: "rifle $1200, sợ trộm → mua rẻ" | AI copy argument này |
| `practical_use_case.reason` | Savage: "limited to 2 cartridges" | AI suy ra Savage = low rank |
| `comparisons` | Đã strip ✅ | — |
| `source_parts` | Đã strip ✅ | — |

**Kết quả:** AI đọc subjective opinions → reconstruct ranking gốc → output y hệt.

---

## Proposed Fixes

### Fix 1: Merge `alternative_rhetoric` đúng cách

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

Sau khi cả enrichment + rhetoric transform hoàn thành, **đọc lại `_rhetoric_transform.json` và merge vào blueprint** trước khi save final. Đồng thời **thay thế** `author_rhetoric` bằng `alternative_rhetoric` (không giữ cả hai).

### Fix 2: Strip subjective fields trước khi gửi outline AI

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

Khi tạo `outline_blueprint` (deep copy trước shuffle), strip thêm:
```python
prod.pop("author_rhetoric", None)       # chứa ranking clues
prod.pop("myths_misconceptions", None)  # chứa subjective arguments  
```
**GIỮ LẠI `alternative_rhetoric`** — đây là data sạch, do AI tạo mới.

### Fix 3: Thêm anti-ranking-copy rule vào outline prompt

#### [MODIFY] [system_review_outline_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_review_outline_firearms_v2.txt)

Thêm rule mới:
```
## RANKING INDEPENDENCE (MANDATORY)
- You MUST create your OWN ranking based on the angle's primary_criterion
- DO NOT replicate the source's ranking order
- Re-evaluate each product's position based strictly on the data_focus fields you selected
```

## Verification

1. Re-run pipeline trên "10 Truck Guns"
2. So sánh ranking order → PHẢI khác bản gốc
3. Kiểm tra Kel-Tec → KHÔNG có "briefcase/maletín"
4. Kiểm tra PSA → KHÔNG có "stolen gun/sợ trộm"
