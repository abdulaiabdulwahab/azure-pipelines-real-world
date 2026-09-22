from app import app


def test_health_endpoint():

    # Flask provides a lightweight test client.
    client = app.test_client()

    response = client.get("/health")

    # Deployment should not continue if health functionality breaks.
    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"