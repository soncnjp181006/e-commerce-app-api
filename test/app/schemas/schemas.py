from pydantic import BaseModel

class UserCreate(BaseModel): # Dùng để xem user
    name: str
    email: str

# Dữ liệu trả về sau khi tạo thành công
class UserResponse(BaseModel):       # Dùng để import user
    id: int
    name: str
    email: str