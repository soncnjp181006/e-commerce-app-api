from sqlalchemy import create_engine

settings = [
    {"DATABASE_URL" : "mysql+pymysql://soncn:tranxuanson2k61810@localhost:3306/pc_shop"},
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

# Base.metadata.create_all(bind=engine)
# print('Tạo bảng thành công')

#############################################################################################
# Thực hiện tạo bảng, ... học truy vấn ở đây, phần bên trên là kết nối database
#############################################################################################
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    # Tên bảng trong MySQL
    __tablename__ = 'users'

    id=Column(Integer, primary_key=True, autoincrement=True)
    username=Column(String(200), nullable=False, unique=True)
    