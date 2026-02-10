from database import sessionlocal
from models.users import User
from fastapi import HTTPException
from auth.jwt import hash_password,encode

def signup_serv(user):
    with sessionlocal() as db:
         
            isValid_name = db.query(User).filter(User.username == user.username).first()
            if isValid_name:
                raise HTTPException(status_code=404,detail="Username already there")
            hashed_pass = hash_password(user.password)
            db_user = User(username = user.username, hashed_password = hashed_pass)
            auth_key = encode(db_user)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            db.close()
      
    return (auth_key,{"User":"Logged in"})