import logging
import httpx
import random
from typing import Any
from .types.user import User
from .types.message import SendMessage


class VkClient:
    def __init__(self, token: str):
        self.log = logging.getLogger("VkClient")

        # POST https://api.vk.com/method/<METHOD>?<PARAMS> HTTP/1.1
        self.api_url: str = "https://api.vk.com/method"
        self.__token: str = token

    async def __call_api(
        self,
        method: str,
        params: dict[Any, Any],
        request_type: str = "get",
        headers: dict[str, str] = {},
    ):
        async with httpx.AsyncClient() as client:
            headers["Authorization"] = f"Bearer {self.__token}"

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
            self.log.debug(f"response = {response.json()}")
            return response.json()

    async def _get_long_poll_server(self, group_id: int):
        response = await self.__call_api(
            "groups.getLongPollServer",
            {"group_id": group_id, "v": "5.131"},
        )
        return response["response"]

    async def get_user(self, user_id: int) -> User:
        response = await self.__call_api(
            "users.get",
            {"user_ids": user_id, "v": "5.131"},
        )
        return User(**response["response"][0])

    async def send_message(self, msg: SendMessage):
        params = {
            "user_id": msg.message_event.object.message.from_id,
            "random_id": random.getrandbits(31) * random.choice([-1, 1]),
            "message": msg.text,
            "v": "5.131",
        }
        if msg.reply_markup:
            params["keyboard"] = msg.reply_markup.model_dump_json()
        await self.__call_api(
            "messages.send",
            params=params,
            request_type="post",
        )
