
from pydantic import BaseModel, Field, Emailstr


class RegisterRequest(BaseModel):
    full_nam: str = Field(min_length=1, max_length=150, description="Full name of the user")
    email: Emailstr
    password: str = Field(min_length=8, max_length=128, description="Password of the user")

class LoginRequest(BaseModel):
    email: Emailstr
    password: str 