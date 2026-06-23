from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request, status
from .utils import decode_token
from fastapi.exceptions import HTTPException


class AccessTokenBearer(HTTPBearer):

    def __init__(self, auto_error =True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds =  await super().__call__(request)
        token = creds.credentials
        token_data = decode_token(token)

        if not self.token_valid:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid/expired token")

        if token_data is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )

        if token_data.get("refresh"):
            raise HTTPException(
                status_code=401,
                detail="Access token required"
            )

        return token_data

    def token_valid(self, token: str) -> bool:

        token_data = decode_token(token)

        return True if token_data is not None else False
