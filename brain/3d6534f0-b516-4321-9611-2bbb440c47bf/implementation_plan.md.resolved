# CLIProxyAPI Management Web Dashboard

Xây dựng một trang web local (single-page) để quản lý CLIProxyAPI, thay vì dùng terminal. Dashboard sẽ giao tiếp trực tiếp với Management API (`/v0/management/*`) của CLIProxyAPI đang chạy tại port 8317.

## Proposed Changes

### Config Update

#### [MODIFY] [config.yaml](file:///F:/1.%20Edit%20Videos/4.%20Tool%20YTB/CLIProxyAPI_6.8.55_windows_amd64/config.yaml)

Thêm `remote-management.secret-key` và `usage-statistics-enabled: true` để bật Management API và usage tracking.

---

### Web Dashboard (Single HTML file)

#### [NEW] [dashboard.html](file:///F:/1.%20Edit%20Videos/4.%20Tool%20YTB/CLIProxyAPI_6.8.55_windows_amd64/dashboard.html)

Một file HTML duy nhất chứa tất cả CSS + JS, gồm các panel:

| Panel | API Endpoint | Chức năng |
|-------|-------------|-----------|
| **Server Info** | `GET /v0/management/config` + `GET /v0/management/latest-version` | Version hiện tại, status, port |
| **Accounts** | `GET /v0/management/auth-files` | Danh sách tài khoản OAuth, provider, status, email |
| **Models** | `GET /v1/models` | Danh sách models khả dụng, nhóm theo provider |
| **Usage** | `GET /usage` | Thống kê: total requests, tokens, success/fail, biểu đồ theo giờ |
| **Config** | `GET /v0/management/config` | Hiển thị cấu hình JSON hiện tại |
| **Add Account** | `GET /v0/management/gemini-cli-auth-url`, `anthropic-auth-url`, etc. | Nút login OAuth cho từng provider |

**Design**: Dark theme, glassmorphism, smooth animations, Vietnamese labels. Tự động refresh mỗi 30s.

## Verification Plan

### Manual Verification
1. Khởi động lại CLIProxyAPI với config mới (có management secret-key)
2. Mở `dashboard.html` trong trình duyệt
3. Kiểm tra: accounts hiện đúng, models load, usage stats hiện, config viewer hoạt động
4. Thử nhấn nút OAuth login xem có mở đúng URL không
