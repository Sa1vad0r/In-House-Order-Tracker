from typing import Optional
from pydantic import BaseModel

#for some reason cant pre define variable
#TODO: Fix that bug as to prety the code
class Order(BaseModel):
    customer_name: str
    desc: str
    items: list
    status: str  
    worth: float
    
class UpdateOrder(BaseModel):
    customer_name: Optional[str] = None
    desc: Optional[str] = None
    items: Optional[list] = None
    status: Optional[str] = None
    worth: Optional[float] = None
    