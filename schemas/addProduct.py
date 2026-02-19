from pydantic import BaseModel

class addProduct(BaseModel):

    name : str
    description : str | None = None
    stock : int
    price : float 