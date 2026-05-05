# Walkthrough: Nâng cấp Step 2a — World Bible

## Tổng quan thay đổi

Tất cả thay đổi nằm trong 1 file: [video_pipeline.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/core/video_pipeline.py)

## 1. Prompt mới — 2 Call Architecture

| Trước | Sau |
|---|---|
| 1 prompt `STEP2_WORLD_BIBLE_PROMPT` | 2 prompts: `STEP2A_IDENTIFY_PROMPT` + `STEP2A_DESCRIBE_PROMPT` |
| LLM vừa đoán era vừa viết visual details | Call 1: xác định era → Call 2: viết details với era đã chốt |

**Call 1 — IDENTIFY** (nhẹ, ~500 tokens output):
- Ép LLM xác định **exact date range** (không chấp nhận "Roman Republic" — phải là "82-44 BC")
- Liệt kê factions với role + allegiance

**Call 2 — DESCRIBE** (nặng, ~3000 tokens output):
- Nhận era/date_range đã chốt từ Call 1 vào system prompt header
- Mô tả visual details chính xác theo đúng date range
- Thêm `role_variants` (general, senator, priest, merchant, slave)
- `heraldry` mô tả vật thể cụ thể (eagle on pole, shield with lion)
- `architecture` là structured array thay vì flat dict
- Bỏ `civilian_clothing` (gộp vào crowd_archetypes)

## 2. Input thay đổi

| Trước | Sau |
|---|---|
| `[{sequence_id, full_text}]` JSON | `cleaned_text` (plain text narrative) |
| Fragmented, có overhead JSON | Liền mạch, tiết kiệm tokens |

## 3. Output schema mới — 3 Domain

```json
{
  "historical_context": { "era", "date_range", "geography" },
  "factions": [{ role_variants, crowd_archetypes, ... }],
  "architecture": [{ name, materials[], structural_elements[], interior, lighting }],
  "props": { military, household, religious, marketplace }
}
```

## 4. Selective downstream injection

| Bước | Trước (inject toàn bộ) | Sau (selective) |
|---|---|---|
| Step 2b | `json.dumps(self.world_bible)` | Chỉ `historical_context` + `factions` |
| Step 2c | `architecture` + `era` + `geo` | Chỉ `historical_context` + `architecture` + `props` |
| Step 3 | Trích field-by-field | Updated cho schema mới + `role_variants` |
| Step 4 | Compact mini bible | Updated đọc từ `historical_context.era` |

## 5. Retry + Error handling

- Cả 2 call đều retry 2 lần
- Validate: Call 1 phải có `era`, Call 2 phải có `factions`
- Fallback: nếu `cleaned_text` trống → build từ sequences

## 6. Backward compatibility

- Checkpoint load: đọc `historical_context.era` trước, fallback về `era` (schema cũ)
- Architecture rendering: kiểm tra `isinstance(arch, dict)` vs `str` để xử lý cả format cũ

## Lưu ý quan trọng

> Nếu đã có checkpoint `_step2_world_bible.json` cũ (schema cũ) → cần XÓA file checkpoint đó để pipeline chạy lại Step 2a với schema mới. Checkpoint cũ vẫn load được nhưng sẽ thiếu `role_variants`, `historical_context`, structured architecture.
