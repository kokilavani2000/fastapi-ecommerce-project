from enum import Enum
from pydantic import BaseModel, ConfigDict


class UserRole(str, Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"


class UserBase(BaseModel):
    full_name: str
    email: str


class UserRead(UserBase):
    id: int
    is_active: bool
    role: UserRole

    model_config = ConfigDict(from_attributes=True)