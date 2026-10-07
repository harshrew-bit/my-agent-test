import pytest
import logging
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

def test_logging_middleware(client, caplog):
    with caplog.at_level(logging.INFO):
        client.get('/hello')
        assert "GET /hello - Status: 200" in caplog.text
        assert "Duration:" in caplog.text
