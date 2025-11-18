from src.services.api.use_cases.balance_editor import BalanceEditorUseCase

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.controller_base_interface import IControllerBase


class BalaceEditorController(IControllerBase):
    def __init__(self, use_case: BalanceEditorUseCase) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        user_id = http_request.params.get("user_id")

        self.__validate_input(new_balance, user_id)

        response = self.__use_case.edit(user_id, new_balance)

        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_input(self, new_balance: any, user_id: any) -> None:
        if not new_balance or not user_id or not isinstance(new_balance, float):
            raise Exception("Invalid input")
