from ..dados.repositories.user_repository import UserRepository
from ..infraestrutura.database import db_connection_handler


def test_repository():
    db_connection_handler.connect()
    connection = db_connection_handler.get_connection()

    repository = UserRepository(connection)

    username = "bobesponja"
    password = "123e4"

    repository.insert(username, password)
    user = repository.get_user_by_username(username)

    print(user)
