# Audit: Promote/Demote Conditions cho main_key_data

## Bộ rules hiện tại

### PROMOTE → main (L16-21)
| Rule | Điều kiện |
|---|---|
| **P1** | `turning_points` + `conflicts` → LUÔN main |
| **P2** | `key_events` IF singular milestone → main |
| **P3** | `achievements` IF concrete + major → main |

### DEMOTE → sub (L23-33)
| Rule | Điều kiện |
|---|---|
| **D1** | Vague gradual processes ("Educated in Turkish") |
| **D2** | Vague legacy statements ("Became known as great thinker") |
| **D3** | Consequences that are ONLY transitions ("Traveled back") |

### RESCUE (L31-33)
| Rule | Điều kiện |
|---|---|
| **R1** | SCENE TEST: Can consequence be developed into SCENE? → giữ main |

---

## Xung đột phát hiện từ Constantine

### ❌ Xung đột 1: `damnatio memoriae` bị D3 demote sai
**Hiện tại**: SUB — *"Emitió damnatio memoriae borrando los nombres de Crispo y Fausta"*
**Lý do**: D3 coi là "consequence/transition" → demote
**Thực tế**: Đây là HÀNH ĐỘNG CHỦ Ý (xóa con trai khỏi lịch sử) — rất dark, rất scene-worthy. SCENE TEST lẽ ra phải cứu.

### ❌ Xung đột 2: Crispus chỉ huy fleet bị D2 demote sai
**Hiện tại**: SUB — *"Crispo demostró ser un comandante brillante al liderar la flota"*
**Lý do**: D2 nghĩ là "legacy statement"
**Thực tế**: Có scene cụ thể (chỉ huy fleet, đánh bại armada) — và quan trọng vì Crispus BỊ GIẾT SAU ĐÓ → build up cần thiết.

### ❌ Xung đột 3: "Dividió el imperio" bị D3 demote sai
**Hiện tại**: SUB — *"Dividió el imperio entre sus tres hijos... provocó purgas sangrientas"*
**Lý do**: D3 coi là "transition to next event"  
**Thực tế**: Là quyết định gây hậu quả lớn (purgas sangrientas) — scene-worthy.

---

## Nguyên nhân gốc

**DEMOTE rules (D1-D3) quá mạnh, RESCUE rule (R1) quá yếu.** AI ưu tiên demote trước, SCENE TEST là afterthought.

Cụ thể:
- D3 nói *"Consequences that are ONLY transitions"* nhưng AI hiểu rộng → bất kỳ consequence nào cũng bị demote
- R1 (SCENE TEST) chỉ áp dụng cho "consequences" → không cover dark events bị D2 nuốt

---

## Đề xuất sửa

### 1. Thêm cửa `dark events` vào PROMOTE (thay `achievements`):
```diff
- ✓ achievements ONLY IF concrete, major milestones that anchor a life phase.
+ ✓ dark events from dark_psychology.moral_compromises, dual_nature.dark_side,
+   or scandals_and_controversies — IF they describe a SPECIFIC ACTION
+   with a clear subject, victim/target, and consequence.
+   ✗ Vague character traits → sub_key_data.
```

### 2. Mở rộng SCENE TEST (R1) để cover TẤT CẢ events, không chỉ consequences:
```diff
- SCENE TEST: Can this consequence be developed into its own SCENE?
+ SCENE TEST: Can this event be developed into its own SCENE
+   (with setting, tension, and resolution)?
+   Apply to ALL events — not just consequences.
+   If YES → main_key_data. Do NOT demote scene-worthy events.
```

### 3. Thêm ví dụ dark vào DEMOTE exceptions:
```diff
  [sub_key_data]:
    ✗ Vague gradual processes
+   EXCEPTION: deliberate actions with victim/target are NOT "vague processes"
+     ✓ main: "Erased his own son's name from all public monuments" (damnatio memoriae)
+     ✗ sub:  "Tended toward authoritarianism" (vague trait)
```

> [!IMPORTANT]
> Thay đổi nằm hoàn toàn trong `system_narrative_phase_plan_biography.txt` (L12-33). Không ảnh hưởng code pipeline hay các prompt khác.
