"""
Application configuration management
"""
from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "CloudDisk"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    SECRET_KEY: str = "your-secret-key-here"
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/netdisk"
    
    # Cloudflare R2
    R2_ACCOUNT_ID: str = ""
    R2_ACCESS_KEY_ID: str = ""
    R2_SECRET_ACCESS_KEY: str = ""
    R2_BUCKET_NAME: str = "netdisk"
    R2_ENDPOINT: str = ""
    
    # OAuth
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GITHUB_CLIENT_ID: str = ""
    GITHUB_CLIENT_SECRET: str = ""
    
    # Quotas (in bytes)
    REGULAR_USER_QUOTA: int = 10485760  # 10 MB
    REGULAR_USER_FILE_LIMIT: int = 107374182400  # 100 GB
    ADMIN_QUOTA: int = -1  # Unlimited
    ADMIN_FILE_LIMIT: int = -1  # Unlimited
    
    # Trash
    TRASH_RETENTION_DAYS: int = 10
    
    # JWT
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 60
    
    # CORS
    ALLOWED_ORIGINS: str = "http://localhost:3000"
    
    # WebSocket
    WS_HEARTBEAT_INTERVAL: int = 30
    
    @property
    def allowed_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
