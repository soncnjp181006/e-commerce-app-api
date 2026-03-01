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