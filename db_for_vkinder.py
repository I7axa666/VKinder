import configparser
import os.path

import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
import sqlalchemy


def get_password():
    config = configparser.ConfigParser()
    dirname = os.path.dirname(__file__)
    path = dirname + '/setting.ini'
    config.read(path)
    PASSWORD = config['PASSWORD_BD']['PASSWORD']
    return PASSWORD


Base = declarative_base()

DSN = f'postgresql://postgres:{get_password()}@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)


class People(Base):
    __tablename__ = "peoples"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    surname = sq.Column(sq.String(length=40), nullable=False)
    link = sq.Column(sq.Text, unique=True, nullable=False)


class Picture(Base):
    __tablename__ = "pictures"

    id = sq.Column(sq.Integer, primary_key=True)
    people_id = sq.Column(sq.Integer, sq.ForeignKey("peoples.id"), nullable=False)
    link = sq.Column(sq.Text, unique=True, nullable=False)

    people = relationship(People, backref="pictures")


class Black_list(Base):
    __tablename__ = "black_list"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    surname = sq.Column(sq.String(length=40), nullable=False)
    link = sq.Column(sq.Text, unique=True, nullable=False)


def create_tables(engine):
    Base.metadata.create_all(engine)


def drop_tables(engine):
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    create_tables(engine)
