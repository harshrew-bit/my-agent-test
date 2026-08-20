import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/hello')
    assert rv.status_code == 200
    assert rv.get_json() == {"message": "Hello World"}
