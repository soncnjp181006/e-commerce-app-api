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