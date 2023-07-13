from peewee import *
from os import path

#creating our first database
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "sampython.db"))

#creating our table inside db
class Student(Model):
    name = CharField()
    age = IntegerField()
    phonenumber = IntegerField()
    studentcode = IntegerField()
    gender = CharField()


    class Meta:
        database = db
Student.create_table(fail_silently=True)
