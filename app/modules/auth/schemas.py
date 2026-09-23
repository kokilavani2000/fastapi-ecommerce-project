
from pydantic import BaseModel, Field, EmailStr


class RegisterRequest(BaseModel):
    full_name: str = Field(min_length=1, max_length=150, description="Full name of the user")
    email: EmailStr
    password: str = Field(min_length=8, max_length=128, description="Password of the user")

class LoginRequest(BaseModel):
    email: EmailStr
    password: str 