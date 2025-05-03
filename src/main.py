from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers import status_controller, superadmin_controller, authorization_controller, \
    vendor_controller, customer_controller, anonymous_controller
from src.sql import schema
from src.sql.database import engine


schema.Base.metadata.create_all(bind=engine)

server = FastAPI(
    title="Hubshub API",
    description="Hubshub Warehouse Project",
    version="0.0.1"
)

origins = ['*']

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


server.include_router(status_controller.router, tags=['Status'])
server.include_router(authorization_controller.router, tags=['Auth'])
server.include_router(superadmin_controller.router, tags=['Super Admin'])
server.include_router(vendor_controller.router, tags=['Vendor'])
server.include_router(customer_controller.router, tags=['Customer'])
server.include_router(anonymous_controller.router, tags=['Anonymous'])
