# So Sánh Chapter 2: Prompt CŨ vs Prompt MỚI

## Thống kê

| Metric | Prompt CŨ | Prompt MỚI |
|---|---|---|
| Ngôn ngữ | English | Vietnamese |
| Số từ | ~1,050 | ~530 |
| Số đoạn | 11 | 7 |
| Target | 550 | 550 |
| Sai lệch | **+91%** (gấp đôi target!) | **-4%** (trong range ±10%) |

> [!IMPORTANT]
> Prompt CŨ vượt word count gần gấp đôi. Prompt MỚI nằm đúng target.

---

## Prompt CŨ (English, ~1050 words)

```
There were no strings. No hidden gears. No wind could touch it. He stared 
at it for hours, a profound sense of wonder mixing with a deep unease...

There is a comforting story we tell about this boy. It's a myth designed to 
make genius feel a little less intimidating, a little more human...

The problem was not that he couldn't do the work. The problem was that he 
refused to do it the way he was told...

His real education took place at home. His father and uncle ran an 
electrotechnical company, and the dinner table was often filled with talk 
of dynamos and direct versus alternating current...
```

### Đánh giá prompt CŨ:
- ✅ Có scene (compass scene khá tốt)
- ✅ Có myth-busting (math failure)  
- ⚠️ **Quá dài** — vượt target 91%
- ⚠️ **Nhiều đoạn expository** — đoạn 6-7 về Max Talmud, Petersschule, violin → kể hơn tả
- ⚠️ **Ít micro-tension** — hầu hết là chronological narration
- ❌ **Không có pattern interrupt** — không rhetorical question, không direct address
- ❌ **Không có perspective filtering** — kể từ narrator xa, không qua mắt cậu bé

---

## Prompt MỚI (Vietnamese, ~530 words)

```
Món đồ chơi đơn giản đó là một chiếc la bàn.

Năm 1884, tại Munich, cậu bé Albert Einstein năm tuổi nằm trên giường 
bệnh, sốt cao. Cha cậu, Hermann, chìa ra một vật nhỏ bằng đồng. Bên 
trong, dưới lớp kính, một cây kim kim loại rung lên rồi dứt khoát chỉ 
về một hướng...

Người ta thường kể rằng Albert Einstein học dốt toán. Đó là một trong 
những huyền thoại phổ biến nhất về các thiên tài... Nhưng sự thật, theo 
ghi chép của nhà viết tiểu sử Walter Isaacson, thì hoàn toàn khác...

Nhưng ở trường, mọi thứ thì khác... Một giáo viên từng thẳng thừng 
tuyên bố rằng cậu sẽ chẳng bao giờ làm nên trò trống gì.

...một thiếu niên nổi loạn, sắp từ bỏ cả quốc tịch Đức của mình, 
có thể đi đâu để tái tạo lại bản thân?
```

### Đánh giá prompt MỚI:
- ✅ **Open loop resolve** — "Món đồ chơi đơn giản đó là một chiếc la bàn" → trả lời loop ch.1
- ✅ **Scene building** — compass: time, place, action, sensory detail (rung, kính, đồng)
- ✅ **Perspective filtering** — "cậu bé nằm trên giường bệnh, sốt cao" → qua mắt cậu bé
- ✅ **Myth vs reality** — math failure debunked với source citation (Isaacson)
- ✅ **Micro-tension** — "Đó là lần đầu tiên ông nhận ra có điều gì đó sâu sắc ẩn giấu"
- ✅ **Contrast** — nhà (khuyến khích) vs trường (kỷ luật sắt)
- ✅ **Closing type** — foreshadow_doom: "có thể đi đâu để tái tạo lại bản thân?"
- ✅ **Word count** — 530 words, trong target ±10%
- ⚠️ **Ít pattern interrupt** — không có rhetorical question trực tiếp
- ⚠️ **Sensory detail** — có nhưng ít (chủ yếu ở scene compass)

---

## Kỹ Thuật Mới Áp Dụng Thành Công

| Kỹ thuật | Prompt CŨ | Prompt MỚI |
|---|---|---|
| Show Don't Tell | ⚠️ Có nhưng lẫn với tell | ✅ Compass scene rõ ràng |
| Micro-tension | ❌ Ít | ✅ "run rẩy trong lòng", contrast nhà/trường |
| Information as story | ⚠️ Có lúc data dump | ✅ Facts nhúng vào scene |
| Perspective filtering | ❌ Narrator xa | ✅ Qua mắt cậu bé |
| Show/Tell balance | ❌ Show quá nhiều → dài | ✅ Gọn, tell cho bridging |
| Pattern interrupts | ❌ Không có | ⚠️ Ít |
| Word count compliance | ❌ +91% | ✅ -4% |

---

## Kết Luận

Prompt MỚI tạo ra output **gọn hơn, cinematic hơn, đúng word count hơn**. Điểm yếu còn lại:
1. Pattern interrupts chưa rõ (cần thêm ví dụ tiếng Việt trong prompt?)
2. Sensory detail chưa đều — compass scene tốt nhưng school section ít hơn

> [!TIP]
> Có thể thêm 1 dòng vào prompt: "Include at least 1 rhetorical question per chapter" để enforce pattern interrupts.
