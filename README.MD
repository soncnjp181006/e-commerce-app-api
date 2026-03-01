# Môi trường Window

# Mục Lục

- [Môi trường Window](#môi-trường-window)
- [Mục Lục](#mục-lục)
- [Phần 1. Thiết lập cơ bản](#phần-1-thiết-lập-cơ-bản)
  - [1.1. Khởi tạo môi trường `venv`](#11-khởi-tạo-môi-trường-venv)
  - [1.2. Khởi tạo file `requirements.txt` - Cài đặt thư viện cần thiết (hoặc có thể)](#12-khởi-tạo-file-requirementstxt---cài-đặt-thư-viện-cần-thiết-hoặc-có-thể)
  - [1.3. Khởi tạo file `.gitignore`, `.env`, và tạo folder `app/` dùng để lưu mã nguồn](#13-khởi-tạo-file-gitignore-env-và-tạo-folder-app-dùng-để-lưu-mã-nguồn)
  - [1.4. Cấu trúc dự án ở thời điểm hiện tại](#14-cấu-trúc-dự-án-ở-thời-điểm-hiện-tại)
  - [1.5. Cấu hình cơ bản cho file `.gitignore`](#15-cấu-hình-cơ-bản-cho-file-gitignore)

# Phần 1. Thiết lập cơ bản

**Folder cha: `e-commerce-app-api/`**

## 1.1. Khởi tạo môi trường `venv`

***`terminal`:***

```shell
python -m venv .venv

.venv\Scripts\activate
```

## 1.2. Khởi tạo file `requirements.txt` - Cài đặt thư viện cần thiết (hoặc có thể)

***`requirements.txt`:***

```requirements
# WEB FRAMEWORK
fastapi  # Framework API hiện đại, hiệu năng cao, hỗ trợ async/await, tự động sinh docs (Swagger/ReDoc)
uvicorn[standard]    # ASGI server để chạy FastAPI, [standard] bao gồm websockets & http tools

# DATABASE
sqlalchemy           # ORM mạnh mẽ nhất Python - ánh xạ class Python ↔ bảng SQL, hỗ trợ nhiều DB
pymysql              # Driver kết nối MySQL/MariaDB thuần Python
cryptography         # Phụ thuộc của pymysql để hỗ trợ xác thực SSL/caching_sha2_password
alembic              # Migration tool cho SQLAlchemy - quản lý version schema database
asyncpg              # Driver PostgreSQL async hiệu năng cao (nếu chuyển sang PostgreSQL)
aiomysql             # Driver MySQL async, thay pymysql khi dùng SQLAlchemy async engine
redis                # Client Redis - dùng cho cache, session, rate limiting, pub/sub
motor                # Driver MongoDB async (nếu cần NoSQL cho một số collection)


# AUTHENTICATION & SECURITY
python-jose[cryptography]  # Tạo và xác thực JWT token (JSON Web Token) cho auth
passlib[bcrypt]    # Hash password an toàn, [bcrypt] dùng thuật toán bcrypt
python-multipart   # (đã có bên dưới, cần thiết cho OAuth2 form login của FastAPI)
authlib            # OAuth2/OpenID Connect client - đăng nhập qua Google, Facebook, GitHub...
pyotp              # Tạo mã OTP (TOTP/HOTP) cho xác thực 2 yếu tố (2FA)
itsdangerous       # Tạo token có chữ ký an toàn - dùng cho email verification, reset password

# VALIDATION & SETTINGS
pydantic[email]     # Validation dữ liệu request/response, [email] thêm validator cho email
pydantic-settings   # Quản lý config từ file .env hoặc biến môi trường với type checking
python-dotenv       # Đọc file .env vào os.environ khi khởi động ứng dụng

# EMAIL
fastapi-mail        # Gửi email HTML/text trong FastAPI, hỗ trợ template Jinja2, async
jinja2              # Template engine - render HTML email động với biến (thường đi kèm fastapi-mail)
emails              # Thư viện gửi email linh hoạt hơn, hỗ trợ SMTP/SendGrid/Mailgun

# FILE UPLOAD & IMAGE PROCESSING
python-multipart # Parse multipart/form-data - bắt buộc để upload file trong FastAPI
Pillow           # Xử lý ảnh: resize, crop, convert định dạng, tạo thumbnail

# Mở rộng - File & Storage
boto3            # AWS SDK - upload/download file lên S3 hoặc S3-compatible storage (MinIO)
cloudinary       # SDK Cloudinary - lưu trữ và transform ảnh/video trên cloud
aiofiles         # Đọc/ghi file bất đồng bộ (async), tránh block event loop khi xử lý file lớn
python-magic     # Detect MIME type thực của file (tránh giả mạo extension khi upload)

# UTILITIES
httpx            # HTTP client hỗ trợ async - gọi API bên ngoài, thay thế requests trong async app
python-slugify   # Tạo slug URL-friendly từ tiếng Việt/Unicode (vd: "Xin Chào" → "xin-chao")
celery           # Task queue - xử lý tác vụ nặng bất đồng bộ (gửi email, xử lý ảnh, report...)
flower           # Web UI giám sát Celery worker và task queue
apscheduler      # Lên lịch chạy task định kỳ (cron job) ngay trong ứng dụng Python
babel            # Đa ngôn ngữ (i18n/l10n) - format ngày giờ, tiền tệ theo locale
pytz             # Xử lý timezone, chuyển đổi múi giờ (zoneinfo là built-in từ Python 3.9+)
orjson           # Serialize/deserialize JSON cực nhanh, hỗ trợ datetime/UUID tự động

# CACHING & RATE LIMITING
fastapi-cache2   # Cache response API tự động với decorator, backend Redis/Memcached
slowapi          # Rate limiting cho FastAPI (giới hạn số request/phút theo IP hoặc user)

# MONITORING & LOGGING
loguru           # Logging đẹp và mạnh hơn module logging chuẩn, hỗ trợ rotation/compression
sentry-sdk       # Theo dõi lỗi và performance realtime trên Sentry platform
prometheus-fastapi-instrumentator  # Expose metrics Prometheus để monitor với Grafana

# WEBSOCKET & REALTIME
websockets       # Thư viện WebSocket thuần Python cho realtime features (chat, notification)

# TESTING & DATA SEEDING
pytest           # Framework test phổ biến nhất Python
pytest-asyncio   # Plugin cho pytest hỗ trợ test các hàm async/await
Faker            # Tạo dữ liệu giả (tên, email, địa chỉ...) để seed database hoặc test

factory-boy      # Tạo fixture/factory object test gắn với SQLAlchemy model, dùng cùng Faker
coverage         # Đo code coverage - xem bao nhiêu % code được test bao phủ
```

**Thực hiện cài đặt:**

***`terminal:`***

```shell
python -m pip install -r requirements.txt
```

## 1.3. Khởi tạo file `.gitignore`, `.env`, và tạo folder `app/` dùng để lưu mã nguồn

- File `.gitignore`: Loại bỏ những folder, file không muốn push lên github.
- File `.env`: Lưu cấu hình nhạy cảm (key, email, password, ...)
- Folder `app/`: Lưu mã nguồn backend.

## 1.4. Cấu trúc dự án ở thời điểm hiện tại

```
e-commerce-app-api/
├── .venv/
├── app/
├── README.MD
├── requirements.txt
├── .gitignore
├── .env
```

## 1.5. Cấu hình cơ bản cho file `.gitignore`

Ta không được push file `.env` lên trên github, đồng thời không push `.venv/` lên github vì rất nặng, thay vì đó ta đã có file `requirements.txt`. Chỉ cần tải về và cài đặt là được.

***`.gitignore`:***

```gitignore
.env
.venv
```
