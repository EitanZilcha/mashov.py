from .models import Grade
from typing import List
from requests import Session

API_BASE_URL = "https://web.mashov.info/api"


def get_grades(session: Session, guid: str) -> List[Grade]:
    r = session.get(f"{API_BASE_URL}/students/{guid}/grades")
    return [Grade.from_dict(grade) for grade in r.json()]
