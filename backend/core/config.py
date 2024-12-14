from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 基础配置
    PROJECT_NAME: str = "Novel Ending Factory"
    API_V1_STR: str = "/api/v1"
    
    # 数据库配置
    DATABASE_URL: str = "mysql+aiomysql://user:password@localhost/novel_ending"
    
    # CORS配置
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # JWT配置
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    
    # Dify API配置
    DIFY_WORKFLOW_ID: str = ""  # 如果需要指定特定工作流
    DIFY_API_KEY: str = "your-dify-api-key"
    DIFY_API_URL: str = "https://api.dify.ai/v1"
    DIFY_TIMEOUT: int = 600  # API 调用超时时间（秒）
    
    class Config:
        env_file = ".env"

settings = Settings() 