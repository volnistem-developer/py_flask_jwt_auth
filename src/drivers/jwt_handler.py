from datetime import datetime, timedelta, timezone

import jwt

from src.configs.jwt_config import jwt_infos


class JWTHandler:
    def create_token(self, body: dict) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc)
                + timedelta(hours=int(jwt_infos["JWT_HOURS"])),
                **body,
            },
            key=jwt_infos["KEY"],
            algorithm=jwt_infos["ALGORITHM"],
        )
        return token

    def decode_token(self, token: str) -> dict:
        token_information = jwt.decode(
            token, key=jwt_infos["KEY"], algorithms=jwt_infos["ALGORITHM"]
        )

        return token_information
