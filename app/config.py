from pydantic import BaseSettings
class Settings(BaseSettings):
    database_details: str
    class Config:
        env_file= ".env"

settings = Settings()