import configparser
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_data():
    config = configparser.ConfigParser()
    path = str(get_project_root()) + "/setting.ini"
    config.read(path)
    name_user = config["DATABASE"]["USER"]
    password = config["DATABASE"]["PASSWORD"]
    name_db = config["DATABASE"]["NAME_DB"]
    token_vk = config["DATABASE"]["TOKEN_VK"]
    new_token_vk = config["DATABASE"]["VK_NEW_TOKEN"]
    return name_user, password, name_db, token_vk, new_token_vk


get_data()
