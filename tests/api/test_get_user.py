import requests


def test_get_user():

    response = requests.get("https://reqres.in/api/users/2")

    assert response.status_code == 200

    data = response.json()

    assert data["data"]["id"] == 2
