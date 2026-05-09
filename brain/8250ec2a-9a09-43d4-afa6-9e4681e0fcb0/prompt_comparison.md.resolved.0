# So sánh Prompt Nhân Vật: v1 (cũ) vs v2 (mới)

## 1. Nhân vật chính (Step 2b)

| Label | v1 (cũ) | v2 (mới) |
|---|---|---|
| Ayyubid-Commander-A | ✅ Có | ✅ Có (visual_description thay đổi nhẹ) |
| Jerusalem-King-A | ✅ Có | ❌ Đổi thành → **Jerusalem-Commander-A** |
| Assassin-Leader-A | ✅ Có | ❌ Đổi thành → **Nizari-Commander-A** |
| Assassin-Warrior-A | ✅ Có | ❌ Đổi thành → **Nizari-Servant-A** |

### Ayyubid-Commander-A — visual_description thay đổi:

```diff
- steel lamellar cuirass worn over a yellow silk kaftan with black eagle embroidery
+ yellow silk kaftan with gold thread embroidery over iron lamellar armor, red linen sirwal
```

> `sheet_prompt` format: **GIỐNG NHAU** — cả 2 đều dùng template chuẩn 3 góc (front, 3/4, side).

---

## 2. Crowd Characters (Step 2d)

| Metric | v1 | v2 |
|---|---|---|
| Số lượng | **0** | **16** |
| sheet_prompt format | N/A | "Full body front view" (1 góc — **chưa chuẩn**) |

> [!WARNING]
> Trong checkpoint JSON, crowd sheet_prompt vẫn là format cũ (1 góc). Code Excel export mới đã override bằng template 3 góc, nhưng chỉ khi re-run pipeline.

---

## 3. Excel Sheet 2 — Reference Images

| Metric | v1 | v2 |
|---|---|---|
| Tổng rows | **4** (chỉ characters) | **20** (4 chars + 16 crowd) |
| Crowd entries | ❌ Không có | ✅ 16 entries, Type = "Crowd" |

### Prompt style thay đổi (cột F):

```diff
- oversized round simplified faces with flat white fill and oval dot eyes
+ circular geometric heads, uniform flat white (#FFFFFF) graphic fill for all exposed parts, minimalist facial features
```

> Đây là do style file `Chibi Storybook Historical.txt` đã được sửa mandatory_style trong phiên trước.

---

## Tóm tắt thay đổi chính

1. **Label convention** thay đổi: `Assassin-*` → `Nizari-*`, `Jerusalem-King` → `Jerusalem-Commander`
2. **Costume description** chi tiết hơn (thêm material, color cụ thể)
3. **Crowd**: 0 → 16 characters, có prompt + description đầy đủ
4. **Style prefix**: đã update theo bản sửa art style prompt
