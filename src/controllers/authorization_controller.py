from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session


from src.models.auth_model import AuthLoginModel, AuthLoginResponseModel, LoginType, AuthForgotPasswordModel,\
    AuthResetPasswordModel, AuthRegisterModel, AuthCustomerRegistrationModel, RefreshTokenResponseModel, RefreshTokenModel
from src.models.model_util import DefaultResponseModel
from src.models.user_model import UserGetModel

from src.sql import schema
from src.sql.database import SessionLocal, get_db

from pydantic import BaseModel, validator

from src.util.jwt import jwt_encode


router = APIRouter()


@router.post(
    '/auth/superadmin/{type}',
    operation_id='auth_superadmin_login',
    response_description='Superadmin Login',
    response_model=AuthLoginResponseModel)
def auth_superadmin_login(type: LoginType, body: AuthLoginModel, db: Session = Depends(get_db)):
    '''API endpoint used to login with superadmin type user'''
    user = None

    # Checks if the login type is email or mobile
    if (type == 'email'):
        user = db.query(schema.User).filter(
            schema.User.email == body.login_id, schema.User.password == body.password).first()
    elif (type == 'mobile'):
        user = db.query(schema.User).get(
            mobile=body.login_id, password=body.password)

    return JSONResponse(content=jwt_encode(user=user), status_code=status.HTTP_200_OK)


@router.post(
    '/auth/vendor/{type}',
    operation_id='auth_vendor_login',
    response_description='Vendor Login',
    response_model=AuthLoginResponseModel)
def auth_vendor_login(type: LoginType, body: AuthLoginModel):
    '''API endpoint used to login with vendor type user'''
    pass


@router.post(
    '/auth/vendor',
    operation_id='auth_vendor_registration',
    response_description='Vendor Created. Not Yet Approved.',
    response_model=UserGetModel)
def auth_vendor_registration(body: AuthRegisterModel):
    '''API endpoint used to register vendor type user'''
    pass


@router.post(
    '/auth/customer/{type}',
    operation_id='auth_customer_login',
    response_description='Customer Login',
    response_model=AuthLoginResponseModel)
def auth_customer_login(type: LoginType, body: AuthLoginModel):
    '''API endpoint used to login with customer type user'''
    pass


@router.post(
    '/auth/customer',
    operation_id='auth_customer_registration',
    response_description='Customer Created.',
    response_model=UserGetModel)
def auth_customer_registration(body: AuthCustomerRegistrationModel):
    '''API endpoint used to register customer type user'''
    pass


@router.post(
    '/auth/forgot_password',
    operation_id='auth_forgot_password_post',
    response_description='Email Sent For Validation',
    response_model=DefaultResponseModel)
def auth_forgot_password_post(body: AuthForgotPasswordModel):
    '''API endpoint used to send email for resetting password'''
    pass


@router.post(
    '/auth/reset_password',
    operation_id='auth_reset_password_post',
    response_description='Password Successfully Changed',
    response_model=DefaultResponseModel)
def auth_reset_password_post(body: AuthResetPasswordModel):
    '''API endpoint used to reset password'''
    pass


@router.post(
    '/auth/refresh',
    operation_id='auth_refresh_post',
    response_description='Get A New Access Token',
    response_model=RefreshTokenResponseModel)
def auth_refresh_post(body: RefreshTokenModel):
    '''API endpoint used to refresh access token'''
    pass
