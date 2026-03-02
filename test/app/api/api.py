from sqlalchemy.orm import Session
from test.app.schemas.schemas import UserCreate, UserResponse
from fastapi import Depends
from test.app.database.session import get_db
from test.app.services.services import(
    create_user_services,
    get_user_services
)

from fastapi import APIRouter #, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/users/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_services(id, db)

# Viết đến đây rồi chạy -> không lỗi -> ok

@router.post('/users', response_model=UserResponse, status_code=201)
def create_user(user_in: UserCreate, db: Session=Depends(get_db)):
    return create_user_services(db, user_in)

# Viết đến đây rồi chạy -> không lỗi -> ok