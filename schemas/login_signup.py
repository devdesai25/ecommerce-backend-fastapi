from pydantic import BaseModel

class userlogin(BaseModel):
    username :str
    password :str


class usersignup(BaseModel):
    username :str
    password :str