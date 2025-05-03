from fastapi import Form, File, UploadFile
from pydantic import BaseModel
from typing import List, Optional, Any
from pathlib import Path

from src.models.model_util import PaginationModel, as_form, as_file
from src.models.user_model import UserBaseModel
from src.models.company_model import CompanyMiniBaseModel

# Extra Util


class WarehouseMiniLocationModel(BaseModel):
    country: str
    state: str
    city: str
    pincode: str


class WarehouseLocationModel(WarehouseMiniLocationModel):
    address: str
    latitude: str
    longitude: str


class WarehouseImageModel(BaseModel):
    file: Path
    description: str


class WarehousePostImageModel(BaseModel):
    file: UploadFile = File(...)
    description: str = Form(...)


class WarehouseLocalityModel(BaseModel):
    id: str
    name: str
    distance: int


class WarehouseAddonServiceModel(BaseModel):
    id: str
    name: str


class WarehouseIndustryTagModel(BaseModel):
    id: str
    name: str


class WarehouseAmenityModel(BaseModel):
    id: str
    name: str


class WarehouseTenantModel(BaseModel):
    first_name: str
    last_name: str
    company: CompanyMiniBaseModel
    mobile: str
    email: str
    country: str
    city: str
    pincode: str


class WarehouseHistoryModel(BaseModel):
    previous: Optional[WarehouseTenantModel] = None
    current: Optional[WarehouseTenantModel] = None


class WarehouseGetUtilModel(BaseModel):
    is_approved: bool
    is_verified: bool


class WarehouseSuperAdminUpdateModel(BaseModel):
    hubshub_rate: int


class WarehouseShortlistModel(BaseModel):
    id: str


class WarehouseContactModel(BaseModel):
    company_name: str
    owner: str
    city: str
    country: str
    email: str
    mobile: str


# Base Models

class WarehouseBaseModel(BaseModel):
    name: str
    license_no: str
    area: int
    area_rate: int
    pallets: int
    pallets_rate: int
    available_from: str
    available_to: str


class WarehouseIdModel(BaseModel):
    warehouse_version_id: str
    id: str


# Get Models

class WarehouseGetModel(WarehouseBaseModel, WarehouseIdModel):
    location: WarehouseMiniLocationModel


class WarehousePaginatedGetModel(PaginationModel):
    data: List[WarehouseGetModel]


class WarehouseMiniBaseDetailModel(WarehouseBaseModel):
    images: List[WarehouseImageModel]
    location: WarehouseLocationModel


class WarehouseMiniGetDetailModel(WarehouseMiniBaseDetailModel, WarehouseIdModel):
    pass


class WarehouseBaseDetailModel(WarehouseMiniBaseDetailModel):
    description: str
    locality: List[WarehouseLocalityModel]
    industry_tag: List[WarehouseIndustryTagModel]
    amenity: List[WarehouseAmenityModel]
    addon_service: List[WarehouseAddonServiceModel]


class WarehouseGetDetailModel(WarehouseBaseDetailModel, WarehouseIdModel):
    certificate: List[Path]
    company: WarehouseContactModel
    history: Optional[WarehouseHistoryModel] = None


class WarehouseCustomerGetDetailModel(WarehouseBaseDetailModel, WarehouseIdModel):
    certificate: List[Path]


class WarehouseGetRentedModel(WarehouseBaseModel, WarehouseIdModel):
    rented_from: str
    rented_to: str
    total_cost: int
    area_utilization: int
    pallets_utilization: int


class WarehouseVendorGetModel(WarehouseBaseModel, WarehouseIdModel):
    location: WarehouseLocationModel
    area_utilization: int
    pallets_utilization: int


class WarehousePaginatedVendorGetModel(PaginationModel):
    data: List[WarehouseVendorGetModel]


class WarehousePaginatedGetRentedModel(PaginationModel):
    data: List[WarehouseGetRentedModel]


# Post

class WarehousePostBaseModel(WarehouseBaseModel):
    location: WarehouseLocationModel
    description: str
    locality: WarehouseLocalityModel
    amenity: WarehouseAmenityModel
    addon_service: WarehouseAddonServiceModel
    industry_tag: WarehouseIndustryTagModel
