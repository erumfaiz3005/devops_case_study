import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My Website" in response.data


def test_about_page(client):
    """Test that the about page loads successfully."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About" in response.data


def test_contact_page(client):
    """Test that the contact page loads successfully."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact" in response.data


def test_404_page(client):
    """Test that an invalid page returns a 404."""
    response = client.get('/invalid-page')
    assert response.status_code == 404
