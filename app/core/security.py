
from pwdlib import PasswordHash
import jwt
from  datetime import  datetime, timedelta, timezone
from app.core.config import Settings
from fastapi import HTTPException, status

password_hash = PasswordHash.recommended()

def hash_password(password: str)->str:
    return password_hash.hash(password)

def verify_password(password:str, hashed_password:str)-> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(subject:str, role:str)->str :

    expires_at = datetime.now(timezone.utc) + timedelta(minutes=60)
    secret_key = Settings.SECRET_KEY
    alogorithm = Settings.ALOGORITHM

    payload = {
        "sub": subject,
        "role": role,
        "exp": expires_at

    }

    token = jwt.encode(
                payload,
                secret_key,
                alogorithm=alogorithm
    )

    return token


def  decode_access_token(token:str)-> dict:
    secret_key = Settings.SECRET_KEY
    alogorithm = Settings.ALOGORITHM

    try:
        payload = jwt.decode(
            token,
            secret_key,
            algorithms=[alogorithm]
        )

        return payload
    
    except jwt.ExpiredSignatureError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired."
        )

    except jwt.InvalidTokenError as exc:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )