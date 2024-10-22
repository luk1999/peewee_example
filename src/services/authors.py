from entities import BaseAuthor, BaseAuthorWithBooks
from errors import DoesNotExistError
from models import Author, Book


class AuthorService:
    @staticmethod
    def get_all() -> tuple[BaseAuthor]:
        return tuple(map(BaseAuthor.from_orm, Author.select()))

    @staticmethod
    def get(author_id: int) -> BaseAuthorWithBooks:
        try:
            author = Author.select().join(Book).where(Author.id == author_id).get()
            return BaseAuthorWithBooks.from_orm(author)
        except Author.DoesNotExist:
            raise DoesNotExistError
