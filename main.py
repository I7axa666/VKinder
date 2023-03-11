import vk_api
from settings import TOKEN_VK


session = vk_api.VkApi(token=TOKEN_VK)
# print(session.method('users.get', {'user_ids': 1, 'fields': 'city, verified'}))

print(session.method('users.get',))