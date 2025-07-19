from pydantic import BaseModel, Field, ConfigDict
from typing import List, Any
from bson import ObjectId
from datetime import datetime
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler
    ) -> core_schema.CoreSchema:
        def validate(v: Any) -> ObjectId:
            if not ObjectId.is_valid(v):
                raise ValueError('Invalid ObjectId')
            return ObjectId(v)

        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(ObjectId),
                    core_schema.chain_schema(
                        [core_schema.str_schema(), core_schema.no_info_plain_validator_function(validate)]
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(lambda x: str(x)),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, schema: core_schema.CoreSchema, handler
    ) -> JsonSchemaValue:
        json_schema = handler(schema)
        json_schema.update(
            type='string',
            examples=['5eb7cf3a86d9755df3a6c593', '5eb7cfb05e32f0a3a420f338'],
        )
        return json_schema

class OrderProduct(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str
    products: List[OrderProduct]
    total_price: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

class OrderCreate(BaseModel):
    user_id: str
    products: List[OrderProduct]
    total_price: float
