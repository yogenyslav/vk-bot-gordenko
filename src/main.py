import asyncio
import logging
from vk.client import VkClient
from vk.dispatcher import Dispatcher
from utils.settings import settings
from router.commands import router as commands_router


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


async def main():
    vk = VkClient(token=settings.vk_token)
    dp = Dispatcher(vk)

    dp.include_router(commands_router)

    await dp.start_polling(settings.vk_group_id)


if __name__ == "__main__":
    asyncio.run(main())
