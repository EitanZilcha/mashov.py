from __future__ import annotations
from typing import NamedTuple

import datetime


class Grade(NamedTuple):
    event_id: int
    grade: int
    grade_range: str
    timestamp: datetime.datetime
    teacher_name: str
    group_id: str
    group_name: str
    subject: str
    event_date: datetime
    id: int
    grading_period: int
    grading_event: str
    type_id: int
    type: str

    @staticmethod
    def from_dict(grade_dict: dict) -> Grade:
        return Grade(
            event_id=grade_dict["gradingEventId"],
            grade=grade_dict["grade"],
            grade_range=grade_dict["rangeGrade"],
            timestamp=datetime.datetime.strptime(grade_dict["timestamp"],
                                                 "%Y-%m-%dT%H:%M:%S"),
            teacher_name=grade_dict["teacherName"],
            group_id=grade_dict["groupId"],
            group_name=grade_dict["groupName"],
            subject=grade_dict["subjectName"],
            event_date=datetime.datetime.strptime(grade_dict["eventDate"],
                                                  "%Y-%m-%dT%H:%M:%S").date(),
            id=grade_dict["id"],
            grading_period=grade_dict["gradingPeriod"],
            grading_event=grade_dict["gradingEvent"],
            type_id=grade_dict["gradeTypeId"],
            type=grade_dict["gradeType"])
