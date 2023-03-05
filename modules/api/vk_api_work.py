import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from db_for_vkinder import get_data

session = vk_api.VkApi(token=get_data()[3])


def sent_message(user_id, message):
    session.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    })


for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text == "hello":
            sent_message(user_id, "hello user")
