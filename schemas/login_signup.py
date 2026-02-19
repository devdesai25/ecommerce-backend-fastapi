from pydantic import BaseModel
from models.users import User
class userlogin(BaseModel):
    username :str
    password :str
    

class usersignup(BaseModel):
    username :str
    password :str