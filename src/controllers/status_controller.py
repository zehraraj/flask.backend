from fastapi import APIRouter, Depends

from src.models.model_util import DefaultResponseModel
from src.models.user_model import UserBaseModel


router = APIRouter()


@router.get('/', operation_id='check_status', response_model=DefaultResponseModel)
def check_status():
    '''
    If successful then server is up and if not then some conf error on server side must be present
    '''
    return DefaultResponseModel(detail='OK').dict()
