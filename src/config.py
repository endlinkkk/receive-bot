from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    BOT_TOKEN: str
    UPLOAD_DIR: str = str(Path(__file__).parent / "data" / "uploaded_files")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
