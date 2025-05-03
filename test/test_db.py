from test.main import db_conn
from src.sql.schema import User

from datetime import datetime

import pytest


# Create Superadmin

@pytest.mark.run(order=1)
def test_create_superuser(db_conn):
    superadmin = User(
        id=1,
        email='admin@gmail.com',
        password='admin123',
        first_name='superuser',
        last_name='admin',
        mobile='1234567890',
        created_at=datetime.now(),
        country_code='91',
        user_type='superadmin',
        user_status='active',
        email_verified=True,
        mobile_verified=True,
        preffered_channel='email',
    )

    db_conn.add(superadmin)
    db_conn.commit()
