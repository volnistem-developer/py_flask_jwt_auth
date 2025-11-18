from ..use_cases.user_use_case import UserUseCase
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class UserController:
    def __init__(self, use_case: UserUseCase) -> None:
        self.__use_case = use_case

    def insert(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")

        response = self.__use_case.insert(username, password)

        return HttpResponse(body={"data": response}, status_code=201)

    def edit(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        user_id = http_request.params.get("user_id")

        response = self.__use_case.edit(user_id, new_balance)
        return HttpResponse(body={"data": response}, status_code=200)
