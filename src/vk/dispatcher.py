import asyncio
import logging
import httpx
from typing import Any
from .client import VkClient
from .router import Router
from .types.event import Event
from .types.message import MessageNewEvent, SendMessage


class Dispatcher:
    def __init__(self, vk_client: VkClient) -> None:
        self.log = logging.getLogger("Dispatcher")

        self.vk_client = vk_client
        self.routers: list[Router] = []

    async def start_polling(self, group_id: int):
        # {$server}?act=a_check&key={$key}&ts={$ts}&wait=25
        server_info = await self.vk_client._get_long_poll_server(group_id)

        server, key, ts = (
            server_info["server"],
            server_info["key"],
            server_info["ts"],
        )
        async with httpx.AsyncClient() as client:
            while True:
                try:
                    response = await client.get(
                        f"{server}?act=a_check&key={key}&ts={ts}&wait=25",
                        timeout=25,
                    )
                    response = response.json()
                    ts = response["ts"]

                    await self.__register_updates(response["updates"])
                except httpx.ReadTimeout:
                    continue
                except Exception as e:
                    self.log.debug(str(e))
                    raise e

    async def __register_updates(self, updates: list[dict[str, Any]]):
        for update in updates:
            match update["type"]:
                case "message_new":
                    user = await self.vk_client.get_user(
                        update["object"]["message"]["from_id"]
                    )
                    asyncio.create_task(
                        self.__handle_update(MessageNewEvent(**update, from_user=user))
                    )
        await self.__handle_pending_updates()

    async def __handle_update(self, update: Event):
        for router in self.routers:
            handle_result = await router.handle(update)
            self.log.debug(type(handle_result))
            self.log.debug(f"handle_result = {handle_result}")
            if handle_result:
                if isinstance(handle_result, SendMessage):
                    await self.vk_client.send_message(handle_result)
                break

    async def __handle_pending_updates(self):
        for task in asyncio.all_tasks():
            if task is not asyncio.current_task():
                await task

    def include_router(self, router: Router):
        self.routers.append(router)
