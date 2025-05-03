from pydantic import BaseModel

from src.models.warehouse_model import WarehouseMiniGetDetailModel
from src.models.model_util import PaginationModel

from typing import Optional, List


# Util Model

class WarehouseServiceBaseUtilModel(BaseModel):
    first_name: str
    last_name: str
    company_name: Optional[str] = None
    email: str
    mobile: str


# Base Model

class EnquiryBaseModel(BaseModel):
    message: str


class ReserveBaseModel(BaseModel):
    start_date: str
    end_date: str


class TourBaseModel(BaseModel):
    datetime: str


# Get Model

class EnquiryBaseGetModel(EnquiryBaseModel, WarehouseServiceBaseUtilModel):
    customer_id: Optional[str] = None


class EnquiryGetModel(EnquiryBaseGetModel):
    id: str


class EnquiryPaginatedGetModel(PaginationModel):
    data: List[EnquiryGetModel]


class EnquiryGetDetailModel(EnquiryBaseGetModel):
    warehouse: WarehouseMiniGetDetailModel


class ReserveGetModel(ReserveBaseModel, WarehouseServiceBaseUtilModel):
    customer_id: Optional[str] = None
    id: str


class ReservePaginatedGetModel(PaginationModel):
    data: List[ReserveGetModel]


class TourGetModel(TourBaseModel, WarehouseServiceBaseUtilModel):
    customer_id: Optional[str] = None
    id: str


class TourPaginatedGetModel(PaginationModel):
    data: List[TourGetModel]


# Post Models

class EnquiryPostModel(EnquiryBaseModel, WarehouseServiceBaseUtilModel):
    pass


class ReservePostModel(ReserveBaseModel, WarehouseServiceBaseUtilModel):
    pass


class TourPostModel(TourBaseModel, WarehouseServiceBaseUtilModel):
    pass
