from pydantic_settings import SettingsConfigDict, BaseSettings

class Settings(BaseSettings):
    
    database_url : str
    secret_key : str
    secret_algorithm : str
    access_token_expire_minutes : int
    model_config = SettingsConfigDict(
        env_file = ".env"
    )
settings = Settings()