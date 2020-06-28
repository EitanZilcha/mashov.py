from .models import School
import requests

from typing import List

API_BASE_URL = "https://web.mashov.info/api"


def fetch_schools() -> List[School]:
    resp = requests.get(f"{API_BASE_URL}/schools")
    return [School.from_params(**school_dict) for school_dict in resp.json()]
