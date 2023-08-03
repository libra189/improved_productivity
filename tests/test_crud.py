from ..app import crud


def test_get_users():
    users = crud.get_users()
    assert len(users) == 3
