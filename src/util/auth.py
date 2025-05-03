from fastapi import Depends
from fastapi.security.http import HTTPBase

from src.util.jwt import jwt_decode


security = HTTPBase(scheme='Bearer')


def fake_decoded_token(user_type):
    return {
        'id': '1',
        'user_type': user_type,
        'created_at': '563678900',
        'status': 'active'
    }


def get_superadmin(token: str = Depends(security)):
    # user = jwt_decode(token.credentials, 'superadmin')
    user = fake_decoded_token('superadmin')
    return user


def get_vendor(token: str = Depends(security)):
    # user = jwt_decode(token, 'vendor')
    user = fake_decoded_token('vendor')
    return user


def get_customer(token: str = Depends(security)):
    # user = jwt_decode(token, 'customer')
    user = fake_decoded_token('customer')
    return user
