from fastapi import APIRouter, Depends, status, Form, File, UploadFile

from sqlalchemy.orm import Session

from src.sql.database import get_db, SessionLocal

from src.models.warehouse_model import WarehousePaginatedGetModel, WarehouseCustomerGetDetailModel
from src.models.warehouse_service_model import EnquiryPostModel, TourPostModel, ReservePostModel
from src.models.model_util import DefaultResponseModel

from typing import Optional


router = APIRouter()


@router.get(
    '/anonymouse/warehouse',
    operation_id='anonymouse_warehouse_get',
    response_description='Successful Response. Get a List of Warehouses',
    response_model=WarehousePaginatedGetModel)
def anonymouse_warehouse_get(area: Optional[str] = None, pallets: Optional[str] = None, duration: Optional[str] = None, price: Optional[str] = None, amenity: Optional[str] = None, service: Optional[str] = None, space_type: Optional[str] = None, db: Session = Depends(get_db)):
    '''API endpoint used to get a list of warehouses'''
    pass


@router.get(
    '/anonymous/warehouse/{id}',
    operation_id='anonymous_warehouse_id_get',
    response_description='Successful Response. Requested Warehouse',
    response_model=WarehouseCustomerGetDetailModel)
def anonymous_warehouse_id_get(id: str, db: Session = Depends(get_db)):
    '''API endpoint used to get details of a particular warehouse'''
    pass


@router.post(
    '/anonymous/warehouse/{id}/enquiry',
    operation_id='anonymous_warehouse_id_enquiry',
    response_description='Successful Response. Added Enquiry.',
    response_model=DefaultResponseModel)
def anonymous_warehouse_id_enquiry(id: str, body: EnquiryPostModel, db: Session = Depends(get_db)):
    '''API endpoint used to enquire about the warehouse'''
    pass


@router.post(
    '/anonymous/warehouse/{id}/reserve',
    operation_id='anonymous_warehouse_id_reserve',
    response_description='Successful Response. Added Reservation.',
    response_model=DefaultResponseModel)
def anonymous_warehouse_id_reserve(id: str, body: ReservePostModel, db: Session = Depends(get_db)):
    '''API endpoint used to reserve the warehouse'''
    pass


@router.post(
    '/anonymous/warehouse/{id}/tour',
    operation_id='anonymous_warehouse_id_tour',
    response_description='Successful Response. Added Tour Request.',
    response_model=DefaultResponseModel)
def anonymous_warehouse_id_tour(id: str, body: TourPostModel, db: Session = Depends(get_db)):
    '''API endpoint used to request tour of the warehouse'''
    pass
