# CLIProxyAPI Management Dashboard — Walkthrough

## Đã làm gì

### 1. Cập nhật Config
Thêm `remote-management.secret-key` và `usage-statistics-enabled` vào [config.yaml](file:///F:/1.%20Edit%20Videos/4.%20Tool%20YTB/CLIProxyAPI_6.8.55_windows_amd64/config.yaml) để bật Management API.

### 2. Tạo Dashboard
File: [dashboard.html](file:///F:/1.%20Edit%20Videos/4.%20Tool%20YTB/CLIProxyAPI_6.8.55_windows_amd64/dashboard.html)

| Tab | Chức năng |
|-----|-----------|
| 📊 **Tổng quan** | Stats cards + bảng tài khoản + model tags |
| 👤 **Tài khoản** | Danh sách OAuth accounts với email, provider, trạng thái |
| 🤖 **Models** | Models nhóm theo provider (Google, Antigravity) |
| 📈 **Thống kê** | Usage stats: requests, tokens, biểu đồ theo giờ |
| ⚙️ **Cấu hình** | Config JSON viewer |
| 🔑 **Đăng nhập** | Nút OAuth login + connection settings |

### 3. Kiểm tra API

| Endpoint | Kết quả |
|----------|---------|
| `GET /v1/models` | ✅ 16 models (Gemini + Antigravity) |
| `GET /v0/management/auth-files` | ✅ 11 tài khoản (5 Antigravity + 6 Gemini CLI) |
| CORS headers | ✅ `Access-Control-Allow-Origin: *` — tương thích file:/// |

## Cách mở

Mở file trực tiếp trong trình duyệt:
```
F:\1. Edit Videos\4. Tool YTB\CLIProxyAPI_6.8.55_windows_amd64\dashboard.html
```
