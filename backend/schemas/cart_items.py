from pydantic import BaseModel

class CartResponse(BaseModel):
    
    product_id: int
    quantity: int

    class Config:
        from_attributes = True