from ..app import crud


def test_get_users():
    users = crud.get_users()
    assert len(users) == 3


def test_get_user():
    user_id = 1
    user = crud.get_user(user_id)
    assert user.id == user_id


def test_get_user_not_found():
    user_id = 100
    user = crud.get_user(user_id)
    assert user is None


def test_get_items():
    items = crud.get_items()
    assert len(items) == 5


def test_get_item():
    item_id = 1
    item = crud.get_item(item_id)
    assert item.id == item_id


def test_get_item_not_found():
    item_id = 100
    item = crud.get_item(item_id)
    assert item is None
