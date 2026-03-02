from sqlalchemy import create_engine
from test.app.core.settings import settings

engine = create_engine(
    settings.DATABASE_URL,               # link kết nối database
    echo=settings.DEBUG,                 # log SQL ra terminal khi debug
    pool_size=settings.POOL_SIZE,        # số kết nối tối đa trong pool
    max_overflow=settings.MAX_OVERFLOW,  # cho phép thêm 20 kết nối khi pool đầy
    pool_pre_ping=settings.POOL_PRE_PING # kiểm tra kết nối trước mỗi lần dùng
)
