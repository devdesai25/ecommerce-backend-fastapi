from passlib.context import CryptContext
from jose import JWTError,jwt
from datetime import datetime, timedelta

SECRET_KEY = 'SECRET'
ALGORITHM = 'HSA256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data:dict , expire_delta: timedelta=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expire_delta if expire_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.enocde(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def decode_access_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        return payload
    except:
        return None