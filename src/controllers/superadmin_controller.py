from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.models.user_model import UserGetPaginatedModel, UserGetCustomerDetailModel, UserBlockModel, UserGetModel, UserPostModel
from src.models.warehouse_model import WarehousePaginatedGetModel, WarehouseGetDetailModel, \
    WarehousePaginatedGetRentedModel, WarehouseMiniLocationModel, WarehouseGetModel, WarehouseSuperAdminUpdateModel
from src.models.warehouse_service_model import EnquiryPaginatedGetModel, EnquiryGetDetailModel, \
    ReservePaginatedGetModel, TourPaginatedGetModel
from src.models.enum_util import BooleanEnum, WarehouseState
from src.models.model_util import SuperAdminDashboardModel, DefaultResponseModel, VerifyModel
from src.models.company_model import CompanyPaginatedGetModel, CompanyBaseGetModel, CompanyBaseModel, CompanyGetModel, CompanyMiniBaseModel
from src.models.auth_model import AuthUserModel

from src.sql.database import SessionLocal, get_db
from src.sql import schema

from src.util.auth import get_superadmin

from typing import Optional, Union

from datetime import datetime


router = APIRouter()


@router.get(
    '/superadmin/profile',
    operation_id='superadmin_profile_get',
    response_description='Successful Response',
    response_model=UserGetModel)
def superadmin_profile_get(user: AuthUserModel = Depends(get_superadmin), db: Session = Depends(get_db)):
    '''API endpoint used to get user profile'''
    _user = db.query(schema.User).get(user['id'])

    response = UserGetModel({
        "id": _user.id,
        "first_name": _user.first_name,
        "last_name": _user.last_name,
        "company": None,
        "mobile": _user.mobile,
        "email": _user.email,
        "user_type": _user.user_type,
        "created_at": str(datetime.timestamp(datetime.now())),
        "status": _user.user_status
    }).dict()

    return JSONResponse(content=response, status_code=200)


@router.post(
    '/superadmin/profile',
    operation_id='superadmin_profile_post',
    response_description='Profile Updated',
    response_model=UserGetModel)
def superadmin_profile_post(body: UserPostModel, db: Session = Depends(get_db)):
    '''API endpoint used to update user profile'''
    pass


@router.get(
    '/superadmin/warehouse',
    operation_id='superadmin_warehouse_get',
    response_description='Successful Response. Get A List Of Warehouses',
    response_model=WarehousePaginatedGetModel)
def superadmin_warehouse_get(state: Optional[WarehouseState] = None, db: Session = Depends(get_db)):
    '''API endpoint used to get a list of warehouses'''
    # return JSONResponse(WarehousePaginatedGetModel(
    #     total_data=0,
    #     per_page=0,
    #     current_page=0,
    #     data=[WarehouseGetModel(
    #         available_from="string",
    #         available_to="string",
    #         is_approved=True,
    #         is_verified=True,
    #         name="string",
    #         license_no="string",
    #         area=0,
    #         area_rate=0,
    #         pallets=0,
    #         pallets_rate=0,
    #         warehouse_version_id="string",
    #         id="string",
    #         location=WarehouseMiniLocationModel(
    #             country="string",
    #             state="string",
    #             city="string",
    #             pincode="string"
    #         )
    #     )]
    # ).dict(), status.HTTP_200_OK)
    pass


@router.get(
    '/superadmin/warehouse/rented',
    operation_id='superadmin_rented_warehouse_get',
    response_description='Successful Response. Get A List Of Rented Warehouses',
    response_model=WarehousePaginatedGetRentedModel)
def superadmin_rented_warehouse_get(db: Session = Depends(get_db)):
    '''API endpoint used to get a list of rented warehouses'''
    pass


@router.get(
    '/superadmin/warehouse/{id}',
    operation_id='superadmin_warehouse_id_get',
    response_description='Successful Response. Requested Warehouses',
    response_model=WarehouseGetDetailModel)
def superadmin_warehouse_id_get(id: str, db: Session = Depends(get_db)):
    '''API endpoint used to get details of a particular warehouse'''
    pass


@router.post(
    '/superadmin/warehouse/{id}',
    operation_id='superadmin_warehouse_id_post',
    response_description='Successful Response. Warehouse Updated',
    response_model=WarehouseGetModel)
def superadmin_warehouse_id_post(id: str, body: WarehouseSuperAdminUpdateModel, db: Session = Depends(get_db)):
    '''API endpoint used to get details of a particular warehouse'''
    pass


@router.post(
    '/superadmin/warehouse/{id}/verify',
    operation_id='superadmin_warehouse_id_verify',
    response_description='Successful Response',
    response_model=DefaultResponseModel)
def superadmin_warehouse_id_verify(id: str, body: VerifyModel, db: Session = Depends(get_db)):
    '''API endpoint used to approve/reject of pending warehouses'''
    pass


@router.get(
    '/superadmin/user',
    operation_id='superadmin_user_get',
    response_description='Successful Response. List of Users',
    response_model=UserGetPaginatedModel)
def superadmin_user_get(
        type: Optional[schema.UserType] = None,
        name: Optional[str] = None, company_name: Optional[str] = None,
        company_cin: Optional[str] = None, db: Session = Depends(get_db)):
    '''API endpoint used to get a list of users that are present in system. 
    If type is specified then only users that are of that same user_type will be returned'''

    if (type):
        if (type == 'superadmin'):
            print('superadmin')
        elif (type == 'manager'):
            print('manager')
        elif (type == 'account_manager'):
            print('account_manager')
        elif (type == 'vendor'):
            print('vendor')
        pass
    pass


@router.get(
    '/superadmin/user/{id}',
    operation_id='superadmin_user_id_get',
    response_description='Successful Response. Requested User',
    response_model=UserGetCustomerDetailModel)
def superadmin_user_id_get(id: str, db: Session = Depends(get_db)):
    ''' 
    API endpoint used to get details of particular user.
    Only Returns Customer Type User Data Since There Is no Page For Vendor Details (as of 22-07-2020)
    '''
    pass


@router.post(
    '/superadmin/user/{id}/verify',
    operation_id='superadmin_user_id_verify',
    response_description='Successful Response',
    response_model=DefaultResponseModel)
def superadmin_user_id_verify(id: str, body: VerifyModel, db: Session = Depends(get_db)):
    '''API Endpoint used for approve/reject of pending owners'''
    pass


@router.put(
    '/superadmin/user/{id}',
    operation_id='superadmin_user_id',
    response_description='Successful Response. User is blocked/unblocked according to the state given',
    response_model=DefaultResponseModel)
def superadmin_user_id_put(id: str, body: UserBlockModel, db: Session = Depends(get_db)):
    '''API Endpoint used for blocking/un-blocking users'''
    pass


@router.get(
    '/superadmin/enquiry',
    operation_id='superadmin_enquiry_get',
    response_description='Successful Response. List of Enquiries',
    response_model=EnquiryPaginatedGetModel)
def superadmin_enquiry_get(db: Session = Depends(get_db)):
    '''API endpoint used to get list of enquiry'''
    pass


@router.get(
    '/superadmin/enquiry/{id}',
    operation_id='superadmin_enquiry_id_get',
    response_description='Successful Response. Requested Enquiry',
    response_model=EnquiryGetDetailModel)
def superadmin_enquiry_id_get(id: str, db: Session = Depends(get_db)):
    '''API endpoint used to get the details of a particular enquiry'''
    pass


@router.get(
    '/superadmin/reserve',
    operation_id='superadmin_reserve_get',
    response_description='Successful Response. List of Reserved Warehouses',
    response_model=ReservePaginatedGetModel)
def superadmin_reserve_get(db: Session = Depends(get_db)):
    '''API endpoint used to get a list of warehouse reservations'''
    pass


@router.post(
    '/superadmin/reserve/{id}/verify',
    operation_id='superadmin_reserve_id_verify',
    response_description='Successful Response',
    response_model=DefaultResponseModel)
def superadmin_reserve_id_verify(id: str, body: VerifyModel, db: Session = Depends(get_db)):
    '''API endpoint used to approve/reject of reservations that are made'''
    pass


@router.get(
    '/superadmin/tour',
    operation_id='superadmin_tour_get',
    response_description='Successful Response. List of Tours',
    response_model=TourPaginatedGetModel)
def superadmin_tour_get(db: Session = Depends(get_db)):
    '''API endpoint used to get a list of all tours'''
    pass


@router.post(
    '/superadmin/tour/{id}/verify',
    operation_id='superadmin_tour_id_verify',
    response_description='Successful Response',
    response_model=DefaultResponseModel)
def superadmin_tour_id_verify(id: str, body: VerifyModel, db: Session = Depends(get_db)):
    '''API endpoint used to approve/reject of tour that are requested'''
    pass


@router.get(
    '/superadmin/statistics',
    operation_id='superadmin_statistics_get',
    response_description='Successful Response.',
    response_model=SuperAdminDashboardModel)
def superadmin_statistics_get(db: Session = Depends(get_db)):
    '''API endpoint used to get the stats data for superadmin dashboard'''
    pass


@router.get(
    '/superadmin/company',
    operation_id='superadmin_company_get',
    response_description='Successful Response.',
    response_model=CompanyPaginatedGetModel)
def superadmin_company_get(db: Session = Depends(get_db)):
    '''API endpoint used to get a list of companies'''
    pass


@router.get(
    '/superadmin/company/{id}',
    operation_id='superadmin_company_id_get',
    response_description='Successful Response.',
    response_model=CompanyBaseGetModel)
def superadmin_company_id_get(id: str, db: Session = Depends(get_db)):
    '''API endpoint used to get a particular company'''
    pass


@router.post(
    '/superadmin/company',
    operation_id='superadmin_company_post',
    response_description='Company Created',
    response_model=CompanyGetModel)
def superadmin_company_post(body: CompanyBaseModel, db: Session = Depends(get_db)):
    '''API endpoint used to get create a register a new company'''
    pass


@router.post(
    '/superadmin/company/{id}',
    operation_id='superadmin_company_id_post',
    response_description='Company Update',
    response_model=CompanyGetModel)
def superadmin_company_id_post(id: str, body: CompanyBaseModel, db: Session = Depends(get_db)):
    '''API endpoint used to update existing company'''
    pass
