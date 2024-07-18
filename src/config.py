from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LINKEDIN_CLIENT_ID: str
    LINKEDIN_CLIENT_SECRET: str
    LINKEDIN_REDIRECT_URI: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
