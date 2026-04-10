# Desktop AI Logging and Debugging Patterns

Robust feedback and error handling are critical for long-running batch AI processes on the desktop.

## 1. Thread-Safe and Unicode-Resilient Logging

Standard Python `print` or `log` calls can crash a GUI application (e.g., PyQt) if called from a background thread with characters the local console doesn't support (especially on Windows).

### Pattern: `_safe_log`
A dedicated logging helper should catch `UnicodeEncodeError` and `UnicodeDecodeError`.
- **Implementation**:
  1. Attempt to log the original message (e.g., to to a `pyqtSignal` or terminal).
  2. If an encoding error occurs, strip all non-ASCII characters (regex: `r'[^\x00-\x7F]+'`).
  3. Re-attempt logging the "clean" version or a generic fallback message.
- **Result**: Even if the AI generates emojis or regional characters (like Vietnamese in a historical context), the app remains stable and the UI doesn't freeze or crash.

## 2. Real-Time Process Cancellation (`check_stopped`)

Heavy analytical steps, such as generating a project's "Visual Bible," should be responsive to user input. If a user clicks "Stop," the application should not wait for the current API call to complete.

### Pattern: Intra-Task Cancellation
1. Define a `check_stopped` lambda or callback that reads a shared `is_stopped` flag.
2. In long worker functions, call `check_stopped()` at granular points:
   - Before starting heavy processing.
   - After parsing local data but before the first API call.
   - Immediately after each API call return.
3. If `check_stopped()` returns True, the function should return early, clean up any partial results, and not save to disk.

## 3. Input Resilience and Token Management

Batch processing can easily hit the context limit of LLMs, especially when sending full video subtitles (SRT) for global analysis.

### Strategies:
- **Capping**: For "Pass 1" analysis (Generating a Visual Bible), if the source text exceeds a certain character threshold (e.g., 30k-100k chars), it should be truncated or summarily analyzed to prevent API failure.
- **Pro-Tier Policy**: Critical analysis steps should be hard-coded to **Pro** models, as these typically have larger context windows and higher reasoning capabilities required for global project context.
- **Fail-Safe Processing**: If an analysis step fails (but the project still needs to run), the system should log the failure and proceed with "Local-Only" knowledge, ensuring some output is still generated even without a global Bible.

## 4. Post-Generation Auditing

A "Self-Audit" phase (either by the developer or another AI agent) should review generated code and artifacts for:
- **Hard-coded limits**: Ensuring limits are necessary and not arbitrary.
- **Residue UI**: Removing leftover popup/modal logic if a feature is moved to "Fully Automatic" mode.
- **Resource Cleanup**: Ensuring background threads are correctly joined and resources freed upon project completion.
