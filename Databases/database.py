from peewee import *
from os import path

#creating our first database
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "sampython.db"))

#creating our table inside db
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
User.create_table(fail_silently=True)







