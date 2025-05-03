from test.main import client

from src.models.user_model import UserGetModel
from src.models import auth_model

import pytest


@pytest.mark.run(order=2)
def test_superadmin_login():
    response = client.post("/auth/superadmin/email", json={
        "login_id": "admin@gmail.com",
        "password": "admin123"
    })

    assert response.status_code == 200
    # assert response.json() == auth_model.AuthLoginResponseModel
