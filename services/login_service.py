from fastapi import HTTPException
from database import sessionlocal
from models.users import User
from auth.jwt import verify,encode,hash_password

def login(user):
    with sessionlocal() as db:
  #      try:
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
            auth_code = encode({"sub":user_id,"username":db_user.username})
            db.close()
 #       except:
#            raise HTTPException(status_code=500,detail="Some error")
    return(auth_code,{"Authenticated":"Done"})