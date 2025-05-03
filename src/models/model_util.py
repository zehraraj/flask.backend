from pydantic import BaseModel

from typing import List, Type

import inspect

from fastapi import Form, File
from pydantic import BaseModel
from pydantic.fields import ModelField


def as_form(cls):
    new_parameters = []

    for field_name, model_field in cls.__fields__.items():
        model_field: ModelField  # type: ignore

        print(field_name, '\t\t\t', model_field)
        if not model_field.required:
            new_parameters.append(
                inspect.Parameter(
                    model_field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=Form(model_field.default),
                    annotation=model_field.outer_type_,
                )
            )
        else:
            new_parameters.append(
                inspect.Parameter(
                    model_field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=Form(...),
                    annotation=model_field.outer_type_,
                )
            )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, 'as_form', as_form_func)
    return cls


def as_file(cls):
    new_parameters = []

    for field_name, model_field in cls.__fields__.items():
        model_field: ModelField  # type: ignore

        print(field_name, '\t\t\t', model_field)
        if not model_field.required:
            new_parameters.append(
                inspect.Parameter(
                    model_field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=File(model_field.default),
                    annotation=model_field.outer_type_,
                )
            )
        else:
            new_parameters.append(
                inspect.Parameter(
                    model_field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=File(...),
                    annotation=model_field.outer_type_,
                )
            )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, 'as_form', as_form_func)
    return cls


class DefaultResponseModel(BaseModel):
    detail: str


class PaginationModel(BaseModel):
    total_data: int = 0
    per_page: int = 0
    current_page: int = 1


class DashboardWarehouseRegistrationUtilModel(BaseModel):
    city: str
    state: str
    warehouse: int


class SuperAdminDashboardModel(BaseModel):
    registered_customer: int
    registered_vendor: int
    pending_vendor: int
    listed_warehouse: int
    pending_warehouse: int
    enquiry: int
    reservation: int
    tour: int
    warehouse_registration: List[DashboardWarehouseRegistrationUtilModel]


class VendorDashboardModel(BaseModel):
    warehouse: int


class VerifyModel(BaseModel):
    approve: bool
