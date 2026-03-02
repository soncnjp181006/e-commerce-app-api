# SessionLocal: factory tạo ra mỗi session làm việc với database
# autocommit=False -> ta tự commit -> an toàn hơn
# autoflush=False -> không tự flush trước query
from sqlalchemy.orm import sessionmaker

from test.app.database.database import engine # import  hàm engine trong database.py

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()