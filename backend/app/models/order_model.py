from pymongo.collection import Collection
from bson import ObjectId
from database import db
from schemas.order_schema import Order, OrderStatus
import datetime

orders_collection: Collection = db["orders"]

def create_order(order: Order):
    order.calculate_total()  # Calcular o total automaticamente
    order.date = datetime.datetime.now()
    order_dict = order.dict()
    result = orders_collection.insert_one(order_dict)
    return str(result.inserted_id) if result.inserted_id else None

def read_order(order_id: str):
    order = orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        order["id"] = str(order["_id"])
    return order

def update_order(order_id: str, order: Order):
    order.calculate_total()  # Calcular o total automaticamente
    order_dict = order.dict()
    result = orders_collection.update_one({"_id": ObjectId(order_id)}, {"$set": order_dict})
    return result.modified_count > 0

def update_order_status(order_id: str, order_status: OrderStatus):
    order_dict = order_status.dict()
    result = orders_collection.update_one({"_id": ObjectId(order_id)}, {"$set": order_dict})
    return result.modified_count > 0

def delete_order(order_id: str):
    result = orders_collection.delete_one({"_id": ObjectId(order_id)})
    return result.deleted_count > 0

def list_orders():
    orders = list(orders_collection.find())
    for order in orders:
        order["id"] = str(order["_id"])
    return orders
