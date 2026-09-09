from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MlSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    ml_service_host: str = Field(default="0.0.0.0", alias="ML_SERVICE_HOST")
    ml_service_port: int = Field(default=8100, alias="ML_SERVICE_PORT")


settings = MlSettings()
