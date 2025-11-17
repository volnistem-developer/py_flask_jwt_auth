import pytest

from src.drivers.password_handler import PasswordHandler
from src.services.api.use_cases.login_creator import LoginCreatorUseCase

username = "iurivolnistem"
password = "123e4"
hashed_password = PasswordHandler().encrypt(password)


class MockUserRepository:
    def get_user_by_username(self, username):
        return (10, username, hashed_password)


def test_create():
    login_creator = LoginCreatorUseCase(MockUserRepository())
    response = login_creator.create(username, password)

    assert response["access"]
    assert response["username"] == username
    assert response["token"] is not None


def test_create_with_wrong_password():
    login_creator = LoginCreatorUseCase(MockUserRepository())

    with pytest.raises(Exception):
        login_creator.create(username, "outrasenha")
