import configparser
import os.path

import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import sqlalchemy


def get_data():
    config = configparser.ConfigParser()
    dirname = os.path.dirname(__file__)
    path = dirname + '/setting.ini'
    config.read(path)
    name_user = config['DATABASE']['USER']
    password = config['DATABASE']['PASSWORD']
    name_db = config['DATABASE']['NAME_DB']
    token_vk = config['DATABASE']['TOKEN_VK']
    new_token_vk = config['DATABASE']['VK_NEW_TOKEN']
    return name_user, password, name_db, token_vk, new_token_vk


Base = declarative_base()

DSN = f'postgresql://{get_data()[0]}:{get_data()[1]}@localhost:5432/{get_data()[2]}'
engine = sqlalchemy.create_engine(DSN)


class User(Base):
    __tablename__ = "users"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    city_id = sq.Column(sq.Integer, nullable=False)
    sex = sq.Column(sq.Integer, nullable=False)
    birth_year = sq.Column(sq.Integer, nullable=False)
    link = sq.Column(sq.Text, unique=True, nullable=False)
    offset = sq.Column(sq.Integer, nullable=True)



class Favorit(Base):
    __tablename__ = "favorites"

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("users.id"), nullable=False)
    name = sq.Column(sq.String(length=40), nullable=False)
    surname = sq.Column(sq.String(length=40), nullable=False)
    link = sq.Column(sq.Text, unique=True, nullable=False)
    photo = sq.Column(sq.Text, unique=True, nullable=False)
    user = relationship(User, backref="favorites")


class Black_list(Base):
    __tablename__ = "black_list"

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("users.id"), nullable=False)
    vk_id = sq.Column(sq.Text, unique=True, nullable=False)
    user = relationship(User, backref="black_list")

def create_tables(engine):
    Base.metadata.create_all(engine)


def drop_tables(engine):
    Base.metadata.drop_all(engine)



def add_user(name, sex, city, bdate,  link, engine=engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    check_user = session.query(User).filter(User.link == link)
    if session.query(check_user.exists()).scalar() == False:
        user = User(name=name, sex=sex, city_id=city, birth_year=bdate, link=link, offset=0)

        session.add(user)
        session.commit()


    session.close()


def get_user_info(user_id, engine=engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    user_data = session.query(User).filter(User.link == user_id).one()
    if user_data.sex == 1:
        sex = 2
    elif user_data.sex == 2:
        sex = 1

    city_id = user_data.city_id

    birth_year = user_data.birth_year

    session.close()
    return sex, city_id, birth_year



if __name__ == '__main__':
    # drop_tables(engine)
    # create_tables(engine)
    # add_user('Павел', 'https://vk.com/559261802')
    get_user_info('https://vk.com/id559261802')