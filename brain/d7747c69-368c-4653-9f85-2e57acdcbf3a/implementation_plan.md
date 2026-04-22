# Thiết kế Data Fields cho Blueprint Súng/Đạn

## 1. Khán giả muốn biết gì?

Tổng hợp từ 5 kịch bản mẫu + nghiên cứu audience:

### Nhóm khán giả và ưu tiên data

| Nhóm | Data ưu tiên hàng đầu |
|------|----------------------|
| **Phòng vệ (Self-Defense)** | Penetration depth, expansion, recoil, over-penetration risk, reliability |
| **Thể thao/bắn chính xác** | Velocity consistency (SD), ballistic coefficient, grouping, trajectory |
| **Săn bắn** | Energy transfer, terminal performance at range, bullet weight retention |
| **Mua sắm/so sánh** | Price per round, availability, platform compatibility, aftermarket |

### Data xuất hiện nhiều nhất trong 5 kịch bản mẫu

| Data point | Số lần xuất hiện (5 video) | Ví dụ |
|-----------|--------------------------|-------|
| Chamber pressure (PSI) | 4/5 | "21,000 PSI — barely half the 9mm's 35,000" |
| Muzzle velocity (fps) | 5/5 | "830 fps", "1250 fps vs 1350 fps" |
| Bullet weight (grains) | 5/5 | "230-grain", "158gr", "240gr" |
| Recoil comparison | 4/5 | "7.7 ft-lb vs 14.9 ft-lb" |
| Penetration/over-penetration | 3/5 | "mất động năng khi xuyên tường" |
| Origin/history | 4/5 | "Moro Rebellion", "1911", FBI load history |
| Price per round | 2/5 | "$390/1000 vs $230/1000" |
| Platform list | 3/5 | "Ruger SP101, Charter Arms, Colt Cobra" |
| Variants/loadings | 3/5 | ".45 Super 1100fps, .460 Rowland 1300fps" |
| Barrel length effect | 2/5 | "16-18 inch optimal for .22 LR" |

---

## 2. Nên tách riêng Súng vs Đạn không?

### Phân tích

| Tiêu chí | Gộp chung | Tách riêng |
|----------|-----------|-----------|
| **Data khác biệt** | ❌ Súng có: trigger, ergonomics, accuracy, aftermarket. Đạn có: ballistic coefficient, penetration, expansion, powder charge. Gộp → nhiều field trống vô nghĩa | ✅ Mỗi loại chỉ có field phù hợp |
| **Nội dung thực tế** | ❌ Video .45 ACP focus 90% vào đạn nhưng phải điền field "trigger", "ergonomics" | ✅ Blueprint biết đây là đạn → chỉ yêu cầu data đạn |
| **Enrich** | ❌ Không biết bổ sung "penetration depth" hay "trigger pull weight" | ✅ Thấy `terminal_performance: {}` trống → biết cần search gel test data |
| **Complexity** | ✅ 1 schema duy nhất | ⚠️ 2 schema, nhưng có shared fields |

> [!IMPORTANT]
> **Khuyến nghị: TÁCH RIÊNG**, nhưng bằng cách dùng `product_type` field để AI tự phân loại, không cần tạo 2 file prompt riêng. Cùng 1 extract prompt, dựa vào `product_type` mà fill field phù hợp.

---

## 3. Đề xuất Schema Data Fields

### Shared fields (cả súng và đạn)

```json
{
  "product_name": "...",
  "product_type": "firearm | ammunition | accessory",
  "category": "...",
  "key_specs": {},
  "origin_history": [],
  "tactical_application": [],
  "cost_availability": {},
  "myths_misconceptions": [],
  "comparisons": [],
  "author_rhetoric": [],
  "source_units": "imperial|metric|mixed"
}
```

### Firearm-specific fields (khi `product_type = "firearm"`)

```json
{
  "ergonomics_handling": {
    "weight": "", "overall_length": "", "barrel_length": "",
    "grip_feel": "", "controls_layout": "", "sight_system": ""
  },
  "action_mechanism": {
    "action_type": "", "trigger_type": "", "trigger_pull_weight": "",
    "safety_mechanism": "", "feeding_system": ""
  },
  "accuracy_precision": {
    "effective_range": "", "grouping_data": "", "barrel_twist_rate": ""
  },
  "reliability_durability": {
    "known_issues": [], "round_count_tested": "", "failure_types": []
  },
  "aftermarket_customization": {
    "rail_system": "", "stock_options": [], "aftermarket_support_level": ""
  },
  "platform_variants": []
}
```

### Ammunition-specific fields (khi `product_type = "ammunition"`)

```json
{
  "cartridge_specs": {
    "bullet_weight_gr": "", "bullet_diameter": "", "case_length": "",
    "overall_length": "", "powder_charge": "", "primer_type": ""
  },
  "internal_ballistics": {
    "chamber_pressure_psi": "", "muzzle_velocity_fps": "",
    "muzzle_energy_ftlb": "", "velocity_consistency_sd": "",
    "test_barrel_length": ""
  },
  "external_ballistics": {
    "ballistic_coefficient": "", "bc_model": "G1|G7",
    "trajectory_drop": {},
    "wind_drift": {},
    "effective_range": ""
  },
  "terminal_performance": {
    "penetration_depth_inches": "", "expansion_diameter": "",
    "weight_retention_pct": "", "sectional_density": "",
    "over_penetration_risk": ""
  },
  "recoil_profile": {
    "recoil_impulse_ftlb": "", "felt_recoil_description": "",
    "physical_translation": ""
  },
  "available_loadings": [],
  "compatible_platforms": []
}
```

---

## 4. Có nên xây dựng ĐẦY ĐỦ tất cả fields?

> [!TIP]
> **KHÔNG cần fill 100%.** Schema đầy đủ nhưng extract/enrich chỉ fill **fields có data**. Fields trống = cơ hội cho enrich step bổ sung. Nguyên tắc:

| Giai đoạn | Kỳ vọng fill rate |
|-----------|-------------------|
| **Extract** (từ transcript) | 40-60% — transcript thường chỉ cover 1 số khía cạnh |
| **Enrich** (AI + search) | 70-85% — bổ sung specs từ manufacturer data, gel test results |
| **Writer** (sử dụng) | Chỉ dùng fields có data — không bịa field trống |

**Lợi ích chính:** Fields trống chính là **trigger để enrich biết cần bổ sung cái gì**. Hiện tại `detailed_facts` không có field trống → enrich vô tác dụng. Với schema mới, `terminal_performance: {}` trống → enrich biết phải search gel test data.

---

## 5. Scope ảnh hưởng nếu triển khai

| File | Cần sửa | Mức độ |
|------|---------|--------|
| `system_extract_blueprint_firearms.txt` | Thay đổi output schema | 🔴 Lớn |
| `system_enrich_blueprint_firearms.txt` | Hướng dẫn fill fields cụ thể | 🔴 Lớn |
| `system_review_outline_firearms.txt` | Cập nhật reference đến field mới | 🟡 Nhỏ |
| `system_write_review_firearms.txt` | Cập nhật field reference | 🟡 Nhỏ |
| `Review_súng_đạn.json` | topic_pool.use_when map đến field mới | 🟡 Nhỏ |
| `rewriter.py` | `_extract_chapter_blueprint()` cần hỗ trợ field mới | 🟡 Kiểm tra |
| **Các niche khác** | ✅ Không ảnh hưởng | ✅ 0 |
