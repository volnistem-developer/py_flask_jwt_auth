from src.services.api.use_cases.insert_user import InsertUserUseCase

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.controller_base_interface import IControllerBase


class CreateUserController(IControllerBase):
    def __init__(self, use_case: InsertUserUseCase) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")

        self.__validate_input(username, password)

        response = self.__use_case.insert(username, password)

        return HttpResponse(body={"data": response}, status_code=201)

    def __validate_input(self, username: any, password: any) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise Exception("Invalid input")
