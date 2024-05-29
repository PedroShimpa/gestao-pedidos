from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional, Any

class Item(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None


class GetOrder(BaseModel): 
    id: str
    customer_name: Optional[str] = None
    delivery_address: Optional[str] = None
    items: Optional[List[Item]] = []
    total: Optional[float] = 0  # Não é obrigatório na entrada
    date: Any
    status: Optional[str] = "Em produção"   

class Order(BaseModel):
    customer_name: Optional[str] = None
    delivery_address: Optional[str] = None
    items: Optional[List[Item]] = []
    total: Optional[float] = 0  # Não é obrigatório na entrada
    date: Any
    status: Optional[str] = "Em produção"
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "customer_name": "John Doe",
                    "delivery_address": "123 Main St",
                    "items": [
                        {"name": "Product 1", "quantity": 2, "price": 10.0},
                        {"name": "Product 2", "quantity": 1, "price": 20.0}
                    ],
                }
            ]
        }
    
    def calculate_total(self):
        if self.items:
            self.total = sum(item.price * item.quantity for item in self.items if item.price and item.quantity)

class OrderStatus(BaseModel):
    status: str