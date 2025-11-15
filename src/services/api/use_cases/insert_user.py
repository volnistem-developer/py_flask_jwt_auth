from src.interfaces.user_repository_interface import IUserRepository

from ....drivers.password_handler import PasswordHandler


class InsertUserUseCase:
    def __init__(self, repository: IUserRepository) -> None:
        self.__repository = repository
        self.__password_handler = PasswordHandler()

    def insert(self, username: str, password: str) -> dict:
        hashed_password = self.__create_password_hash(password)
        self.__insert_into_db(username, hashed_password)

        return self.__format_response(username)

    def __create_password_hash(self, password: str) -> bytes:
        hashed = self.__password_handler.encrypt(password)
        return hashed

    def __insert_into_db(self, username: str, password: bytes) -> None:
        self.__repository.insert(username, str(password))

    def __format_response(self, username: str) -> dict:
        return {"type": "User", "count": 1, "username": username}
