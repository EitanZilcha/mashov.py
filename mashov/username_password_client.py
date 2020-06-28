from .client import Client
from .exceptions import InvalidLoginError, InvalidPasswordError, InvalidUsernameError
from .models import School
import requests

API_BASE_URL = "https://web.mashov.info/api"
API_VERSION = "3.20190301"
APP_NAME = "com.mashov.main"


class UsernamePasswordClient(Client):
    """
        Represents a client created with a username and password

        :param username: The user's username
        :param password: The user's password
        :param school: The user's school
        :param year: The selected school year (use 0 for latest, default is 0)
    """
    def __init__(self, username: str, password: str, school: School, year: int = 0) -> None:
        self._school = school
        if year != 0:
            self._year = year
        else:
            self._year = self._school.years[-1]
        self._username = username
        self._password = password
        self._session: requests.Session = requests.session()
        self._guid: str = None

    def login(self):
        """
        Attempt to log in with the current Client's details
        """
        auth_dict = {
            "apiVersion": API_VERSION,
            "appName": APP_NAME,
            "school": self._school._asdict(),
            "semel": self._school.semel,
            "year": self._year,
            "username": self._username,
            "password": self._password
        }
        r = self._session.post(f"{API_BASE_URL}/login", json=auth_dict)
        if r.status_code == 200:
            self._session.headers.update({"X-Csrf-Token": self.csrf_token})
            self._guid = r.json()["credential"]["userId"]
        elif r.status_code == 401:
            raise InvalidLoginError()
        elif r.status_code == 400:
            resp_dict = r.json()
            if "errors" in resp_dict:
                errors = resp_dict["errors"]
                if "password" in errors:
                    raise InvalidPasswordError(", ".join(errors["password"]))
                if "username" in errors:
                    raise InvalidUsernameError(", ".join(errors["username"]))
