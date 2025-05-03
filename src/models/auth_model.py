from pydantic import BaseModel, validator

from src.models._validators import *
from src.models.user_model import CompanyMiniBaseModel

from src.sql import schema

import enum


# Enum

class LoginType(str, enum.Enum):
    email: str = 'email'
    mobile: str = 'mobile'


# Util

class AuthRegisterCompanyModel(BaseModel):
    company_name: str
    registration_no: str
    gst_no: str


class AuthUserModel(BaseModel):
    id: str
    user_type: schema.UserType
    created_at: str
    status: schema.Status


# Post Model

class AuthForgotPasswordModel(BaseModel):
    email: str

    _email = validator('email', allow_reuse=True)(validate_email)


class AuthLoginModel(BaseModel):
    login_id: str
    password: str


class AuthRegisterModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    mobile: str
    password: str
    company: AuthRegisterCompanyModel


class AuthCustomerRegistrationModel(AuthRegisterModel):
    company: str


class AuthResetPasswordModel(BaseModel):
    password: str
    token: str


class RefreshTokenModel(BaseModel):
    refresh_token: str


# Response Model

class AuthLoginResponseModel(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenResponseModel(BaseModel):
    access_token: str
