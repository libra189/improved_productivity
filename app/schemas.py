from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    user_id: int


class ItemDetail(BaseModel):
    id: int
    user_id: int
    name: str
    price: int
    tax: int
    selling_price: int


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
