# Fix: Hook luôn lặp cùng 1 pattern

## Root Cause

LLM là máy match pattern. Khi hệ thống chỉ cho nó **1 mẫu tham khảo** cho "good hook", nó sẽ copy mẫu đó mỗi lần.

Cụ thể:
- Outline prompt: **1** GOOD example duy nhất → AI copy pattern đó vào mọi depth_focus
- hook_methods: **3** methods, cùng 1 hướng aggressive → AI không có lựa chọn khác
- Writer prompt: **4/4** framework focus đều dùng cùng hướng "wrong/incomplete" → AI chỉ biết 1 cách mở

## Fix: Mở rộng reference — cho AI nhiều lựa chọn

### 1. [MODIFY] [system_review_outline_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_review_outline_firearms_v2.txt)

**Line 26-28** — Thêm nhiều GOOD example đa dạng (thay vì chỉ 1):

```diff
  depth_focus for hook must be a PROVOCATIVE ANGLE or THESIS — never a technical explanation or mechanism comparison. The hook creates curiosity, not education.
    BAD depth_focus:  "The difference between direct blowback and delayed systems"
-   GOOD depth_focus: "The market sells a $2,000 illusion — the data exposes which platforms actually deliver"
+   GOOD depth_focus examples (each uses a DIFFERENT approach — pick the one that fits the blueprint):
+   - Data surprise: "One $400 entry outperforms three guns at triple the price — the reason has nothing to do with specs"
+   - Scenario: "At 3 AM in a narrow hallway, the spec sheet advantage disappears — something else decides the outcome"
+   - Contrast: "The gun every forum dismisses sits at the top of one critical metric"
+   - Deception reveal: "The market sells a $2,000 illusion — the data exposes which platforms actually deliver"
+   - Bold question: "Is the most popular caliber in America actually the worst choice for its most common use case?"
```

Giữ nguyên "deception reveal" như 1 trong 5 options — không ban, nhưng AI giờ có 4 lựa chọn khác ngang giá trị.

---

### 2. [MODIFY] [system_write_review_firearms_v2.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_write_review_firearms_v2.txt)

**Line 80-84** — Đa dạng hóa framework focus (mỗi framework gợi ý 1 hướng KHÁC nhau):

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

Mỗi framework giờ gợi ý 1 hướng khác nhau (surprise, relevance, matchup, revelation) thay vì tất cả cùng hướng "wrong".

---

### 3. [MODIFY] [Review_firearms_v2.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/Review_firearms_v2.json)

**A. Thêm 2 hook_methods** (line 127, trước `hook_writing_rules`) — cho AI thêm lựa chọn:

```json
"scenario_cold_open": {
  "description": "Drop the viewer into a vivid real-world moment where the topic matters.",
  "structure": "Vivid scenario (2-3 sentences) → Why this moment matters → What we're about to discover",
  "rule": "Scenario must use real-world context from blueprint data."
},
"data_surprise_opener": {
  "description": "Lead with a single counter-intuitive number or comparison that reframes the topic.",
  "structure": "Surprising data point → Why it contradicts expectations → Set up analysis",
  "rule": "Number must come from blueprint data. No invented stats."
}
```

Tổng hook_methods: 3 → 5. AI giờ có 5 cách mở khác nhau thay vì 3 cách cùng hướng.

## Verification Plan

- Chạy lại 2 video đã test (AR-9, 20 vs 12 Gauge)
- Kiểm tra depth_focus trong `_review_outline.json` có đa dạng không
- Kiểm tra `ch_01_Intro.txt` có đa dạng cách mở không
