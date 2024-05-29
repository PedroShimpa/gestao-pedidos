from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class MenuItem(BaseModel):
    name: str
    description: str
    price: float
