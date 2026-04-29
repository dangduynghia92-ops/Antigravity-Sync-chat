# No grep_search Rule

**MANDATORY across ALL conversations:**

- **NEVER** use the `grep_search` tool. It hangs the terminal and blocks the workflow.
- Use `view_file` to read file contents directly instead.
- If you need to find something in a file, open the file with `view_file` and read through it.
- If you need to find files matching a pattern, use `run_command` with PowerShell commands like `Get-ChildItem -Filter`.
