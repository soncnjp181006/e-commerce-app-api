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
- [Phần 6. Thư mục `database` - Kết nối database](#phần-6-thư-mục-database---kết-nối-database)
- [Phần 7. Thư mục `schemas/`  - Nơi chứa Pydantic models](#phần-7-thư-mục-schemas----nơi-chứa-pydantic-models)
- [Phần 8. Thư mục `services/` - Xử lí nghiệp vụ chính của ứng dụng](#phần-8-thư-mục-services---xử-lí-nghiệp-vụ-chính-của-ứng-dụng)
  - [8.1. Phân tích](#81-phân-tích)
  - [8.2. Ví dụ](#82-ví-dụ)
- [Phần 9. Thư mục `middlewares/` - Lớp chạy trước mỗi request](#phần-9-thư-mục-middlewares---lớp-chạy-trước-mỗi-request)
  - [9.1 Middleware dùng cho](#91-middleware-dùng-cho)
  - [9.2. Mối quan hệ với `core/`](#92-mối-quan-hệ-với-core)
    - [`core/` là gì?](#core-là-gì)
    - [`middlewares/` là gì?](#middlewares-là-gì)
    - [Ví dụ 1](#ví-dụ-1)
- [Phần 10. Thư mục `api/` - Định nghĩa các route/endpoint (REST API, WebSocket...)](#phần-10-thư-mục-api---định-nghĩa-các-routeendpoint-rest-api-websocket)
- [Phần 11. Thư mục `dependencies/`](#phần-11-thư-mục-dependencies)
  - [11.1. Chức năng](#111-chức-năng)
  - [11.2. Ví dụ](#112-ví-dụ)
    - [11.2.1. Inject DB](#1121-inject-db)
    - [11.2.2. Lấy current user (Auth)](#1122-lấy-current-user-auth)
    - [11.2.3. Phân quyền](#1123-phân-quyền)
  - [Lưu ý](#lưu-ý)
  - [11.3. Mối quan hệ với `core/`](#113-mối-quan-hệ-với-core)

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

```py
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

# Phần 6. Thư mục `database` - Kết nối database

+ database.py - Tạo Engine (kết nối database, cấu hình engine)
- session.py - Quản lý session (mỗi request có 1 session riêng, tránh rò rỉ khi kết nối)
- base.py - Base ORM (Tạo class Base để các model kế thừa)
- `models/` - Thư mục khởi tạo, lưu giữ các file tạo bảng database (mapping bảng db thành class Python)
- `repositories/` - Thư mục chứa các file, hàm truy vấn database
- `migrations/` - Alembic Migration (được Alembic tạo ra) (quản lí thay đổi schema DB, version control cho database)

# Phần 7. Thư mục `schemas/`  - Nơi chứa Pydantic models

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

# Phần 8. Thư mục `services/` - Xử lí nghiệp vụ chính của ứng dụng

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
def create_task_service(db: Session, name: str):
    if len(name) < 3:
        raise ValueError("Tên quá ngắn")

    return create_task(db, name)
```

***`services/` [file cụ thể xử lí] xử lý nghiệp vụ:***

```py
from db.repositories.task_repository import create_task

def create_task_service(db: Session, name: str):
    if len(name) < 3:
        raise ValueError("Tên quá ngắn")

    return create_task(db, name)
```

***`api/` (nói sau) chỉ có router gọi `service/`***

```py
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db, task.name)
```

# Phần 9. Thư mục `middlewares/` - Lớp chạy trước mỗi request

```
Client → Middleware → Router → Middleware → Response
```

Tức là:
- Chạy trước khi vào router
- Chạy sau khi router trả response
- Nó áp dụng toàn bộ ứng dụng, không phải từng endpoint riêng lẻ.

## 9.1 Middleware dùng cho

+ CORS
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

# Phần 10. Thư mục `api/` - Định nghĩa các route/endpoint (REST API, WebSocket...)

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

+ dependencies/ KHÔNG phải là business layer.
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
