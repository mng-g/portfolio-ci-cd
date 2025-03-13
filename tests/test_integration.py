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


def test_home_page(client):
    """
    Test the home page endpoint.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Portfolio CI/CD Application!" in response.data


def test_health_check(client):
    """
    Test the health check endpoint.
    """
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data


def test_echo_endpoint(client):
    """
    Test the echo endpoint.
    """
    data = {"message": "Hello, World!"}
    response = client.post('/echo', json=data)
    assert response.status_code == 200
    assert response.get_json() == {"echo": data, "status": "success"}
