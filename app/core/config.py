from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./quizapp.db"
    secret_key: str = "supersecretkey"

    class Config:
        env_file = ".env"

settings = Settings()
