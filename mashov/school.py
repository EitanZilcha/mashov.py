from __future__ import annotations
from typing import List, NamedTuple


class School(NamedTuple):
    id: int
    name: str
    years: List[str]

    @staticmethod
    def from_dict(school_dict: dict) -> School:
        return School(school_dict["semel"], school_dict["name"],
                      school_dict["years"])
