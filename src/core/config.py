from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME:str
    APP_VERSION:str
    OPENAI_API_KEY:str
    
    ALLOWED_FILE_TYPES:list 
    ALLOWED_FILE_SIZE:int
    FILE_DEFAULT_CHUNK_SIZE:int
    
    class Config:
        env_file = ".env"
        

def get_settings():
    return Settings()