import logging
import httpx
from typing import Any
from .types.user import User


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class VkClient:
    def __init__(self, token: str):
        self.log = logging.getLogger("VkClient")

        # POST https://api.vk.com/method/<METHOD>?<PARAMS> HTTP/1.1
        self.api_url = "https://api.vk.com/method"
        self._token = token

    async def _call_api(
        self,
        method: str,
        params: dict[Any, Any],
        request_type: str = "get",
        headers: dict[str, str] = {},
    ):
        async with httpx.AsyncClient() as client:
            headers["Authorization"] = f"Bearer {self._token}"

            response: httpx.Response | None = None
            if request_type == "get":
                response = await client.get(
                    f"{self.api_url}/{method}", params=params, headers=headers
                )
            elif request_type == "post":
                response = await client.post(
                    f"{self.api_url}/{method}", params=params, headers=headers
                )
            if response is None:
                raise ValueError("Request type must be 'get' or 'post'")
            return response.json()

    async def start_polling(self, group_id: int):
        self.log.debug(await self._get_long_poll_server(group_id))
        pass

    async def _get_long_poll_server(self, group_id: int):
        response = await self._call_api(
            "groups.getLongPollServer",
            {"group_id": group_id, "v": "5.131"},
        )
        self.log.debug(response)
        return response["response"]

    async def get_user(self, user_id: int) -> User:
        response = await self._call_api(
            "users.get",
            {"user_ids": user_id, "v": "5.131"},
        )
        self.log.debug(response)
        return User(**response["response"][0])
