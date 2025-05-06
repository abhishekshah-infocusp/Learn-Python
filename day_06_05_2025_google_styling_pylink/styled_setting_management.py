from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationConfig(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,  # required for alias use
    )

    database_host: HttpUrl = Field(alias="DATABASE_HOST")
    database_user: str = Field(alias="DATABASE_USER", min_length=6)
    database_password: str = Field(alias="DATABASE_PASSWORD", min_length=8)
    api_key: str = Field(alias="API_KEY", min_length=10)
