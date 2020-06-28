from mashov.username_password_client import UsernamePasswordClient
from mashov.models import School
from mashov.exceptions import InvalidLoginError, InvalidPasswordError, InvalidUsernameError
import pytest
import responses

API_BASE_URL = "https://web.mashov.info/api"


@pytest.fixture
def school():
    return {"semel": 123123, "name": "Testing School", "years": [2019, 2020]}


@pytest.fixture
def username_password_client(school):
    return UsernamePasswordClient(school=School.from_params(**school),
                                  username="test_username",
                                  password="test_password")


@pytest.fixture
def invalid_password_json():
    return {"errors": {"password": ["Invalid password"]}}


@responses.activate
def test_invalid_password(username_password_client, invalid_password_json):
    """
    invalid passwords are handled
    """
    responses.add(responses.POST,
                  f"{API_BASE_URL}/login",
                  json=invalid_password_json,
                  status=400)
    with pytest.raises(InvalidPasswordError):
        username_password_client.login()


@pytest.fixture
def invalid_username_json():
    return {"errors": {"username": ["Invalid username"]}}


@responses.activate
def test_invalid_username(username_password_client, invalid_username_json):
    """
    invalid usernames are handled
    """
    responses.add(responses.POST,
                  f"{API_BASE_URL}/login",
                  json=invalid_username_json,
                  status=400)
    with pytest.raises(InvalidUsernameError):
        username_password_client.login()


@responses.activate
def test_invalid_login(username_password_client):
    """
    invalid login is handled
    """
    responses.add(responses.POST, f"{API_BASE_URL}/login", status=401)
    with pytest.raises(InvalidLoginError):
        username_password_client.login()
