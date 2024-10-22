from peewee import CharField, DateField, ForeignKeyField, IntegerField, ManyToManyField, Model, SqliteDatabase

import config
from enums import UserStatus

db = SqliteDatabase(**config.DATABASE)


class Author(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    date_of_birth = DateField()

    class Meta:
        database = db
        indexes = (
            # Composite unq key
            (("first_name", "last_name", "date_of_birth"), True),
        )


class Book(Model):
    author = ForeignKeyField(Author, backref="books")
    title = CharField(max_length=100)
    year = IntegerField()
    genre = CharField(max_length=30)

    class Meta:
        database = db
        indexes = ((("author", "title"), True),)  # Composite unq key


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=32)
    first_name = CharField(max_length=100, null=True)
    last_name = CharField(max_length=100, null=True)
    status = CharField(max_length=30, default=UserStatus.inactive.value)
    books = ManyToManyField(Book, backref="users")

    class Meta:
        database = db


UserBook = User.books.get_through_model()


db.connect()
db.create_tables([Author, Book, User, UserBook])
