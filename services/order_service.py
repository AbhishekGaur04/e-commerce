from config.database import database
from models.order import Order, OrderCreate
from bson import ObjectId
from datetime import datetime

order_collection = database.get_collection("orders")

async def create_order(order: OrderCreate):
    order_dict = order.dict()
    order_dict["created_at"] = datetime.utcnow()
    result = await order_collection.insert_one(order_dict)
    return str(result.inserted_id)

async def get_orders_by_user(user_id: str, limit: int = 10, offset: int = 0):
    orders = await order_collection.find({"user_id": user_id}).sort("_id").skip(offset).limit(limit).to_list(length=limit)
    return orders
