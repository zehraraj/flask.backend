from pydantic import BaseModel

from src.models.model_util import PaginationModel

from typing import List


class CompanyMiniBaseModel(BaseModel):
    company_name: str
    id: str


class CompanyBaseModel(BaseModel):
    company_name: str
    company_cin: str
    gstin: str
    email: str
    mobile: str
    pan: str


class CompanyBaseGetModel(CompanyBaseModel):
    created_at: str


class CompanyGetModel(CompanyBaseGetModel):
    id: str


class CompanyPaginatedGetModel(PaginationModel):
    data: List[CompanyGetModel]
