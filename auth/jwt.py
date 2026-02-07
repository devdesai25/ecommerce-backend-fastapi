from passlib.context import CryptContext
from jose import jwt,JWTError
from datetime import timedelta, datetime

pwd_context = CryptContext(schemes=["bcrypt_sha256","bcrypt"], deprecated="auto")
#move this later to .env
SECRET_KEY = "SECRET"
SECRET_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password:str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verify(hash_password:str, plain_password:str):
    plain_password = pwd_context.verify(plain_password,hash_password)
    return plain_password

def encode(data):
    to_encode = data.copy()
    expire = datetime.utcnow() + (ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.add({"expire":expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, SECRET_ALGORITHM)
    return encoded

def decode(data):
    try:
        payload = jwt.decode(data, SECRET_KEY, SECRET_ALGORITHM)
        return payload
    except:
        return data