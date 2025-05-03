from fastapi import APIRouter, Depends, status, Form, File, UploadFile

from sqlalchemy.orm import Session

from src.sql.database import get_db, SessionLocal

from src.models.model_util import VendorDashboardModel, DefaultResponseModel
from src.models.enum_util import WarehouseState
from src.models.warehouse_model import WarehousePostImageModel, WarehousePaginatedVendorGetModel, \
    WarehousePaginatedGetModel, WarehouseGetDetailModel, WarehouseGetModel, WarehousePostBaseModel

from typing import List, Dict, Optional

router = APIRouter()


@router.get(
    '/vendor/warehouse',
    operation_id='vendor_warehouse_get',
    response_description='Successful Response. Get a List of Warehouses',
    response_model=WarehousePaginatedVendorGetModel)
def vendor_warehouse_get(state: Optional[WarehouseState] = None, db: Session = Depends(get_db)):
    '''API endpoint used to get a list of warehouses'''
    pass


@router.post(
    '/vendor/warehouse',
    operation_id='vendor_warehouse_post',
    response_description='Warehouse Created',
    response_model=WarehouseGetModel)
def vendor_warehouse_post(body: WarehousePostBaseModel, db: Session = Depends(get_db)):
    '''
    API endpoint used to register a new warehouse.  \n
    Use /vendor/warehouse/{id} PUT endpoint to add images and certificates
    '''
    pass


@router.put(
    '/vendor/warehouse/{id}',
    operation_id='vendor_warehouse_id_put',
    response_description='Images And Certificates Added',
    response_model=DefaultResponseModel)
def vendor_warehouse_id_put(id: str, images: List[UploadFile] = File(...), certificates: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    '''
    API endpoint used to add images and certificates to a warehouse record.
    For the images field change the name of the file since that name will be used in view warehouse details.
    '''
    pass


@router.post(
    '/vendor/warehouse/{id}',
    operation_id='vendor_warehouse_id_post',
    response_description='Warehouse Updated',
    response_model=WarehouseGetModel)
def vendor_warehouse_id_post(id: str, body: WarehousePostBaseModel, db: Session = Depends(get_db)):
    '''
    API endpoint used to update existing warehouse. \n
    Use /vendor/warehouse/{id} PUT endpoint to update images and certificates
    '''
    pass


@router.get(
    '/vendor/warehouse/{id}',
    operation_id='vendor_warehouse_id_get',
    response_description='Successful Response. Requested Warehouse',
    response_model=WarehouseGetDetailModel)
def vendor_warehouse_id_get(id: str, db: Session = Depends(get_db)):
    '''API endpoint used to get details of a particular warehouse'''
    pass


@router.get(
    '/vendor/statistics',
    operation_id='vendor_statistics_get',
    response_description='Successful Response',
    response_model=VendorDashboardModel)
def vendor_statistics_get(db: Session = Depends(get_db)):
    '''API endpoint used to get the stats data for vendor dashboard'''
    pass
