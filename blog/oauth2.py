from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwttoken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate Credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return jwttoken.verify_token(token, credentials_exception)
