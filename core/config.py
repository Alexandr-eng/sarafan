from pathlib import Path
from  pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"
    db_echo: bool = False
settings = Settings()

from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

