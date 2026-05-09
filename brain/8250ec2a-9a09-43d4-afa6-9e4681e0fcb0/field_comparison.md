# So sánh Fields: Character vs Crowd — Từng Step

## Step 2: Dữ liệu gốc (Character Sheet)

| Field | Character | Crowd | Giống? |
|---|:---:|:---:|---|
| `label` | ✅ | ✅ | ✅ |
| `visual_description` | ✅ | ✅ | ✅ (cùng format BODY/FACE/COSTUME/Acc) |
| `sheet_prompt` | ✅ | ✅ | ✅ |
| `default_stance` | ✅ | ✅ | ✅ |
| `original_name` | ✅ | ❌ | ⚠ Crowd không có |
| `faction` | ❌ | ✅ | ⚠ Character không có |
| `crowd_type` | ❌ | ✅ | ⚠ Character không có |
| `group` | ❌ | ✅ (`CROWD`) | ⚠ Character không có |

> **Kết luận Step 2**: Cả hai đều có `visual_description` chi tiết đầy đủ (BODY, FACE, COSTUME, Acc). **Không thiếu.**

---

## Step 3: Scene Data

| Field | Character | Crowd |
|---|:---:|:---:|
| `character_labels` | ✅ `['Ayyubid-Commander-A']` | — |
| `crowd_labels` | — | ✅ `['EXT-Ayyubid-Soldier-Infantry']` |
| `physical_action` | ✅ Mô tả hành động char | ✅ Có thể bao gồm crowd action |
| `character_interaction` | ✅ | ❌ Không có `crowd_interaction` |
| `has_crowd` | — | ✅ true/false |

> **Kết luận Step 3**: Crowd có label + action chung trong `physical_action`. **Không thiếu nghiêm trọng.**

---

## Step 4: Prompt Output — ĐÂY LÀ CHỖ CHÊNH LỆCH LỚN

| Field | Character | Crowd | Giống? |
|---|:---:|:---:|---|
| `characters` | ✅ Label list | — | — |
| `character_info` | ✅ **Full visual description** | — | — |
| `characters_detail` | ✅ **Costume JSON chi tiết** | — | — |
| `crowd_labels` | — | ✅ Label list | — |
| `extras` | — | ✅ Mô tả text (LLM tự viết) | — |
| `flat_prompt` | ✅ Chi tiết costume | ⚠ **Costume sơ sài** | ❌ |

> [!WARNING]
> ## Vấn đề cốt lõi
> **Step 4 gửi cho LLM thông tin KHÔNG ĐỐI XỨNG:**
> 
> | Input cho LLM | Character | Crowd |
> |---|---|---|
> | Label | ✅ `Ayyubid-Commander-A` | ✅ `EXT-Ayyubid-Soldier-Infantry` |
> | Costume LOCKED | ✅ **Chi tiết từ visual_description** | ❌ **KHÔNG GỬI** |
> | Action | ✅ `physical_action` | ❌ Không riêng |
> | Default stance | — | ❌ **KHÔNG GỬI** |
> 
> → LLM có costume character nên viết chính xác, nhưng **không có costume crowd** nên phải tự bịa hoặc viết sơ sài.

---

## Fix cần làm

Thêm vào Step 4 (`_process_sequence_step4`):
1. **crowd_costume_lookup**: build từ `self.crowd_data` giống `costume_lookup`
2. **Gửi costume crowd** trong `scenes_text_parts`, ví dụ:
   ```
   Crowd Costume (LOCKED — copy exactly):
       [EXT-Ayyubid-Soldier-Infantry]: yellow padded cotton kazaghand, iron skullcap, wooden recurve bow...
   ```
