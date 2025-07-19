from fastapi import APIRouter, HTTPException, status
from typing import List
from services import product_service
from models.product import Product, ProductCreate

router = APIRouter()

@router.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    product_id = await product_service.create_product(product)
    return {"message": "Product created successfully", "product_id": product_id}

@router.get("/products", response_model=List[Product])
async def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    products = await product_service.list_products(name, size, limit, offset)
    return products
