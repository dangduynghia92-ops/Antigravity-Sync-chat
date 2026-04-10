# So sánh Prompt: Hiện tại vs Cải tiến

> Câu gốc: *"El joven Galileo creció en una casa donde el aire vibraba con esta herejía."*

## So sánh kết quả

````carousel
### Version A — Prompt hiện tại (style suffix ở cuối)

![Version A - Current pipeline output](C:\Users\Admin\.gemini\antigravity\brain\d2556abd-b5f2-4289-9934-a66c2d200c59\version_a_current_1775717505655.png)

**Prompt kiểu cũ**: Mô tả cảnh thuần túy → append `Mandatory Style: ...` ở cuối

```
Interior of a modest 16th-century Italian home in Pisa, warm candlelight 
illuminating a cluttered wooden table... A young boy around 10 years old 
with dark curly hair, wearing a simple linen tunic...

[APPENDED AT END] Classical oil painting, Baroque chiaroscuro, 
Rembrandt lighting, thick impasto brushstrokes...
```

<!-- slide -->
### Version B — Prompt cải tiến (chất liệu sơn dầu xen trong mô tả)

![Version B - Enhanced anti-digital output](C:\Users\Admin\.gemini\antigravity\brain\d2556abd-b5f2-4289-9934-a66c2d200c59\version_b_enhanced_1775717520503.png)

**Prompt cải tiến**: Chất liệu sơn dầu **đan xen ngay trong mô tả** + từ khóa anti-digital

```
A classical oil painting with visible thick impasto brushstrokes and 
cracked varnish surface depicting the interior... rough-spun linen tunic 
with visible fabric weave... The paint is applied in thick ridges on the 
illuminated skin... thin transparent glazes allow warm undertones to glow...
Palette knife textures visible on the stone wall... museum-aged patina 
with yellowed varnish warmth... 

NOT a digital painting, NOT 3D render, NOT concept art.
```
````

---

## Phân tích sự khác biệt

### Vấn đề của Version A (pipeline hiện tại)

| Vấn đề | Giải thích |
|---|---|
| **Style keywords ở cuối** | Nhiều model AI (đặc biệt Stable Diffusion, Nano/Banana) **không đọc hết prompt** — token cuối bị "attention decay" |
| **Mô tả chất liệu trừu tượng** | "simple linen tunic" — không nói rõ chất liệu vải thô, sợi dệt |
| **Thiếu mô tả kỹ thuật vẽ** | Không có "thick paint ridges", "glazes", "varnish" trong phần scene description |
| **Negative prompt yếu** | Chỉ nói "Avoid photorealism" — cần nói rõ "NOT digital painting, NOT 3D render, NOT concept art, NOT Artstation" |

### Giải pháp trong Version B

| Cải tiến | Kỹ thuật |
|---|---|
| **Medium-first** | Mở đầu bằng "A classical oil painting with visible thick impasto brushstrokes" — model biết ngay đây là tranh |
| **Chất liệu xen kẽ** | "rough-spun linen with visible fabric weave", "worn wool doublet with dull brass buttons" — mô tả như đang vẽ, không chụp ảnh |
| **Kỹ thuật vẽ cụ thể** | "paint applied in thick ridges", "thin transparent glazes", "palette knife textures" — ép model hiểu quy trình sơn dầu |
| **Tuổi tranh** | "museum-aged patina", "yellowed varnish warmth", "cracked varnish surface" — tạo cảm giác tranh cổ |
| **Anti-digital mạnh** | "NOT a digital painting, NOT 3D render, NOT concept art" — phủ định trực tiếp |

---

## Kết luận

> [!IMPORTANT]
> Vấn đề **không nằm ở style file**, mà nằm ở cách `flat_prompt` được tạo ra. Hiện tại AI (Gemini Flash) tạo `flat_prompt` chỉ mô tả **nội dung cảnh** — không mô tả **chất liệu vẽ** bên trong prompt. Style suffix được append ở cuối nhưng nhiều model gen ảnh **bỏ qua token cuối**.

### Cần sửa gì?

Cần thêm instruction vào style file `Rembrandt Candlelight Historical.txt` yêu cầu AI **bắt buộc nhúng từ khóa chất liệu sơn dầu vào trong flat_prompt**, không phải chỉ mô tả cảnh:

1. Mở đầu flat_prompt bằng `"A classical oil painting with visible brushstrokes depicting..."`
2. Xen kẽ mô tả kỹ thuật vẽ (impasto, glazes, palette knife) vào giữa mô tả cảnh
3. Kết thúc bằng anti-digital keywords: `"NOT digital, NOT 3D, NOT concept art"`
