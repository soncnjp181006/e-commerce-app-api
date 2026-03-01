# Tạo bảng
from sqlalchemy import Column, Integer, String
from test.app.database.base import Base

class User(Base):
    __tablename__ = "users_test"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)