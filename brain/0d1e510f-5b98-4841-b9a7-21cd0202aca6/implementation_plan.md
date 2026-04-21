# Manual Framework Selection Feature

Add an "Auto Framework" checkbox. When unchecked + Framework = "Auto (detect & switch)", the pipeline pauses after framework scoring to show the existing ranking popup for user selection.

## Proposed Changes

### UI Layout

#### [MODIFY] [script_creation_tab.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/2.Script_Split_Chapter/ui/script_creation_tab.py)

**Change 1: Add checkbox (after Auto-Patch, ~L321)**
```python
self._chk_auto_fw = QCheckBox("🤖 Auto Framework")
self._chk_auto_fw.setChecked(True)  # default = auto (current behavior)
self._chk_auto_fw.setToolTip(
    "Auto-select framework based on AI ranking.\n"
    "OFF = Show ranking popup for manual selection after scoring."
)
btn_row.addWidget(self._chk_auto_fw)
```

**Change 2: New Content — intercept after scoring (~L2645)**

Current flow:
```
L2627: recommend_framework_new_content() → rankings
L2640: rankings.sort()
L2645: log AI ranking
L2647-2679: AUTO-select top frameworks
```

New flow (insert between L2645 and L2647):
```python
# ── Manual selection if Auto Framework unchecked ──
if not self._chk_auto_fw.isChecked():
    # Reuse existing dialog pattern from Rewrite flow
    self._fw_ranking_event.clear()
    self._fw_ranking_result = None
    fw_info_json = json.dumps({"name": "AI Recommendation", "confidence": "N/A", "reasoning": ""})
    self._fw_ranking_request.emit(rankings, fw_info_json)
    self._fw_ranking_event.wait()
    if self._fw_ranking_result is None:
        log("✗ User cancelled framework selection")
        return
    selected_fws = [self._fw_ranking_result]
    log(f"✓ User selected: '{self._fw_ranking_result}'")
else:
    # existing auto-selection logic (L2647-2679)
```

**Change 3: `_show_fw_ranking_dialog` — set event after dialog closes (~L1609)**

The dialog already sets `_fw_ranking_result` but the `_fw_ranking_event.set()` call may be missing for the New Content path. Need to ensure `_fw_ranking_event.set()` is called at the end of `_show_fw_ranking_dialog`.

## Verification Plan

### Manual Verification
1. Launch app → select "Auto (detect & switch)" framework
2. Check "Auto Framework" → New Content → should auto-select (unchanged behavior)
3. Uncheck "Auto Framework" → New Content → should show popup after scoring
4. Select a framework from popup → pipeline continues
5. Cancel popup → pipeline stops cleanly
