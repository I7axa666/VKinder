<h1 align="center">VKinder<img src='https://user-images.githubusercontent.com/74038190/206662607-d9e7591e-bbf9-42f9-9386-29efc927bc16.gif' width="40"> </h1>

**VKinder** - бот-программа для поиска своего спутника жизни в социальной сети Вконтакте. Бот осуществляет поиск партнера учитывая Ваши предпочтения (возраст, пол, город) и выбирает три самые популярные фотографии. Потенциальных спутников жизни можно добавлять в список избранных и черный список. Бот имеет максимально понятный интерфейс и кнопки для управления командами. 
# <img src='https://user-images.githubusercontent.com/74038190/206662693-4a4f6595-0378-4e2c-b347-561bac728308.gif' width="40"> Команда проекта:
- Павел Соловей
- Илья Карьялайнен
- Николай Золотухин


Этот проект написан в рамках курса "Python разработчик с нуля" ООО "Нетологии"

<img src="https://www.animatedimages.org/data/media/562/animated-line-image-0184.gif" width="1920" />

# Установка <img src="https://user-images.githubusercontent.com/74038190/221857969-f37e1717-1470-4fe4-abb5-88b334cf64ea.png" alt="icon of todo list" width="40" />

### 1. Скачайте код

Скопируйте все файлы из репозитория в вашу среду разработки. Например, PyCharm.

Для этого используйте команду:
`git clone`

### 2. Установите библиотеки

Для корректной работы бота установите все библиотеки, которые находятся в файле requirements.txt

### 3. Получите токены

Для запуска программы необходимы 2 ключа доступа: ключ доступа пользователя и ключ доступа сообщества.

Откройте файл setting.ini. Поменяйте значения TOKEN_VK - ключ доступа пользователя, VK_NEW_TOKEN - ключ доступа сообщества

ВНИМАНИЕ!!! ЗНАЧЕНИЯ УКАЗЫВАЮТСЯ БЕЗ КОВЫЧЕК
```
[DATABASE]
USER = postgres
PASSWORD = 
NAME_DB = netology_db
TOKEN_VK = 
VK_NEW_TOKEN = 

```

<details>
  <summary> Как получить ключ доступа пользователя</summary>
  
  1. Перейдите в среду разработчиков VK по ссылке https://dev.vk.com/
  
  2. Создайте приложение
  
  ![image](https://i.imgur.com/se4MzlZ.png)
  
  3. Укажите название сообщества и выберете «Standalone-приложение»
  
  ![image](https://i.imgur.com/oEF0tmM.png)
  
  4. Перейдите в настройки, включите Open API
  
  ![image](https://i.imgur.com/HUgE8OF.png)
  
  5. В поле «Адрес сайта» введите http://localhost
  
  ![image](https://i.imgur.com/wTAU8oy.png)
  
  6. В поле «Базовый домен» введите localhost
  
  ![image](https://i.imgur.com/VFNkUHI.png)
  
  7. Сохраните изменения
  
  8. Скопируйте ID приложения
  
  ![image](https://i.imgur.com/92giyev.png)
  
  9. В данную ссылку в параметр client_id вместо 1 вставьте ID вашего приложения:
  https://oauth.vk.com/authorize?client_id=1&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=stats.offline&response_type=token
  
  10. Перейдите по ссылке и сохраните из полученной адресной строки ваш токен пользователя
  
  ![image](https://i.imgur.com/lZPX8Ss.png)
  
  Подробнее про ключи доступа VK API: https://dev.vk.com/api/access-token/getting-started
  
</details>

<details>
  <summary> Как получить ключ доступа сообщества</summary>
  
  1. Для начала нужно иметь свое сообщество, которое и будет непосредственно осуществлять общение. 
  Подробнее про создание сообщества: https://vk.com/faq18025
  
  2. Перейдите в настройки, в раздел «Работа с API»
  
  ![image](https://i.imgur.com/MKqtKO0.png)
  
  3. Нажмите «Создать ключ»
  
  ![image](https://i.imgur.com/1MfUQFU.png)
  
  4. Выберите необходимые права для ключа. В данном случае вам нужен доступ к управлению и сообщениям сообщества
  
  ![image](https://i.imgur.com/LOxhMXD.png)
  
  5. Сохраните созданный ключ доступа сообщества
  
  ![image](https://i.imgur.com/qSbE7Tc.png)
  
  Подробнее про ключи доступа VK API: https://dev.vk.com/api/access-token/getting-started
  
</details>


### 4. Настройте ваше сообщество

1. Перейдите в управление сообщества в раздел «Сообщения», включите «Сообщения сообщества» и сохраните изменения

![image](https://i.imgur.com/QhCqVCG.png)

2. Перейдите в раздел «Настройки для бота», включите «Возможности ботов» и сохраните изменения

![image](https://i.imgur.com/dUDEyBS.png)

3. Перейдите в настройки, в раздел «Работа с API», откройте вкладку «Long Poll API» и включите «Long Poll API»

![image](https://i.imgur.com/CQ4Saeo.png)

4. В этом же разделе откройте вкладку «Типы событий» и поставьте галочки во входящих и исходящих сообщениях

![image](https://i.imgur.com/NqUGdWf.png)

### 5. Создайте вашу базу данных

Не забудьте создать базу данных. Мы использовали СУБД PostgreSQL.
В файле setting.ini укажите значения USER (пользователь БД, обычно это postgres), password и NAME_DB

ВНИМАНИЕ!!! ЗНАЧЕНИЯ УКАЗЫВАЮТСЯ БЕЗ КОВЫЧЕК
```
[DATABASE]
USER = postgres
PASSWORD = 
NAME_DB = netology_db
TOKEN_VK = 
VK_NEW_TOKEN = 
```
### 6. ВОТ И ВСЁ, БОТ ГОТОВ К РАБОТЕ.


