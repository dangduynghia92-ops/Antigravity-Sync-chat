# Hướng Dẫn Cài Đặt CLIProxyAPI & Kết Nối Với Tool Script_Split_Chapter

## CLIProxyAPI Là Gì?

CLIProxyAPI là một **proxy server** biến đăng ký Gemini CLI / Claude Code / OpenAI Codex (OAuth miễn phí) thành **API endpoint chuẩn OpenAI** (`/v1/chat/completions`).

Điều này có nghĩa: **bạn dùng tài khoản Google/Anthropic/OpenAI OAuth miễn phí** → CLIProxyAPI tạo ra API endpoint → Tool Script_Split_Chapter gọi API qua endpoint đó → **không cần trả tiền API key**.

---

## Bước 1: Tải Bản Build Cho Windows

CLIProxyAPI viết bằng Go. Bạn **không cần build từ source** — tải bản release sẵn:

1. Truy cập: https://github.com/router-for-me/CLIProxyAPI/releases
2. Tải file `cli-proxy-api_windows_amd64.zip` (hoặc tương tự)
3. Giải nén vào thư mục, ví dụ: `F:\1. Edit Videos\4. Tool YTB\CLIProxyAPI-main\bin\`

> [!TIP]
> Hoặc tải **GUI Desktop App** (dễ dùng hơn): https://github.com/router-for-me/EasyCLI/releases

---

## Bước 2: Tạo File Config

Tạo file `config.yaml` cùng thư mục với file exe. Nội dung tối thiểu:

```yaml
# Chỉ cho phép truy cập từ máy local
host: "127.0.0.1"

# Port mặc định
port: 8317

# API key để tool của bạn dùng khi gọi API
api-keys:
  - "my-secret-key-123"

# Tắt debug (bật nếu cần troubleshoot)
debug: false

# Retry khi bị lỗi
request-retry: 3
```

---

## Bước 3: Đăng Nhập OAuth (Lấy Token Miễn Phí)

Chạy CLIProxyAPI lần đầu, nó sẽ tự mở trình duyệt để bạn đăng nhập:

### Gemini (Google) — Khuyến nghị cho tool của bạn:
```powershell
# Chạy proxy
.\cli-proxy-api.exe
```

Sau khi chạy, truy cập management UI tại `http://127.0.0.1:8317` để đăng nhập Google account.

Hoặc dùng CLI flow:
```powershell
# Auth Gemini CLI bằng tay
.\cli-proxy-api.exe auth gemini
```

### Claude (Anthropic):
```powershell
.\cli-proxy-api.exe auth claude
```

> [!IMPORTANT]
> Bạn có thể đăng nhập **nhiều tài khoản** cho mỗi provider. CLIProxyAPI sẽ tự động **round-robin** giữa các tài khoản để tránh rate limit.

---

## Bước 4: Chạy CLIProxyAPI

```powershell
cd "F:\1. Edit Videos\4. Tool YTB\CLIProxyAPI-main\bin"
.\cli-proxy-api.exe
```

Server chạy tại: `http://127.0.0.1:8317`

Kiểm tra hoạt động:
```powershell
curl http://127.0.0.1:8317/v1/models -H "Authorization: Bearer my-secret-key-123"
```

---

## Bước 5: Kết Nối Với Tool Script_Split_Chapter

Tool của bạn dùng format **OpenAI-compatible** (`/v1/chat/completions` + Bearer token). CLIProxyAPI cung cấp đúng format này.

### Cấu hình trong Tool:

Mở **Settings** trong app → Tab **API Endpoints**, điền:

| Field | Giá trị |
|-------|---------|
| **Base URL** | `http://127.0.0.1:8317` |
| **API Key** | `my-secret-key-123` (key bạn đặt trong `config.yaml`) |
| **Flash Model** | `gemini-2.5-flash` |
| **Pro Model** | `gemini-2.5-pro` |
| **Enabled** | ✅ |

> [!NOTE]
> Tool sẽ tự nối thêm `/v1/chat/completions` vào Base URL, nên chỉ cần nhập `http://127.0.0.1:8317`.

### Cách hoạt động:

```
Tool (Script_Split_Chapter)
    │
    ▼ POST http://127.0.0.1:8317/v1/chat/completions
    │ Header: Authorization: Bearer my-secret-key-123
    │ Body: { model: "gemini-2.5-flash", messages: [...] }
    │
CLIProxyAPI (proxy)
    │
    ▼ Forward request dùng OAuth token (Google/Claude/OpenAI)
    │
Google Gemini / Claude / OpenAI API
```

---

## Bước 6 (Tùy Chọn): Multi-Account Load Balancing

Nếu bạn có **nhiều tài khoản Google**, đăng nhập tất cả để CLIProxyAPI tự phân tải:

```powershell
# Đăng nhập thêm tài khoản
.\cli-proxy-api.exe auth gemini
# (mở browser → đăng nhập tài khoản Google khác)
```

CLIProxyAPI round-robin giữa các account → giảm đáng kể rate limit 429.

---

## Tóm Tắt Nhanh

| Mục | Chi tiết |
|-----|----------|
| **Tải về** | [Releases](https://github.com/router-for-me/CLIProxyAPI/releases) hoặc [EasyCLI GUI](https://github.com/router-for-me/EasyCLI/releases) |
| **Config tối thiểu** | `host`, `port`, `api-keys` |
| **Auth** | `.\cli-proxy-api.exe auth gemini` |
| **Chạy** | `.\cli-proxy-api.exe` → server tại `http://127.0.0.1:8317` |
| **Trong Tool** | Base URL = `http://127.0.0.1:8317`, API Key = key trong config |
| **Model** | Flash: `gemini-2.5-flash`, Pro: `gemini-2.5-pro` |

> [!CAUTION]
> CLIProxyAPI dùng **OAuth token từ free tier** nên có giới hạn quota. Nếu bị rate limit nhiều, hãy thêm nhiều tài khoản Google để round-robin.
