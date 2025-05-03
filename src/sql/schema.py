from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.orm import relationship, backref

from .database import Base

import enum


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    gstin = Column(String(50))
    pin = Column(String(50))
    pan = Column(String(50))
    email = Column(String(50))
    country_code = Column(String(50))
    mobile = Column(String(50))
    account_manager = Column(Integer)

    def __repr__(self):
        return "<Company(id='%s', name='%s', email='%s')>" % (self.id, self.name, self.email)


class UserType(str, enum.Enum):
    superadmin: str = 'superadmin'
    customer: str = 'customer'
    vendor: str = 'vendor'
    account_manager: str = 'account_manager'


class Status(str, enum.Enum):
    active: str = 'active'
    de_active: str = 'de_active'
    blocked: str = 'blocked'


class PreferedChannel(str, enum.Enum):
    mobile: str = 'mobile'
    email: str = 'email'


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
    mobile = Column(String(10))
    created_at = Column(TIMESTAMP)
    country_code = Column(String(50))
    company_id = Column(Integer)
    updated_at = Column(TIMESTAMP)
    last_login = Column(TIMESTAMP)
    user_type = Column(Enum(UserType))
    user_status = Column(Enum(Status))
    email_verified = Column(Boolean, default=False)
    mobile_verified = Column(Boolean, default=False)
    preffered_channel = Column(Enum(PreferedChannel))

    def __repr__(self):
        return "<User(id='%s', email='%s', first_name='%s', last_name='%s')>" % (self.id, self.email, self.first_name, self.last_name)


class GeneralAction(Base):
    __tablename__ = "general_action"

    id = Column(Integer, primary_key=True, index=True)
    action_name = Column(String(50))
    description = Column(String(50))

    def __repr__(self):
        return "<GeneralAction(id='%s', action_name='%s')>" % (self.id, self.action_name)


class SystemLogResult(str, enum.Enum):
    success: str = 'success'
    pending: str = 'pending'
    failure: str = 'failure'


class SystemLog(Base):
    __tablename__ = 'system_log'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    action_id = Column(Integer)
    fingerprint = Column(String(50))
    device = Column(String(50))
    ip_address = Column(String(50))
    ip_location = Column(String(50))
    json_data = Column(String(50))                  # File System Storage
    action_at = Column(TIMESTAMP)
    result = Column(Enum(SystemLogResult))

    def __repr__(self):
        return "<SystemLog(id='%s', user_id='%s')>" % (self.id, self.user_id)


class IndustryCategory(Base):
    __tablename__ = 'industry_category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    added_on = Column(TIMESTAMP)

    def __repr__(self):
        return "<IndustryCategory(id='%s', name='%s')>" % (self.id, self.name)


class Contract(Base):
    __tablename__ = 'contract'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    company_id = Column(Integer)
    signing_authority = Column(String(50))
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)

    def __repr__(self):
        return "<Contract(id='%s', customer_id='%s')>" % (self.id, self.customer_id)


class PreferenceType(str, enum.Enum):
    industry: str = 'industry'
    product: str = 'product'
    package: str = 'package'


class PreferenceList(Base):
    __tablename__ = 'preference_list'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    type = Column(Enum(PreferenceType))
    added_on = Column(TIMESTAMP)

    def __repr__(self):
        return "<PreferenceList(id='%s', name='%s', type='%s')>" % (self.id, self.name, self.type)


class CustomerPreference(Base):
    __tablename__ = 'customer_preference'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    preference_id = Column(Integer)

    def __repr__(self):
        return "<CustomerPreference(id='%s', customer_id='%s', preference_id='%s')>" % (self.id, self.customer_id, self.preference_id)


class WarehouseOperation(str, enum.Enum):
    new: str = 'new'
    edit: str = 'edit'


class Warehouse(Base):
    __tablename__ = 'warehouse'

    warehouse_version_id = Column(Integer, primary_key=True, index=True)
    id = Column(Integer, unique=True, index=True)
    user_id = Column(Integer)
    company_id = Column(Integer)
    name = Column(String(50))
    area = Column(Integer)
    area_rate = Column(Integer)
    pallets = Column(Integer)
    pallets_rate = Column(Integer)
    license_no = Column(String(50))
    desc = Column(String(50))
    is_active = Column(Boolean, default=False)
    operation = Column(Enum(WarehouseOperation))
    is_approved = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    verified_by = Column(Integer)
    verified_on = Column(TIMESTAMP)
    required_review = Column(Boolean, default=False)
    address = Column(Integer)
    available_from = Column(TIMESTAMP)
    available_to = Column(TIMESTAMP)

    def __repr__(self):
        return "<Warehouse(warehouse_version_id='%s', id='%s', name='%s')>" % (self.warehouse_version_id, self.id, self.name)


class WarehouseImage(Base):
    __tablename__ = 'warehouse_image'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer)
    image = Column(String(50))
    desc = Column(String(50))

    def __repr__(self):
        return "<WarehouseImage(id='%s', warehouse_id='%s')>" % (self.id, self.warehouse_id)


class Identity(Base):
    __tablename__ = 'identity'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    company_name = Column(String(50))
    email = Column(String(50))
    mobile = Column(String(50))

    def __repr__(self):
        return "<Identity(id='%s', name='%s')>" % (self.id, self.name)


class Amenity(Base):
    __tablename__ = 'amenity'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    def __repr__(self):
        return "<Amenity(id='%s', name='%s')>" % (self.id, self.name)


class WarehouseAmenity(Base):
    __tablename__ = 'warehouse_amenity'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer)
    amenity_id = Column(Integer)

    def __repr__(self):
        return "<WarehouseAmenity(id='%s', warehouse_id='%s', amenity_id='%s')>" % (self.id, self.warehouse_id, self.amenity_id)


class AddonService(Base):
    __tablename__ = 'addon_service'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    def __repr__(self):
        return "<AddonService(id='%s', name='%s')>" % (self.id, self.name)


class WarehouseAddonService(Base):
    __tablename__ = 'warehouse_addon_service'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer)
    addon_service = Column(Integer)

    def __repr__(self):
        return "<WarehouseAddonService(id='%s', warehouse_id='%s', addon_service='%s')>" % (self.id, self.warehouse_id, self.addon_service)


class IndustryTag(Base):
    __tablename__ = 'industry_tag'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    def __repr__(self):
        return "<IndustryTag(id='%s', name='%s')>" % (self.id, self.name)


class WarehouseTag(Base):
    __tablename__ = 'warehouse_tag'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer)
    industry_tag = Column(Integer)

    def __repr__(self):
        return "<WarehouseTag(id='%s', warehouse_id='%s', industry_tag='%s')>" % (self.id, self.warehouse_id, self.industry_tag)


class Locality(Base):
    __tablename__ = 'locality'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    def __repr__(self):
        return "<Locality(id='%s', name='%s')>" % (self.id, self.name)


class WarehouseLocality(Base):
    __tablename__ = 'warehouse_locality'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer)
    locality = Column(Integer)
    distance = Column(Integer)

    def __repr__(self):
        return "<WarehouseLocality(id='%s', warehouse_id='%s', locality='%s')>" % (self.id, self.warehouse_id, self.locality)


class WarehouseReserve(Base):
    __tablename__ = 'warehouse_reserve'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer)
    identity = Column(Integer)
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)

    def __repr__(self):
        return "<WarehouseReserve(id='%s', warehouse_id='%s', identity='%s')>" % (self.id, self.warehouse_id, self.identity)


class WarehouseTour(Base):
    __tablename__ = 'warehouse_tour'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer)
    identity = Column(Integer)
    datetime = Column(TIMESTAMP)
    status = Column(String(50))

    def __repr__(self):
        return "<WarehouseTour(id='%s', warehouse_id='%s', identity='%s')>" % (self.id, self.warehouse_id, self.identity)


class WarehouseEnquiry(Base):
    __tablename__ = 'warehouse_enquiry'

    id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer)
    identity = Column(Integer)
    message = Column(String(50))

    def __repr__(self):
        return "<WarehouseEnquiry(id='%s', warehouse_id='%s', identity='%s')>" % (self.id, self.warehouse_id, self.identity)


class ContactRequest(Base):
    __tablename__ = 'contact_request'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    interested_in = Column(String(50))
    city = Column(String(50))
    country_code = Column(Integer)

    def __repr__(self):
        return "<ContactRequest(id='%s', name='%s', city='%s', interested_in='%s')>" % (self.id, self.name, self.city, self.interested_in)


class State(Base):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    def __repr__(self):
        return "<State(id='%s', name='%s')>" % (self.id, self.name)


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    def __repr__(self):
        return "<City(id='%s', name='%s')>" % (self.id, self.name)


class Shortlist(Base):
    __tablename__ = 'shortlist'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    warehouse_id = Column(Integer)

    def __repr__(self):
        return "<Shortlist(id='%s', customer_id='%s', warehouse_id='%s')>" % (self.id, self.customer_id, self.warehouse_id)


class Service(Base):
    __tablename__ = 'Service'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))

    def __repr__(self):
        return "<Service(id='%s', title='%s')>" % (self.id, self.title)


class ServiceRequest(Base):
    __tablename__ = 'ServiceRequest'

    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer)
    warehouse_id = Column(Integer)
    message = Column(String(50))
    user_id = Column(Integer)
    time_created = Column(TIMESTAMP)
    is_complete = Column(Boolean)

    def __repr__(self):
        return "<ServiceRequest(id='%s', warehouse_id='%s', user_id='%s')>" % (self.id, self.warehouse_id, self.user_id)


class CustomerProperty(Base):
    __tablename__ = 'CustomerProperty'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    warehouse_id = Column(Integer)
    total_costing = Column(Integer)
    rent_from = Column(TIMESTAMP)
    rent_to = Column(TIMESTAMP)
    area = Column(Integer)
    pallets = Column(Integer)

    def __repr__(self):
        return "<CustomerProperty(id='%s', customer_id='%s', warehouse_id='%s')>" % (self.id, self.customer_id, self.warehouse_id)


class Address(Base):
    __tablename__ = 'Address'

    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Integer)
    latitude = Column(Integer)
    location = Column(Integer)
    area = Column(Integer)
    address = Column(Integer)

    def __repr__(self):
        return "<Address(id='%s', longitude='%s', latitude='%s')>" % (self.id, self.longitude, self.latitude)
