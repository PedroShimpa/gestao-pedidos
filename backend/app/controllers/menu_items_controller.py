from fastapi import APIRouter, HTTPException
from typing import List
from models import menu_item_model
from schemas.menu_item_schema import MenuItem

router = APIRouter()

@router.post("/items", response_model=dict)
def create_menu_item(menu_item: MenuItem):
    menu_item_id = menu_item_model.create_menu_item(menu_item)
    if menu_item_id:
        return {"id": menu_item_id}
    else:
        raise HTTPException(status_code=500, detail="Menu item could not be created")

@router.get("/items/{menu_item_id}", response_model=MenuItem)
def read_menu_item(menu_item_id: str):
    read_menu_item = menu_item_model.read_menu_item(menu_item_id)
    if read_menu_item:
        return read_menu_item
    else:
        raise HTTPException(status_code=404, detail="menu item not found")

@router.put("/items/{menu_item_id}", response_model=dict)
def update_menu_item(menu_item_id: str, menu_item: MenuItem):
    success = menu_item_model.update_menu_item(menu_item_id, menu_item)
    if success:
        return {"message": "Menu item updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Menu item not found")

@router.delete("/items/{menu_item_id}", response_model=dict)
def delete_menu_item(menu_item_id: str):
    success = menu_item_model.delete_menu_item(menu_item_id)
    if success:
        return {"message": "menu item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Menu item not found")

@router.get("/items", response_model=List[MenuItem])
def list_menu_items():
    return menu_item_model.list_menu_items()
