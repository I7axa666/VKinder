import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from db_for_vkinder import get_data, add_user, get_user_info, change_user_info, add_favorite, add_black_list, show_favorites
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class VKBot:
    def __init__(self):
        self.vk = vk_api.VkApi(token=get_data()[3])
        self.long_pool = VkLongPoll(self.vk)
        self.listen = self.long_pool.listen()
        self.person_dict = {}


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
        # self.vk.method('messages.send', {'user_id': user_id, 'message': person_info, 'attachment': "photo353616539_405298694,photo353616539_404294376", 'random_id': 0})


    def save_profile_info(self, user_id):
        info = self.vk.method('users.get', {"user_ids": user_id, "fields": "bdate, sex, city"})
        first_name = info[0]['first_name']
        bdate = int(info[0]['bdate'].split(".")[2])
        sex = info[0]['sex']
        city = info[0]['city']['id']
        link = f'https://vk.com/id{user_id}'
        add_user(first_name, sex, city, bdate, link)


    def pair_up(self, user_id, keyboard):

        user_info = get_user_info(f'https://vk.com/id{user_id}')
        sex = user_info[0]
        city_id = user_info[1]
        birth_year = user_info[2]
        offset = user_info[3]
        db_user_id = user_info[4]
        session = vk_api.VkApi(token=get_data()[4])
        while True:
            persons = session.method('users.search', {'sex': sex, 'birth_year': birth_year, 'has_photo': 1, 'city': city_id, 'offset': offset, 'count': 1, 'v': '5.131'})
            if persons['items'][0]['is_closed'] is True:
                offset += 1
                change_user_info(f'https://vk.com/id{user_id}', offset)

            else:
                person_id = persons['items'][0]['id']
                photos = session.method('photos.get',
                                        {'owner_id': person_id, 'album_id': 'profile', 'extended': 1,
                                         'v': '5.131'})
                photos_dict = {}
                owner_id = photos['items'][0]['owner_id']
                for photo in photos['items']:

                    photos_dict[photo['id']] = photo['likes']['count']

                photos_list = dict(sorted(photos_dict.items(), key=lambda item: item[1]))

                if len(photos_list) > 3:
                    count_photo = 3
                else:
                    count_photo = len(photos_list)

                attachment = ''

                for photo in range(count_photo):
                    attachment += f'photo{owner_id}_{photos_list.popitem()[0]},'

                attachment = attachment[:-1]

                self.person_dict['user_id'] = db_user_id
                self.person_dict['name'] = persons['items'][0]['first_name']
                self.person_dict['surname'] = persons['items'][0]['last_name']
                self.person_dict['link'] = f'https://vk.com/id{owner_id}'
                self.person_dict['owner_id'] = owner_id



                person_info = f"{self.person_dict['name']} {self.person_dict['surname']}\n{self.person_dict['link']}"

                self.vk.method(
                    'messages.send',
                    {
                        'user_id': user_id,
                        'message': person_info,
                        'attachment': attachment,
                        'random_id': 0
                    }
                )
                offset += 1
                change_user_info(f'https://vk.com/id{user_id}', offset)
                break

        self.write_some_msg(user_id, "Добавляем в Блэк-лист или в Избранное?", keyboard)



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
            key_get_person = VkKeyboard()

            key_get_person.add_button("Найти пару", VkKeyboardColor.PRIMARY)
            self.write_some_msg(
                event.user_id,
                "Поехали!!!",
                key_get_person
            )

        elif keys == "add_favorite":
            self.key_find_person = VkKeyboard()
            buttons = ['Блэк лист', 'Избранные', 'Показ фаворитов']
            button_color = [VkKeyboardColor.NEGATIVE, VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY]
            for btn, btn_color in zip(buttons, button_color):
                self.key_find_person.add_button(btn, btn_color)

            self.pair_up(event.user_id, self.key_find_person)



    def run(self):
        for event in self.listen:
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text.lower()

                    if request == "start":
                        self.create_keybord(event, "find_person")

                    elif request == "найти пару":
                        self.create_keybord(event, "add_favorite")

                    elif request == "избранные":
                        # добавить проверку на наличие данных в person_dict
                        add_favorite(self.person_dict)
                        self.person_dict.clear()
                        self.pair_up(event.user_id, self.key_find_person)

                    elif request == "блэк лист":
                        add_black_list(self.person_dict)
                        self.person_dict.clear()
                        self.pair_up(event.user_id, self.key_find_person)

                    elif request == "показ фаворитов":
                        self.person_dict.clear()
                        persons = show_favorites(f'https://vk.com/id{event.user_id}')
                        message = '\n'.join('{} {}'.format(key, val) for key, val in persons.items())
                        self.write_some_msg(event.user_id, message)
                        self.create_keybord(event, "find_person")



                    else:
                        self.create_keybord(event, 'start')
                        # self.save_profile_info(event.user_id)
                        # self.pair_up(event.user_id)



                    # elif request == "фото":
                    #     self.send_photo(event.user_id, "")
                    # elif request == "данные":
                    #     self.send_profile_info(event.user_id)


if __name__ == "__main__":
    bot = VKBot()
    bot.run()
