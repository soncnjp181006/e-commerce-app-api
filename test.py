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

# Base.metadata.create_all(bind=engine)
# print('Tạo bảng thành công')

#############################################################################################
# Thực hiện tạo bảng, ... học truy vấn ở đây, phần bên trên là kết nối database
#############################################################################################
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