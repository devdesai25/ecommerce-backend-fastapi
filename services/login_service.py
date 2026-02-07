from fastapi import HTTPException
from database import sessionlocal
from models.users import User
from auth.jwt import verify,encode,hash_password

def login(user):
    with sessionlocal() as db:
        try:
            isValid = db.get(User).filter(User.name == user.name).first()
            if not isValid:
                raise HTTPException(status_code=404,detail="Invalid Password or Username")
            hashed_password = hash_password(user.password)
            isValid = db.get(User).filter(User.hashed_password == hashed_password)
            if not isValid:
                raise HTTPException(status_code=404,detail="Invalid Password Or Username")
            jwt = encode(user)
            db.close()
        except:
            raise HTTPException(status=500,detail="Fill it perfectly") 
    return{"message":"Done"}