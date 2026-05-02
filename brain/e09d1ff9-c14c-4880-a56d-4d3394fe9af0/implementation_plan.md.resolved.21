# Cross-Audit: event_cause + physical_state Changes

## Pipeline Flow Map

```mermaid
graph LR
  A[phase_plan_pov] -->|event_timeline| B[validate_sub_key_pov]
  B -->|corrected timeline| C[chapter_plan_pov]
  C -->|curated timeline + event_cause| D[outline_pov]
  D -->|chapters JSON| E[audit_pov]
  E -->|audited chapters| F[write_pov]
```

Each step passes data to the next. Changes must be consistent across all 6 files.

---

## A. event_cause — Full Audit

### Current Definition (chapter_plan_pov.txt, line 58):
> `event_cause = the EXTERNAL TRIGGER that forces this event to happen.`

### Problem:
"EXTERNAL TRIGGER" → AI writes immediate action (WHAT starts) instead of strategic context (WHY it happens). Result: event_cause ≈ scene_open (trùng lặp).

### Where event_cause appears:

| # | File | Location | Current Text | Change Needed |
|---|---|---|---|---|
| 1 | `chapter_plan_pov.txt` | Line 54-89 | **DEFINITION + EXAMPLES** (owner) | ✅ REWRITE definition |
| 2 | `chapter_plan_pov.txt` | Line 102 | Output format: `"event_cause": "WHY..."` | ✅ Update description |
| 3 | `chapter_plan_pov.txt` | Line 130 | Critical rule 3: "generate event_cause for EVERY surviving event" | ⚪ Keep (still true) |
| 4 | `outline_pov.txt` | Line 8 (ownership) | "Event cause generation → chapter_plan_pov.txt" | ⚪ Keep (still true) |
| 5 | `outline_pov.txt` | Line 144 | `"event_cause": "WHY this event happens — the trigger. COPY from event_timeline."` | ✅ Update description |
| 6 | `write_pov.txt` | Line 33 | `Event cause (WHY this event happens): {event_cause}` | ✅ Update label |
| 7 | `write_pov.txt` | Line 78-87 | **PART 2 CAUSE/CONTEXT examples** | ✅ Update examples |
| 8 | `write_pov.txt` | Line 124 | "A chapter with CAUSE + SCENE + WEIGHT LINE = complete" | ⚪ Keep (still true) |
| 9 | `rewriter.py` | Line 5857 | `_event_cause = chapter_outline.get("event_cause", "")` | ⚪ Keep (data flow) |
| 10 | `rewriter.py` | Line 5860 | `cause_line = f"CONTEXT (why this event happens):\n  {_event_cause}"` | ⚪ Keep (label already correct) |
| 11 | `validate_sub_key_pov.txt` | Line 73 | Output format: `"physical_state": "..."` | See Issue #3 |
| 12 | `phase_plan_pov.txt` | Nowhere | Phase plan does NOT generate event_cause | ⚪ N/A |

### Proposed Changes — event_cause

#### File 1: `chapter_plan_pov.txt` (OWNER — lines 54-89)

```diff
-event_cause = the EXTERNAL TRIGGER that forces this event to happen.
-NOT what the character does. NOT a summary of the event.
-
-CAUSE = What happened OUTSIDE or BEFORE that made this event inevitable?
-  → Enemy action, political shift, death, betrayal, treaty, crisis
-
-FIND CAUSE in blueprint:
-  → turning_points[].before_state — what was happening just before
-  → conflicts[].catalyst — what triggered the conflict
-  → age_timeline[age-1 or age] — what happened right before this event
-  → Previous event's consequence — what the last event left behind
-
-FORMAT: 1-2 sentences. Subject = the external trigger, NOT "you".
-
-EXAMPLES:
-  ✓ "King Amalric I dies of dysentery. The crown passes to a 13-year-old leper."
-  ✓ "Saladin breaks the truce and marches 26,000 men toward an undefended Jerusalem."
-  ✓ "William of Montferrat dies of malaria, leaving Sibylla a widow.
-     Philip of Flanders crosses the sea to fill the power vacuum."
-
-ANTI-PATTERNS (NEVER write these):
-  ✗ "Seeking to maintain momentum, you intercept Saladin..."
-  ✗ "With your health failing, you desperately need a protector..."
-  ✗ "You refuse to remain a puppet of the regency..."

+event_cause = the BACKGROUND CONTEXT that explains WHY this event happens.
+NOT the immediate trigger (that belongs in event_description's opening).
+NOT what the character does. NOT a summary of the event.
+
+CAUSE = What political, strategic, or personal SITUATION made this event inevitable?
+  → What was building up? What pressure broke? What opportunity appeared?
+  → Think: "Why does this happen NOW, at THIS moment in history?"
+
+FIND CAUSE in blueprint:
+  → turning_points[].before_state — the situation BEFORE the shift
+  → conflicts[] — the broader conflict driving this event
+  → Previous event's consequence — what the last event left behind
+  → key_relationships — political dynamics that created pressure
+
+FORMAT: 2-3 sentences. Background situation, NOT immediate action.
+
+EXAMPLES:
+  ✓ "Saladin has unified Egypt and Syria under one banner, creating the
+     largest Muslim army since the First Crusade. The Kingdom of Jerusalem
+     is fractured — its king is a dying leper, and William of Montferrat's
+     death has reopened the succession crisis."
+     → STRATEGIC CONTEXT: why Saladin attacks NOW
+
+  ✓ "King Amalric I has died of dysentery during a northern campaign. The
+     kingdom cannot survive a power vacuum — Saladin controls Egypt and
+     Syria, and the Haute Cour needs a crowned king immediately."
+     → POLITICAL CONTEXT: why coronation is urgent
+
+  ✓ "For two years, Raymond of Tripoli has ruled as regent. The barons
+     see a crippled boy on the throne and calculate their odds. Philip of
+     Flanders arrives with fresh knights and dangerous ambition."
+     → POWER DYNAMICS: why the confrontation happens
+
+ANTI-PATTERNS:
+  ✗ "Saladin marches 26,000 men toward Jerusalem."
+     → This is the IMMEDIATE ACTION, not WHY. This belongs in event_description.
+  ✗ "Seeking to maintain momentum, you intercept Saladin..."
+     → This is what the CHARACTER DOES, not the background.
+  ✗ "With your health failing, you desperately need a protector..."
+     → This is the character's MOTIVATION, not the situation.
```

#### File 2: `outline_pov.txt` (line 144)

```diff
-"event_cause": "WHY this event happens — the trigger (1-2 sentences). COPY from event_timeline if present.",
+"event_cause": "BACKGROUND CONTEXT — why this event happens (2-3 sentences). COPY from event_timeline if present.",
```

#### File 3: `write_pov.txt` (line 33 + lines 78-87)

```diff
 Line 33:
-Event cause (WHY this event happens): {event_cause}
+Background context (WHY this event happens): {event_cause}

 Lines 78-87:
   PART 2 — CAUSE/CONTEXT (the setup):
-    Develop the event_cause field into POV sentences.
-    This is WHY this event happens — the trigger, the external force.
+    Develop the event_cause field into POV sentences that SET THE STAGE.
+    This is the background situation that MADE this event inevitable.
     
-    ✓ "Your father has just died of dysentery. The crown passes to you —
-       a 13-year-old leper in a kingdom that devours weak rulers."
-    ✓ "Saladin's army of 26,000 marches toward Jerusalem. Your scouts
-       count the fires at night. There are too many."
+    ✓ "The most dangerous man alive has unified the entire Muslim world.
+       His name is Saladin. He wants Jerusalem back. Your kingdom is a
+       thin strip of land, and you — a dying leper — are all that stands
+       in his way."
+    ✓ "Your father is gone. Dysentery took him on a campaign in the north.
+       The kingdom cannot survive without a crowned king — Saladin controls
+       both Egypt and Syria, and the barons are already calculating."
     ✗ "This chapter covers the coronation." (meta)
     ✗ "It was a difficult time." (vague)
+    ✗ "Saladin marches 26,000 men toward Jerusalem." (immediate action, not background)
```

### Conflict Check — event_cause

| Potential Conflict | Status |
|---|---|
| chapter_plan generates cause → outline copies → writer develops | ✅ Compatible. Chain preserved. |
| write_pov PART 2 examples vs chapter_plan examples | ✅ Will align (both rewritten) |
| write_pov says "trigger" in line 80 | ⚠ Must change to "background situation" |
| user_msg in rewriter.py says "CONTEXT (why this event happens)" | ✅ Already correct label |
| scene_open in write_pov says "WHERE the event begins" | ✅ No conflict — scene_open = immediate, event_cause = background |
| validate_sub_key_pov doesn't mention event_cause | ✅ No conflict |
| phase_plan_pov doesn't generate event_cause | ✅ No conflict |

---

## B. physical_state — Full Audit

### Where physical_state appears:

| # | File | Location | Current Text | Change |
|---|---|---|---|---|
| 1 | `phase_plan_pov.txt` | Line 136-144 | Output example: had `physical_state` field | ✅ Already removed |
| 2 | `phase_plan_pov.txt` | Line 172 | Coverage checklist: "body changes distributed as sub_key_data" | ⚪ Keep (already correct) |
| 3 | `phase_plan_pov.txt` | Line 34-37 | BODY STATE RULE: "NEVER standalone, ALWAYS sub_key_data" | ⚪ Keep (reinforces change) |
| 4 | `validate_sub_key_pov.txt` | Line 33-36 | CHECK 4: body state as standalone event → move to sub_key_data | ⚪ Keep |
| 5 | `validate_sub_key_pov.txt` | Line 73 | Output format: `"physical_state": "..."` | ✅ REMOVE field |
| 6 | `chapter_plan_pov.txt` | Line 104 | Output format: `"physical_state": "..."` | ✅ REMOVE field |
| 7 | `outline_pov.txt` | Line 8 | Ownership: "age_anchor, physical_state requirements" | ✅ Remove physical_state |
| 8 | `outline_pov.txt` | Line 140 | Output: `"physical_state": "Healthy appearance..."` | ✅ REMOVE field |
| 9 | `outline_pov.txt` | Line 169 | Rule #6: "physical_state is MANDATORY for every chapter" | ✅ REMOVE rule |
| 10 | `audit_pov.txt` | Line 18 | Scope: "opening_style, closing_type, ..., physical_state" | ✅ REMOVE from list |
| 11 | `audit_pov.txt` | Line 26 | Checklist #3: "physical_state? Body changes MUST show progression" | ✅ REMOVE check |
| 12 | `audit_pov.txt` | Line 46 | Output type: includes "physical_state" | ✅ REMOVE from enum |
| 13 | `write_pov.txt` | Line 43 | Template: `Physical state: {physical_state}` | ✅ REMOVE line |
| 14 | `write_pov.txt` | Line 97 | "Weave sub_key_data and physical_state INTO action" | ✅ Remove "and physical_state" |
| 15 | `rewriter.py` | Line 1441 | `_NICHE_OUTLINE_FIELDS`: `"{physical_state}": "physical_state"` | ✅ REMOVE entry |
| 16 | `style JSON` | N/A | Not present | ⚪ N/A |

### How body data still flows (no physical_state field):

```
Blueprint has physical_state_arc
  ↓
phase_plan_pov: BODY STATE RULE says "ALWAYS sub_key_data" (line 34)
  → AI puts body details in sub_key_data: ["Claw hand deformity worsening", ...]
  ↓
validate: CHECK 4 enforces body state never standalone (line 33)
  ↓
chapter_plan: copies sub_key_data through (already includes body data)
  ↓  
outline: copies sub_key_data into each chapter
  ↓
write_pov: "Weave sub_key_data INTO action" (line 97, updated)
  → Writer sees "Claw hand deformity worsening" in sub_key_data
  → Weaves: "Your clawed fingers cannot grip the reins"
```

**For characters WITHOUT body progression**: blueprint lacks `physical_state_arc` → no body items in sub_key_data → writer doesn't receive any → doesn't bịa.

### Conflict Check — physical_state

| Potential Conflict | Status |
|---|---|
| phase_plan BODY STATE RULE says "always sub_key_data" | ✅ Aligned — field removed |
| validate CHECK 4 says "move body state to sub_key_data" | ✅ Aligned — no field to check |
| chapter_plan output format has `physical_state` | ⚠ Must remove |
| validate output format has `physical_state` | ⚠ Must remove |
| outline generates `physical_state` → writer receives it | ⚠ Must remove from both |
| audit checks physical_state progression | ⚠ Must remove check |
| `_NICHE_OUTLINE_FIELDS` maps `{physical_state}` | ⚠ Must remove mapping |
| write_pov template `{physical_state}` placeholder left unreplaced if removed from FIELDS | ⚠ Must remove from template |
| `_inject_level_anchor` reads `chapter_outline.get("physical_state")` | ⚪ No — only reads age_anchor |

---

## C. Summary of ALL Changes

### Total: 6 files, 16 edits

| File | Edits | Type |
|---|---|---|
| `chapter_plan_pov.txt` | 3 | event_cause definition + examples + output format |
| `outline_pov.txt` | 4 | event_cause desc + physical_state field/rule/ownership |
| `audit_pov.txt` | 3 | physical_state scope/check/output |
| `write_pov.txt` | 4 | event_cause label/examples + physical_state field/weave |
| `validate_sub_key_pov.txt` | 1 | physical_state output format |
| `rewriter.py` | 1 | _NICHE_OUTLINE_FIELDS remove physical_state |

> [!IMPORTANT]
> Tất cả 16 edits đều chỉ ảnh hưởng POV pipeline. Biography pipeline không có files nào trong danh sách này.

> [!NOTE]
> Issue #2 (Level anchor strip) đã được fix. Không cần thay đổi thêm.
