from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

@lru_cache
def get_settings():
    return Settings()

class Settings(BaseSettings):
    database_uri: str = "sqlite:///database.db"
    secret_key: str = "ThisIsAnExampleOfWhatNotToUseAsTheSecretKeyIRL"
    env: str = "development"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expires: int = 30
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    
    model_config = SettingsConfigDict(env_file=".env")