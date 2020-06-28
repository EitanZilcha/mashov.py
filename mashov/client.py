from .models import Grade
from .client_helper_funcs import get_grades as get_grades_helper
import requests

from typing import List

API_BASE_URL = "https://web.mashov.info/api"
API_VERSION = "3.20190301"
APP_NAME = "com.mashov.main"


class Client:
    """
    The main client class. The other client inherit from this one.
    This class has no constructor, and is read-only.
    """
    @property
    def csrf_token(self) -> str:
        """
        The csrf token for the current session
        """
        return self.session.cookies["Csrf-Token"]

    @property
    def guid(self) -> str:
        """
        The client's user ID
        """
        return self._guid

    @property
    def session(self) -> requests.Session:
        """
        The client's session
        """
        return self._session

    @property
    def session_id(self) -> str:
        """
        The client's Mashov session ID
        """
        return self._session.cookies["MashovSessionID"]

    def get_grades(self) -> List[Grade]:
        """
        Retrieves the client's grades

        :rtype: List[Grade]
        """
        return get_grades_helper(self.session, self.guid)
