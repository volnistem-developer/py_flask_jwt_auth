from ..drivers.password_handler import PasswordHandler


def test_password_encrypt():
    handler = PasswordHandler()

    password = "123e4"
    hashed = handler.encrypt(password)
    checked = handler.check(password, hashed)

    assert checked
