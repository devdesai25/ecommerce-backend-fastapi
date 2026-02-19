from database import sessionlocal
from models.users import User
from fastapi import HTTPException
from auth.jwt import hash_password,encode

def signup_serv(user, db):
                
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=404,detail="Username already there")
    hashed_pass = hash_password(user.password)
    db_user = User(username = user.username, hashed_password = hashed_pass, role="admin")

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = {"sub":db_user.id,"username":db_user.username}

    auth_key = encode(token)

    return (auth_key,{"User":"Logged in"})