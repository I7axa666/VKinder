import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from db_for_vkinder import get_data
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


class VKBot:
    def __init__(self):
        self.vk = vk_api.VkApi(token=get_data()[3])
        self.long_pool = VkLongPoll(self.vk)
        self.listen = self.long_pool.listen()

    def write_some_msg(self, user_id, some_msg, keyboard=None):
        post = {
            'user_id': user_id,
            'message': some_msg,
            'random_id': 0
        }

        if keyboard != None:
            post["keyboard"] = keyboard.get_keyboard()
        else:
            post = post

        self.vk.method('messages.send', post)

    def send_photo(self, user_id, photo_id):
        self.vk.method('messages.send', {'user_id': user_id, 'attachment': "photo" + photo_id, 'random_id': 0})

    def send_profile_info(self, user_id):
        info = self.vk.method('users.get', {"user_ids": user_id, "fields": "bdate, sex, city, photo_id"})
        photo_id = info[0]['photo_id']
        first_name = info[0]['first_name']
        last_name = info[0]['last_name']
        user_info = f'{first_name} {last_name}\n' \
                    f'https://vk.com/{user_id}\n'
        self.vk.method('messages.send', {'user_id': user_id, 'message': user_info, 'random_id': 0})
        self.vk.method('messages.send', {'user_id': user_id, 'attachment': "photo" + photo_id, 'random_id': 0})


    def create_keybord(self, event, keys):
        if keys == 'start':
            key_start = VkKeyboard(one_time=True)

            key_start.add_button("START", VkKeyboardColor.PRIMARY)
            self.write_some_msg(
                event.user_id,
                "Приветствую тебя в чат-боте VKinder! Он поможет тебе найти кого-нибудь)) Начнем?",
                key_start
            )

        elif keys == "find_person":
            key_get_person = VkKeyboard(one_time=True)

            key_get_person.add_button("Найти пару", VkKeyboardColor.PRIMARY)
            self.write_some_msg(
                event.user_id,
                "Поехали!!!",
                key_get_person
            )

        # elif keys == "add_favorit":
        #     key_get_person = VkKeyboard()
        #
        #     key_get_person.add_button("Найти пару", VkKeyboardColor.PRIMARY)
        #     self.write_some_msg(
        #         event.user_id,
        #         "Поехали!!!",
        #         key_get_person
        #     )

    def run(self):
        for event in self.listen:
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text.lower()

                    if request == "start":
                        self.create_keybord(event, "find_person")

                    elif request == "найти пару":
                        self.write_some_msg(
                            event.user_id,
                            "Код еще не дописан)))"
                        )

                    else:
                        self.create_keybord(event, 'start')


                    # elif request == "фото":
                    #     self.send_photo(event.user_id, "")
                    # elif request == "данные":
                    #     self.send_profile_info(event.user_id)


if __name__ == "__main__":
    bot = VKBot()
    bot.run()