from .exceptions import InvalidLoginError, InvalidPasswordError, InvalidUsernameError
from .school import School
import requests

API_BASE_URL = "https://web.mashov.info/api"
API_VERSION = "3.20190301"
APP_NAME = "com.mashov.main"


class Client:
    def __init__(self,
                 school: School,
                 username: str,
                 password: str,
                 year: int = 0) -> None:
        """
        Create a new `Client`.
        If the year is set to `0`,
        it will default to the latest year of the selected school.
        """
        self._school = school
        if year != 0:
            self._year = year
        else:
            self._year = school.years[-1]
        self._username = username
        self._password = password
        self._session: requests.Session = requests.session()

    def login(self):
        """
        Attempt to log in with the current `Client`'s details
        """
        auth_dict = {
            "apiVersion": API_VERSION,
            "appName": APP_NAME,
            "school": self._school._asdict(),
            "semel": self._school.id,
            "year": self._year,
            "username": self._username,
            "password": self._password
        }
        r = self._session.post(f"{API_BASE_URL}/login", json=auth_dict)
        if r.status_code == 200:
            self._session.headers.update(
                {"X-Csrf-Token": self._session.cookies["Csrf-Token"]})
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
