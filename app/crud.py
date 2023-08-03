from .schemas import Item, User

user_list: list[User] = [
    User(id=1, email="user1@example.com", is_active=True),
    User(id=2, email="user2@example.com", is_active=True),
    User(id=3, email="user3@example.com", is_active=False),
]

item_list: list[Item] = [
    Item(id=1, name="Item #1", user_id=1, price=1980),
    Item(id=2, name="Item #2", user_id=1, price=5600),
    Item(id=3, name="Item #3", user_id=1, price=110),
    Item(id=4, name="Item #4", user_id=1, price=2000),
    Item(id=5, name="Item #5", user_id=2, price=10050),
]


def get_users(is_active_only: bool = False) -> list[User]:
    """ユーザ一覧を取得

    Args:
        is_active_only (bool, optional): 有効なユーザのみ取得. Defaults to False.

    Returns:
        list[User]: ユーザ一覧
    """
    users = [x for x in user_list if x.is_active] if is_active_only else user_list
    for user in users:
        user.items = [x for x in item_list if x.user_id == user.id]

    return users


def get_user(user_id: int) -> User | None:
    """ユーザを取得

    Args:
        user_id (int): ユーザID

    Returns:
        User | None: ユーザ情報
    """
    user = next(filter(lambda x: x.id == user_id, user_list), None)
    if user is None:
        return None

    user.items = [x for x in item_list if x.user_id == user_id]
    return user


def get_items() -> list[Item]:
    """アイテム一覧を取得

    Returns:
        list[Item]: アイテム一覧
    """
    return item_list


def get_item(item_id: int) -> Item | None:
    """アイテムを取得

    Args:
        item_id (int): アイテムID

    Returns:
        Item | None: アイテム情報
    """
    item = next(filter(lambda x: x.id == item_id, item_list), None)
    return item
