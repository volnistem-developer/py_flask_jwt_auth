from src.services.api.use_cases.insert_user import InsertUserUseCase


class MockUserRepository:
    def __init__(self) -> None:
        self.insert_user_attributes = {}

    def insert(self, username, password) -> None:
        self.insert_user_attributes["username"] = username
        self.insert_user_attributes["password"] = password


def test_insert_user():
    repository = MockUserRepository()
    use_case = InsertUserUseCase(repository)

    username = "iurisanches"
    password = "123e4"

    response = use_case.insert(username, password)

    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.insert_user_attributes["username"] == username
    assert repository.insert_user_attributes["password"] is not None
    assert repository.insert_user_attributes["password"] != password
