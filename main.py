from fastapi import FastAPI, HTTPException

from app import schemas

JP_TAX: float = 0.1  # 10%

user_list: list[schemas.User] = [
    schemas.User(id=0, email="user0@example.com", is_active=True),
    schemas.User(id=1, email="user1@example.com", is_active=True),
    schemas.User(id=2, email="user2@example.com", is_active=False),
]

item_list: list[schemas.Item] = [
    schemas.Item(id=0, name="Item #0", price=1980, user_id=1),
    schemas.Item(id=1, name="Item #1", price=5600, user_id=1),
    schemas.Item(id=2, name="Item #2", price=110, user_id=1),
    schemas.Item(id=3, name="Item #3", price=2000, user_id=1),
    schemas.Item(id=4, name="Item #4", price=10050, user_id=2),
]

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok", "message": "Hello world"}


@app.get("/items")
def get_items() -> list[schemas.Item]:
    return item_list


@app.get("/items/{id}")
def get_item(id: int) -> schemas.Item | None:
    if id < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    elif id > len(item_list):
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return item_list[id]


@app.get("/items/{id}/sell")
def get_price_including_tax(id: int) -> schemas.ItemDetail:
    if id < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    elif id > len(item_list):
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        item: schemas.Item = item_list[id]

        ret = item.model_dump()
        ret.update(tax=item.tax(), selling_price=item.selling_price())
        return schemas.ItemDetail(**ret)


@app.get("/users")
def get_users(is_active: str | None = None) -> list[schemas.User]:
    target_user_list = user_list
    if is_active:
        target_user_list = list(filter(lambda x: x.is_active, user_list))

    users: list[schemas.User] = []
    for user in target_user_list:
        user.items = list(filter(lambda x: x.user_id == user.id, item_list))
        users.append(user)

    return users


@app.get("/users/{id}")
def get_user(id: int) -> schemas.User:
    if id < 0:
        raise HTTPException(status_code=404, detail="User not found")
    elif id > len(user_list):
        raise HTTPException(status_code=404, detail="User not found")
    else:
        user = user_list[id]
        user.items = list(filter(lambda x: x.user_id == id, item_list))
        return user
