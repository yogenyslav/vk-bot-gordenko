from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    vk_token: str = Field(..., env="VK_TOKEN")
    vk_group_id: int = Field(..., env="VK_GROUP_ID")


settings = Settings(_env_file=".env")
