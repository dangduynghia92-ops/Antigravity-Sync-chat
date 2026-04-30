# Đánh giá Pipeline Output — Baldwin IV (11 chapters)

## Tổng quan

| Step | Output | Đánh giá |
|---|---|---|
| Step 0 | 244 sentences, 11 files | ✅ |
| Step 1 | 56 sequences | ✅ |
| Step 2a | 11 characters | ⚠️ |
| Step 2b | 14 locations | ✅ |
| Step 2c | 1 era, 16 items | ✅ |
| Step 3 | 156 scenes | ✅ |
| Step 4 | 156 prompts (100% label usage) | ✅ |

---

## Step 1: Sequences — ✅ Tốt

**56 sequences** từ 11 chapters, phân loại:
- **Physical**: 32 seq (57%) — có location rõ
- **Abstract**: 16 seq (29%) — ẩn dụ, suy tư
- **Montage**: 8 seq (14%) — nhiều location/thời gian

> [!TIP]
> `location_type` hoạt động tốt! Abstract/montage đều có `location_shift: ""` đúng như thiết kế.

**Duration**: 1.5s – 24.2s, đa số trong khoảng 5-15s ✅

---

## Step 2a: Characters — ⚠️ Có vấn đề

**11 characters** nhưng **tất cả `original_name` đều TRỐNG**:

| Label | original_name |
|---|---|
| `Crusader-King-A-Child` | *(trống)* |
| `Crusader-King-A-Teen` | *(trống)* |
| `Saracen-Sultan-A` | *(trống)* |

> [!WARNING]
> **`original_name` trống** → Cột "Character Info" mới thêm sẽ không hiển thị tên thật.
> Nguyên nhân: LLM Step 2a có thể không output field `original_name`, hoặc schema không yêu cầu.

**Lifecycle đúng**: Baldwin có 3 stage (Child, Teen, YoungAdult) ✅
**Labels rõ ràng**: Crusader-King, Royal-Tutor, Saracen-Sultan... ✅

---

## Step 2b: Locations — ✅ Tốt

**14 locations** đa dạng, đúng bối cảnh:
- Palace Courtyard, Balcony, Interior
- King's Bedchamber, Throne Room
- Battlefield of Montgisard
- Saladin's Army Camp

---

## Step 2c: World Bible — ✅ Tốt

1 era, đủ 4 categories:
- Military: 3 items
- Civilian: 6 items
- Weapons: 3 items
- Architecture: 4 items

> [!NOTE]
> `era` field trống — LLM không ghi tên era. Nên kiểm tra prompt Step 2c.

---

## Step 3: Scenes — ✅ Tốt

**156 scenes** từ 56 sequences (trung bình 2.8 scenes/seq)

**Shot types phân bố đều**:
- Medium Shot: 56 (36%)
- Wide Shot: 55 (35%)
- Close-up: 45 (29%)

> [!TIP]
> Không có Extreme Close-up ✅ — Rule 4 hoạt động.

**Location consistency**: SEQ_05 (montage, `location_shift: ""`) → được gán `Throne Room` ✅

---

## Step 4: Prompts — ✅ Tốt

- **156/156 prompts** chứa `[Label]` brackets (100%) ✅
- Mở đầu đúng style: "A stylized historical animation illustration with thick dark outlines depicting..."
- Labels chính xác: `[Crusader-King-A-Child]`, `[Palace Courtyard]`
- Costume mô tả cụ thể: "dust-stained 12th-century white linen tunic"

---

## Vấn đề cần fix

### 1. ❌ `original_name` trống trong Step 2a
- **Ảnh hưởng**: Cột "Character Info" trong Excel sẽ không có tên nhân vật thật
- **Cần**: Kiểm tra Step 2a prompt có yêu cầu field `original_name` không

### 2. ⚠️ `era` trống trong World Bible
- **Ảnh hưởng**: Không hiển thị tên thời đại trong reference
- **Cần**: Kiểm tra Step 2c prompt

### 3. ⚠️ Tỷ lệ abstract/montage cao (43%)
- 24/56 sequences không có physical location
- Có thể khiến nhiều scenes kế thừa location → visual lặp
- **Cần theo dõi**: Xem flat_prompt có đa dạng không

---

## Điểm chất lượng

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| Sequence segmentation | 9/10 | location_type hoạt động tốt |
| Character extraction | 7/10 | Labels đúng nhưng thiếu original_name |
| Location extraction | 9/10 | Đa dạng, đúng bối cảnh |
| World Bible | 7/10 | Đủ data nhưng era trống |
| Scene design | 9/10 | Shot types đều, không có extreme close-up |
| Prompt writing | 9/10 | 100% label usage, style đúng |
| **Tổng** | **8.3/10** | |
