from passlib.context import CryptContext
from jose import jwt,JWTError
import json
from datetime import timedelta, datetime
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from config import settings

pwd_context = CryptContext(schemes=["bcrypt_sha256","bcrypt"], deprecated="auto")

def hash_password(password:str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verify(plain_password:str,hash_password:str):
    plain_password = pwd_context.verify(plain_password, hash_password)
    return plain_password

def encode(data:dict):
    assert isinstance(data,dict)    
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes= settings.access_token_expire_minutes)
    to_encode.update({"exp":expire})

    encoded = jwt.encode(to_encode , settings.secret_key, algorithm= settings.secret_algorithm)
    return encoded

def decode(data):
    try:
        payload = jwt.decode(data, settings.secret_key,algorithms=[settings.secret_algorithm])
        return payload
    except JWTError as e:
        print("JWT ERROR",e)
        return None
    
oauth2scheme = OAuth2PasswordBearer(tokenUrl = "/login")