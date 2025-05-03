from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

import os

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"
#SQLALCHEMY_DATABASE_URL = "mysql://admin:admin@db/hubshub"

SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

if (SQLALCHEMY_DATABASE_URL.split(':')[0] == 'mysql'):
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                           "check_same_thread": False})

SessionLocal = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_test_db():
    return SessionLocal()
