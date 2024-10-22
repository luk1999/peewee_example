from datetime import date

from enums import Genre, UserStatus
from models import Author, Book, User
from services.users import UserService


def init_data():
    clarke = Author.create(first_name="Arthur Charles", last_name="Clarke", date_of_birth=date(1917, 12, 16))
    king = Author.create(first_name="Stephen", last_name="King", date_of_birth=date(1947, 9, 21))
    grisham = Author.create(first_name="John", last_name="Grisham", date_of_birth=date(1955, 2, 8))

    Book.create(author=clarke, title="2001: A Space Odyssey", year=1968, genre=Genre.sci_fi)
    Book.create(author=king, title="It", year=1986, genre=Genre.horror)
    Book.create(author=king, title="The Shining", year=1977, genre=Genre.horror)
    gunslinger = Book.create(author=king, title="The Gunslinger", year=1982, genre=Genre.fantasy)
    pelican = Book.create(author=grisham, title="The Pelican Brief", year=1992, genre=Genre.thriller)
    rainmaker = Book.create(author=grisham, title="The Rainmaker", year=1995, genre=Genre.thriller)

    smith = User.create(
        username="john_smith",
        password=UserService.encode_password("12345678"),
        first_name="John",
        last_name="Smith",
        status=UserStatus.active,
    )
    smith.books.add(
        [
            rainmaker,
            gunslinger,
        ]
    )
    rambo = User.create(
        username="rambo",
        password=UserService.encode_password("abcdefgh"),
        status=UserStatus.active,
    )
    rambo.books.add(pelican)
    smith = User.create(
        username="test_account",
        password=UserService.encode_password("abcd1234"),
        first_name="Test",
        last_name="Account",
        status=UserStatus.disabled,
    )


if __name__ == "__main__":
    print("Initializing db tables and data...")
    init_data()
    print("Done.")
