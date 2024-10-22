from entities import BaseBook, BaseBookWithAuthor
from errors import DoesNotExistError
from models import Author, Book


class BookService:
    @staticmethod
    def get_all() -> tuple[BaseBook]:
        return tuple(map(BaseBook.from_orm, Book.select()))

    @staticmethod
    def get(book_id: int) -> BaseBookWithAuthor:
        try:
            book = Book.select().join(Author).where(Book.id == book_id).get()
            return BaseBookWithAuthor.from_orm(book)
        except Book.DoesNotExist:
            raise DoesNotExistError
