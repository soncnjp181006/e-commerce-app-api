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