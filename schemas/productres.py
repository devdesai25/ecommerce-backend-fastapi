from pydantic import BaseModel

class productResponse(BaseModel):
    product_id : int
    name : str
    description: str
    price : float

    class config:
        orm_mode = True
