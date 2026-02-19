from pydantic import BaseModel

class UserResponse(BaseModel):

    id: int
    role: str
    username: str

    class config:
        orm_mode = True