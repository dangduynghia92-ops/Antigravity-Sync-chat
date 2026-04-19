# Enhancing "Dark Data" in Biography Blueprint

## Problem

Blueprint hiện tại có 6 fields liên quan "dark": `dual_nature.dark_side`, `vices_and_obsessions`, `dark_impact`, `downfall_pattern`, `scandals`, `conflicts`. Nhưng chúng chỉ capture **SỰ KIỆN** — không capture **TÂM LÝ** đằng sau. Kết quả: narrative kể cuộc đời đều đều, giai đoạn nào cũng như nhau.

**User muốn:** Pipeline phải ưu tiên trích xuất data "dark" — nguyên nhân, diễn biến, hậu quả, giằng xé nội tâm, góc khuất tâm lý. Dùng taxonomy dark types (Tragic, Existential, Machiavellian, Fanatical, Complicit) để AI biết TẬP TRUNG vào đâu.

## Proposed Changes

### Research Blueprint Prompt

#### [MODIFY] [system_research_blueprint_biography.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_research_blueprint_biography.txt)

**Thêm field mới `dark_psychology`** (Section 25) sau optional domain-specific fields:

```json
"dark_psychology": {
  "dark_type": "Tragic | Existential | Machiavellian | Fanatical | Complicit | Mixed",
  "dark_type_description": "1-2 dòng mô tả dạng dark phù hợp nhân vật",
  "internal_conflicts": [
    {
      "conflict": "Mô tả xung đột nội tâm",
      "trigger": "Gì gây ra",
      "manifestation": "Biểu hiện bên ngoài",
      "resolution_or_escalation": "Giải quyết hay leo thang"
    }
  ],
  "moral_compromises": [
    {
      "situation": "Tình huống buộc phải chọn",
      "choice_made": "Họ đã chọn gì",
      "cost": "Cái giá phải trả",
      "justification": "Họ tự biện minh thế nào"
    }
  ],
  "psychological_wounds": [
    {
      "wound": "Tổn thương tâm lý cụ thể",
      "cause_event": "Sự kiện gây ra",
      "age_when_inflicted": "Khi nào",
      "lifelong_effect": "Ảnh hưởng suốt đời"
    }
  ],
  "pattern_of_darkness": "Mô tả 2-3 câu: pattern lặp lại xuyên suốt cuộc đời (chuỗi self-sabotage, escalation of power, moral decay, etc.)"
}
```

**Thêm DARK DATA PRIORITY instruction** vào COMPLETENESS RULES:

```
DARK DATA PRIORITY:
- Dark psychology data is the HIGHEST PRIORITY for narrative engagement
- For every life_phase, ask: "What was the darkest thing that happened here?"
- For every achievement, ask: "What did it COST them psychologically?"
- For every relationship, ask: "Was there betrayal, manipulation, or sacrifice?"
- THIN phases (childhood, education) can be brief. THICK phases (conflict, downfall, moral crisis) need maximum detail
- If a person seems "clean" — dig deeper: everyone has moral compromises, fears, and inner demons
```

**5 dark types (taxonomy cho AI):**

| Dark Type | Tên Tiếng Việt | Đặc Trưng | Ví Dụ |
|-----------|----------------|-----------|-------|
| **Tragic** | Bi kịch & Tự hủy hoại | Self-destruction, addiction, talent wasted, karmic suffering | Van Gogh, Nikola Tesla, Alexander the Great |
| **Existential** | Hiện sinh & Ám ảnh | Inner torment, obsession, meaninglessness, haunting memories | Dostoevsky, Nietzsche, Oppenheimer |
| **Machiavellian** | Quyền lực & Tham vọng | Calculated manipulation, ruthless decisions, ends justify means | Napoleon, Catherine the Great, Genghis Khan |
| **Fanatical** | Lý tưởng & Cuồng tín | Blind faith, ideological extremism, sacrificing others for a cause | Robespierre, Torquemada, Mao Zedong |
| **Complicit** | Đạo đức giả & Đồng lõa | Looking the other way, moral cowardice, benefiting from evil | Many scientists under Nazi/Soviet regimes |

> [!IMPORTANT]
> **KHÔNG thêm field vào mọi section.** Chỉ thêm 1 field `dark_psychology` ở root level. Các field hiện có (`vices_and_obsessions`, `downfall_pattern`, `dark_impact`) giữ nguyên — chúng capture SỰ KIỆN, field mới capture TÂM LÝ.

### Output Schema

Thêm `dark_psychology` object vào JSON output schema (sau `downfall_pattern`).

### No Other Files Need Changes

- **`rewriter.py`**: Không cần sửa — `_extract_chapter_blueprint()` đã scan ALL remaining sections cho fuzzy key_data matching. `dark_psychology` sẽ tự động được include khi chapter key_data mention liên quan.
- **Style JSON / frameworks**: Không cần sửa — frameworks đã có `evaluation_focus` dùng `dark_side`, `downfall_pattern` etc. Field mới là **supplementary data** cho writer.
- **Writer prompt**: Không cần sửa — writer đã có rule "weave data INTO narrative". Data hay hơn → narrative hay hơn.
- **Outline prompt**: Không cần sửa — outline picks key_data từ blueprint. Nhiều dark data hơn → outline tự chọn dark key_data hơn.

## Verification Plan

### Manual Verification
1. Chạy pipeline với 1 nhân vật (Galileo hoặc nhân vật mới)
2. Check `_blueprint.json` → xem `dark_psychology` field có xuất hiện không
3. Check `dark_type` có đúng taxonomy không
4. Check `internal_conflicts`, `moral_compromises`, `psychological_wounds` có chi tiết không
5. So sánh output narrative trước/sau → dark data có làm story hay hơn không
