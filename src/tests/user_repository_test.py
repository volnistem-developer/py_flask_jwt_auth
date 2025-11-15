from unittest.mock import Mock

from ..dados.repositories.user_repository import UserRepository
from ..infraestrutura.database import db_connection_handler


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_insert_user():
    mock_connection = MockConnection()
    repository = UserRepository(mock_connection)

    repository.insert(username="fred", password="flinstone")

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == ("fred", "flinstone", 0)


def test_edit_balance():
    mock_connection = MockConnection()
    repository = UserRepository(mock_connection)

    repository.edit_balance(user_id=1, new_balance=100.10)

    cursor = mock_connection.cursor.return_value

    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (100.10, 1)

    mock_connection.commit.assert_called_once()


def test_get_user_by_username():
    mock_connection = MockConnection()
    repository = UserRepository(mock_connection)

    repository.get_user_by_username(username="iurivolnistem")

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == ("iurivolnistem",)

    cursor.fetchone.assert_called_once()
