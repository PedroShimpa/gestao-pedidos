from pymongo.collection import Collection
from bson import ObjectId
from database import db
from schemas.menu_item_schema import MenuItem

menu_items_collection: Collection = db["menu_items"]

def create_menu_item(menu_item: MenuItem):
    menu_item_dict = menu_item.dict()
    result = menu_items_collection.insert_one(menu_item_dict)
    return str(result.inserted_id) if result.inserted_id else None

def read_menu_item(menu_item_id: str):
    menu_item = menu_items_collection.find_one({"_id": ObjectId(menu_item_id)})
    if menu_item:
        menu_item["id"] = str(menu_item["_id"])
    return menu_item

def update_menu_item(menu_item_id: str, menu_item: MenuItem):
    menu_item_dict = menu_item.dict()
    result = menu_items_collection.update_one({"_id": ObjectId(menu_item_id)}, {"$set": menu_item_dict})
    return result.modified_count > 0

def delete_menu_item(menu_item_id: str):
    result = menu_items_collection.delete_one({"_id": ObjectId(menu_item_id)})
    return result.deleted_count > 0

def list_menu_items():
    menu_items = list(menu_items_collection.find())
    for menu_item in menu_items:
        menu_item["id"] = str(menu_item["_id"])
    return menu_items
