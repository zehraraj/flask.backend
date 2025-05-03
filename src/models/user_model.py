from pydantic import BaseModel, validator
from pydantic.dataclasses import dataclass

from src.models._validators import *
from src.models.model_util import PaginationModel
from src.models.company_model import CompanyMiniBaseModel

from src.sql import schema

from typing import List, Optional


# class UserPostModel(BaseModel):
#     email: str
#     password: str

#     '''

#     You can also use the validator function as a decorator
#     @validator('email')
#     def validate_email(cls, email: str):
#         .
#         .
#         .

#     '''
#     validate_email = validator('email', allow_reuse=True)(validate_email)


# Util

class UserPropertyModel(BaseModel):
    id: str
    name: str


class UserBlockModel(BaseModel):
    state: bool


# Base

class UserBaseModel(BaseModel):
    first_name: str
    last_name: str
    company: Optional[CompanyMiniBaseModel] = None
    mobile: str
    email: str
    user_type: schema.UserType
    created_at: str
    status: schema.Status

    # Validation on fields
    # validate_email = validator('email', allow_reuse=True)(validate_email)

    class Config:
        orm_mode = True


# Get

class UserGetModel(UserBaseModel):
    def __init__(self, data):
        super().__init__(
            id=data['id'],
            email=data['email'],
            mobile=data['mobile'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            company=None,
            created_at=data['created_at'],
            user_type=data['user_type'],
            status=data['status'],
        )

    id: str


class UserGetPaginatedModel(PaginationModel):
    data: List[UserGetModel]


class UserGetCustomerDetailModel(UserBaseModel):
    shortlisted: List[UserPropertyModel]
    currently_rented_property: List[UserPropertyModel]
    previously_rented_property: List[UserPropertyModel]


# Post

class UserPostModel(BaseModel):
    first_name: str
    last_name: str
    mobile: str
    email: str
