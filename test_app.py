import pytest
from app import app, somar, carregar_mensagem

@pytest.fixture
def client():
    """Cria um cliente de teste para a API Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "API is running"}

def test_login(client):
    response = client.post('/login')
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_protected_no_token(client):
    response = client.get('/protected')
    assert response.status_code == 401

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_carregar_mensagem():
    assert carregar_mensagem() == "Hello, Lab!"

