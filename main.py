import vk_api
from settings import VK_NEW_TOKEN
from db_for_vkinder import get_data

session = vk_api.VkApi(token=get_data()[4])
persons = session.method('users.search', {'sex': 1, 'birth_year': 1988, 'has_photo': 1,'city': 69,'offset': 3, 'v': '5.131'})
for i in persons['items']:
    if i['is_closed'] is not True:
        print(i['id'], i['first_name'])





# print(x)

# import time
# import requests
# import json
#
# from pprint import pprint
#
# URL = 'https://api.vk.com/method/users.search'
# params = {
#     'access_token': 'vk1.a.fKMNn7YP8se9UzAc_YzamxEgEy0B1oUnlEIPfmUZCVOvPkK0UY7D1sNfBoA83iwSmfZHVVSjPluDet2bHbNTTRp9CZsKJ9jveBS7a5vQDrAhDxgAcUlGz3zDP1gAkNgoWqixh6dfLHM-gcYiyjo8dI5YPXkkx7ubKlQAeuJNn51SxQaktE0p4S21CXoxSnZ723kkiaUjfkN82jtKK9yaHw',
#     # 'count': 3,
#     'sex': 1,
#     'birth_year': 1988,
#     'has_photo': 1,
#     # 'is_closed': 'True',
#     'city': 69,
#     'offset': 3,
#     'v': 5.131
# }
#
# res = requests.get(URL, params=params)
#
# # pprint(res.json())
# print(len(res.json()['response']['items']['first_name']))
#
# for i in res.json()['response']:
#     print(res.json()['response'])

