from fastapi import HTTPException
from database import sessionlocal
from models.users import User
from auth.jwt import verify,encode,hash_password

def login(user):
    with sessionlocal() as db:
  #      try:
            isValid = db.query(User).filter(User.username == user.username).first()
            if not isValid:
                raise HTTPException(status_code=404,detail="Invalid Password or Username")
            hashed_password = hash_password(user.password)
            isValid = db.query(User).filter(User.hashed_password == hashed_password)
            if not isValid:
                raise HTTPException(status_code=404,detail="Invalid Password Or Username")
            auth_code = encode(user)
            db.close()
 #       except:
#            raise HTTPException(status_code=500,detail="Some error")
    return(auth_code,{"Authenticated":"Done"})