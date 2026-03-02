from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database - Import cấu hình từ .env
    DB_USER: str=''
    DB_PASSWORD: str=''
    DB_HOST: str=''
    DB_PORT: str=''
    DB_NAME: str=''
    POOL_SIZE: int=10          # số kết nối tối thiểu
    MAX_OVERFLOW: int=20       # số kết nối mở thêm khi quá tải -> max 30 kết nối
    POOL_PRE_PING: bool=True   # kiểm tra Ping trước khi bắt đầu
    DEBUG: bool=True       

    @property
    def DATABASE_URL(self) -> str:
        return(
            f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
            f'?charset=utf8mb4' # hỗ trợ emoji và kí tự đặc biệt
        )

    class Config:
        env_file = '.env'           # path đến file .env
        env_file_encoding = 'utf-8' # hỗ trợ emoji
        case_sensitive = True       # phân biệt hoa/thường

# Cho phép tái sử dụng
@lru_cache
def get_setting() -> Settings:
    return Settings()

# Instance dùng trực tiếp: from app.core import settings
settings = Settings()