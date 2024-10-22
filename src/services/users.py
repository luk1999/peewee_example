import hashlib

from pydantic import BaseModel, validator

from entities import BaseUser, BaseUserWithBooks
from enums import UserStatus
from errors import DoesNotExistError
from models import User


MIN_PASS_LEN = 8


def encode_password(password: str) -> str:
    """Just for demo purpose. It should not be used in real-world app!"""
    return hashlib.md5(password.encode()).hexdigest()


class UserError(Exception): ...


class UserCannotBeActivatedError(UserError): ...


class UserCannotBeDisabledError(UserError): ...


class BaseUserCreate(BaseModel):
    username: str
    first_name: str | None = None
    last_name: str | None = None
    password: str

    @validator("password")
    def password_validator(cls, password: str) -> str:
        if not password or len(password) < MIN_PASS_LEN:
            raise ValueError(f"Password must have at least {MIN_PASS_LEN} chars")

        return encode_password(password)

    @validator("username")
    def username_validator(cls, username: str) -> str:
        try:
            User.select().where(User.username == username).get()
            raise ValueError("User already exists")
        except User.DoesNotExist:
            return username


class UserService:
    encode_password = encode_password

    @staticmethod
    def get_all() -> tuple[BaseUser]:
        return tuple(map(BaseUser.from_orm, User.select()))

    @staticmethod
    def get(user_id: int) -> BaseUserWithBooks:
        try:
            user = User.select().where(User.id == user_id).get()
            return BaseUserWithBooks.from_orm(user)
        except User.DoesNotExist:
            raise DoesNotExistError

    @staticmethod
    def add(user: BaseUserCreate) -> BaseUser:
        user = User.create(**dict(user))
        return BaseUser.from_orm(user)

    @staticmethod
    def activate(username: str) -> None:
        if user := User.select().where(User.username**username).first():
            if user.status != UserStatus.inactive:
                raise UserCannotBeActivatedError("User cannot be activated")

            user.status = UserStatus.active
            user.save()
            return

        raise DoesNotExistError

    @staticmethod
    def deactivate(username: str) -> None:
        if user := User.select().where(User.username**username).first():
            if user.status != UserStatus.active:
                raise UserCannotBeDisabledError("User cannot be disabled")

            user.status = UserStatus.disabled
            user.save()
            return

        raise DoesNotExistError
