# Hướng Dẫn Xây Dựng Ứng Dụng Desktop PyQt6

> Tổng hợp từ quá trình xây dựng, sửa đổi và cải tiến ứng dụng SRT Prompt Generator.

---

## 1. Cấu Trúc Dự Án

```
project/
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
├── core/                    # Backend logic (không phụ thuộc UI)
│   ├── api_client.py
│   ├── process_controller.py
│   └── prompt_generator.py
└── ui/                      # Toàn bộ giao diện
    ├── __init__.py
    ├── theme.py             # QSS stylesheet tập trung
    ├── icons/               # SVG icons cho arrows, buttons
    │   ├── arrow_down.svg
    │   └── arrow_up.svg
    ├── main_window.py       # Cửa sổ chính
    ├── settings_dialog.py   # Dialog cài đặt
    └── [feature]_section.py # Mỗi section/tab riêng 1 file
```

> [!IMPORTANT]
> **Tách biệt UI và Backend.** Core logic KHÔNG import bất kỳ module UI nào. UI gọi core qua interface rõ ràng. Điều này giúp thay đổi framework UI mà không ảnh hưởng logic.

---

## 2. Quản Lý Theme (QSS)

### Nguyên tắc cốt lõi

```python
# theme.py - Mẫu chuẩn
import os

_ICONS_DIR = os.path.join(os.path.dirname(__file__), "icons").replace("\\", "/")
_ARROW_DOWN = f"{_ICONS_DIR}/arrow_down.svg"
_ARROW_UP = f"{_ICONS_DIR}/arrow_up.svg"

def _build_stylesheet(bg_base, fg_primary, accent, border, ...):
    """Tạo QSS từ color tokens — DUY NHẤT 1 hàm tạo stylesheet."""
    return f"""
    QWidget {{ background-color: {bg_base}; color: {fg_primary}; }}
    /* ... tất cả rules ở đây ... */
    """

def get_dark_stylesheet():
    return _build_stylesheet(bg_base="#0f0f1a", fg_primary="#E2E8F0", ...)

def get_light_stylesheet():
    return _build_stylesheet(bg_base="#F8FAFC", fg_primary="#1E293B", ...)

def apply_theme(app, theme_name):
    app.setStyleSheet(get_light_stylesheet() if theme_name == "Light" 
                      else get_dark_stylesheet())
```

> [!CAUTION]
> **KHÔNG dùng inline `setStyleSheet()` rải rác.** Mọi styling phải tập trung trong `theme.py`. Inline style chỉ dùng cho các trường hợp đặc biệt (nút có màu riêng biệt).

---

## 3. QSS Pitfalls — Những Bẫy Phải Tránh

### 3.1. Mũi tên QComboBox / QSpinBox

> [!WARNING]
> **CSS `border-triangle` KHÔNG hoạt động trong Qt QSS** — render thành hình chữ nhật.
> Khi style BẤT KỲ sub-control nào (`::drop-down`, `::up-button`), Qt **xóa** native arrow.

**❌ KHÔNG làm:**
```css
/* Border-triangle — KHÔNG hoạt động trong Qt */
QComboBox::down-arrow {
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid white;
}

/* image: none — xóa luôn mũi tên */
QComboBox::down-arrow { image: none; }
```

**✅ Cách đúng duy nhất: dùng file SVG**
```css
QComboBox::down-arrow {
    image: url(path/to/arrow_down.svg);
    width: 10px;
    height: 6px;
}
QSpinBox::up-arrow {
    image: url(path/to/arrow_up.svg);
    width: 8px;
    height: 5px;
}
```

**File SVG mẫu (`arrow_down.svg`):**
```xml
<svg xmlns="http://www.w3.org/2000/svg" width="10" height="6" viewBox="0 0 10 6">
  <polygon points="0,0 10,0 5,6" fill="#94A3B8"/>
</svg>
```

> [!TIP]
> Dùng `os.path` + `.replace("\\", "/")` để tạo đường dẫn SVG — Qt QSS yêu cầu forward-slash trên Windows.

### 3.2. Font và Emoji

**❌ KHÔNG dùng emoji cho button text:**
```python
btn = QPushButton("↻")      # Có thể render thành ô vuông
btn = QPushButton("❌")     # Font QSS override gây lỗi
```

**✅ Dùng text thuần hoặc SVG icon:**
```python
btn = QPushButton("Refresh")  # Luôn hiển thị đúng
btn = QPushButton("X")        # Đơn giản, đáng tin cậy
```

### 3.3. Sizing — setFixedSize vs setMinimumWidth

| Method | Khi nào dùng |
|--------|-------------|
| `setFixedSize(w, h)` | Biết chính xác kích thước cần thiết (icon button `"..."`) |
| `setFixedHeight(h)` + `setMinimumWidth(w)` | Text button có thể dài ngắn khác nhau |
| `setFixedHeight(h)` chỉ | Cho input fields, muốn co giãn theo layout |

```python
# Button text ngắn, kích thước biết trước
btn_browse = QPushButton("...")
btn_browse.setFixedSize(28, 26)

# Button text có thể thay đổi
btn_refresh = QPushButton("Refresh")
btn_refresh.setFixedSize(60, 26)  # Compact, đã test vừa text
```

---

## 4. Layout Best Practices

### 4.1. Cấu trúc layout chuẩn

```python
def _build_ui(self):
    main_layout = QVBoxLayout(self)
    main_layout.setContentsMargins(8, 4, 8, 4)
    main_layout.setSpacing(2)

    # Mỗi row là 1 QHBoxLayout
    row = QHBoxLayout()
    row.setSpacing(4)
    row.addWidget(label)
    row.addWidget(combo)
    row.addWidget(button)
    row.addStretch()          # ← Đẩy widgets sang trái
    main_layout.addLayout(row)
```

> [!IMPORTANT]
> **Luôn dùng `addStretch()`** sau nhóm widgets để chúng không bị kéo giãn ra toàn bộ chiều ngang.

### 4.2. Splitter cho layout 2 cột

```python
splitter = QSplitter(Qt.Orientation.Horizontal)
splitter.addWidget(left_panel)
splitter.addWidget(right_panel)
splitter.setSizes([600, 400])      # Tỷ lệ ban đầu
splitter.setStretchFactor(0, 3)    # Left co giãn nhiều hơn
splitter.setStretchFactor(1, 2)
```

---

## 5. Thread Safety

> [!CAUTION]
> **KHÔNG BAO GIỜ** update UI từ background thread. PyQt6 sẽ crash.

```python
import threading
from PyQt6.QtCore import QTimer

# ❌ SAI: update trực tiếp từ thread
def worker():
    result = api_call()
    self.label.setText(result)  # CRASH!

# ✅ ĐÚNG: dùng QTimer.singleShot chuyển về main thread
def worker():
    result = api_call()
    QTimer.singleShot(0, lambda: self.label.setText(result))

threading.Thread(target=worker, daemon=True).start()
```

---

## 6. Dialog Pattern

```python
class SettingsDialog(QDialog):
    def __init__(self, parent, config):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setMinimumWidth(600)
        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint
        )
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        content_layout = QVBoxLayout(content)
        # ... add sections ...
        scroll.setWidget(content)
        layout.addWidget(scroll)
```

---

## 7. Nút Icon Tròn (Pattern)

```python
# Nút X tròn đỏ (xoá endpoint, đóng dialog, v.v.)
btn = QPushButton("✕")
btn.setFixedSize(26, 26)
btn.setStyleSheet("""
    QPushButton {
        background-color: #f44336;
        color: white;
        border: none;
        border-radius: 13px;   /* = size/2 → hình tròn */
        font-size: 13px;
        font-weight: bold;
    }
    QPushButton:hover { background-color: #d32f2f; }
""")
```

---

## 8. Checklist Trước Khi Hoàn Thành

- [ ] **Theme tập trung** — Mọi styling trong `theme.py`, không rải rác inline
- [ ] **Arrows dùng SVG** — `image: url()`, KHÔNG dùng CSS border-triangle
- [ ] **Không emoji trong buttons** — Dùng text thuần hoặc SVG icon
- [ ] **Thread safety** — Mọi UI update qua `QTimer.singleShot(0, ...)`
- [ ] **Layout stretch** — `addStretch()` sau nhóm widgets
- [ ] **Button sizing** — `setFixedSize` cho button nhỏ, `setMinimumWidth` cho button co giãn
- [ ] **Import check** — `python -c "from ui.main_window import MainWindow"`
- [ ] **Forward-slash paths** — SVG/icon paths dùng `/` trên Windows
- [ ] **Tách backend/UI** — Core logic không import module UI

---

## 9. Dependencies Tối Thiểu

```txt
# requirements.txt
PyQt6>=6.5.0
```

```python
# main.py — Entry point mẫu
import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.theme import get_dark_stylesheet

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(get_dark_stylesheet())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```
