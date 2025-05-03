from test.main import client

from src.models.model_util import DefaultResponseModel


def test_get_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == DefaultResponseModel(detail='OK').dict()
