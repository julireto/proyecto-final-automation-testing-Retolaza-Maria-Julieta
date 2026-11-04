import requests


def test_create_user():

    payload = {"name": "Maria", "job": "QA"}

    response = requests.post("https://reqres.in/api/users", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Maria"
