from typing import Optional, List
from pydantic import BaseModel, Field


class createbookModel(BaseModel):
    id: str = Field(min_length=3, max_length=10)
    book_name: str
    category: str
    price: int


class updatebookModel(BaseModel):

    book_name: Optional[str]
    category: Optional[str]
    price: Optional[int]
