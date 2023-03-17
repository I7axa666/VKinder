import configparser
import os.path


def get_data():
    config = configparser.ConfigParser()
    dirname = os.path.dirname(__file__)
    path = dirname + "/setting.ini"
    config.read(path)
    name_user = config["DATABASE"]["USER"]
    password = config["DATABASE"]["PASSWORD"]
    name_db = config["DATABASE"]["NAME_DB"]
    token_vk = config["DATABASE"]["TOKEN_VK"]
    new_token_vk = config["DATABASE"]["VK_NEW_TOKEN"]
    return name_user, password, name_db, token_vk, new_token_vk
