import allure
import pytest
import requests

BASE_URL = "https://postman-echo.com/"


@allure.title("Проверка корректности статус кодов, возвращаемых сервером")
@allure.description(
    "Тест проверяет корректность статус кодов, возвращаемых сервером в зависимости от отправленного метода запроса")
@pytest.mark.parametrize(('method', 'endpoint', 'expected_code'), [
    ('get', 'get', 200),
    ('post', 'post', 200),
    ('get', 'post', 404),
    ('post', 'get', 404)
])
def test_postman_echo_status_codes(method, endpoint, expected_code):
    """Проверка статус кодов ответов от сервера"""
    response = requests.request(method, BASE_URL + endpoint)
    assert response.status_code == expected_code


@allure.title("Проверка GET запроса с корректными параметрами")
@allure.description(
    "Тест проверяет корректность статуса и возвращаемых данных ответа на GET запрос с корректными id и names")
def test_get_request_with_valid_query():
    """Проверка GET запроса корректными параметрами"""
    queries = {
        "id": 12,
        "name": "test_user"
    }
    expected = {
        "id": '12',
        "name": "test_user"
    }
    response = requests.get("https://postman-echo.com/get", params=queries)
    assert response.status_code == 200
    assert isinstance(response.json()['args'], dict)
    assert response.json()['args'] == expected


@allure.title("Проверка POST запроса с корректными параметрами")
@allure.description("тест проверяет корректность статуса и данных ответа на POST запрос с корректными id и names")
def test_post_request_with_valid_query():
    """Проверка POST запроса корректными параметрами"""
    queries = {
        "id": 12,
        "name": "test_user"
    }
    expected = {
        "id": '12',
        "name": "test_user"
    }
    response = requests.post("https://postman-echo.com/post", params=queries)
    assert response.status_code == 200
    assert isinstance(response.json()['args'], dict)
    assert response.json()['args'] == expected


@allure.title("Проверка GET запроса с некорректными параметрами")
@allure.description("Тест проверяет корректность статуса и ответа на GET запрос с некорректными id")
def test_invalid_query_type():
    """Проверка GET запроса с некорректным типом параметра"""
    response = requests.get("https://postman-echo.com/get", params={"id": None})
    assert response.status_code == 200
    assert response.json()["args"] == {}
