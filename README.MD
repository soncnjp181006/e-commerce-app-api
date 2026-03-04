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
- [Phần 2. Các phương thức HTTP phổ biến \& Các mã HTTP Status](#phần-2-các-phương-thức-http-phổ-biến--các-mã-http-status)
  - [2.1. Các phương thức HTTP phổ biến](#21-các-phương-thức-http-phổ-biến)
  - [2.2. Các mã HTTP Status](#22-các-mã-http-status)
    - [2.2.1. Tổng quan về HTTP Status](#221-tổng-quan-về-http-status)
    - [2.2.2. Mã 1xx – Informational (Thông Tin)](#222-mã-1xx--informational-thông-tin)
    - [2.2.3. Mã 2xx – Success (Thành Công)](#223-mã-2xx--success-thành-công)
    - [2.2.4. Mã 3xx – Redirection (Chuyển Hướng)](#224-mã-3xx--redirection-chuyển-hướng)
    - [2.2.5. Mã 4xx – Client Error (Lỗi Từ Client)](#225-mã-4xx--client-error-lỗi-từ-client)
    - [2.2.6. Mã 5xx – Server Error (Lỗi Từ Server)](#226-mã-5xx--server-error-lỗi-từ-server)
    - [2.2.7. Tóm tắt](#227-tóm-tắt)
- [Phần 3. Làm quen với router - Phần này không có trong dự án chính thức](#phần-3-làm-quen-với-router---phần-này-không-có-trong-dự-án-chính-thức)
  - [3.1. Cách sử dụng `APIRouter`](#31-cách-sử-dụng-apirouter)
  - [3.2. Viết API cơ bản - Viết các router của một app todo-list cơ bản](#32-viết-api-cơ-bản---viết-các-router-của-một-app-todo-list-cơ-bản)
  - [3.3. Thiết kế chuẩn REST API - Thiết kế lại 3.2](#33-thiết-kế-chuẩn-rest-api---thiết-kế-lại-32)
  - [3.4. Thực hiện request](#34-thực-hiện-request)
- [Phần 4. Dữ liệu được định nghĩa từ trước - Phần này không có trong dự án chính thức](#phần-4-dữ-liệu-được-định-nghĩa-từ-trước---phần-này-không-có-trong-dự-án-chính-thức)
- [Phần 5. Thư mục `app/core` - Lưu cấu hình trung tâm](#phần-5-thư-mục-appcore---lưu-cấu-hình-trung-tâm)
- [Phần 6. Thư mục `app/database` - Kết nối database](#phần-6-thư-mục-appdatabase---kết-nối-database)
- [Phần 7. Thư mục `app/schemas/`  - Nơi chứa Pydantic models](#phần-7-thư-mục-appschemas----nơi-chứa-pydantic-models)
- [Phần 8. Thư mục `app/services/` - Xử lí nghiệp vụ chính của ứng dụng](#phần-8-thư-mục-appservices---xử-lí-nghiệp-vụ-chính-của-ứng-dụng)
  - [8.1. Phân tích](#81-phân-tích)
  - [8.2. Ví dụ](#82-ví-dụ)
- [Phần 9. Thư mục `app/middlewares/` - Lớp chạy trước mỗi request](#phần-9-thư-mục-appmiddlewares---lớp-chạy-trước-mỗi-request)
  - [9.1 Middleware dùng cho](#91-middleware-dùng-cho)
  - [9.2. Mối quan hệ với `core/`](#92-mối-quan-hệ-với-core)
    - [`core/` là gì?](#core-là-gì)
    - [`middlewares/` là gì?](#middlewares-là-gì)
    - [Ví dụ 1](#ví-dụ-1)
- [Phần 10. Thư mục `app/api/` - Định nghĩa các route/endpoint (REST API, WebSocket...)](#phần-10-thư-mục-appapi---định-nghĩa-các-routeendpoint-rest-api-websocket)
- [Phần 11. Thư mục `dependencies/`](#phần-11-thư-mục-dependencies)
  - [11.1. Chức năng](#111-chức-năng)
  - [11.2. Ví dụ](#112-ví-dụ)
    - [11.2.1. Inject DB](#1121-inject-db)
    - [11.2.2. Lấy current user (Auth)](#1122-lấy-current-user-auth)
    - [11.2.3. Phân quyền](#1123-phân-quyền)
  - [Lưu ý](#lưu-ý)
  - [11.3. Mối quan hệ với `core/`](#113-mối-quan-hệ-với-core)
- [Phần 12. Kết nối database MySQL - Test](#phần-12-kết-nối-database-mysql---test)
  - [12.1. Triển khai code test](#121-triển-khai-code-test)
  - [12.2. Triển khai code vào thư mục test](#122-triển-khai-code-vào-thư-mục-test)
    - [12.2.1. Khởi tạo file cấu hình trung tâm `settings.py`](#1221-khởi-tạo-file-cấu-hình-trung-tâm-settingspy)
    - [12.2.2. Khởi tạo file `.env` - lưu thông tin nhạy cảm](#1222-khởi-tạo-file-env---lưu-thông-tin-nhạy-cảm)
    - [12.2.3. Chuyển mã từ `test.py` vào thư mục /test/app/database](#1223-chuyển-mã-từ-testpy-vào-thư-mục-testappdatabase)
      - [12.2.3.1. Khởi tạo file `database.db` - Tạo Engine (kết nối database, cấu hình engine)](#12231-khởi-tạo-file-databasedb---tạo-engine-kết-nối-database-cấu-hình-engine)
      - [12.2.3.2. Khởi tạo file `base.py` - Base ORM (Tạo class Base để các model kế thừa)](#12232-khởi-tạo-file-basepy---base-orm-tạo-class-base-để-các-model-kế-thừa)
      - [12.2.3.3. Khởi tạo thư mục `models/` - khởi tạo, lưu trữ các bảng database](#12233-khởi-tạo-thư-mục-models---khởi-tạo-lưu-trữ-các-bảng-database)
        - [12.2.3.3.1. Khởi tạo `models/models.py`](#122331-khởi-tạo-modelsmodelspy)
        - [12.2.3.3.2. Khởi tạo `models/create_table.py` dùng để tạo bảng db trong MySQL - Mục tiêu của file này là import các file cấu trúc bảng như `models.py` (các file tương tự này mới chỉ viết cấu trúc bảng, chứ chưa tạo bảng trong MySQL)vào và sẽ thực hiện tạo bảng trong file này (điều này giúp các file lập bảng trông gọn, sạch)](#122332-khởi-tạo-modelscreate_tablepy-dùng-để-tạo-bảng-db-trong-mysql---mục-tiêu-của-file-này-là-import-các-file-cấu-trúc-bảng-như-modelspy-các-file-tương-tự-này-mới-chỉ-viết-cấu-trúc-bảng-chứ-chưa-tạo-bảng-trong-mysqlvào-và-sẽ-thực-hiện-tạo-bảng-trong-file-này-điều-này-giúp-các-file-lập-bảng-trông-gọn-sạch)
    - [12.2.4. Test thành quả đến hết 12.2.3](#1224-test-thành-quả-đến-hết-1223)
- [Phần 13. Viết API, Thực hiện truy vấn - Test](#phần-13-viết-api-thực-hiện-truy-vấn---test)
  - [13.1. Triển khai code test](#131-triển-khai-code-test)
  - [13.2. Triển khai code từ `test.py` vào thư mục `test/`](#132-triển-khai-code-từ-testpy-vào-thư-mục-test)
    - [13.2.1. Cấu trúc folder](#1321-cấu-trúc-folder)
    - [13.2.1. Khởi tạo file `database/session.py` lưu hàm `get_db()`, sau đó import vào `database.py`](#1321-khởi-tạo-file-databasesessionpy-lưu-hàm-get_db-sau-đó-import-vào-databasepy)
    - [13.2.2. Khởi tạo file `schemas/schemas.py`](#1322-khởi-tạo-file-schemasschemaspy)
    - [12.2.3. Khởi tạo file `repository/repository.py`](#1223-khởi-tạo-file-repositoryrepositorypy)
    - [Phần 13.2.3. Khởi tạo file `services/services.py`](#phần-1323-khởi-tạo-file-servicesservicespy)
    - [Phần 13.2.4. Khởi tạo file `api/api.py`](#phần-1324-khởi-tạo-file-apiapipy)
  - [13.3. Test thành quả đến hết 13.2](#133-test-thành-quả-đến-hết-132)
- [Phần 14. \[Dự án chính thức\] - Kết Nối Database](#phần-14-dự-án-chính-thức---kết-nối-database)
  - [14.1. MySQL - Tạo cơ sở dữ liệu liệu và cấp quyền cho user](#141-mysql---tạo-cơ-sở-dữ-liệu-liệu-và-cấp-quyền-cho-user)
  - [14.2. Cấu hình kết nối database](#142-cấu-hình-kết-nối-database)
    - [14.2.1. Thiết lập file cấu hình nhạy cảm `.env`](#1421-thiết-lập-file-cấu-hình-nhạy-cảm-env)
    - [14.2.2. Thiết lập file `app/core/settings.py` - Cấu hình trung tâm](#1422-thiết-lập-file-appcoresettingspy---cấu-hình-trung-tâm)
      - [Cấu hình chung của các file `settings.py` khi khởi tạo](#cấu-hình-chung-của-các-file-settingspy-khi-khởi-tạo)
      - [Import cấu hình kết nối database từ `.env` vào `settings.py`](#import-cấu-hình-kết-nối-database-từ-env-vào-settingspy)
    - [14.2.3. Thực hiện quá trình test có lỗi không](#1423-thực-hiện-quá-trình-test-có-lỗi-không)
    - [14.2.4. Chuyển phần 14.2.3 vào các file trong `database/`](#1424-chuyển-phần-1423-vào-các-file-trong-database)
    - [14.2.3. Thực hiện quá trình test lỗi](#1423-thực-hiện-quá-trình-test-lỗi)
- [Phần 15. Thứ tự thiết kế:](#phần-15-thứ-tự-thiết-kế)
- [Phần 16. SQL \[Phần này không có trong dự án chính thức\]](#phần-16-sql-phần-này-không-có-trong-dự-án-chính-thức)
  - [16.1. Tổng quan](#161-tổng-quan)
    - [16.1.1. Database (Cơ sở dữ liệu)](#1611-database-cơ-sở-dữ-liệu)
    - [16.1.2. Table (Bảng)](#1612-table-bảng)
    - [16.1.3. Kiểu dữ liệu](#1613-kiểu-dữ-liệu)
      - [INT (Số nguyên)](#int-số-nguyên)
      - [VARCHAR](#varchar)
      - [DATE (Ngày tháng)](#date-ngày-tháng)
      - [TEXT (Văn bản lớn)](#text-văn-bản-lớn)
      - [JSON (Dữ liệu cấu trúc)](#json-dữ-liệu-cấu-trúc)
  - [16.2. Thao tác trên MySQL \& `sqlalchemy` trong Python](#162-thao-tác-trên-mysql--sqlalchemy-trong-python)
    - [Tạo bảng cơ bản](#tạo-bảng-cơ-bản)
      - [Bảng Users](#bảng-users)
  - [16.3. Mối quan hệ giữa `FOREIGN KEY` và `PRIMARY KEY`](#163-mối-quan-hệ-giữa-foreign-key-và-primary-key)
    - [16.3.1. Định nghĩa](#1631-định-nghĩa)
      - [`PRIMARY KEY` (PK - Khóa chính)](#primary-key-pk---khóa-chính)
      - [`FOREIGN KEY` (FK - Khóa ngoại)](#foreign-key-fk---khóa-ngoại)
      - [Mối quan hệ giữa `PRIMARY KEY` và `FOREIGN KEY`](#mối-quan-hệ-giữa-primary-key-và-foreign-key)

# Phần 1. Thiết lập cơ bản

**Folder cha: `e-commerce-app-api/`**

## 1.1. Khởi tạo môi trường `venv`

***`terminal`:***

```shell
python -m venv .venv # python và py như nhau

.venv\Scripts\activate
```

hoặc:

```shell
py -3.14 -m venv .venv
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

***`terminal`:***

```shell
python -m pip install -r requirements.txt
```

## 1.3. Khởi tạo file `.gitignore`, `.env`, và tạo folder `app/` dùng để lưu mã nguồn

- File `.gitignore`: Loại bỏ những folder, file không muốn push lên github.
- File `.env`: Lưu cấu hình nhạy cảm (key, email, password, ...)
- Folder `app/`: Lưu mã nguồn backend.

## 1.4. Cấu trúc dự án ở thời điểm hiện tại

```txt
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

# Phần 2. Các phương thức HTTP phổ biến & Các mã HTTP Status

## 2.1. Các phương thức HTTP phổ biến

- **GET**: Dùng để lấy thông tin từ máy chủ web. Thông tin được gửi trong URL của yêu cầu.  
- **POST**: Dùng để gửi thông tin đến máy chủ web. Thông tin được gửi trong phần thân (body) của yêu cầu.  
- **PUT**: Dùng để cập nhật thông tin trên máy chủ web. Thông tin được gửi trong phần thân của yêu cầu.  
- **PATCH**: Dùng để cập nhật một phần thông tin trên máy chủ web. Thông tin được gửi trong phần thân của yêu cầu.  
- **DELETE**: Dùng để xóa thông tin khỏi máy chủ web. Thông tin được gửi trong URL của yêu cầu.  

```
@app.get(<URI>)
@app.post(<URI>)
@app.put(<URI>)
@app.patch(<URI>)
@app.delete(<URI>)
```

## 2.2. Các mã HTTP Status

### 2.2.1. Tổng quan về HTTP Status

| Dãy Mã | Phân Loại | Ý Nghĩa Tổng Quát |
|--------|-----------|-------------------|
| 1xx | Informational | Yêu cầu đã nhận, đang tiếp tục xử lý |
| 2xx | Success | Yêu cầu đã được nhận, hiểu và xử lý thành công |
| 3xx | Redirection | Cần thêm hành động để hoàn tất yêu cầu |
| 4xx | Client Error | Yêu cầu có lỗi từ phía client (sai cú pháp, thiếu quyền, v.v.) |
| 5xx | Server Error | Server gặp lỗi khi xử lý yêu cầu hợp lệ |

### 2.2.2. Mã 1xx – Informational (Thông Tin)

Ít khi sử dụng trong REST API thông thường, chủ yếu dùng trong giao thức WebSocket hoặc yêu cầu đặc biệt.

| Mã | Tên | Mô Tả | Trường Hợp Sử Dụng |
|----|-----|-------|-------------------|
| 100 | Continue | Client nên tiếp tục gửi yêu cầu | Dùng trong yêu cầu lớn có header `Expect: 100-continue` |
| 101 | Switching Protocols | Server đồng ý đổi giao thức | Nâng cấp từ HTTP sang WebSocket |

### 2.2.3. Mã 2xx – Success (Thành Công)

| Mã | Tên | Mô Tả | Trường Hợp Sử Dụng Trong API |
|----|-----|-------|-----------------------------|
| 200 | OK | Yêu cầu thành công | GET, PUT, PATCH thành công, trả về dữ liệu |
| 201 | Created | Tài nguyên mới được tạo thành công | POST tạo mới user, task, bài viết |
| 202 | Accepted | Yêu cầu đã chấp nhận nhưng chưa xử lý xong | Xử lý bất đồng bộ, hàng đợi tác vụ (background job) |
| 204 | No Content | Thành công nhưng không có nội dung trả về | DELETE thành công, hoặc cập nhật không cần trả dữ liệu |

**Lưu ý nghiệp vụ:**

- Khi tạo tài nguyên mới (POST), luôn trả về **201** kèm header `Location` trỏ đến resource mới.
- Khi xóa thành công và không cần trả dữ liệu, dùng **204** để tiết kiệm băng thông.

### 2.2.4. Mã 3xx – Redirection (Chuyển Hướng)

| Mã | Tên | Mô Tả | Trường Hợp Sử Dụng |
|----|-----|-------|-------------------|
| 301 | Moved Permanently | Tài nguyên đã chuyển vĩnh viễn | SEO, chuyển đổi URL cũ sang URL mới |
| 302 | Found | Chuyển hướng tạm thời | Chuyển hướng sau khi login, A/B testing |
| 304 | Not Modified | Tài nguyên không thay đổi (dùng với cache) | Khi client gửi `If-None-Match` hoặc `If-Modified-Since`, server trả 304 để client dùng cache |

**Lưu ý:** Trong REST API thuần túy, 3xx ít được dùng trực tiếp mà thường xử lý chuyển hướng ở phía frontend hoặc API gateway.

### 2.2.5. Mã 4xx – Client Error (Lỗi Từ Client)

| Mã | Tên | Mô Tả | Trường Hợp Sử Dụng Trong API |
|----|-----|-------|-----------------------------|
| 400 | Bad Request | Yêu cầu không hợp lệ về cú pháp hoặc dữ liệu | Dữ liệu gửi lên thiếu trường, sai định dạng, validation thất bại |
| 401 | Unauthorized | Chưa xác thực hoặc token không hợp lệ | Thiếu JWT token, token hết hạn, sai credentials |
| 403 | Forbidden | Đã xác thực nhưng không có quyền truy cập | User thường cố truy cập endpoint admin |
| 404 | Not Found | Tài nguyên không tồn tại | Request đến URL không có, hoặc ID user/task không tồn tại |
| 405 | Method Not Allowed | Phương thức HTTP không được hỗ trợ | Gọi DELETE vào endpoint chỉ hỗ trợ GET/POST |
| 409 | Conflict | Xung đột với trạng thái hiện tại của server | Đăng ký email đã tồn tại, version conflict trong cập nhật |
| 422 | Unprocessable Entity | Dữ liệu hợp lệ về cú pháp nhưng không thể xử lý về ngữ nghĩa | Validation lỗi chi tiết (FastAPI trả về mã này mặc định khi Pydantic validation fail) |
| 429 | Too Many Requests | Vượt quá giới hạn request (rate limit) | Client gửi quá nhiều yêu cầu trong thời gian ngắn |

**Phân biệt quan trọng:**

- **401 vs 403**: 401 là "chưa biết bạn là ai" (cần login), 403 là "biết bạn là ai nhưng bạn không được phép làm việc này".
- **400 vs 422**: 400 là lỗi cú pháp tổng quát, 422 là lỗi ngữ nghĩa/dữ liệu chi tiết (FastAPI ưu tiên dùng 422 cho validation error).

### 2.2.6. Mã 5xx – Server Error (Lỗi Từ Server)

| Mã | Tên | Mô Tả | Trường Hợp Sử Dụng |
|----|-----|-------|-------------------|
| 500 | Internal Server Error | Lỗi tổng quát khi server gặp sự cố không mong muốn | Exception không được xử lý, lỗi code, lỗi database bất ngờ |
| 501 | Not Implemented | Server không hỗ trợ chức năng được yêu cầu | Endpoint chưa được triển khai |
| 502 | Bad Gateway | Server nhận phản hồi không hợp lệ từ upstream server | Lỗi khi gọi API bên thứ ba, reverse proxy lỗi |
| 503 | Service Unavailable | Server tạm thời không khả dụng | Bảo trì hệ thống, quá tải, database đang khởi động lại |
| 504 | Gateway Timeout | Server không nhận được phản hồi từ upstream kịp thời | Timeout khi gọi external API, database query quá lâu |

**Lưu ý xử lý:**

- Luôn có cơ chế ghi log (logging) khi trả về 5xx để phục vụ debug.
- Với 503, nên kèm header `Retry-After` để client biết khi nào nên thử lại.

### 2.2.7. Tóm tắt

| Nghiệp Vụ | Status Code Khuyến Nghị | Ghi Chú |
|-----------|------------------------|---------|
| Tạo mới thành công | 201 Created | Kèm Location header |
| Đọc dữ liệu thành công | 200 OK | Trả về danh sách hoặc chi tiết |
| Cập nhật thành công | 200 OK hoặc 204 No Content | 204 nếu không cần trả dữ liệu mới |
| Xóa thành công | 204 No Content | Không có body trả về |
| Validation lỗi | 422 Unprocessable Entity | Kèm chi tiết lỗi từng trường |
| Không tìm thấy resource | 404 Not Found | Kiểm tra tồn tại trước khi xử lý |
| Thiếu xác thực | 401 Unauthorized | Yêu cầu client gửi token/credentials |
| Không có quyền | 403 Forbidden | Kiểm tra role/permission trước khi thực thi |
| Dữ liệu xung đột | 409 Conflict | Kiểm tra unique constraint trước khi insert |
| Lỗi server không xác định | 500 Internal Server Error | Ghi log đầy đủ, không lộ thông tin nhạy cảm |

# Phần 3. Làm quen với router - Phần này không có trong dự án chính thức

## 3.1. Cách sử dụng `APIRouter`

***`main.py`:***

```py
from fastapi import FastAPI

app = FastAPI()

app.get('/get')                    # http://127.0.0.1:8000/get
def hello_world() -> dict:
    return {'hello': 'world'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

**Để có thể nhìn thấy trực quan, rõ ràng hơn là nhìn màn hình chỉ có đầu ra JSON. Ta làm như sau:**

***`main.py`:***

```py
from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

@router.get('/')                # http://127.0.0.1:8000/get
def hello_world() -> dict:
    return {'hello': 'world'}

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

Khi chạy trên trình duyệt, nếu dùng đường link: `http://127.0.0.1:8000/get` thì hai đoạn mã trên có đầu ra như nhau. Nhưng đoạn mã thứ hai, ta chỉ cần thay thành: `http://127.0.0.1:8000/docs` thì sẽ có đầu ra như sau:

!['p3a1'](/assets/p3a1.png)

## 3.2. Viết API cơ bản - Viết các router của một app todo-list cơ bản

***`main.py`:***

```py
from fastapi import FastAPI, APIRouter, HTTPException
from typing import Dict

app = FastAPI()
router = APIRouter()

# Một mhiệm vụ có cấu trúc: {id: name}
task_list = [] # Danh sách nhiệm vụ 

# Xem nhiệm vụ -> get (lấy thông tin từ server)
@router.get("/{id}")
def get_task(id: int) -> Dict[str, object]:

    res = next((task for task in task_list if task["id"] == id), None)

    if res is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")

    return res

# Thêm nhiệm vụ -> post (gửi thông tin mới -> yêu cầu server thêm và lưu lại)
@router.post("/")
def add_task(name: str) -> Dict[str, object]:

    if not name.strip():
        # raise tương tự return -> nhung dùng để bắt lỗi
        # HTTPException -> lỗi API
        # status_code -> trạng thái lỗi
        # detail -> đầu ra
        # return detail, status_code
        raise HTTPException(status_code=400, detail="Tên nhiệm vụ không hợp lệ")

    new_task = {
        "id": len(task_list),
        "name": name
    }

    task_list.append(new_task)

    return new_task


app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

## 3.3. Thiết kế chuẩn REST API - Thiết kế lại 3.2

***`main.py`:***

```py
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
router = APIRouter()

task_list = []

# Định nghĩa model
class TaskCreate(BaseModel): # Dùng để xem task
    name: str

class Task(BaseModel):       # Dùng để import task
    id: int
    name: str

@router.post('/', response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    new_task = {
        "id": len(task_list),
        "name": task.name
    }

    task_list.append(new_task)
    return new_task

@router.get('/{id}')
def get_task(id: int):
    res = next((task for task in task_list if task["id"] == id), None)

    if res is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")

    return res

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

**Giải thích:**

```py
@router.post('/', response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    new_task = {
        "id": len(task_list),
        "name": task.name
    }

    task_list.append(new_task)
    return new_task
```

**Ta có:**

- `response_model=Task`: bộ lọc thông báo đầu vào lấy từ client được lọc thành kiểu tương tự của class `Task`.  (Tức là loại bỏ các hàng dư thừa, chỉ giữ lại key `name`)
- `status_code` ở đây cho vào cũng được, không cho vào cũng được.
- `task: TaskCreate`: biến nhiệm vụ task có kiểu tương tự của class `TaskCreate`, nếu bị thiếu một key, thì key đó tự có value mặc định (0, ... hay gì không cần biết).

> Ở đây, đầu vào từ client được lọc bởi `Task` còn mỗi key `name`, không có key `id` sau đó ép thành biến `task`. Biến `task` buộc tuân theo `TaskCreate` nên `task{'name' = value_name}` sẽ được chuyển thành `task{'id': id_value, 'name': name_value}`

## 3.4. Thực hiện request

> Truy cập lại trang: <http://127.0.0.1:8000/docs>
>
> Ấn vào các nút `Try it out` để thực hiện request dễ dàng, thay vì sử dụng terminal để thực hiện request.
>
> Các trường `URL` trong trang web chính là các mẫu lệnh dùng để request trên terminal. Thay vì request trên web.

# Phần 4. Dữ liệu được định nghĩa từ trước - Phần này không có trong dự án chính thức

```py
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import Dict

app = FastAPI()
router = APIRouter()
task_list = []

class StatusType(str, Enum):
    game = 'fi5' # key game có value mặc định 'fi5'

# Định nghĩa model
class TaskCreate(BaseModel): # Dùng để xem task
    name: str

class Task(BaseModel):       # Dùng để import task
    id: int
    name: str


@router.get('/{id}')
def get_task(id: int):
    res = next((task for task in task_list if task["id"] == id), None)

    if res is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")

    return res

@router.post('/', response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    new_task = {
        "id": len(task_list),
        "name": task.name,
        "game": StatusType.game # fi5
    }

    task_list.append(new_task)
    return new_task


app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

# Phần 5. Thư mục `app/core` - Lưu cấu hình trung tâm

Thư mục `core` dùng để lưu các file cấu hình trung tâm:

- settings.py - Cấu hình hệ thống (quản lý: Biến môi trường, Database URL, Secret Key, CORS, Debug mode)
- security.py - Bảo mật (Hash password, JWT token, OAuth2, Authentication logic)
- logging.py  - Ghi log hệ thống (ghi log request, ghi log lỗi, theo dõi hệ thống)
- constants.py - Hằng số hệ thống (chứa các giá trị không thể thay đổi)

# Phần 6. Thư mục `app/database` - Kết nối database

- database.py - Tạo Engine (kết nối database, cấu hình engine)

- session.py - Quản lý session (mỗi request có 1 session riêng, tránh rò rỉ khi kết nối)
- base.py - Base ORM (Tạo class Base để các model kế thừa)
- `models/` - Thư mục khởi tạo, lưu giữ các file tạo bảng database (mapping bảng db thành class Python)
- `repositories/` - Thư mục chứa các file, hàm truy vấn database
- `migrations/` - Alembic Migration (được Alembic tạo ra) (quản lí thay đổi schema DB, version control cho database)

# Phần 7. Thư mục `app/schemas/`  - Nơi chứa Pydantic models

> Dùng cho:
>
> - Validate dữ liệu đầu vào (request)
> - Serialize dữ liệu đầu ra (response)
> - Định nghĩa contract API
>
> Không liên quan trực tiếp đến database

| Loại              | Thuộc tầng nào | Dùng để làm gì       |
| ----------------- | -------------- | -------------------- |
| ORM Model         | db/models      | Mapping bảng DB      |
| Schema (Pydantic) | schemas        | Validate & serialize |
| Domain Model      | service layer  | Business logic       |

|              | db/base.py       | schemas              |
| ------------ | ---------------- | -------------------- |
| Thuộc tầng   | Database         | API                  |
| Kế thừa từ   | declarative_base | BaseModel            |
| Mục đích     | Mapping DB       | Validate/Serialize   |
| Chạy khi nào | Làm việc với DB  | Khi nhận/trả request |

> Tóm lại:
> `schemas/` lưu các file định nghĩa cấu trúc `BaseModel` cho dữ liệu đầu vào, và ra như ở [(Thiết kế chuẩn REST API - Thiết kế lại 3.2)](#33-thiết-kế-chuẩn-rest-api---thiết-kế-lại-32)
>
> Cụ thể:
>
> - Validate request (Xác thực dữ liệu đầu vào, lọc dữ liệu - bộ lọc [chuẩn hóa dữ liệu])
> - Serialize response (Chuẩn hóa dữ liệu đầu ra)
> - Define API contract (Định nghĩa hợp đồng dữ liệu API)
>
> ---
> `base.py` tạo class `Base` duy nhất, và chỉ có như thế này:
>
> ```py
> # db/base.py
> from sqlalchemy.orm import declarative_base
> Base = declarative_base()
> ````
>
> Rồi trong các file của `db/models/` kế thừa class `Base` sau đó định nghĩa cấu trúc cho các bảng

# Phần 8. Thư mục `app/services/` - Xử lí nghiệp vụ chính của ứng dụng

## 8.1. Phân tích

**Không:**

- Không validate cấu trúc request (việc đó do schemas)
- Không truy vấn DB trực tiếp (việc đó do repository)
- Không xử lý HTTP (việc đó do router)

**Service có thể làm gì:**

Ví dụ: tạo task.

- Không chỉ đơn giản là thêm vào DB.
- Nghiệp vụ có thể gồm:
  - Kiểm tra trùng tên

  - Chuẩn hóa dữ liệu

  - Ghi log

  - Gửi event

  - Xử lý transaction

Như vậy `repository/` chỉ lập hàm truy vấn database. Còn `services/` thực hiện nghiệp vụ truy vấn database, chỉ việc gọi lại hàm có trong `repository/` và sử dụng, bổ sung thêm để hoàn chỉnh nghiệp vụ.

## 8.2. Ví dụ

***`repository/` [file cụ thể xử lí] chỉ làm db:***

```py
def create_task(db: Session, name: str):
    task = Task(name=name)
    db.add(task)
    return task
```

***`services/` [file cụ thể xử lí] xử lý nghiệp vụ:***

```py
from db.repositories.task_repository import create_task

def create_task_service(db: Session, name: str):
    if len(name) < 3:
        raise ValueError("Tên quá ngắn")

    return create_task(db, name)
```

***`api/` (nói sau) chỉ có router gọi `services/`***

```py
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db, task.name)
```

# Phần 9. Thư mục `app/middlewares/` - Lớp chạy trước mỗi request

```
Client → Middleware → Router → Middleware → Response
```

Tức là:

- Chạy trước khi vào router
- Chạy sau khi router trả response
- Nó áp dụng toàn bộ ứng dụng, không phải từng endpoint riêng lẻ.

## 9.1 Middleware dùng cho

- CORS

- Logging request/response
- Rate limit
- Xử lý header
- Gắn request_id
- Đo thời gian xử lý
- Global exception handler (ở mức framework)

## 9.2. Mối quan hệ với `core/`

### `core/` là gì?

`core/` chứa:

- Cấu hình hệ thống (settings)
- Cấu hình logging
- Security utilities (hash, JWT)
- Database config
- Các thành phần nền tảng

Nó không xử lý request.

Nó chỉ **định nghĩa và cung cấp công cụ** cho hệ thống.

### `middlewares/` là gì?

Middleware:

- Chạy mỗi request
- Dùng những thứ đã được cấu hình sẵn trong `core`
- Thực hiện logic hệ thống toàn cục

### Ví dụ 1

***`core/logging.py`:***

```py
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("app")
```

Nó chỉ tạo logger.

***`middlewares/logging.py`:***

```py
from app.core.logging import logger

@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"Incoming request: {request.url}")

    response = await call_next(request)

    logger.info(f"Response status: {response.status_code}")
    return response
```

Middleware chỉ dùng logger đã được cấu hình.

# Phần 10. Thư mục `app/api/` - Định nghĩa các route/endpoint (REST API, WebSocket...)

`api/` là interface layer của hệ thống. Nó chịu trách nhiệm:

- Định nghĩa route (GET, POST, PUT, DELETE…)
- Nhận request
- Gắn dependency
- Trả response
- Gắn response_model
- Xử lý HTTP exception
- Nó không chứa nghiệp vụ.

**Cấu trúc cơ bản:**

```
app/
├── api/
│   ├── routers/
│   │   ├── user_router.py
│   │   ├── task_router.py
│   │   └── __init__.py
│   │
│   ├── dependencies/
│   └── api_router.py
```

Thư mục `dependencies/` nói sau.

**Ví dụ, với cấu trúc trên, router chuẩn:**

```py
# api/routers/task_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskResponse
from app.services.task_service import create_task_service
from app.dependencies.db import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db, task.name)
```

# Phần 11. Thư mục `dependencies/`

## 11.1. Chức năng

Chứa các hàm:

- Xác thực (auth)
- Phân quyền (authorization)
- Inject DB session
- Inject current user
- Inject service/repository nếu muốn
- Reusable dependency logic

Nó thuộc API layer, vì nó phục vụ HTTP request.

**Ví dụ, cấu trúc:**

```
app/
├── api/
│   ├── routers/
│   └── dependencies/
│       ├── auth.py
│       ├── permissions.py
│       └── db.py
│
├── services/
├── repositories/
├── models/
└── schemas/
```

hoặc:

```
app/
├── dependencies/
├── api/
```

Tùy theo phong cách tổ chức.

## 11.2. Ví dụ

### 11.2.1. Inject DB

```py
# dependencies/db.py

from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Router dùng:

```py
@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    ...
```

### 11.2.2. Lấy current user (Auth)

```py
# dependencies/auth.py

from fastapi import Depends, HTTPException
from jose import jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=401)

    return user_id
```

### 11.2.3. Phân quyền

```py
# dependencies/auth.py

from fastapi import Depends, HTTPException
from jose import jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=401)

    return user_id
```

Router:

```py
@router.post("/", dependencies=[Depends(require_admin)])
```

## Lưu ý

- dependencies/ Không phải là business layer.

- Không chứa nghiệp vụ chính
- Không xử lý logic phức tạp hệ thống
- Không gọi DB trực tiếp (trừ auth lookup user)

## 11.3. Mối quan hệ với `core/`

***`core/logging.py`:***

```py
def create_access_token(data: dict):
    ...
```

***`dependencies/auth.py`:***

```py
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)  # gọi từ core.security
```

core  → cung cấp cấu hình / utility
middlewares → dùng cấu hình để xử lý request toàn cục
dependencies → dùng cấu hình để xử lý logic HTTP
services → dùng utility để xử lý nghiệp vụ

# Phần 12. Kết nối database MySQL - Test

> Thư mục `test/` có thể được coi như thư mục `e-commerce-app-api/`

```
app/
test/
```

## 12.1. Triển khai code test

***`test.py`: - file nằm ngoài thư mục test (test xong file này -> triển khai cấu trúc mẫu vào thư mục test)***

```py
from sqlalchemy import create_engine

settings = [
    {"DATABASE_URL" : "mysql+pymysql://root:password@localhost:3306/shop_db"},
    {"DEBUG": True},
    {"pool_size": 10},
    {"max_overflow": 20},
    {"pool_pre_ping": True}
]

engine = create_engine(
    settings[0]['DATABASE_URL'],               # link kết nối database
    echo=settings[1]['DEBUG'],                 # log SQL ra terminal khi debug
    pool_size=settings[2]["pool_size"],        # số kết nối tối đa trong pool
    max_overflow=settings[3]["max_overflow"],  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings[4]["pool_pre_ping"] # kiểm tra kết nối trước mỗi lần dùng
)

# SessionLocal: factory tạo ra mỗi session làm việc với database
# autocommit=False -> ta tự commit -> an toàn hơn
# autoflush=False -> không tự flush trước query
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: tất cả models phải kế thừa class này
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

##############################################################################
# Test chức năng xem kết nối được chưa
##############################################################################

# models.py (tạo bảng mẫu)
# from database import Base
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = "users_test"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email =  Column(String(100), unique=True, index=True)

# create_table.py (tạo bảng trong db)
# from database import engine, Base
# import models # file models.py
Base.metadata.create_all(bind=engine)
print('Tạo bảng thành công') # Viết đến đây, chạy -> kiểm tra database

# test_insert.py (test kết nối + thêm dữ liệu)
# from database import SessionLocal
# from models import User
db = SessionLocal()

try: 
    new_user = User(name="Son", email="son@example.com")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print("Thêm user thành công:", new_user.id)
except Exception as e:
    db.rollback()
    print("Lỗi:", e)
finally:
    db.close()

# Viết đến đây, chạy -> kiểm tra database
```

## 12.2. Triển khai code vào thư mục test

> Triển khai cấu trúc `test/` tương tự như `e-ecommerce-app-api/`

### 12.2.1. Khởi tạo file cấu hình trung tâm `settings.py`

**Giải thích:**

[Phần 5](#phần-5-thư-mục-appcore---lưu-cấu-hình-trung-tâm) nêu rõ:
> file `core/settings.py` là file cấu hình hệ thống. Nó phụ trách quản lí:
>
> - Biến môi trường, Database URL, Secret Key, CORS, Debug mode

Mà trong file `test.py` ta có cấu hình kết nối MySQL bằng `DATABASE_URL` thế nên ta cần đưa nó vào trong file `core/settings.py`

**form của file `settings.py` thông thường:**

```py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    
    # import cấu hình ở đây

    class Config:
        env_file = '.env'              # load cấu hình từ file .env
        env_file_encoding = 'utf-8'    # hỗ trợ emoji
        case_sensitive = True          # phân biệt hoa thường
    
# lru_cache: chỉ tạo Settings 1 lần, dùng lại cho toàn app
@lru_cache()
def get_setting() -> Settings:
    return Settings()

# Instance dùng trực tiếp: app.core import settings
settings = Settings()

```

**Bây giờ thực hiện đưa cấu hình của `engine` vào file `settings.py`:**

Cấu hình của engine khi ở trong file `test.py`:

```py
settings = [
    {"DATABASE_URL" : "mysql+pymysql://root:password@localhost:3306/shop_db"},
    {"DEBUG": True},
    {"pool_size": 10},
    {"max_overflow": 20},
    {"pool_pre_ping": True}
]

engine = create_engine(
    settings[0]['DATABASE_URL'],               # link kết nối database
    echo=settings[1]['DEBUG'],                 # log SQL ra terminal khi debug
    pool_size=settings[2]["pool_size"],        # số kết nối tối đa trong pool
    max_overflow=settings[3]["max_overflow"],  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings[4]["pool_pre_ping"] # kiểm tra kết nối trước mỗi lần dùng
)
```

Ta sẽ thực hiện import từng phần trong danh sách `settings` vào `settings.py`, như sau:

```py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database - cấu hình của engine
    DATABASE_URL: str= "mysql+pymysql://root:password@localhost:3306/shop_db"
    DEBUG: bool= True
    POOL_SIZE: int= 10
    MAX_OVERFLOW: int= 20
    POOL_PRE_PING: bool= True

    class Config:
        # đường dẫn tới '.env'
        env_file = '.env'              # load cấu hình từ file .env
        env_file_encoding = 'utf-8'    # hỗ trợ emoji
        case_sensitive = True          # phân biệt hoa thường
    
# lru_cache: chỉ tạo Settings 1 lần, dùng lại cho toàn app
@lru_cache()
def get_setting() -> Settings:
    return Settings()

# Instance dùng trực tiếp: app.core import settings
settings = Settings()
```

> Cấu hình trung tâm đã khởi tạo xong, tuy nhiên vẫn còn nhiều rủi ro. Ta đã để lộ thông tin database, lẫn mật khẩu của nó. Để an toàn, ta sẽ chuyển thông tin nhạy cảm sang một file `.env` và load nó vào trong file `settings.py`

### 12.2.2. Khởi tạo file `.env` - lưu thông tin nhạy cảm

Ta chuyển các thông tin nhạy cảm từ file `settings.py` sang `.env`

***`.env`:***

```env
# DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/shop_db"
DB_HOST = localhost
DB_PORT = 3306
DB_NAME = shop_db
DB_USER = root
DB_PASSWORD = password
```

Ở file `settings.py`, ta cần chỉnh sửa lại cho phù hợp.

`settings.py`:

```py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    '''Cấu hình trung tâm'''
    # Database - cấu hình của engine
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DEBUG: bool = True
    POOL_SIZE: int= 10
    MAX_OVERFLOW: int= 20
    POOL_PRE_PING: bool= True

    @property # khi call fun không cần () , settings.DATABASE_URL thay vì có thêm ()
    def DATABASE_URL(self) -> str:
        return(
            # DB_USER, ... được load từ test/.env
            f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
            f'?charset=utf8mb4' # Hỗ trợ emoji và ký tự đặc biệt
        )


    class Config:
        # đường dẫn tới '.env'
        env_file = 'test/.env'        # load cấu hình từ file .env
        env_file_encoding = 'utf-8'    # hỗ trợ emoji
        case_sensitive = True          # phân biệt hoa thường
    
# lru_cache: chỉ tạo Settings 1 lần, dùng lại cho toàn app
@lru_cache()
def get_setting() -> Settings:
    return Settings()

# Instance dùng trực tiếp: app.core import settings
settings = Settings()
```

**Bây giờ để chắc chắn mã hoạt động, ta thực hiện test với file `test.py`, bằng cách import file `settings.py` và thay thế một số chỗ liên quan đến database trong file `test.py`.**

Tuy nhiên, trước hết ta phải tạo file `__init__.py` để được coi là một package mới import được vào file `test.py`. Cấu trúc folder `test/` sẽ có thêm các file `__init__.py`:

```
test/__init__.py
test/app/__init__.py
test/app/core/__init__.py
```

Cấu trúc hiện tại `test/` tương tự như trong ảnh:

![test folder](/assets/testpyfolder.png)

***`test.py`:***

Ta thay đoạn:

```py
settings = [
    {"DATABASE_URL" : "mysql+pymysql://root:password@localhost:3306/shop_db"},
    {"DEBUG": True},
    {"pool_size": 10},
    {"max_overflow": 20},
    {"pool_pre_ping": True}
]

engine = create_engine(
    settings[0]['DATABASE_URL'],               # link kết nối database
    echo=settings[1]['DEBUG'],                 # log SQL ra terminal khi debug
    pool_size=settings[2]["pool_size"],        # số kết nối tối đa trong pool
    max_overflow=settings[3]["max_overflow"],  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings[4]["pool_pre_ping"] # kiểm tra kết nối trước mỗi lần dùng
)
```

Thành:

```py
from test.app.core.settings import settings

engine = create_engine(
    settings.DATABASE_URL,               # link kết nối database
    echo=settings.DEBUG,                 # log SQL ra terminal khi debug
    pool_size=settings.POOL_SIZE,        # số kết nối tối đa trong pool
    max_overflow=settings.MAX_OVERFLOW,  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings.POOL_PRE_PING # kiểm tra kết nối trước mỗi lần dùng
)
```

Thực hiện chạy lại file `test.py`, với tham số test mới để không bị lỗi db, nếu file không báo lỗi (code) -> hoàn tất.

Ví dụ, trong file `test.py`, ta có:

- Cũ: `new_user = User(name="Son", email="son@example.com")`
- Thay mới thành: `new_user = User(name="Hieu", email="Hieu@example.com")`

Thực hiện chạy nếu không có lỗi -> hoàn tất.

### 12.2.3. Chuyển mã từ `test.py` vào thư mục /test/app/database

#### 12.2.3.1. Khởi tạo file `database.db` - Tạo Engine (kết nối database, cấu hình engine)

Ta sẽ chuyển phần `engine` trong file `test.py` vào file `database.py`

***`database.py`:***

```py
from sqlalchemy import create_engine
from test.app.core.settings import settings

engine = create_engine(
    settings.DATABASE_URL,               # link kết nối database
    echo=settings.DEBUG,                 # log SQL ra terminal khi debug
    pool_size=settings.POOL_SIZE,        # số kết nối tối đa trong pool
    max_overflow=settings.MAX_OVERFLOW,  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings.POOL_PRE_PING # kiểm tra kết nối trước mỗi lần dùng
)

# SessionLocal: factory tạo ra mỗi session làm việc với database
# autocommit=False -> ta tự commit -> an toàn hơn
# autoflush=False -> không tự flush trước query
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

#### 12.2.3.2. Khởi tạo file `base.py` - Base ORM (Tạo class Base để các model kế thừa)

***`base.py`:***

```py
# Base: tất cả models phải kế thừa class này
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```

#### 12.2.3.3. Khởi tạo thư mục `models/` - khởi tạo, lưu trữ các bảng database

##### 12.2.3.3.1. Khởi tạo `models/models.py`

**Trong `models/`, tạo `models.py` (file `models.py`) đề cập ở `test.py`**

***`models.py`:***

```py
# Tạo bảng
from sqlalchemy import Column, Integer, String
from test.app.database.base import Base

class User(Base):
    __tablename__ = "users_test"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
```

##### 12.2.3.3.2. Khởi tạo `models/create_table.py` dùng để tạo bảng db trong MySQL - Mục tiêu của file này là import các file cấu trúc bảng như `models.py` (các file tương tự này mới chỉ viết cấu trúc bảng, chứ chưa tạo bảng trong MySQL)vào và sẽ thực hiện tạo bảng trong file này (điều này giúp các file lập bảng trông gọn, sạch)

***`create_table.py`***

```py
from test.app.database.database import engine
from test.app.database.base import Base

# Tạo tất cả các bảng (được import từ models/ vào create_table.py) trong MySQL
Base.metadata.create_all(bind=engine)
```

### 12.2.4. Test thành quả đến hết [12.2.3](#1223-chuyển-mã-từ-testpy-vào-thư-mục-testappdatabase)

**Sửa đổi file `test.py`, thành cấu trúc mới**

***`test.py`:***

```py
from sqlalchemy import create_engine
from test.app.core.settings import settings

engine = create_engine(
    settings.DATABASE_URL,               # link kết nối database
    echo=settings.DEBUG,                 # log SQL ra terminal khi debug
    pool_size=settings.POOL_SIZE,        # số kết nối tối đa trong pool
    max_overflow=settings.MAX_OVERFLOW,  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings.POOL_PRE_PING # kiểm tra kết nối trước mỗi lần dùng
)

# SessionLocal: factory tạo ra mỗi session làm việc với database
from test.app.database.database import SessionLocal

# Base: tất cả models phải kế thừa class này
from test.app.database.base import Base

##############################################################################
# Test chức năng xem kết nối được chưa
##############################################################################

# models.py (tạo bảng mẫu)
from test.app.database.models.models import User

# create_table.py (tạo bảng trong db)
from test.app.database.models import create_table # import cả file create_table
create_table # Gọi cả file create_table

# test_insert.py (test kết nối + thêm dữ liệu)
# from database import SessionLocal
# from models import User
db = SessionLocal()

try: 
    new_user = User(name="Hieu", email="Hieu@example.com")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print("Thêm user thành công:", new_user.id)
except Exception as e:
    db.rollback()
    print("Lỗi:", e)
finally:
    db.close()

# Viết đến đây, chạy -> kiểm tra database 
```

Nếu thực hiện đến đây, và không có lỗi xảy ra -> thành công.

**Cấu trúc thư mục `test/` đến thời điểm hiện tại như sau:**

![alt text](/assets/image.png)

Trong `test/` có một số thư mục `__pycache__` là thư mục khi chạy module `__init__` tạo ra, không quan trọng. Ta muốn loại bỏ chúng khi push lên github thì thêm `__pycache__` vào file `.gitignore`

# Phần 13. Viết API, Thực hiện truy vấn - Test

## 13.1. Triển khai code test

Điều chỉnh lại trước khi bổ sung, ở file `test.py`, ta sẽ bỏ đoạn và sẽ chỉnh sửa phần này ở phía dưới:

```py
# test_insert.py (test kết nối + thêm dữ liệu)
# from database import SessionLocal
# from models import User
db = SessionLocal()

try: 
    new_user = User(name="Hieu", email="Hieu@example.com")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print("Thêm user thành công:", new_user.id)
except Exception as e:
    db.rollback()
    print("Lỗi:", e)
finally:
    db.close()
```

***`test.py` - Tiếp tục triển khai vào cuối file:***

```py
from sqlalchemy import create_engine
from test.app.core.settings import settings

engine = create_engine(
    settings.DATABASE_URL,               # link kết nối database
    echo=settings.DEBUG,                 # log SQL ra terminal khi debug
    pool_size=settings.POOL_SIZE,        # số kết nối tối đa trong pool
    max_overflow=settings.MAX_OVERFLOW,  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings.POOL_PRE_PING # kiểm tra kết nối trước mỗi lần dùng
)

# SessionLocal: factory tạo ra mỗi session làm việc với database
from test.app.database.database import SessionLocal

# Base: tất cả models phải kế thừa class này
from test.app.database.base import Base

##############################################################################
# Test chức năng xem kết nối được chưa
##############################################################################

# models.py (tạo bảng mẫu)
from test.app.database.models.models import User

# create_table.py (tạo bảng trong db)
from test.app.database.models import create_table # import cả file create_table
create_table # Gọi cả file create_table


# Viết đến đây, chạy -> kiểm tra database

##############################################################################
# Phần 13. Viết API, Thực hiện truy vấn - Test
##############################################################################
# test_insert.py (test kết nối + thêm dữ liệu)
# from database import SessionLocal
# from models import User
def get_db():
    '''
    Sử dụng trọng FastAPI với Depend
    @app.get('/users')
    def get_users(db: Session = Depends(get_db)):
        ....
    '''
    db = SessionLocal()
    try:
        yield db    # trả session cho api (endpoint) sử dụng
        # db.commit() # tự động commit -> lưu vào MySQL
    except Exception as e:
        db.rollback()    # Rollback nếu có lỗi
        raise e  # ném lỗi
    finally:
        db.close() # luôn đóng session để trả kết quả kết nối

# schemas/ -> bộ lọc định nghĩa dữ liệu đầu vào, ra 
# các class trong schemas kế thừa từ BaseModel 
from pydantic import BaseModel
class UserCreate(BaseModel): # Dùng để xem user
    name: str
    email: str

# Dữ liệu trả về sau khi tạo thành công
class UserResponse(BaseModel):       # Dùng để import user
    id: int
    name: str
    email: str


# services/ -> thực hiện nghiệp vụ truy vấn user
# import sechmas/
# from test.app.database.models.models import User
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
def get_user_services(id: int, db: Session):
    # Xem lại phần code bị lược bỏ phần trước và so sánh thấy rõ hơn 
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def create_user_services(db: Session, user_in: UserCreate):
    '''Tạo mới user và lưu vào database'''
    db_user = User(name=user_in.name, email=user_in.email) # tạo đối tượng User từ dữ liệu đầu vào
    db.add(db_user) # thêm vào session
    db.commit()
    db.refresh(db_user) # cập nhật đối tượng với id tự tăng từ database
    return db_user



# api/ -> chỉ gọi services/ đã xử lí nghiệp vụ
# from test_insert import get_db
# from services import ...
from fastapi import FastAPI, APIRouter #, Depends
from sqlalchemy.orm import Session
app = FastAPI()
router = APIRouter()

@router.get('/users/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    '''
    1. FastAPI gọi get_db()
    2. Tạo session
    3. yield db -> truyền db vào endpoint
    4. endpoint chạy xong
    5. Quay lại get_db()
    6. commit() hoặc rollback
    7. close session

    Ví dụ:
        @app.post("/users")
        def create_user(db: Session = Depends(get_db)):
            user = User(name="A")
            db.add(user)
    Luồng:
        get_db()
          └─ tạo session
          └─ yield db → truyền vào create_user
              └─ db.add(user)
          └─ quay lại get_db()
          └─ db.commit()
          └─ db.close()
    Nếu lỗi:
        db.add(user)
        → lỗi
        → except
        → rollback
        → close
    '''
    return get_user_services(id, db)

# Viết đến đây rồi chạy -> không lỗi -> ok

@router.post('/users', response_model=UserResponse, status_code=201)
def create_user(user_in: UserCreate, db: Session=Depends(get_db)):
    """
    Tạo user mới
    
    Luồng thực thi:
    1. FastAPI validate request body → UserCreate
    2. Gọi get_db() → yield session
    3. Gọi create_user_service() → add + commit + refresh
    4. Trả về UserResponse với id mới sinh
    """
    return create_user_services(db, user_in)

# Viết đến đây rồi chạy -> không lỗi -> ok

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

Khi chạy trên terminal, không có thông báo lỗi -> ta đã hoàn thiện được toàn bộ logic của một backend cơ bản.

**Liên hệ với phần [3.3. Thiết kế chuẩn REST API - Thiết kế lại 3.2](#33-thiết-kế-chuẩn-rest-api---thiết-kế-lại-32):**

```py
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
router = APIRouter()

task_list = []

# schemas/                   <- schemas định nghĩa cấu trúc dữ liệu
# Định nghĩa model
class TaskCreate(BaseModel): # Dùng để xem task
    name: str

class Task(BaseModel):       # Dùng để import task
    id: int
    name: str

# api/                       <- router
@router.post('/', response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    # toàn bộ phần dưới là nghiệp vụ serviecs/ trừ dòng return
    new_task = {
        "id": len(task_list),
        "name": task.name
    }

    task_list.append(new_task)
    return new_task

# api/                       <- router
@router.get('/{id}')
def get_task(id: int):
    # toàn bộ phần dưới là nghiệp vụ serviecs/ trừ dòng return
    res = next((task for task in task_list if task["id"] == id), None)

    if res is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy nhiệm vụ")

    return res

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

## 13.2. Triển khai code từ `test.py` vào thư mục `test/`

### 13.2.1. Cấu trúc folder

```
test/
   app/
     api/
     schemas/
     services/
```

**Thứ tự triển khai:**

- Dữ liệu đầu vào phải được định dạng, chuẩn hóa thông qua bộ lọc -> `schemas/`
- Thực hiện nghiệp vụ (lấy dữ liệu -> thao tác trên dữ liệu) -> `services/`
- Gọi các hàm nghiệp vụ sử dụng trong router -> `api/`

Ngoài ra, các hàm truy vấn dữ liệu sẽ được đặt trong folder `repository/`. Ta có cấu trúc thư mục chuẩn là:

![img](/assets/image%20copy%202.png)

Và thứ tự triển khai chuẩn là:

- Dữ liệu đầu vào phải được định dạng, chuẩn hóa thông qua bộ lọc -> `schemas/`
- Các hàm truy vấn được viết trong `repository/`
- Thực hiện nghiệp vụ (lấy dữ liệu -> dùng các hàm truy vấn trong `repository/` thao tác trên dữ liệu) -> `services/`
- Gọi các hàm nghiệp vụ sử dụng trong router -> `api/`

Do đó ta sẽ điều chỉnh lại trong code cũ như sau:

```py
from sqlalchemy import create_engine
from test.app.core.settings import settings

engine = create_engine(
    settings.DATABASE_URL,               # link kết nối database
    echo=settings.DEBUG,                 # log SQL ra terminal khi debug
    pool_size=settings.POOL_SIZE,        # số kết nối tối đa trong pool
    max_overflow=settings.MAX_OVERFLOW,  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings.POOL_PRE_PING # kiểm tra kết nối trước mỗi lần dùng
)

# SessionLocal: factory tạo ra mỗi session làm việc với database
from test.app.database.database import SessionLocal

# Base: tất cả models phải kế thừa class này
from test.app.database.base import Base

##############################################################################
# Test chức năng xem kết nối được chưa
##############################################################################

# models.py (tạo bảng mẫu)
from test.app.database.models.models import User

# create_table.py (tạo bảng trong db)
from test.app.database.models import create_table # import cả file create_table
create_table # Gọi cả file create_table


# Viết đến đây, chạy -> kiểm tra database

##############################################################################
# Phần 13. Viết API, Thực hiện truy vấn - Test
##############################################################################
# test_insert.py (test kết nối + thêm dữ liệu)
# from database import SessionLocal
# from models import User
def get_db():
    '''
    Sử dụng trọng FastAPI với Depend
    @app.get('/users')
    def get_users(db: Session = Depends(get_db)):
        ....
    '''
    db = SessionLocal()
    try:
        yield db    # trả session cho api (endpoint) sử dụng
        # db.commit() # tự động commit -> lưu vào MySQL
        # nếu dùng db.commit ở đây -> một số hàm repository/ như create_user sẽ phải thay db.commit()  thành db.flush()
    except Exception as e:
        db.rollback()    # Rollback nếu có lỗi
        raise e  # ném lỗi
    finally:
        db.close() # luôn đóng session để trả kết quả kết nối

# schemas/ -> bộ lọc định nghĩa dữ liệu đầu vào, ra 
# các class trong schemas kế thừa từ BaseModel 
from pydantic import BaseModel
class UserCreate(BaseModel): # Dùng để xem user
    name: str
    email: str

# Dữ liệu trả về sau khi tạo thành công
class UserResponse(BaseModel):       # Dùng để import user
    id: int
    name: str
    email: str


# repository/ -> viết các hàm truy vấn
# from test.app.database.models.models import User
# from test.app.schemas.schemas import UserCreate
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
def get_user_respository(id: int, db:Session):
    return db.query(User).filter(User.id == id).first()

def create_user_respository(db: Session, user_in: UserCreate):
    '''Tạo mới user và lưu vào database'''
    db_user = User(name=user_in.name, email=user_in.email) # tạo đối tượng User từ dữ liệu đầu vào
    db.add(db_user) # thêm vào session
    db.commit() # thay thành db.flush() nếu get_db() để db.commit()
    db.refresh(db_user) # cập nhật đối tượng với id tự tăng từ database
    return db_user

# services/ -> thực hiện nghiệp vụ truy vấn user
# import sechmas/
# import respository/
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
def get_user_services(id: int, db: Session):
    # Xem lại phần code bị lược bỏ phần trước và so sánh thấy rõ hơn 
    user = get_user_respository(id, db)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def create_user_services(db: Session, user_in: UserCreate):
    return create_user_respository(db, user_in)



# api/ -> chỉ gọi services/ đã xử lí nghiệp vụ
# from test_insert import get_db
# from models.user import User
# from services import ...
from fastapi import FastAPI, APIRouter #, Depends
from sqlalchemy.orm import Session
app = FastAPI()
router = APIRouter()

@router.get('/users/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_services(id, db)

# Viết đến đây rồi chạy -> không lỗi -> ok

@router.post('/users', response_model=UserResponse, status_code=201)
def create_user(user_in: UserCreate, db: Session=Depends(get_db)):
    return create_user_services(db, user_in)

# Viết đến đây rồi chạy -> không lỗi -> ok

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

### 13.2.1. Khởi tạo file `database/session.py` lưu hàm `get_db()`, sau đó import vào `database.py`

**Giải thích: Liên hệ [Phần 6.Thư mục app/database - Kết nối database](#phần-6-thư-mục-appdatabase---kết-nối-database)**

File `session.py` Quản lý session (mỗi request có 1 session riêng, tránh rò rỉ khi kết nối)

Trong file `database.py` đang có đoạn mã sau:

```py
# SessionLocal: factory tạo ra mỗi session làm việc với database
# autocommit=False -> ta tự commit -> an toàn hơn
# autoflush=False -> không tự flush trước query
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

Nó thuộc `session` do đó ta sẽ chuyển nó sang file `session.py` cùng với `get_db()`.

***`session.py`:***

```py
# SessionLocal: factory tạo ra mỗi session làm việc với database
# autocommit=False -> ta tự commit -> an toàn hơn
# autoflush=False -> không tự flush trước query
from sqlalchemy.orm import sessionmaker

from test.app.database.database import engine # import  hàm engine trong database.py

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
```

***`database.py`:***

```py
from sqlalchemy import create_engine
from test.app.core.settings import settings

engine = create_engine(
    settings.DATABASE_URL,               # link kết nối database
    echo=settings.DEBUG,                 # log SQL ra terminal khi debug
    pool_size=settings.POOL_SIZE,        # số kết nối tối đa trong pool
    max_overflow=settings.MAX_OVERFLOW,  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings.POOL_PRE_PING # kiểm tra kết nối trước mỗi lần dùng
)
```

### 13.2.2. Khởi tạo file `schemas/schemas.py`

***`schemas.py`:***

```py
from pydantic import BaseModel

class UserCreate(BaseModel): # Dùng để xem user
    name: str
    email: str

# Dữ liệu trả về sau khi tạo thành công
class UserResponse(BaseModel):       # Dùng để import user
    id: int
    name: str
    email: str
```

### 12.2.3. Khởi tạo file `repository/repository.py`

***`repository.py`:***

```py
from test.app.database.models.models import User
from sqlalchemy.orm import Session
from test.app.schemas.schemas import UserCreate

def get_user_respository(id: int, db:Session):
    return db.query(User).filter(User.id == id).first()

def create_user_respository(db: Session, user_in: UserCreate):
    '''Tạo mới user và lưu vào database'''
    db_user = User(name=user_in.name, email=user_in.email) # tạo đối tượng User từ dữ liệu đầu vào
    db.add(db_user) # thêm vào session
    db.commit()
    db.refresh(db_user) # cập nhật đối tượng với id tự tăng từ database
    return db_user
```

### Phần 13.2.3. Khởi tạo file `services/services.py`

***`services.py`:***

```py
from test.app.repository.repository import (
    get_user_respository,
    create_user_respository
)
from test.app.schemas.schemas import UserCreate

from fastapi import HTTPException
from sqlalchemy.orm import Session
def get_user_services(id: int, db: Session):
    # Xem lại phần code bị lược bỏ phần trước và so sánh thấy rõ hơn 
    user = get_user_respository(id, db)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def create_user_services(db: Session, user_in: UserCreate):
    return create_user_respository(db, user_in)
```

### Phần 13.2.4. Khởi tạo file `api/api.py`

***`api.py`:***

```py
from sqlalchemy.orm import Session
from test.app.schemas.schemas import UserCreate, UserResponse
from fastapi import Depends
from test.app.database.session import get_db
from test.app.services.services import(
    create_user_services,
    get_user_services
)

from fastapi import APIRouter #, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/users/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_services(id, db)

@router.post('/users', response_model=UserResponse, status_code=201)
def create_user(user_in: UserCreate, db: Session=Depends(get_db)):
    return create_user_services(db, user_in)
```

## 13.3. Test thành quả đến hết [13.2](#132-triển-khai-code-từ-testpy-vào-thư-mục-test)

Xóa hết toàn bộ đi vì đã import vào các file, sau đó import vào `api.py` rồi import vào `test.py`.

***`test.py`:***

```py
from fastapi import FastAPI, APIRouter #, Depends
from test.app.api.api import router
app = FastAPI()

app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

Thực hiện chạy file `test.py` không có lỗi -> ok.

> Hoàn thiện logic backend cơ bản


# Phần 14. [Dự án chính thức] - Kết Nối Database
## 14.1. MySQL - Tạo cơ sở dữ liệu liệu và cấp quyền cho user

> **Lưu ý:** Nếu đã có cơ sở dữ liệu và đã cấp quyền cho user thì không phải làm phần này.

**Phần này thao tác trên MySQL:**

Giả sử, ta có tài khoản `root`, bây giờ ta sẽ tạo một database: `e_commerce` và tạo một `user` sau đó cấp quyền cho nó.

***`query`:***

```sql
CREATE DATABASE e_commerce;

CREATE USER 'your_name'@'localhost' IDENTIFIED BY 'your_password';

GRANT ALL ON e_commerce.* TO 'your_name'@'localhost'
```

Kết nối với user vừa được tạo:

![Pasted image 20260302145026.png](/assets/connect.png)

## 14.2. Cấu hình kết nối database
### 14.2.1. Thiết lập file cấu hình nhạy cảm `.env`

> Trong file này, ta sẽ lưu tài khoản, mật khẩu, ... (những thông tin không để bị lộ để tránh mất dữ liệu, database, ...)

***`.env` - file `env` nằm ngoài thư mục `test/`:***

![Pasted image 20260302150332.png](/assets/Pasted%20image%2020260302150332.png)

```env
# DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/shop_db"
DB_HOST=localhost
DB_PORT=3306
DB_NAME=e_commerce
DB_USER=your_name
DB_PASSWORD=your_password
```

### 14.2.2. Thiết lập file `app/core/settings.py` - Cấu hình trung tâm

> Import thông tin, dữ liệu nhạy cảm từ file `.env` vào file `settings.py`

#### Cấu hình chung của các file `settings.py` khi khởi tạo
***`settings.py`:***

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):

    # import cấu hình ở đây

    class Config:
        env_file = '.env'           # path đến file .env
        env_file_encoding = 'utf-8' # hỗ trợ emoji
        case_sensitive = True       # phân biệt hoa/thường

# Cho phép tái sử dụng
@lru_cache
def get_setting() -> Settings:
    return Settings()

# Instance dùng trực tiếp: from app.core import settings
settings = Settings()
```

#### Import cấu hình kết nối database từ `.env` vào `settings.py`

***`settings.py`:***

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database - Import cấu hình từ .env
    DB_USER: str=''
    DB_PASSWORD: str=''
    DB_HOST: str=''
    DB_PORT: str=''
    DB_NAME: str=''
    POOL_SIZE: int=10          # số kết nối tối thiểu
    MAX_OVERFLOW: int=20       # số kết nối mở thêm khi quá tải -> max 30 kết nối
    POOL_PRE_PING: bool=True   # kiểm tra Ping trước khi bắt đầu
    DEBUG: bool=True

    @property
    def DATABASE_URL(self) -> str:
        return(
            f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
            f'?charset=utf8mb4' # hỗ trợ emoji và kí tự đặc biệt
        )

    class Config:
        env_file = '.env'           # path đến file .env
        env_file_encoding = 'utf-8' # hỗ trợ emoji
        case_sensitive = True       # phân biệt hoa/thường

# Cho phép tái sử dụng
@lru_cache
def get_setting() -> Settings:
    return Settings()

# Instance dùng trực tiếp: from app.core import settings
settings = Settings()
```

### 14.2.3. Thực hiện quá trình test có lỗi không

Trong file `test.py`, ta sẽ thiết lập cấu hình `engine` để kết nối với database.

***`test.py`:***

```python
from app.core.settings import settings

# test kết nối database
from sqlalchemy import create_engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=settings.POOL_SIZE,
    max_overflow=settings.MAX_OVERFLOW,
    pool_pre_ping=settings.POOL_PRE_PING
)


# Test
from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column
Base = declarative_base()

class User(Base):
    __tablename__ = 'users_test'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(100), nullable=True)
    email=Column(String(100), unique=True, index=True)

Base.metadata.create_all(bind=engine)
print("Tạo bảng thành công")
```

> Build: Không có lỗi xảy ra -> OK.

### 14.2.4. Chuyển phần [14.2.3](#1423-thực-hiện-quá-trình-test-có-lỗi-không) vào các file trong `database/`
***`database/database.py`:***

```python
from app.core.settings import settings

# test kết nối database
from sqlalchemy import create_engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=settings.POOL_SIZE,
    max_overflow=settings.MAX_OVERFLOW,
    pool_pre_ping=settings.POOL_PRE_PING
)
```

***`database/session.py`:***
```python
from app.database.database import engine
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
```

***`database/base.py`:***

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

### 14.2.3. Thực hiện quá trình test lỗi

***`test.py`:***

```python
from app.database.database import engine
from app.database.base import Base

from sqlalchemy import String, Integer, Column

class User(Base):
    __tablename__ = 'users_test'

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(100), nullable=True)
    email=Column(String(100), unique=True, index=True)

Base.metadata.create_all(bind=engine)
print("Tạo bảng thành công")
```

> Build: Không có lỗi xảy ra -> OK.

# Phần 15. Thứ tự thiết kế:

```
1. models      (ORM mapping bảng DB)
2. schemas     (Pydantic validate request/response)
3. repository  (tầng thao tác DB)
4. service     (business logic)
5. api/router  (endpoint)
6. test
```

# Phần 16. SQL [Phần này không có trong dự án chính thức]

## 16.1. Tổng quan
### 16.1.1. Database (Cơ sở dữ liệu)
Database là một tập hợp có tổ chức của dữ liệu được lưu trữ điện tử. Trong MySQL Database đóng vai trò là container chứa các Table, View, Stored Procedure, và các đối tượng khác

+ **Chức năng:** Quản lý quyền truy cập, mã hóa ký tự (charset), và collation (quy tắc so sánh)
+ **Lưu ý:** Một server MySQL có thể chứa nhiều Database độc lập

### 16.1.2. Table (Bảng)
Table là cấu trúc lưu trữ dữ liệu thực tế dưới dạng hàng (rows), và cột (columns)

+ **Row (Record):** Đại diện cho một cấu trúc thực thể duy nhất (ví dụ: một người dùng)
+ **Column (Field):** Đại diện cho một thuộc tính của thực thể (ví dụ: tên, tuổi, email)
+ **Schema:** Định nghĩa cấu trúc của Table (tên cột, kiểu dữ liệu, ràng buộc)

### 16.1.3. Kiểu dữ liệu 
#### INT (Số nguyên)
+ `TINYINT`
+ `SMALLINT`
+ `MEDIUMINT`
+ `BIGINT`

#### VARCHAR
+ `VARCHAR(n)`: Chuỗi ký tự tối đa `n` ký tự

#### DATE (Ngày tháng)
+ `DATE`: `YYYY-MM-DD`
+ `DATETIME`: `YYYY-MM-DD HH:MM:SS` 
+ `TIMESTAMP`: Lưu số giây từ Epoch. Tự động chuyển đổi theo múi giờ kết nối client

#### TEXT (Văn bản lớn)
Dùng để lưu trữ lượng lớn dữ liệu chuỗi vượt quá giới hạn `VARCHAR`
+ `TINYTEXT`
+ `TEXT`
+ `MEDIUMTEXT`
+ `LONGTEXT`

#### JSON (Dữ liệu cấu trúc)
Lưu trữ dữ liệu định dạng JSON dưới dạng nhị phân tối ưu

**Hàm hỗ trợ:**
+ `JSON_EXTRACT`, `JSON_SET`, `JSON_CONTAINS`, `->` (toán tử trích xuất)

## 16.2. Thao tác trên MySQL & `sqlalchemy` trong Python

### Tạo bảng cơ bản 
#### Bảng Users
***`query_test.sql`:***

```sql
CREATE TABLE USERS_MYSQL (
    -- id: INT, PRIMARY KEY: Khóa chính, AUTO_INCREMENT: Tự động tăng
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    
    -- username: VARCHAR(100): Chuỗi max 100 ký tự, NOT NULL: Không bỏ trống, UNIQUE: Duy nhất
    `username` VARCHAR(100) NOT NULL UNIQUE,
    
    -- email: VARCHAR(200): Chuỗi max 200 ký tự, NOT NULL: Không bỏ trống, UNIQUE: Duy nhất
    `email` VARCHAR(200) NOT NULL UNIQUE,
    
    -- is_active: TINYINT, DEFAULT 1: Giá trị mặc định là 1 -> Kích hoạt tài khoản
    `is_active` TINYINT DEFAULT 1, -- 0/1: 0 - bị ban, 1 - đang kích hoạt
    
    -- birth_date: DATE: Chỉ cần YYYY-MM-DD, NULL: Có thể bỏ trống
    `birth_date` DATE NULL,
    
    -- create_at: TIMESTAMP: Ghi thời gian tạo, DEFAULT CURRENT_TIMESTAMP: Mặc định thời gian tạo
    `create_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB;
```

**Để sử dụng SQLALCHEMY trong Python, trước hết ta cần kết nối database MySQL, ở các phần sau, tự hiểu là có phần này ở trên đầu file `test.py`**

***`test.py`:***
```python
from sqlalchemy import create_engine

settings = [
    {"DATABASE_URL" : "mysql+pymysql://your_user:your_password@localhost:3306/your_database"},
    {"DEBUG": True},
    {"pool_size": 10},
    {"max_overflow": 20},
    {"pool_pre_ping": True}
]

engine = create_engine(
    settings[0]['DATABASE_URL'],               # link kết nối database
    echo=settings[1]['DEBUG'],                 # log SQL ra terminal khi debug
    pool_size=settings[2]["pool_size"],        # số kết nối tối đa trong pool
    max_overflow=settings[3]["max_overflow"],  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings[4]["pool_pre_ping"] # kiểm tra kết nối trước mỗi lần dùng
)
```

***`test.py`:***
```python
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "USERS_SQLALCHEMY"
    # Integer <-> INT, BIGINT, TINYINT trong MySQL
    # primary_key <-> PRIMARY KEY trong MySQL
    # autoincrement <-> AUTO_INCREMENT trong MySQL
    # nullable=False <-> NOT NULL; nullable=True <-> NULL trong MySQL
    # unique <-> UNIQUE trong MySQL
    # DATETIME: YYYY-MM-DD HH:MM:SS
    # datetime.utcnow: thời điểm hiện tại (thời điểm thực hiện)
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(200), nullable=False, unique=True)
    is_active = Column(Integer, default=1)
    birthdate = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Tạo bảng khi bảng chưa tồn tại
Base.metadata.create_all(bind=engine)
print("Tạo bảng thành công")
```

## 16.3. Mối quan hệ giữa `FOREIGN KEY` và `PRIMARY KEY`

### 16.3.1. Định nghĩa
#### `PRIMARY KEY` (PK - Khóa chính)
**Định nghĩa:**
> Là một cột hoặc một tập hợp các cột dùng để xác định duy nhất mỗi hàng trong một bảng

**Đặc tính:**
> + Giá trị phải là duy nhất (UNIQUE)
> + Không được phép `NULL` (`NOT NULL`)
> + Một bảng chỉ có thể có một `PRIMARY KEY`

**Vai trò:**
> Đảm bảo tính toàn vẹn thực thể (Entity Integrity), làm điểm neo để các bảng khác tham chiếu đến

#### `FOREIGN KEY` (FK - Khóa ngoại)
**Định nghĩa:**
> Là một cột hoặc một tập hơn các cột trong một bảng (bảng con) tham chiếu đến `PRIMARY KEY` (hoặc `UNIQUE KEY`) của một bảng khác (bảng cha)

**Đặc tính:**
> + Giá trị có thể trùng lặp (nếu quan hệ 1 - N)
> + Có thể chấp nhận `NULL` (tùy thiết kế)
> + Một bảng có thể có nhiều `FOREIGN KEY`

**Vai trò:**
> Đảm bảo tính toàn vẹn tham chiếu (Referential Integrity), liên kết dữ liệu giữa các bảng.


#### Mối quan hệ giữa `PRIMARY KEY` và `FOREIGN KEY`

Mối quan hệ giữ PK và FK là nền tảng của mô hình cơ sở dữ liệu (RDBMS)

> + **Bảng cha (Parent Table):** Chứa `PRIMARY KEY`
> + **Bảng con (Child Table):** Chứa `FOREIGN KEY` tham chiếu đến PK của bảng cha
> + **Ràng buộc (Constraint):** MySQL ngăn chặn các hành động làm mất liên kết dữ liệu (ví dụ: xóa bản ghi cha khi bản ghi con vẫn đang tham chiếu đến nó, trừ khi có cấu hình đặc biệt)


### 16.3.2. Cơ chế hoạt động và ràng buộc 
#### Tính toàn vẹn tham chiếu (Referential Integrity)
Khi một Foreign Key được thiết lập, MySQL (với engine InnoDB) sẽ enforced các quy tắc sau:
1. **Insert/Update ở bảng con:** Giá trị đưa vào cột FK phải tồn tại trong cột PK của bảng cha hoặc là `NULL`.
2. **Delete/Update ở bảng cha:** Hành động phụ thuộc vào cấu hình `ON DELETE` và `ON UPDATE`.

#### Các hành động (Actions)
+ **RESTRICT (Mặc định):** Ngăn chặn việc xóa/cập nhật bản ghi cha nếu có bản ghi con tham chiếu
+ **CASCADE:** Tự động xóa/cập nhật bản ghi con khi bản ghi cha bị xóa/cập nhật
+ **SET NULL:** Đặt giá trị FK về `NULL` khi bản ghi cha bị xóa/cập nhật (cột FK phải cho phép `NULL`)
+ **NO ACTION:** Tương tự RESTRICT, kiểm tra sau khi statement hoàn thành
+ **SET DEFAULT:** Đặt về giá trị mặc định (ít hỗ trợ trong MySQL)

### 16.3.3. Ví dụ 
#### 16.3.3.1. Tạo Bảng và Thiết Lập Quan Hệ 
***`query_test.sql`:***
```sql
-- Đảm bảo sử dụng engine InnoDB để hỗ trọ Foreign Key
-- Tạo bảng cha: departments (Phòng ban)
CREATE TABLE departments_mysql (
    `dept_id` INT AUTO_INCREMENT PRIMARY KEY, -- id phòng <1>
    `dept_name` VARCHAR(100) NOT NULL, -- tên phòng
    `location` VARCHAR(255) -- địa chỉ
) ENGINE = InnoDB;

-- Tạo bảng con: employees (Nhân viên)
-- Có khóa ngoại tham chiếu đến departments
CREATE TABLE employees_mysql (
    `emp_id` INT AUTO_INCREMENT PRIMARY KEY, -- id nhân viên
    `emp_name` VARCHAR(100) NOT NULL, -- tên nhân viên
    `dept_id` INT NOT NULL, -- id phòng <1>
    -- Định nghĩa Foreign Key
    CONSTRAINT fk_emp_department  -- fk_<bảng con>_<bảng cha>
        Foreign Key (`dept_id`)    -- cột ở bảng con
        REFERENCES departments_mysql (`dept_id`) -- cột ở bảng cha
        ON DELETE RESTRICT -- không được phép xóa phòng ban nếu còn nhân viên ở phòng đó
        -- Khi cột dept_id ở bảng cha thay đổi giá trị -> ở bảng con cập nhật theo bảng cha
        ON UPDATE CASCADE  -- tự động cập nhật xuống bảng employees 
) ENGINE=InnoDB;
```

***`test.py`:***
```python
class Departments(Base):
   __tablename__ = 'departments_sqlalchemy'
   dept_id=Column(Integer, autoincrement=True, primary_key=True)
   dept_name=Column(String(100), nullable=False)
   location=Column(String(255))

class Employees(Base):
   __tablename__ = 'employees_sqlalchemy'
   emp_id=Column(Integer, autoincrement=True, primary_key=True)
   emp_name=Column(String(100), nullable=False)
   dept_id=Column(
      Integer,
      ForeignKey(
         'departments_sqlalchemy.dept_id',
         ondelete='RESTRICT',
         onupdate='CASCADE'
      ),
      nullable=False
   )
```

