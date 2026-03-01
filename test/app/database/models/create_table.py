from test.app.database.database import engine
from test.app.database.base import Base

# Tạo tất cả các bảng (được import từ models/ vào create_table.py) trong MySQL
Base.metadata.create_all(bind=engine)