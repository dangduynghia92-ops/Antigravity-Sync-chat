# Data Integrity and Structured Output Policies

These systems prioritize structured data to enable batch processing, reviewability, and resilience.

## The CSV-Only Export Standard

In complex AI workflows, unstructured text files (.txt) are often difficult to review or aggregate. A consistent design decision across projects is to **deprecate TXT exports** in favor of strictly structured **CSV files**.

### Advantages of a CSV Policy:
- **Reviewability**: Content is neatly aligned with time ranges and original source text.
- **Aggregation**: Multiple output files can be merged into a single `_MERGED_xxx.csv` for bulk review.
- **Automation**: Structured data allows for automated scoring (e.g., narrative scores < 8.0) and easier import into other video/scripting tools.

## Resilient File Writing and Management

### 1. Incremental Real-time Saving
Generation results are never held only in memory. An "Incremental Save" is performed after **every** successful AI call. This ensures that even in the case of a crash or power loss, only the *current* failing segment is lost.

### 2. Handling File Locks (`PermissionError`)
On Windows desktops, users often keep CSV results open in Excel, which locks the file and prevents the application from saving updates.
- **Pattern**: When a `PermissionError` is encountered, the system should catch it and attempt to write to an auto-incremented filename (e.g., `result_2.csv`, `result_3.csv`) rather than simply failing.

### 3. Encoding Standards
To ensure compatibility across Python and spreadsheet software:
- Always save files using **`utf-8-sig`** (UTF-8 with BOM). This ensures that special characters (Vietnamese, emojis, symbols) are correctly displayed in Excel.

## Versioning and Project Isolation
- Each run should be isolated in its own output directory or clearly versioned (e.g., `v1`, `v2`) to prevent accidental overwrites of valuable narrative data.
- Metadata files (like the generated Visual Bible or Review Reports) should be stored alongside the results for auditability.

## 4. In-Place Output Resolution (Relative Pathing)
For systems processing multiple independent source folders, it is more efficient to resolve output directories **relative to the input source** rather than in a fixed global location.
- **Pattern**: When a project is scanned, the system determines the absolute path of the input file and creates a project-specific subdirectory (e.g., `style_rewrite/`) within that same folder.
- **Benefits**:
  - **Organization**: Users find rewritten content exactly where their source files are.
  - **No Name Clashes**: Files with duplicate names across different projects (e.g., `Ch.1.txt`) are naturally isolated by their parent directories.
  - **Batch Ready**: High-level scripts can easily iterate through `**/style_rewrite/` to find all results.
