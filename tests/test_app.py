import pytest
from src.app import create_app


@pytest.fixture
def client():
    """
    Fixture to create a test client for the Flask application.
    """
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """
    Test the home endpoint.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {
        "message": "Welcome to the Portfolio CI/CD Application!",
        "status": "running"
    }


def test_health(client):
    """
    Test the health endpoint.
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_echo(client):
    """
    Test the echo endpoint.
    """
    data = {"test": "data"}
    response = client.post('/echo', json=data)
    assert response.status_code == 200
    assert response.json == {
        "echo": data,
        "status": "success"
    }
