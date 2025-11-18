import pytest

from src.services.api.controllers.create_user_controller import CreateUserController

from ..services.api.controllers.http_types.http_request import HttpRequest
from ..services.api.controllers.http_types.http_response import HttpResponse


class MockUseCase:
    def insert(self, username, password):
        return {"message": "something"}


def test_handle_create_user():
    body = {"username": "iurisanches", "password": "123e444"}

    request = HttpRequest(body)
    use_case = MockUseCase()
    controller = CreateUserController(use_case)

    response = controller.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {"data": {"message": "something"}}
    assert response.status_code == 201


def test_handle_create_user_with_validation_error():
    body = {"password": "123e444"}

    request = HttpRequest(body)
    use_case = MockUseCase()
    controller = CreateUserController(use_case)

    with pytest.raises(Exception):
        controller.handle(request)
