import pytest
import requests


BASE_URL = "https://postman-echo.com/"


@pytest.mark.parametrize(('method', 'endpoint', 'expected_code'), [
    ('get', 'get', 200),
    ('post', 'post', 200),
    ('get', 'post', 404),
    ('post', 'get', 404)
])
def test_postman_echo_status_codes(method, endpoint, expected_code):
    response = requests.request(method, BASE_URL + endpoint)
    assert response.status_code == expected_code



def test_get_request_with_valid_query():
    queries = {
        "id": 12,
        "name": "test_user"
    }
    expected = {
        "id": '12',
        "name": "test_user"
    }
    response = requests.get("https://postman-echo.com/get", params=queries)
    assert isinstance(response.json()['args'], dict)
    assert response.json()['args'] == expected


def test_post_request_with_valid_query():
    queries = {
        "id": 12,
        "name": "test_user"
    }
    expected = {
        "id": '12',
        "name": "test_user"
    }
    response = requests.post("https://postman-echo.com/post", params=queries)
    assert isinstance(response.json()['args'], dict)
    assert response.json()['args'] == expected


def test_invalid_query_type():
    response = requests.get("https://postman-echo.com/get", params={"id": None})
    assert response.status_code == 200
    assert response.json()["args"] == {}
