from typing import Any

from fastapi import FastAPI, HTTPException

from app import crud, schemas
from app.services import item_service

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok", "message": "Hello world"}


@app.get("/items", response_model=list[schemas.Item])
def get_items() -> Any:
    return crud.get_items()


@app.get("/items/{id}", response_model=schemas.Item | None)
def get_item(id: int) -> Any:
    item = crud.get_item(id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.get("/items/{id}/sell", response_model=schemas.ItemDetail)
def get_price_including_tax(id: int) -> Any:
    item = crud.get_item(id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item_service.detail(item)


@app.get("/users", response_model=list[schemas.User])
def get_users(is_active: str | None = None) -> Any:
    return crud.get_users(is_active_only=bool(is_active))


@app.get("/users/{id}", response_model=schemas.User)
def get_user(id: int) -> Any:
    user = crud.get_user(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
