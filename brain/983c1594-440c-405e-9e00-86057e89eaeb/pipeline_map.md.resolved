# Xác Nhận Tách Bạch: Top/List Review vs Narrative

## Kết luận: ✅ Review và Narrative HOÀN TOÀN TÁCH BẠCH

---

## Top/List Review — Code flow

```
Rewrite tab:
  _job_wrapper → if mode == "Top/List Review" → _do_renew_review()
    → extract_blueprint_review()      ← RIÊNG
    → recommend_framework()            ← CHUNG (không bị sửa)
    → reality_check_blueprint()        ← RIÊNG  
    → verify_specs_google()            ← RIÊNG
    → enrich_prices_google()           ← RIÊNG
    → check_blueprint()               ← RIÊNG
    → create_review_outline()          ← RIÊNG
    → audit_outline_review()           ← RIÊNG (khác audit_outline!)
    → write_review_chapter()           ← RIÊNG
    → review_cross_chapter()           ← RIÊNG
```

> **Review KHÔNG gọi**: `_run_shared_fw_pipeline`, `generate_phase_plan`, 
> `generate_renew_outline_v2`, `audit_outline`, `write_from_blueprint`

---

## Narrative — Code flow

```
New Content tab:
  _new_content_worker → extract_blueprint() → recommend_framework()
    → _run_single_fw → _run_shared_fw_pipeline()
      Step A: generate_phase_plan()          ⚠️ biography code lẫn
      Step B: generate_renew_outline_v2()    ⚠️ nhận phase_plan
      Step C: audit_outline()                ⚠️ diff-based mới
      Step D: write_from_blueprint()         ✅ OK (prompt riêng per niche)
      Step E: review_narrative_full()        ✅ OK (prompt riêng per niche)
      Step F: patch_chapter_overlap()        ✅ OK
      Step G: merge_to_version()             ✅ OK

Rewrite tab:
  _job_wrapper → else → _do_renew_style()
    → _run_shared_fw_pipeline() (dùng lại đúng function trên)
```

---

## Vấn đề chồng chéo: CHỈ xảy ra TRONG Narrative

```
              _run_shared_fw_pipeline()
                    │
        ┌───────────┼───────────┐
     Biography   Mystery     Battle
        │           │           │
  ✅ phase_plan  ❌ CRASH!   ❌ CRASH!     ← biography code lẫn
  ✅ main_key    ✅ fallback  ✅ fallback   ← có fallback key_data
  ✅ audit diff  ⚠️ unknown  ⚠️ unknown   ← có legacy fallback
```

### Kết luận

| Câu hỏi | Trả lời |
|---|---|
| Review có bị ảnh hưởng bởi biography code? | **KHÔNG** ✅ |
| Review dùng chung function nào với Narrative? | `recommend_framework()` — **không bị sửa** ✅ |
| Mystery/Battle có bị ảnh hưởng? | **CÓ** ⚠️ — qua `_run_shared_fw_pipeline` |
| Chỗ nào sẽ crash? | `generate_phase_plan()` — thiếu prompt cho mystery/battle |
