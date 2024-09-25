from database import Base
from typing import Optional
from sqlalchemy import String, Integer, Boolean, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, date


class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(32))
    category: Mapped[str] = mapped_column(String(16))
    price: Mapped[int] = mapped_column(default=0)
    description: Mapped[Optional[str]]
    date: Mapped[date]
    active: Mapped[bool] = mapped_column(Boolean, default=0)


