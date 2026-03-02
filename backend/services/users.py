from database import get_db
from models.users import User
from fastapi import HTTPException
from auth.jwt import hash_password, encode, verify, encode

def signup_service(user, db):
                
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


def login_service(user,db):
#    try:
        db_user = db.query(User).filter(User.username == user.username).first()
        if not db_user:
            raise HTTPException(
                status_code=404,
                detail="Invalid Password or Username"
                )
            
        if not verify(user.password, db_user.hashed_password):
            raise HTTPException(
                status_code=404,
                detail="Invalid Password Or Username"
                )
        user_id = db_user.id 
        access_token = encode({"sub":str(user_id),"username":db_user.username})
#    except:
#        raise HTTPException(status_code=500,detail="Some error")
        return {"access_token":access_token,
            "token_type":"bearer"}