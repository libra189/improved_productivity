from app.schemas import Item, ItemDetail
from app.util import tax_rate


def detail(item: Item) -> ItemDetail:
    tax = int(item.price * tax_rate())
    return ItemDetail(**item.model_dump(), tax=tax, selling_price=item.price + tax)
