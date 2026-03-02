from test.app.repository.repository import (
    get_user_respository,
    create_user_respository
)
from test.app.schemas.schemas import UserCreate

from fastapi import HTTPException
from sqlalchemy.orm import Session
def get_user_services(id: int, db: Session):
    # Xem lại phần code bị lược bỏ phần trước và so sánh thấy rõ hơn 
    user = get_user_respository(id, db)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def create_user_services(db: Session, user_in: UserCreate):
    return create_user_respository(db, user_in)