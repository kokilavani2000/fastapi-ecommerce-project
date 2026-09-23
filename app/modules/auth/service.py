from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.modules.users.repository import UserRepository
from app.modules.users.model import User
from app.modules.auth.schemas import RegisterRequest, LoginRequest
from app.modules.users.schemas import UserRole, UserRead
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(self, payload: RegisterRequest) -> dict:
        existing_user = self.user_repository.get_by_email(payload.email)

        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists",
            )

        user = User(
            full_name=payload.full_name,
            email=payload.email,
            password_hash=hash_password(payload.password),
            is_active=True,
            role=UserRole.CUSTOMER.value,
        )

        db_user = self.user_repository.create(user)

        # create access token for the user
        access_token = create_access_token(str(db_user.id), db_user.role)

        return {
            "access_token": access_token,
            "user": UserRead.model_validate(db_user).model_dump(),
        }

    def login(self, payload: LoginRequest) -> dict:
        user = self.user_repository.get_by_email(payload.email)

        if user is None or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not verify_password(payload.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        access_token = create_access_token(str(user.id), user.role)

        return {
            "access_token": access_token,
            "user": UserRead.model_validate(user).model_dump(),
        }