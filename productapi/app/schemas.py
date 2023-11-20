import uuid
from pydantic import BaseModel
from typing import List


class ProductBase(BaseModel):
    name: str
    weight: float
    description: str


class ProductResponse(ProductBase):
    id: uuid.UUID


class CreateProduct(ProductBase):
    pass


class UpdateProduct(BaseModel):
    name: str
    weight: float
    description: str    


class ListProducts(BaseModel):
    status: str
    results: int
    products: List[ProductResponse]

