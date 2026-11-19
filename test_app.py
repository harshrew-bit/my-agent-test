import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello World"}

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.json
    assert data['status'] == 'ok'
    assert isinstance(data['uptime'], float)
    assert data['uptime'] >= 0
