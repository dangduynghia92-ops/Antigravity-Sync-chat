# PyQt6 Migration — Walkthrough

## Summary
Migrated entire UI layer from **customtkinter** to **PyQt6** across 11 files + entry point. Backend (api_client, process_controller, prompt_generator, srt_parser) unchanged.

## Files Rewritten

| File | Key Change |
|---|---|
| `theme.py` | ttk Style → QSS stylesheet (~240 lines of CSS-like styling) |
| `log_section.py` | CTkTextbox → QTextEdit + QLabel status |
| `searchable_combo.py` | Custom dropdown (242 lines) → QComboBox + QCompleter (~55 lines) |
| `srt_preview.py` | CTkFrame → QWidget + QTextEdit |
| `config_section.py` | CTkFrame + CTkCheckBox → QWidget + QCheckBox + QSpinBox |
| `projects_section.py` | ttk.Treeview → QTreeWidget with QHeaderView |
| `actions_section.py` | CTkButton → QPushButton |
| `settings_dialog.py` | CTkToplevel → QDialog + QScrollArea |
| `product_tab.py` | CTkFrame (782 lines) → QWidget + QSplitter (~600 lines) |
| `main_window.py` | CTk + CTkSegmentedButton → QMainWindow + QTabWidget |
| `main.py` | CTk mainloop → QApplication.exec() |

## Key Improvements

### Performance
- **GPU-accelerated rendering** vs Canvas-based
- **Native QTabWidget** — instant tab switching, no `grid_remove` hack needed
- **QSplitter** — native, smooth resizable panels

### Thread Safety
- `self.after(ms, fn)` → `QTimer.singleShot(0, fn)` — Qt's thread-safe scheduling
- `threading.Event` popup pattern preserved for rate-limit recovery

### Styling
- Single **QSS stylesheet** applied globally — consistent dark theme everywhere
- No more per-widget color configs — one source of truth in `theme.py`

### Simplification  
- `SearchableCombo`: 242 → 55 lines (QCompleter does all the work)
- No more `pack_propagate(False)` hacks
- No `tkinter` or `ttk` imports anywhere

## Verification
- ✅ `python -c "from ui.main_window import MainWindow"` → All imports OK
- ✅ `python main.py` → App launched, no errors, no console output
