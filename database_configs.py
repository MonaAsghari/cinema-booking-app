import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRESQL_NAME: str
    POSTGRESQL_USER: str
    POSTGRESQL_PASS: str
    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: int

    model_config = SettingsConfigDict(
        env_file=os.path.abspath(
            os.path.join(os.path.dirname(__file__), '.env')
        ),
        extra="allow",
        env_file_encoding='utf-8'
    )


settings = Settings()
