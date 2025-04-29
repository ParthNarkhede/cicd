from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask app" in response.data
    assert b"Go to About Page" in response.data  # Check for the button label

def test_about():
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Page" in response.data
    assert b"second page from your Flask app" in response.data
