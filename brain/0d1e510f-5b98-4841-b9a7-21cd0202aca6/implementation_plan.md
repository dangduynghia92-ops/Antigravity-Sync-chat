# Generalizing Audit & Crossref Pipeline (All Niches)

## Goal
Refactor battle-specific `audit_battle_blueprint()` / `crossref_battle_blueprint()` into niche-generic functions. Add biography support with empty audit prompt (auto-skip) and SCENE TEST crossref prompt.

## Proposed Changes

---

### Rewriter Functions

#### [MODIFY] [rewriter.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/core/rewriter.py)

**Rename + add prompt dispatch:**

```diff
-def audit_battle_blueprint(blueprint, topic, api_client, lang, log_callback):
-    system_template = _load_prompt("system_audit_battle_blueprint.txt")
-    user_msg = f"BATTLE/WAR: {topic}\n\nCOMPLETED BLUEPRINT:\n{bp_json}"
+def audit_blueprint(blueprint, topic, niche, api_client, lang, log_callback):
+    prompt_file = _AUDIT_PROMPT_MAP.get(matched_kw, None)
+    if not prompt_file:
+        log("Step 1.5: No audit prompt for this niche — skip")
+        return None
+    system_template = _load_prompt(prompt_file)
+    if not system_template.strip():
+        log("Step 1.5: Audit prompt is empty — skip")
+        return None
+    user_msg = f"TOPIC: {topic}\n\nCOMPLETED BLUEPRINT:\n{bp_json}"
```

```diff
-def crossref_battle_blueprint(blueprint, reference_texts, api_client, lang, log_callback):
-    system_template = _load_prompt("system_crossref_battle_blueprint.txt")
+def crossref_blueprint(blueprint, reference_texts, niche, api_client, lang, log_callback):
+    prompt_file = _CROSSREF_PROMPT_MAP.get(matched_kw, None)
+    if not prompt_file:
+        log("Step 1.6: No crossref prompt for this niche — skip")
+        return None
+    system_template = _load_prompt(prompt_file)
```

**New dispatch maps:**

```python
_AUDIT_PROMPT_MAP = {
    "battle": "system_audit_battle_blueprint.txt",
    "war": "system_audit_battle_blueprint.txt",
    "trận": "system_audit_battle_blueprint.txt",
    "biography": "system_audit_biography_blueprint.txt",
    "tiểu sử": "system_audit_biography_blueprint.txt",
}

_CROSSREF_PROMPT_MAP = {
    "battle": "system_crossref_battle_blueprint.txt",
    "war": "system_crossref_battle_blueprint.txt",
    "trận": "system_crossref_battle_blueprint.txt",
    "biography": "system_crossref_biography_blueprint.txt",
    "tiểu sử": "system_crossref_biography_blueprint.txt",
}
```

**Return `None` when skipped** → caller checks `if result is None: skip save`

---

### UI Pipeline Gating

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

```diff
-from core.rewriter import audit_battle_blueprint, crossref_battle_blueprint
+from core.rewriter import audit_blueprint, crossref_blueprint
```

**Remove `_BATTLE_KW` gating** — let the functions dispatch by niche:

```diff
-_BATTLE_KW = ("battle", "war", "military", "combat", "trận", "chiến")
-if any(kw in _niche for kw in _BATTLE_KW):
+# Step 1.5: Blueprint audit (all narrative niches — skips if no prompt)
+if True:  # Always attempt — function handles dispatch
     audit_path = os.path.join(pipeline_dir, "_audit.json")
     ...
-    audit_result = audit_battle_blueprint(blueprint, topic, api_audit, ...)
+    audit_result = audit_blueprint(blueprint, topic, _niche, api_audit, ...)
+    if audit_result is None:
+        pass  # Skipped — no prompt for this niche
+    else:
+        # save audit_result + re-save blueprint
```

Same pattern for crossref.

---

### Prompt Files

#### [NEW] [system_audit_biography_blueprint.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_audit_biography_blueprint.txt)
- **Empty file** — `audit_blueprint()` detects empty prompt → auto-skip

#### [NEW] [system_crossref_biography_blueprint.txt](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/prompts/system_crossref_biography_blueprint.txt)
- Adapted from battle version
- **SCENE TEST** tailored for biography:
  - ✅ Paradoxes, hidden relationships, visceral personal details, myth-busting, dramatic irony
  - ❌ Admin titles, publication lists, genealogy filler, award chronology
- `merge_into_existing` sections match biography blueprint schema: `life_phases`, `achievements`, `conflicts`, `key_relationships`, `myths_vs_reality`, `dual_nature`, `personal_profile`
- All sources tagged `"reference_transcript"`

---

### Style JSON

#### [MODIFY] [narrative_phân_tích_trận_đánh_v2.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_phân_tích_trận_đánh_v2.json)
- Add `"additional_findings"` to `excerpt_fields` if not already present (done earlier)

#### [MODIFY] [narrative_tiểu_sử_nhân_vật.json](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/styles/narrative_tiểu_sử_nhân_vật.json)
- Add `"additional_findings"` to `excerpt_fields` (to let phase planner access crossref data)

---

## Verification Plan

### Automated
1. `py_compile.compile("core/rewriter.py")` — syntax check
2. `py_compile.compile("ui/script_creation_tab.py")` — syntax check

### Manual
- Battle niche: runs same as before (no regression)
- Biography niche with **no scripts loaded** → step 1.5 skip, step 1.6 skip
- Biography niche with **scripts loaded** → step 1.5 skip, step 1.6 runs crossref
