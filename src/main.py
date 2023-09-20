import asyncio
from vk.client import VkClient
from utils.settings import settings


async def main():
    vk = VkClient(token=settings.vk_token)
    await vk.get_user(1)
    await vk.start_polling(222562045)


if __name__ == "__main__":
    asyncio.run(main())

# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         if event.text == "Начать":
#             reply = commands.start(event)
#             vk.messages.send(user_id=event.user_id, message=reply)
# if event.text.startswith("+"):
#     vk.messages.send(
#         user_id=event.user_id, random_id=get_random_id(), message="asdf"
#     )
# else:
#     vk.messages.send(
#         user_id=event.user_id, random_id=get_random_id(), message=event.text
#     )
