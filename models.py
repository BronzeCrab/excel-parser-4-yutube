from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    DateField,
    IntegerField,
    ForeignKeyField,
)


db = SqliteDatabase("companies.db")


class Company(Model):
    name = CharField(unique=True)

    class Meta:
        database = db


class Foo(Model):
    company = ForeignKeyField(Company)
    data1 = IntegerField()
    data2 = IntegerField()
    date = DateField()

    class Meta:
        database = db


class Bar(Model):
    company = ForeignKeyField(Company)
    data1 = IntegerField()
    data2 = IntegerField()
    date = DateField()

    class Meta:
        database = db
