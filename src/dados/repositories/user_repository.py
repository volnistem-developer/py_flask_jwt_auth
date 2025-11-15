from sqlite3 import Connection

from src.interfaces.user_repository_interface import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def insert(self, username: str, password: str) -> None:
        cursor = self.__connection.cursor()

        cursor.execute(
            """INSERT INTO users
                (username, password, balance)
            VALUES
                (?,?,?)""",
            (username, password, 0),
        )

        self.__connection.commit()

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
            UPDATE users
            SET balance = ?
            WHERE id = ?
            """,
            (new_balance, user_id),
        )

        self.__connection.commit()

    def get_user_by_username(self, username: str) -> tuple[int, str, str]:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
            SELECT id, username, password
            FROM users
            WHERE username = ?
            """,
            (username,),
        )
        user = cursor.fetchone()
        return user
