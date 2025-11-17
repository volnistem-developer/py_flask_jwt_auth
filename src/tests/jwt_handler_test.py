from src.drivers.jwt_handler import JWTHandler


def test_jwt_handler():
    handler = JWTHandler()
    body = {
        'username': 'iurivolnistem',
        'role': 'admin'
    }

    token = handler.create_token(body)
    token_info = handler.decode_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_info['username'] == body['username']
    assert token_info['role'] == body['role']