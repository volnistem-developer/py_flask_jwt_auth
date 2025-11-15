import bcrypt as bc


class PasswordHandler:
    def encrypt(self, password: str) -> bytes:
        salt = bc.gensalt()
        hashed = bc.hashpw(password.encode("utf-8"), salt)

        return hashed

    def check(self, password: str, hashed: bytes) -> bool:
        return bc.checkpw(password.encode("utf-8"), hashed)
