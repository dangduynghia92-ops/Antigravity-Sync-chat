"""
COMPREHENSIVE AUDIT — Crowd Pipeline Integration
Checks: syntax, data flow, field naming, missing references, logic conflicts
"""
import ast, re, json, os

FP = r'f:\1. Edit Videos\8.AntiCode\1.Prompt_Image\1.Prompt_Image\core\video_pipeline.py'

with open(FP, encoding='utf-8') as f:
    content = f.read()
    lines = content.splitlines()

errors = []
warnings = []
info = []

# ════════════════════════════════════════════
# 1. SYNTAX CHECK
# ════════════════════════════════════════════
try:
    ast.parse(content)
    info.append("✅ Syntax: OK")
except SyntaxError as e:
    errors.append(f"❌ Syntax Error: {e}")

# ════════════════════════════════════════════
# 2. PROMPT FIELD CONSISTENCY
# ════════════════════════════════════════════

# 2a. Check present_labels is fully removed from prompts
present_labels_in_prompts = []
in_prompt = False
for i, line in enumerate(lines, 1):
    if '"""' in line or "'''" in line:
        in_prompt = not in_prompt
    if in_prompt and 'present_labels' in line:
        present_labels_in_prompts.append(f"L{i}: {line.strip()[:100]}")

if present_labels_in_prompts:
    errors.append(f"❌ 'present_labels' still found in prompts ({len(present_labels_in_prompts)} refs):")
    for ref in present_labels_in_prompts:
        errors.append(f"   {ref}")
else:
    info.append("✅ present_labels: fully renamed to character_labels in prompts")

# 2b. Check present_labels in code (should be 0)
present_labels_code = []
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if 'present_labels' in stripped and not stripped.startswith('#') and not stripped.startswith('"') and not stripped.startswith("'"):
        present_labels_code.append(f"L{i}: {stripped[:100]}")

if present_labels_code:
    warnings.append(f"⚠ 'present_labels' still in code ({len(present_labels_code)} refs):")
    for ref in present_labels_code:
        warnings.append(f"   {ref}")
else:
    info.append("✅ present_labels: no code references (clean)")

# ════════════════════════════════════════════
# 3. STEP2D PROMPT + METHOD CHECK
# ════════════════════════════════════════════

if 'STEP2D_CROWD_PROMPT' in content:
    info.append("✅ STEP2D_CROWD_PROMPT: defined")
else:
    errors.append("❌ STEP2D_CROWD_PROMPT: NOT FOUND")

if 'def _run_step2d' in content:
    info.append("✅ _run_step2d(): defined")
else:
    errors.append("❌ _run_step2d(): NOT FOUND")

if '"step2d"' in content and 'StepStatus' in content:
    # Check step2d has StepStatus
    if '"step2d": StepStatus' in content:
        info.append("✅ step2d StepStatus: defined")
    else:
        errors.append("❌ step2d StepStatus: NOT FOUND")
else:
    errors.append("❌ step2d step status: missing")

if 'self.crowd_data' in content:
    info.append("✅ self.crowd_data: defined")
else:
    errors.append("❌ self.crowd_data: NOT FOUND")

# ════════════════════════════════════════════
# 4. DATA FLOW TRACING
# ════════════════════════════════════════════

# 4a. Step 1 → crowd_types
step1_output_has_crowd = 'crowd_types' in content and '"crowd_types"' in content
if step1_output_has_crowd:
    info.append("✅ Step 1: crowd_types in output format")
else:
    errors.append("❌ Step 1: crowd_types NOT in output format")

# 4b. Step 2d reads crowd_types from sequences
if "seq.get(\"crowd_types\"" in content or 'seq.get("crowd_types"' in content:
    info.append("✅ Step 2d: reads crowd_types from sequences")
else:
    errors.append("❌ Step 2d: does NOT read crowd_types from sequences")

# 4c. _extract_valid_labels includes crowd
if '"crowd"' in content and 'self.crowd_data.get("characters"' in content:
    info.append("✅ _extract_valid_labels: includes crowd")
else:
    errors.append("❌ _extract_valid_labels: missing crowd")

# 4d. Step 3.1 input includes crowd_labels
if '"crowd_labels": crowd_labels' in content:
    info.append("✅ Step 3.1 input: crowd_labels included")
else:
    errors.append("❌ Step 3.1 input: crowd_labels NOT included")

# 4e. Step 3.1 output format has character_labels + crowd_labels
step31_output = content[content.find('STEP3_1_SYSTEM_PROMPT'):content.find('STEP3_SYSTEM_PROMPT')]
if '"character_labels"' in step31_output:
    info.append("✅ Step 3.1 output: character_labels in JSON template")
else:
    errors.append("❌ Step 3.1 output: character_labels MISSING from JSON template")
if '"crowd_labels"' in step31_output:
    info.append("✅ Step 3.1 output: crowd_labels in JSON template")
else:
    errors.append("❌ Step 3.1 output: crowd_labels MISSING from JSON template")

# 4f. Step 3.2 output has crowd_labels
step32_output = content[content.find('STEP3_SYSTEM_PROMPT'):content.find('STEP4_USER_TEMPLATE')]
if '"crowd_labels"' in step32_output:
    info.append("✅ Step 3.2 output: crowd_labels in JSON template")
else:
    errors.append("❌ Step 3.2 output: crowd_labels MISSING from JSON template")

# 4g. Step 4 mini_bible includes crowd
if 'self.crowd_data.get("characters"' in content:
    # Count occurrences
    count = content.count('self.crowd_data.get("characters"')
    info.append(f"✅ Step 4 mini_bible: references crowd_data ({count} refs)")
else:
    errors.append("❌ Step 4 mini_bible: does NOT reference crowd_data")

# 4h. Step 4 scene data includes crowd info
if "crowd_labels" in content and "scene.get('crowd_labels'" in content or 'scene.get("crowd_labels"' in content:
    info.append("✅ Step 4 scene data: crowd_labels included")
else:
    errors.append("❌ Step 4 scene data: crowd_labels NOT included")

# 4i. Prompt result items include crowd_labels
prompt_result_section = content[content.find('results.append({'):content.find('results.append({') + 2000]
if '"crowd_labels"' in prompt_result_section:
    info.append("✅ Prompt result items: crowd_labels included")
else:
    errors.append("❌ Prompt result items: crowd_labels MISSING")

# 4j. NO characters check includes crowd_labels
no_chars_area = content[content.find('NO characters'):content.find('NO characters') + 500]
if 'crowd_labels' in no_chars_area:
    info.append("✅ NO characters check: includes crowd_labels")
else:
    errors.append("❌ NO characters check: does NOT check crowd_labels")

# ════════════════════════════════════════════
# 5. PIPELINE ORDER CHECK
# ════════════════════════════════════════════
pipeline_area = content[content.find('steps = ['):content.find('for key, step_fn in steps')]
step_order = re.findall(r'"(\w+)"', pipeline_area)
info.append(f"✅ Pipeline order: {' → '.join(step_order)}")

# Check step2d is BEFORE _labels
if 'step2d' in step_order and '_labels' in step_order:
    idx_2d = step_order.index('step2d')
    idx_labels = step_order.index('_labels')
    if idx_2d < idx_labels:
        info.append("✅ step2d runs BEFORE _labels extraction")
    else:
        errors.append("❌ step2d runs AFTER _labels — crowd labels will be empty!")
else:
    if 'step2d' not in step_order:
        errors.append("❌ step2d NOT in pipeline order")

# Check step2d is AFTER step2a and step2b
if 'step2d' in step_order:
    idx_2d = step_order.index('step2d')
    idx_2a = step_order.index('step2a') if 'step2a' in step_order else -1
    idx_2b = step_order.index('step2b') if 'step2b' in step_order else -1
    if idx_2d > idx_2a and idx_2d > idx_2b:
        info.append("✅ step2d runs AFTER step2a + step2b")
    else:
        errors.append("❌ step2d runs BEFORE step2a or step2b — missing input data!")

# ════════════════════════════════════════════
# 6. CROWD LABEL MAPPING LOGIC CHECK
# ════════════════════════════════════════════

# Check Step 3.1 maps crowd_types to crowd_labels
mapping_area = content[content.find('# Map crowd_types to crowd_labels'):content.find('# Map crowd_types to crowd_labels') + 500] if '# Map crowd_types to crowd_labels' in content else ''
if mapping_area:
    if 'ct_lower in cl.lower()' in mapping_area:
        warnings.append("⚠ Crowd label mapping uses substring match (ct_lower in cl.lower()). "
                         "May cause false positives: 'guard' matches 'EXT-Guard-Sentry' AND 'EXT-Bodyguard-Heavy'. "
                         "Consider exact match on crowd_type field instead.")
    info.append("✅ Crowd label mapping: exists in Step 3.1 input building")
else:
    errors.append("❌ Crowd label mapping: NOT FOUND in Step 3.1")

# ════════════════════════════════════════════
# 7. STEP 2a-2 CROWD ARCHETYPES CHECK
# ════════════════════════════════════════════
step2a_people = content[content.find('STEP2A_PEOPLE_PROMPT'):content.find('STEP2A_WORLD_PROMPT')]
if 'soldier' in step2a_people and 'civilian_man' in step2a_people and 'civilian_woman' in step2a_people:
    warnings.append("⚠ Step 2a-2: still has hardcoded soldier/civilian_man/civilian_woman?")
    # Check if they're in example or fixed format
    if '"soldier": [' in step2a_people:
        errors.append("❌ Step 2a-2: STILL has fixed soldier array format — change NOT applied!")
    else:
        info.append("✅ Step 2a-2: old fixed categories removed, open-ended format")
else:
    info.append("✅ Step 2a-2: no hardcoded category names found")

# ════════════════════════════════════════════
# 8. CHECKPOINT NAMING CHECK
# ════════════════════════════════════════════
checkpoints = re.findall(r'_checkpoint_path\("([^"]+)"\)', content)
info.append(f"✅ Checkpoints: {', '.join(checkpoints)}")
if '_step2d_crowd.json' in checkpoints:
    info.append("✅ Step 2d checkpoint: exists")
else:
    errors.append("❌ Step 2d checkpoint: NOT FOUND")

# ════════════════════════════════════════════
# 9. Step 3.2 READS crowd_labels from Step 3.1
# ════════════════════════════════════════════
# Step 3.2 input construction — check if it passes crowd info from filmable_scenes
step32_input_area = content[content.find('def _process_sequence_step3'):content.find('def _process_sequence_step3') + 3000] if 'def _process_sequence_step3' in content else ''
if 'crowd' in step32_input_area.lower():
    info.append("✅ Step 3.2 input: references crowd data")
else:
    warnings.append("⚠ Step 3.2 input construction: does NOT explicitly pass crowd data. "
                     "Step 3.2 LLM relies on visual_treatment text only — crowd_labels in output "
                     "depends on LLM inferring from text. May need explicit crowd_labels pass-through.")

# ════════════════════════════════════════════
# 10. valid_labels INITIALIZATION CHECK
# ════════════════════════════════════════════
init_line = [l for l in lines if 'valid_labels' in l and '{"characters"' in l]
if init_line:
    if '"crowd"' in init_line[0]:
        info.append("✅ valid_labels init: includes 'crowd' key")
    else:
        errors.append("❌ valid_labels init: missing 'crowd' key")

# ════════════════════════════════════════════
# REPORT
# ════════════════════════════════════════════
print("=" * 70)
print("CROWD PIPELINE AUDIT REPORT")
print("=" * 70)

print(f"\n📋 INFO ({len(info)}):")
for item in info:
    print(f"  {item}")

print(f"\n⚠ WARNINGS ({len(warnings)}):")
for item in warnings:
    print(f"  {item}")

print(f"\n❌ ERRORS ({len(errors)}):")
if errors:
    for item in errors:
        print(f"  {item}")
else:
    print("  None! 🎉")

print(f"\n{'=' * 70}")
print(f"SUMMARY: {len(info)} OK | {len(warnings)} warnings | {len(errors)} errors")
print(f"{'=' * 70}")
