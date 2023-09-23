import asyncio
import logging
from vk.client import VkClient
from vk.dispatcher import Dispatcher
from utils.settings import settings
from utils.logging import get_logger


log = get_logger("main")


async def main():
    vk = VkClient(token=settings.vk_token)
    log.debug("Created vk api instance")
    dp = Dispatcher(vk)

    from router.commands import router as commands_router
    from router.solve import router as solve_router

    dp.include_router(commands_router)
    dp.include_router(solve_router)

    log.debug("Registered routers")

    await dp.start_polling(settings.vk_group_id)


if __name__ == "__main__":
    asyncio.run(main())
