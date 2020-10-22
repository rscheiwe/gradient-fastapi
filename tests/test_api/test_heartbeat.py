from fastapi.testclient import TestClient

from gradient.main import get_app

app = get_app()
client = TestClient(app)


def test_heartbeat() -> None:
    response = client.get('/api/health/heartbeat')
    assert response.status_code == 200
    assert response.json() == {"is_alive": True}


def test_default_route() -> None:
    response = client.get('/')
    assert response.status_code == 404
