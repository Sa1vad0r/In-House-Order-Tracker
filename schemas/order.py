from typing import Optional
from pydantic import BaseModel

#for some reason cant pre define variable
#TODO: Fix that bug as to prety the code
class Order(BaseModel):
    id: int 
    customer_name: str
    desc: str
    Items: list
    status: str  
    worth: float
    
class UpdateOrder(BaseModel):
    id: Optional[int] = None
    customer_name: Optional[str] = None
    desc: Optional[str] = None
    Items: Optional[list] = None
    status: Optional[str] = None
    worth: Optional[float] = None
    