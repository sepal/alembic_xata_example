
from pydantic import SecretStr, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


    postgres_server: str
    postgres_port: int = 5432
    postgres_user: str
    postgres_password: SecretStr
    postgres_db: str

    @computed_field
    @property
    def sqllachemy_uri(self) -> str:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.postgres_user,
            password=self.postgres_password.get_secret_value(),
            host=self.postgres_server,
            port=self.postgres_port,
            path=self.postgres_db,
        )
    

settings = AppSettings()
