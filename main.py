import vk_api
import constantKeeper as keeper
import database.repository
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = vk_api.VkApi(token=keeper.BOT_TOKEN)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, keeper.MY_VK_GROUP_ID)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=vk_api.utils.get_random_id(),
                    message=event.obj.text)
