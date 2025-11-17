from src.drivers.jwt_handler import JWTHandler
from src.drivers.password_handler import PasswordHandler
from src.interfaces.user_repository_interface import IUserRepository


class LoginCreatorUseCase:
    def __init__(self, repository: IUserRepository) -> None:
        self.__repository = repository
        self.__jwt_handler = JWTHandler()
        self.__password_handler = PasswordHandler()

    def create(self, username: str, password: str) -> dict:
        user = self.__find_user(username)
        user_id = user[0]

        hashed = user[2]

        self.__verify_correct_password(password, hashed)
        token = self.__create_jwt_token(user_id)

        return self.__format_response(username, token)

    def __find_user(self, username: str) -> tuple[int, str, bytes]:
        user = self.__repository.get_user_by_username(username)

        if not user:
            raise Exception("User not found")

        return user

    def __verify_correct_password(self, password: str, hashed_password: bytes) -> None:
        is_password_correct = self.__password_handler.check(password, hashed_password)

        if not is_password_correct:
            raise Exception("Wrong Password")

    def __create_jwt_token(self, user_id: int) -> str:
        payload = {"user_id": user_id}
        token = self.__jwt_handler.create_token(payload)
        return token

    def __format_response(self, username: str, token: str) -> dict:
        return {"access": True, "username": username, "token": token}
