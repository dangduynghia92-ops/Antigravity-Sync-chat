# Pipeline Output Analysis — Baldwin IV Test Run

## Data Examined

| Chapter | Characters | Factions | Locations | Scenes |
|---|---|---|---|---|
| Ch1 (Childhood) | 2 | 1 | 3 | 10 |
| Ch4 (Montgisard) | 2 | 4 | 6 | 16 |
| Ch7 (Last Ride) | 3 | 3 | 4 | 14 |

---

## Issue 1: Per-Chapter Isolation (ROOT CAUSE)

Each chapter runs as completely independent pipeline. The same character gets **DIFFERENT labels** across chapters:

| Chapter | Baldwin IV Label | Saladin Label |
|---|---|---|
| Ch1 | `Jerusalem-Prince-A` | ❌ (not present) |
| Ch4 | `Crusader-King-A` | `Ayyubid-Sultan-A` |
| Ch7 | `Crusader-King-A` | `Ayyubid-Sultan-A` |

> [!CAUTION]
> Ch1 uses `Jerusalem-Prince-A` while Ch4/7 use `Crusader-King-A` for the SAME person. These are treated as separate reference images. In the video tool, `[Jerusalem-Prince-A]` and `[Crusader-King-A]` would be two different images instead of age variants of the same character.

---

## Issue 2: No Age Variants Generated

Despite the AGE VARIANT RULE in the system prompt, **no chapter generated age variants** because each chapter only sees ONE life stage:

- Ch1 → only "child" Baldwin → `Jerusalem-Prince-A` (child)
- Ch4 → only "teen" Baldwin → `Crusader-King-A` (teen)
- Ch7 → only "adult" Baldwin → `Crusader-King-A` (adult)

**Expected with merged pipeline:**
```
Jerusalem-King-A-Child   (Ch1-2)
Jerusalem-King-A-Teen    (Ch3-4)
Jerusalem-King-A-Adult   (Ch5-7)
Jerusalem-King-A-Elder   (Ch8-11)
```

---

## Issue 3: Location Prompt Contains Character Style

Current location prompt (from Excel Sheet 2, row 7):
```
Stylized historical animation illustration, oversized round pure white faces 
with oval dot eyes and expressive eyebrows and mouth shapes and no nose, 
compact stylized body proportions...
A 12th-century Crusader council chamber built with heavy limestone arches...
```

> [!WARNING]
> The `mandatory_style` (line 52 in style file) includes character appearance rules:
> "oversized round pure white faces with oval dot eyes... no nose, compact stylized body proportions"
> 
> When prepended to location prompts, the AI generates CHARACTERS inside the location image.

**Fix needed:** Location prompts should use a **background-only** style:
```
Stylized historical animation illustration, detailed painterly backgrounds,
scene-driven natural palette, scene-driven lighting, clean consistent design,
full frame, no border, no text, no watermark, 16:9 aspect ratio.
NO characters, NO people, empty scene.
```

---

## Issue 4: Character Sheet Missing Multi-Angle Views

Current `sheet_prompt` (Ch1, Jerusalem-Prince-A):
```
"Character reference on clean white background. Compact 3-heads-tall child body... 
Label 'Jerusalem-Prince-A'."
```

**Missing:** "Three neutral standing views: front view, 3/4 angle, side profile."

---

## Issue 5: flat_prompt Duplicates Label as Plain Text

Example from Ch1 scene 1:
```
...In [Palace Courtyard]. [Jerusalem-Prince-A] Jerusalem-Prince-A pins a larger boy...
```

The label appears TWICE:
1. `[Jerusalem-Prince-A]` ← correct reference bracket
2. `Jerusalem-Prince-A` ← redundant plain text leaked from `physical_action`

**Root cause:** Step 4 code prepends `[label]` but doesn't strip the label from the existing `physical_action` text where LLM already wrote it.

---

## Issue 6: Faction Labels Not Consistent

| Chapter | Crusader Army Label |
|---|---|
| Ch4 | `The Crusader Army` |
| Ch7 | `Army of Jerusalem` |

Same army, different names — cannot use the same reference image.

---

## Summary of Fixes Needed

| # | Issue | Fix |
|---|---|---|
| 1 | Per-chapter isolation | **Multi-chapter merge** — all files → one pipeline |
| 2 | No age variants | Solved by #1 (LLM sees full story) |
| 3 | Location prompt has character style | **Split style** into character vs background sections |
| 4 | Missing multi-angle views | Update `sheet_prompt` template |
| 5 | Label duplication in flat_prompt | Strip existing label text from `physical_action` before prepending `[label]` |
| 6 | Inconsistent faction labels | Solved by #1 (single character extraction) |
