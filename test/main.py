from fastapi.testclient import TestClient
from fastapi import Depends

from src.main import server
from src.sql.schema import User
from src.sql.database import get_db, get_test_db

from sqlalchemy.orm import Session

from datetime import datetime

import pytest
import os


client = TestClient(server)


@pytest.fixture(scope='session', autouse=True)
def db_conn():
    '''
    This function provides the test database session
    '''
    # Will be executed before the first test
    conn = get_test_db()
    yield conn

    # Will be executed after the last test
    conn.close()
