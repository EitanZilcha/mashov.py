from .grade import Grade
from .client_helper_funcs import get_grades as get_grades_helper
import requests

from typing import List

API_BASE_URL = "https://web.mashov.info/api"
API_VERSION = "3.20190301"
APP_NAME = "com.mashov.main"


class Client:
    @property
    def csrf_token(self) -> str:
        return self.session.cookies["Csrf-Token"]

    @property
    def guid(self) -> str:
        return self._guid

    @property
    def session(self) -> requests.Session:
        return self._session

    @property
    def session_id(self) -> str:
        return self._session.cookies["MashovSessionID"]

    def get_grades(self) -> List[Grade]:
        return get_grades_helper(self.session, self.guid)
