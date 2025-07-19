from fastapi import APIRouter, HTTPException, status
from typing import List
from services import order_service
from models.order import Order, OrderCreate

router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    order_id = await order_service.create_order(order)
    return {"message": "Order placed successfully", "order_id": order_id}

@router.get("/orders/{user_id}", response_model=List[Order])
async def get_orders_by_user(user_id: str, limit: int = 10, offset: int = 0):
    orders = await order_service.get_orders_by_user(user_id, limit, offset)
    return orders
