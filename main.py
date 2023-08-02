from fastapi import FastAPI

JP_TAX: float = 0.1  # 10%

item_list = [
    {"id": 1, "name": "Item #1", "price": 1980},
    {"id": 2, "name": "Item #2", "price": 5600},
    {"id": 3, "name": "Item #3", "price": 110},
    {"id": 4, "name": "Item #4", "price": 2000},
    {"id": 5, "name": "Item #5", "price": 10050},
]

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok", "message": "Hello world"}


@app.get("/items")
def get_items():
    return item_list


@app.get("/items/{id}")
def get_item(id: int):
    if id <= 0:
        return {}
    elif id > len(item_list):
        return {}
    else:
        return item_list[id]


@app.get("/items/{id}/tax")
def get_price_including_tax(id: int):
    if id <= 0:
        return {}
    elif id > len(item_list):
        return {}
    else:
        item = item_list[id]
        tax = int(item["price"] * JP_TAX)
        item["tax"] = tax
        item["selling price"] = item["price"] + tax
        return item
