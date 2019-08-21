from .client import Client
from .grade import Grade
from typing import List

API_BASE_URL = "https://web.mashov.info/api"


def get_grades(client: Client) -> List[Grade]:
    r = client.session.get(f"{API_BASE_URL}/students/{client.guid}/grades")
    return [Grade.from_dict(grade) for grade in r.json()]
