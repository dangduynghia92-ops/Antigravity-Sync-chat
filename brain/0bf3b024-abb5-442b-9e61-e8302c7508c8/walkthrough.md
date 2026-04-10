# Walkthrough — Bug Fix + User Manual

## 1. Bug Fix: All chapters skipped (SKIP)

**Root cause**: `_create_and_submit_job` in `rewrite_style_tab.py` created job dicts without caching word count values. Worker threads defaulted to `(0, 0)` → `build_word_count_rule(0, 0)` returned `"SKIP"` for ALL chapter sections.

**Fix**: Added 7 cached values to the job dict at creation time:

render_diffs(file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/rewrite_style_tab.py)

---

## 2. User Manual — In-App Help System

### Files changed

| File | Change |
|------|--------|
| [user_manual.html](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/user_manual.html) | **[NEW]** HTML manual, 11 tabs, dark theme, Vietnamese |
| [header_bar.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/header_bar.py) | Added `❓ Help` button + `help_clicked` signal |
| [main_window.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/main_window.py) | Connected Help → opens manual at active tab section |

### How it works
- Click **❓ Help** on header bar → browser opens `user_manual.html#<tab-id>`
- Tab ID maps 1:1 with app tabs (index 0 = `auto-pipeline`, index 5 = `style-rewrite`, etc.)

### Verification

````carousel
![Auto Pipeline tab in manual](file:///C:/Users/Admin/.gemini/antigravity/brain/0bf3b024-abb5-442b-9e61-e8302c7508c8/.system_generated/click_feedback/click_feedback_1774540969464.png)
<!-- slide -->
![Style Rewrite tab in manual](file:///C:/Users/Admin/.gemini/antigravity/brain/0bf3b024-abb5-442b-9e61-e8302c7508c8/.system_generated/click_feedback/click_feedback_1774540975597.png)
````
