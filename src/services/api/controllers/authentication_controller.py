from src.services.api.use_cases.authentication_use_case import AuthenticationUseCase

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class AuthenticationController:
    def __init__(self, use_case: AuthenticationUseCase) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")

        response = self.__use_case.create(username, password)
        return HttpResponse(body={"data": response}, status_code=200)
