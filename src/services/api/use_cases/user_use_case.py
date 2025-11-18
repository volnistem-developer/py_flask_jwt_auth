from src.interfaces.user_repository_interface import IUserRepository

from ....drivers.password_handler import PasswordHandler


class UserUseCase:
    def __init__(self, repository: IUserRepository) -> None:
        self.__repository = repository
        self.__password_handler = PasswordHandler()

    def insert(self, username: str, password: str) -> dict:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise Exception("Invalid input")

        hashed_password = self.__create_password_hash(password)
        self.__insert_into_db(username, hashed_password)

        return self.__format_response(username)

    def edit(self, user_id: int, new_balance: float) -> dict:
        if not new_balance or not user_id or not isinstance(new_balance, float):
            raise Exception("Invalid input")

        self.__repository.edit_balance(user_id, new_balance)

        return {"type": "User", "count": 1, "new_balance": new_balance}

    def find(self, username: str) -> tuple[int, str, bytes]:
        user = self.__repository.get_user_by_username(username)

        if not user:
            raise Exception("User not found")

        return user

    def __create_password_hash(self, password: str) -> bytes:
        hashed = self.__password_handler.encrypt(password)
        return hashed

    def __insert_into_db(self, username: str, password: bytes) -> None:
        self.__repository.insert(username, str(password))

    def __format_response(self, username: str) -> dict:
        return {"type": "User", "count": 1, "username": username}
