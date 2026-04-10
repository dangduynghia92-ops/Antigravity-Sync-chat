# PyQt Desktop AI App Design Patterns: Threading and UI

Integrating heavy LLM processing into a responsive desktop application requires careful multi-threading architecture to keep the UI from freezing.

## The Thread-Safe Worker Pattern

Standard `QThread` or `threading.Thread` usage can lead to crashes if they attempt to modify GUI widgets directly. The most stable approach is to use `pyqtSignal` for asynchronous communication.

### 1. The Controller/Worker Relationship
- The **`MainWindow`** or **`TabWidget`** (Main Thread) manages the UI.
- A **`ProcessController`** (Background Thread) manages the core logic, API calls, and queuing.
- **Safe Feedback**: The controller defines signals (e.g., `on_log`, `on_progress`, `on_project_updated`) that are emitted from the worker and connected to slots in the main thread.

### 2. Interaction from Background Threads
If the background thread requires user input (e.g., a decision on a rate-limit error or a narrative review check), it must not open a dialog directly. Instead:
1. The worker `emits` a signal.
2. The UI slot `opens` the modal dialog (`popup.exec()`).
3. The UI `signals` the result back to the worker (often through a shared thread-safe object or a callback result block).

## Multi-Threaded Batch Processing

For heavy workloads (e.g., processing multiple SRT files or script projects), a two-level concurrency model is used:

### 1. Multi-Folder/Project Concurrency (The Concurrent Folder Pattern)
When a user scans a parent directory containing multiple project folders, the system should process folders in parallel while keeping internal operations (like narrative flow) sequential.

- **Grouping Logic (`OrderedDict`)**: Group input files by their absolute parent directory path using an `OrderedDict`. This ensures that even when parallelized, the discovery order is respected and files remain grouped with their siblings.
- **Per-Folder Worker Tasks**: Wrap the entire project pipeline (Load -> Outline -> Rewrite -> Verify -> Merge) in a single worker function (e.g., `_process_one_folder`).
- **Parallel Dispatch**: Use a **`ThreadPoolExecutor`** to submit one `_process_one_folder` task per folder. The `max_workers` is set to the user-defined thread limit.
- **Progress Aggregation**: Use a thread-safe counter or list (e.g., `done_folders = [0]`) inside the worker thread (with a `Lock`) to track batch progress (e.g., "Folder 3/10 done").

### 2. Intra-Project Concurrency (Sequential vs. Parallel)
Within a single project folder, the processing mode depends on the narrative requirements:
- **Top/List Style**: Chapters can be processed **concurrently** (in parallel) because they are independent.
- **Narrative Style**: Chapters MUST be processed **sequentially**. Each chapter requires context (the previous 1-2 chapters) to maintain flow and avoid repetition.
- **The Mixed Parallelism Pattern**: To maximize throughput, the system parallelizes multiple **folders** (projects) while keeping chapters **sequential** within each. This architecture allows the system to remain lightning-fast in batch mode while preserving narrative integrity.

### Thread Safety and Shared State
- **Shared Status**: The global `status` dictionary must be updated using a **`threading.Lock`** when multiple threads (across folders or chapters) finish their tasks.
- **UI Refresh**: Emitting signals (e.g., `self.tree_refresh.emit()`) from multiple threads must be handled carefully. Usually, a final "Done" check or a debounced refresh in the UI avoids excessive re-renders.

## Centralized Logging

A dedicated **`LogSection`** or **`LogSectionWidget`** should handle all process feedback.
- Use a thread-safe logging helper that automatically handles `UnicodeEncodeError` (common on Windows CMD/older PyQt versions) by stripping unsupported characters or using robust encoding before writing to the terminal or a `QPlainTextEdit`.

## 4. Input Range Logic and Special Values

When providing LLMs with numeric constraints (like word counts or chapter counts), the UI often uses `QSpinBox` pairs.

### Handling "No Limit" (The Zero-Pattern)
A robust pattern for these inputs is to treat `0` as an "undefined" or "no limit" state.
- **UI Representation**: Set `specialValueText` to a symbol like `"—"` or `"∞"` so the user sees a dash instead of `0`.
- **String Generation**: A helper function (e.g., `build_word_count_rule`) converts these values into natural language for the LLM prompt:
  - `(Min=500, Max=1000)` -> `"500 to 1000 words"`
  - `(Min=500, Max=0)` -> `"at least 500 words"`
  - `(Min=0, Max=1000)` -> `"at most 1000 words"`
  - `(Min=0, Max=0)` -> `"no specific limit"`

This decoupling of UI values from prompt instructions prevents technical jargon (like "0-max") from entering the creative prompt.
