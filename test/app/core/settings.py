from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    '''Cấu hình trung tâm'''
    # Database - cấu hình của engine
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DEBUG: bool = True
    POOL_SIZE: int= 10
    MAX_OVERFLOW: int= 20
    POOL_PRE_PING: bool= True

    @property # khi call fun không cần () , settings.DATABASE_URL thay vì có thêm ()
    def DATABASE_URL(self) -> str:
        return(
            # DB_USER, ... được load từ test/.env
            f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
            f'?charset=utf8mb4' # Hỗ trợ emoji và ký tự đặc biệt
        )


    class Config:
        # đường dẫn tới '.env'
        env_file = 'test/.env'        # load cấu hình từ file .env
        env_file_encoding = 'utf-8'    # hỗ trợ emoji
        case_sensitive = True          # phân biệt hoa thường
    
# lru_cache: chỉ tạo Settings 1 lần, dùng lại cho toàn app
@lru_cache()
def get_setting() -> Settings:
    return Settings()

# Instance dùng trực tiếp: from app.config import settings
settings = Settings()