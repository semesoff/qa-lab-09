"""API-тесты JSONPlaceholder для лабораторной работы №9."""

import requests


BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


class TestUsersAPI:
    """Проверяет операции получения, создания и обновления пользователя."""

    def test_get_user_status_code(self):
        """Проверяет успешный статус GET /users/1."""
        response = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT)

        assert response.status_code == 200

    def test_get_user_contains_id_name_email(self):
        """Проверяет обязательные поля пользователя."""
        response = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT)
        data = response.json()

        assert {"id", "name", "email"}.issubset(data)
        assert data["id"] == 1

    def test_get_user_structure(self):
        """Проверяет вложенную структуру адреса и компании."""
        response = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT)
        data = response.json()

        assert {
            "id", "name", "username", "email", "address", "phone", "website", "company"
        }.issubset(data)
        assert {"street", "suite", "city", "zipcode", "geo"}.issubset(data["address"])
        assert {"name", "catchPhrase", "bs"}.issubset(data["company"])

    def test_create_user_status_code(self):
        """Проверяет статус создания пользователя."""
        payload = {"name": "John Doe", "job": "QA Engineer"}
        response = requests.post(f"{BASE_URL}/users", json=payload, timeout=TIMEOUT)

        assert response.status_code == 201

    def test_create_user_contains_name_and_job(self):
        """Проверяет поля созданного пользователя."""
        payload = {"name": "John Doe", "job": "QA Engineer"}
        response = requests.post(f"{BASE_URL}/users", json=payload, timeout=TIMEOUT)
        data = response.json()

        assert data.get("name") == payload["name"]
        assert data.get("job") == payload["job"]

    def test_update_user_status_code(self):
        """Проверяет статус обновления пользователя."""
        payload = {"name": "Updated Name", "job": "Updated Job"}
        response = requests.put(f"{BASE_URL}/users/1", json=payload, timeout=TIMEOUT)

        assert response.status_code == 200

    def test_update_user_contains_fields(self):
        """Проверяет поля обновленного пользователя."""
        payload = {"name": "Updated Name", "job": "Updated Job"}
        response = requests.put(f"{BASE_URL}/users/1", json=payload, timeout=TIMEOUT)
        data = response.json()

        assert data.get("name") == payload["name"]
        assert data.get("job") == payload["job"]
