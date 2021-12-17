from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    national_id: Optional[str] = None

class ShowUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    class Config():
        orm_mode = True


class Product(BaseModel):
    product_id: str
    name: str
    price: int
    description: str

class ShowProduct(BaseModel):
    product_id: str
    name: str
    price: int    
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None