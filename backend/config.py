from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    
    DATABASE_URL: str
    SECRET_KEY: str
    SECRET_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore", # ignore extra env vars
        case_sensitive=True  #makes it casesensitive
    )
settings = Settings()