# Pipeline Rewrite Tasks

## 1. narrative_review.py
- [ ] Remove load_visual_bible, save_visual_bible cache functions  
- [ ] Remove generate_locations function
- [ ] Rewrite generate_visual_bible — no cache, accept style_content + exclude_characters
- [ ] Rewrite run_character_pipeline — no cache check, 3 groups only

## 2. process_controller.py  
- [ ] Rewrite _process_single_project visual bible section — no cache
- [ ] Rewrite _process_loop narrative pipeline — no cache
- [ ] Clean up imports (remove load_visual_bible, save_visual_bible)

## 3. Verify
- [ ] Import check
- [ ] Test run
