# Fix: Hook luôn mở bằng "mentira / lời nói dối"

## Vấn đề

6/6 hook outputs gần nhất đều mở bằng pattern "lie/deception":
- "te ha vendido una **mentira**" (3 lần)
- "es una **trampa**"
- "La **falsa** premisa"
- "La **ilusión** de $2,000"

## Root Cause Analysis

Chuỗi tạo hook: **Outline prompt** → tạo `depth_focus` → **Writer prompt** nhận `depth_focus` → viết hook.

### Nguồn gốc 1: Outline prompt (system_review_outline_firearms_v2.txt line 28)
```
GOOD depth_focus: "The market sells a $2,000 illusion — the data exposes which platforms actually deliver"
```
→ AI outline **copy pattern "illusion/lie"** vào mọi depth_focus.

**Bằng chứng**: 5/5 outline outputs có depth_focus chứa "ilusión", "falsa premisa", hoặc "paradoja".

### Nguồn gốc 2: Writer prompt (system_write_review_firearms_v2.txt line 80-84)
```
- Ranking: ...why the conventional ranking wisdom is wrong.
- Catalog: ...why the viewer's current knowledge is incomplete.
- Head-to-Head: ...why this comparison matters and what's at stake.
- Deep Dive: ...what the consensus gets wrong about this single product/topic.
```
→ Mọi framework đều dùng ngôn ngữ "sai/thiếu/wrong" → AI hiểu hook = phải vạch trần sai lầm.

### Nguồn gốc 3: Style JSON hook_methods (Review_firearms_v2.json line 113)
```json
"damning_verdict_first": {
    "description": "Deliver a shocking verdict that breaks consensus..."
}
```
→ AI ưu tiên chọn method này vì nó aggressive nhất.

## Proposed Changes

### [MODIFY] [system_review_outline_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_review_outline_firearms_v2.txt)

**Line 26-28**: Thay example "illusion" bằng example trung tính + thêm BAD example chặn pattern lừa dối:

```diff
- GOOD depth_focus: "The market sells a $2,000 illusion — the data exposes which platforms actually deliver"
+ BAD depth_focus: "The market sells a $2,000 illusion" (cliché — NEVER use lie/deception/illusion framing)
+ GOOD depth_focus: "One $400 entry outperforms three guns at triple the price — and the reason has nothing to do with specs"
```

---

### [MODIFY] [system_write_review_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_write_review_firearms_v2.txt)

**Line 80-84**: Rewrite framework-specific focus — bỏ ngôn ngữ "wrong/incomplete/gets wrong":

```diff
 FRAMEWORK-SPECIFIC HOOK FOCUS:
-- Ranking: Tease the surprising winner/loser and why the conventional ranking wisdom is wrong.
-- Catalog: Establish the category's relevance and why the viewer's current knowledge is incomplete.
-- Head-to-Head: Frame the central matchup tension — why this comparison matters and what's at stake.
-- Deep Dive: Establish what the consensus gets wrong about this single product/topic.
+- Ranking: Create tension around which product earns which position — and why the order will surprise.
+- Catalog: Show why this category matters right now and what most buyers overlook.
+- Head-to-Head: Set up the central matchup — what each side brings and why the outcome isn't obvious.
+- Deep Dive: Reveal the one thing about this product that changes how you evaluate it.
```

**Thêm VARIETY RULE** (sau line 84) — cấm rõ ràng pattern lặp:

```
VARIETY RULE: Do NOT open with "you've been lied to", "they sold you a lie", or any deception/illusion framing.
  The hook can open with: a scenario, a question, a contrast, a bold claim, a story, or a provocation.
  Choose the approach that fits THIS specific topic — never default to the same formula.
```

---

### [MODIFY] [Review_firearms_v2.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/Review_firearms_v2.json)

**Line 112-136**: Thêm thêm hook methods mới (scenario, question) để AI không chỉ chọn "damning_verdict_first":

```diff
 "hook_methods": {
     "damning_verdict_first": { ... },
     "stress_test_cold_open": { ... },
     "provocative_caliber_question": { ... },
+    "scenario_cold_open": {
+      "description": "Drop the viewer into a specific real-world situation where the topic matters.",
+      "structure": "Vivid scenario → Why this moment matters → What we're about to find out",
+      "rule": "Scenario must be grounded in real use-case from blueprint data."
+    },
+    "contrast_opener": {
+      "description": "Juxtapose two extremes — price, performance, reputation — to create immediate tension.",
+      "structure": "Extreme A vs Extreme B → The gap is the story → Tease the answer",
+      "rule": "Both extremes must reference real products or data from blueprint."
+    },
     "hook_writing_rules": { ... }
 }
```

## Open Questions

> [!IMPORTANT]
> Ngoài 3 thay đổi trên, có cần thêm banned_patterns cụ thể cho tiếng Tây Ban Nha không? (ví dụ: "te ha vendido una mentira", "el mercado te ha engañado", etc.)

## Verification Plan

### Manual Verification
- Chạy lại 2-3 video đã test trước đó, so sánh hook output trước/sau.
- Kiểm tra depth_focus trong `_review_outline.json` có còn chứa "illusion/mentira/lie" không.
