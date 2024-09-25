from typing import Optional
from pydantic import BaseModel, PositiveInt
from datetime import date,datetime


class ProductListValidate(BaseModel):
    id: int
    product_name: str
    category: str
    price: PositiveInt
    description: Optional[str] = None
    date: date
    active: bool

