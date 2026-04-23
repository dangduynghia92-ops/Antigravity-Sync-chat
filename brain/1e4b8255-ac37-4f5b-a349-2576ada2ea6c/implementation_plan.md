# Auto-Output + Skip Merge + Sound Notification

## 3 Features

### 1. Auto-output to SRT folder when output is empty
When the Output field is blank, use the **parent folder of the first SRT file** as the output directory, creating a `style_rewrite/` subdirectory.

### 2. Skip merge for single SRT
When there's only 1 project file, skip the `_merge_output()` call since merge is redundant — the per-project CSV already has all the data.

### 3. Sound on completion/error
Play a Windows system sound (`winsound.MessageBeep`) when processing finishes (success or error).

## Proposed Changes

### [MODIFY] [main_window.py](file:///f:/1.%20Edit%20Videos/8.AntiCode/1.Prompt_Image/1.Prompt_Image/ui/main_window.py)

**Feature 1** — `_start_processing()` (line 405-473) and `_retry_failed()` (line 475-515):
- Remove the early return when `output_dir` is empty
- Instead: derive output from `os.path.dirname(projects[0].srt_path)` + `style_rewrite/`
- Pass this derived path to `controller.start()`

**Feature 2** — `_thread_safe_state_changed()` (line 879-913):
- Before calling `_merge_output()`, check `len(self.controller.projects)`
- If only 1 project → skip merge, log `[MERGE] ⏭ Chỉ có 1 file, bỏ qua merge.`

**Feature 3** — `_thread_safe_state_changed()`:
- `import winsound` at top of file
- After IDLE state handling: `winsound.MessageBeep(winsound.MB_OK)` for success
- After STOPPED state handling: `winsound.MessageBeep(winsound.MB_ICONHAND)` for error/stop

## Verification
- Run with empty output → verify output goes to SRT source folder
- Run 1 file → verify no merge file created
- Run multiple files → verify merge still works
- Listen for sound on complete/stop
