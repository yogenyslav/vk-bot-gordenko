from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    vk_token: str = Field(..., env="VK_TOKEN")


settings = Settings(_env_file=".env")
