from test.app.database.models.models import User
from sqlalchemy.orm import Session
from test.app.schemas.schemas import UserCreate

def get_user_respository(id: int, db:Session):
    return db.query(User).filter(User.id == id).first()

def create_user_respository(db: Session, user_in: UserCreate):
    '''Tạo mới user và lưu vào database'''
    db_user = User(name=user_in.name) # tạo đối tượng User từ dữ liệu đầu vào
    db.add(db_user) # thêm vào session
    db.commit()
    db.refresh(db_user) # cập nhật đối tượng với id tự tăng từ database
    return db_user