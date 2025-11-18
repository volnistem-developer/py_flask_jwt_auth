from src.interfaces.user_repository_interface import IUserRepository


class BalanceEditor:
    def __init__(self, repository: IUserRepository) -> None:
        self.__repository = repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__repository.edit_balance(user_id, new_balance)

        return {"type": "User", "count": 1, "new_balance": new_balance}
