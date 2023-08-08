from app.schemas import Item, ItemDetail
from app.services import item_service
from app.util import tax_rate


def test_detail():
    item: Item = Item(id=1, name="Test", price=1200, user_id=1)
    item_derail: ItemDetail = item_service.detail(item)
    assert item.id == item_derail.id
    assert item.price * tax_rate() == item_derail.tax
    assert item.price * (tax_rate() + 1) == item_derail.selling_price
