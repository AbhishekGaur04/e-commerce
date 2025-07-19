from config.database import database
from models.product import Product, ProductCreate
from bson import ObjectId
import re

product_collection = database.get_collection("products")

async def create_product(product: ProductCreate):
    product_dict = product.dict()
    result = await product_collection.insert_one(product_dict)
    return str(result.inserted_id)

async def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": re.compile(name, re.IGNORECASE)}
    if size:
        query["sizes"] = size
    
    products = await product_collection.find(query).sort("_id").skip(offset).limit(limit).to_list(length=limit)
    return products
