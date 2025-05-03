from fastapi import APIRouter, Depends, status, Form, File, UploadFile

from sqlalchemy.orm import Session

from src.sql.database import get_db, SessionLocal

from src.models.warehouse_model import WarehousePaginatedGetModel, WarehouseCustomerGetDetailModel, WarehouseShortlistModel
from src.models.warehouse_service_model import EnquiryBaseModel, ReserveBaseModel, TourBaseModel
from src.models.model_util import DefaultResponseModel


from typing import Optional

router = APIRouter()


@router.get(
    '/customer/warehouse',
    operation_id='customer_warehouse_get',
    response_description='Successful Response. Get a List of Warehouses',
    response_model=WarehousePaginatedGetModel)
def customer_warehouse_get(area: Optional[str] = None, pallets: Optional[str] = None, duration: Optional[str] = None, price: Optional[str] = None, amenity: Optional[str] = None, service: Optional[str] = None, space_type: Optional[str] = None, db: Session = Depends(get_db)):
    '''API endpoint used to get a list of warehouses'''
    pass


@router.get(
    '/customer/warehouse/{id}',
    operation_id='customer_warehouse_id_get',
    response_description='Successful Response. Requested Warehouse',
    response_model=WarehouseCustomerGetDetailModel)
def customer_warehouse_id_get(id: str, db: Session = Depends(get_db)):
    '''API endpoint used to get details of a particular warehouse'''
    pass


@router.put(
    '/customer/warehouse/{id}',
    operation_id='customer_warehouse_id_put',
    response_description='Successful Response. Shortlisted.',
    response_model=DefaultResponseModel)
def customer_warehouse_id_put(id: str, body: WarehouseShortlistModel, db: Session = Depends(get_db)):
    '''API endpoint used to shortlist the warehouse'''
    pass


@router.post(
    '/customer/warehouse/{id}/enquiry',
    operation_id='customer_warehouse_id_enquiry',
    response_description='Successful Response. Added Enquiry.',
    response_model=DefaultResponseModel)
def customer_warehouse_id_enquiry(id: str, body: EnquiryBaseModel, db: Session = Depends(get_db)):
    '''API endpoint used to enquire about the warehouse'''
    pass


@router.post(
    '/customer/warehouse/{id}/reserve',
    operation_id='customer_warehouse_id_reserve',
    response_description='Successful Response. Added Reservation.',
    response_model=DefaultResponseModel)
def customer_warehouse_id_reserve(id: str, body: ReserveBaseModel, db: Session = Depends(get_db)):
    '''API endpoint used to reserve the warehouse'''
    pass


@router.post(
    '/customer/warehouse/{id}/tour',
    operation_id='customer_warehouse_id_tour',
    response_description='Successful Response. Added Tour Request.',
    response_model=DefaultResponseModel)
def customer_warehouse_id_tour(id: str, body: TourBaseModel, db: Session = Depends(get_db)):
    '''API endpoint used to request tour of the warehouse'''
    pass
