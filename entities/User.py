from peewee import *
from database.BaseModel import BaseModel


class User(BaseModel):
    id = AutoField()
    nome = CharField(max_length=80)
    nick = CharField()
    email = CharField(unique=True)
    password = CharField()
    criadoem = DateField()