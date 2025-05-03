from fastapi import Depends, FastAPI, HTTPException, status

from src.models.user_model import UserBaseModel
from src.models.auth_model import AuthUserModel, AuthLoginResponseModel

from fastapi.security.http import HTTPBase

from pydantic import BaseModel

from typing import Dict

import jwt
import time


JWT_SECRET = 'RAK-SAMA'
JWT_ISSUER = 'com.hubshub.portal'
JWT_ACCESS_LIFETIME_SECONDS = 300000  # 5 min
JWT_REFRESH_LIFETIME_SECONDS = 86400  # 1 day
JWT_ALGORITHM = 'HS256'
JWT_DECODE = 'utf-8'


class JWTPayload(BaseModel):
    iss: str
    iat: int
    exp: int
    token_type: str
    sub: Dict


def jwt_encode(user):
    timestamp = int(time.time())
    user_payload = AuthUserModel(
        id=user.id,
        user_type=user.user_type,
        status=user.user_status,
        created_at=str(user.created_at)).dict()

    access_payload = JWTPayload(
        iss=JWT_ISSUER,
        iat=timestamp,
        exp=timestamp + JWT_ACCESS_LIFETIME_SECONDS,
        token_type='access',
        sub=user_payload).dict()

    refresh_payload = JWTPayload(
        iss=JWT_ISSUER,
        iat=timestamp,
        exp=timestamp + JWT_REFRESH_LIFETIME_SECONDS,
        token_type='refresh',
        sub=user_payload).dict()

    access = jwt.encode(access_payload, JWT_SECRET,
                        algorithm=JWT_ALGORITHM).decode(JWT_DECODE)
    refresh = jwt.encode(refresh_payload, JWT_SECRET,
                         algorithm=JWT_ALGORITHM).decode(JWT_DECODE)

    return AuthLoginResponseModel(access_token=access, refresh_token=refresh).dict()


def jwt_decode(token: bytes, user_type: str):
    print(token)
    try:
        user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if user['status'] == 'active' and user['user_type'] == user_type:
            return user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Not authenticated')
    except jwt.exceptions.DecodeError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Token')


def jwt_refresh(token: str):
    user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

    timestamp = int(time.time())

    payload = JWTPayload(
        iss=JWT_ISSUER,
        iat=timestamp,
        exp=timestamp + JWT_ACCESS_LIFETIME_SECONDS,
        token_type='access',
        sub=user
    ).to_dict()

    return jwt.encode(access_payload, JWT_SECRET,
                      algorithm=JWT_ALGORITHM).decode(JWT_DECODE)
