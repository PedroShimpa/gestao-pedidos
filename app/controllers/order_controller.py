from fastapi import APIRouter, HTTPException
from typing import List
from models import order_model
from schemas.order_schema import Order,OrderStatus,GetOrder

router = APIRouter()

@router.post("/orders", response_model=dict)
def create_order(order: Order):
    order_id = order_model.create_order(order)
    if order_id:
        return {"id": order_id}
    else:
        raise HTTPException(status_code=500, detail="Order could not be created")

@router.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: str):
    order = order_model.read_order(order_id)
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="Order not found")

@router.put("/orders/{order_id}", response_model=dict)
def update_order(order_id: str, order: Order):
    success = order_model.update_order(order_id, order)
    if success:
        return {"message": "Order updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Order not found")
    
@router.put("/orders/update-order-status/{order_id}", response_model=dict)
def update_order_status(order_id: str, order: OrderStatus):
    success = order_model.update_order_status(order_id, order)
    if success:
        return {"message": "Order status update successfully"}
    else:
        raise HTTPException(status_code=404, detail="Order not found")

@router.delete("/orders/{order_id}", response_model=dict)
def delete_order(order_id: str):
    success = order_model.delete_order(order_id)
    if success:
        return {"message": "Order deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Order not found")

@router.get("/orders", response_model=List[GetOrder])
def list_orders():
    return order_model.list_orders()
