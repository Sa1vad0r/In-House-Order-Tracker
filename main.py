try:
    from fastapi import FastAPI, Path, HTTPException, status
    from typing import Optional
    from pydantic import BaseModel
except ImportError:
    class FastAPI:
        def get(self, path):
            def decorator(func):
                return func
            return decorator



#    def Path(default=None, **kwargs):
#        return default

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

orders = {
    1: {
        "id": 1,
        "customer-name": "Johnah",
        "desc": "Office supplies order",
        "Items": [
            "Stapler",
            "Printer paper",
            "Highlighter set"
        ],
        #update order status (e.g. "pending" → "ready" → "picked_up")
        "status": "pending",
        "worth": 24.75
    },
    2: {
        "id": 2,
        "customer-name": "Mateo",
        "desc": "Cafeteria restock",
        "Items": [
            "Coffee pods",
            "Sugar packets",
            "Tea bags"
        ],
        "status": "pending",
        "worth": 18.40
    },
    3 : {
        "id": 3,
        "customer-name": "Glen",
        "desc": "Cleaning supplies",
        "Items": [
            "Disinfectant spray",
            "Paper towels",
            "Trash bags"
        ],
        "status": "ready",
        "worth": 27.60
    },
    4: {
        "id": 4,
        "customer-name": "Sandra",
        "desc": "Lunch delivery",
        "Items": [
            "Turkey sandwich",
            "Salad",
            "Bottled water"
        ],
        "status": "picked_up",
        "worth": 32.25
    }
}
#currently Hard coded to 4 
#TODO: Make a function that reads the amount of current orders and then sets sour Var to That number
total_orders=len(orders)

app = FastAPI()
print("works")


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/orders")
async def order_print():
    return orders

@app.get("/order/{order_id}")
async def order_print_specified(order_id: int):
    #TODO: find out why path is dropping succh a big error
    # = Path(None, Description="The ID of The Order your Seacrching for.", gt = 0, lt=total_orders)
    if order_id not in orders:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Order with the ID: {order_id} does not exist"
        )
    return orders[order_id]

#TODO: build this out as a search feature bring up all names that are like that
#it would be custorer servise tool
@app.get("/Customer/{name}")
async def find_order_by_customer_name(name: str):
    for order_id, order in orders.items():
        if order["customer-name"] == name:
            return order
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Order with the Name: {name} does not exist"
        )
    #return {"Data": "Order Not Found"}
             
             
    # Example order data:
    # 4: {
    #     "id": 4,
    #     "customer-name": "Sandra",
    #     "desc": "Lunch delivery",
    #     "Items": [
    #         "Turkey sandwich",
    #         "Salad",
    #         "Bottled water"
    #     ],
    #     "worth": 32.25
    # }
#POST
@app.post("/orders", status_code=201)
async def add_to_orders(order: Order):
    order_id = total_orders+1
    order.id = order_id
    order.status = "pending"
    orders[order_id] = order
    return {orders[order_id]}

#update
@app.put("/order/{order_id}")
async def update_order(order_id: int, order: UpdateOrder):
    if order_id not in orders:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Order with the ID: {order_id} does not exist"
        )

    stored_order = orders[order_id]
    if order.customer_name is not None:
        stored_order["customer-name"] = order.customer_name
    if order.desc is not None:
        stored_order["desc"] = order.desc
    if order.Items is not None:
        stored_order["Items"] = order.Items
    if order.status is not None:
        stored_order["status"] = order.status
    if order.worth is not None:
        stored_order["worth"] = order.worth

    return stored_order

@app.delete("/order/delete")
async def delete_order(order_id: int):
    if order_id not in orders:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Order with the ID: {order_id} does not exist"
        )
    
    del orders[order_id]