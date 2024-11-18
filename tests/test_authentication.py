from main import app
from fastapi.testclient import TestClient
from datetime import date, timedelta

client = TestClient(app)

def test_create_user():
    """Teste para verificar se é possível a criação do usuário"""
    response = client.post("/auth/", json={"username":"teste", "password":"1233"})
    assert response.status_code == 201

def test_create_existent_user():
    """Teste para verificar se é possível a criação de um usuário já existente"""
    response = client.post("/auth/", json={"username":"teste", "password":"1233"})
    assert response.status_code == 400

def test_authenticate_user():
    """Teste para verificar se é possível autenticar um usuário"""
    response = client.post("/auth/token", data={"username":"teste", "password":"1233"})
    assert response.status_code == 200

def test_not_authenticate_user():
    """Teste para verificar se é possível não autenticar um usuário"""
    response = client.post("/auth/token", data={"username":"teste", "password":"1234"})
    assert response.status_code == 401

def test_post_busca_authenticated():
    """Teste para verificar se é possível realizar uma busca com usuário autenticado"""
    response = client.post(f"/busca?origem=MCZ&destino=GRU&moeda=BRL&data={date.today() + timedelta(days=1)}", json={"id":1,"travelerType":"ADULT"}, headers={"Authorization":f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImlkIjoyLCJleHAiOjE3MzE5ODUyMzF9.XDWMnNxoVj2crYoD8i0ovh7GeVQ0tb1k9B9TYd2kP7g"})
    assert response.status_code == 200

def test_post_busca_not_authenticated():
    """Teste para verificar se é possível realizar uma busca com usuário não autenticado"""
    response = client.post(f"/busca?origem=MCZ&destino=GRU&moeda=BRL&data={date.today() + timedelta(days=1)}", json={"id":1,"travelerType":"ADULT"})
    assert response.status_code == 401