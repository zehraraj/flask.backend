import enum


class BooleanEnum(str, enum.Enum):
    true: str = 'true'
    false: str = 'false'


class WarehouseState(str, enum.Enum):
    pending: str = 'pending'
    approved: str = 'approved'
