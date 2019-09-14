from .client import Client

import requests

BASE_URL = "web.mashov.info"


class TokenClient(Client):
    def __init__(self, user_id: str, csrf_token: str, session_id: str) -> None:
        self._guid = user_id
        self._session: requests.Session = requests.session()
        cookie_config = {"domain": BASE_URL, "path": "/"}
        self._session.cookies.set(name="Csrf-Token",
                                  value=csrf_token,
                                  **cookie_config)
        self._session.cookies.set(name="MashovSessionID",
                                  value=session_id,
                                  **cookie_config)
        self._session.headers.update({"X-Csrf-Token": self.csrf_token})
