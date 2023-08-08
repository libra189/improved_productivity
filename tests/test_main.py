from fastapi.testclient import TestClient

from ..app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Hello world"}


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200


def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200


def test_get_item_not_found():
    response = client.get("/items/100")
    assert response.status_code == 404


def test_get_price_including_tax():
    response = client.get("/items/1/sell")
    assert response.status_code == 200


def test_get_price_including_tax_not_found():
    response = client.get("/items/100/sell")
    assert response.status_code == 404


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200


def test_get_user_not_found():
    response = client.get("/users/100")
    assert response.status_code == 404
