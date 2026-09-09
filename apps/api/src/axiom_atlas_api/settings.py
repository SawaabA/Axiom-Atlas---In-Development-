from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    ml_service_url: str | None = Field(default=None, alias="ML_SERVICE_URL")
    redis_url: str | None = Field(default=None, alias="REDIS_URL")


settings = ApiSettings()
