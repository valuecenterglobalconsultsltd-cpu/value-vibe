from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Value Vibe"
    APP_ENV: str = "development"

    SECRET_KEY: str

    DATABASE_URL: str

    REDIS_URL: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
