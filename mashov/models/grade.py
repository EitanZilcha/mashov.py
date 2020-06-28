from __future__ import annotations
from typing import NamedTuple

import datetime


class Grade(NamedTuple):
    """
    A :class:`~typing.NamedTuple` representing a grade

    .. py:attribute:: event_id

        :class:`~int` - The grading event's ID

    .. py:attribute:: grade

        :class:`~int` - The grade

    .. py:attribute:: grade_range

        :class:`~str` - The range of the grade (example - "מצוין" if the grade is 100)

    .. py:attribute:: timestamp

        :class:`~datetime.datetime` - The time the grade was given at

    .. py:attribute:: teacher_name

        :class:`~str` - The name of the teacher who gave the grade

    .. py:attribute:: group_id

        :class:`~str` - The group ID of the group who was given the grade

    .. py:attribute:: group_name

        :class:`~str` - The group name of the group who was given the grade

    .. py:attribute:: subject

        :class:`~str` - The grade's subject (example - "מדעי המחשב")

    .. py:attribute:: event_date

        :class:`~datetime.date` - The date of the event that got the grade

    .. py:attribute:: id

        :class:`~int` - The grading event's ID

    .. py:attribute:: grading_period

        :class:`~int`

    .. py:attribute:: grading_event

        :class:`~str` - The grading event's name (example - "מבחן 2 מחצית ב")

    .. py:attribute:: type_id

        :class:`~int`

    .. py:attribute:: type

        :class:`~str` - The grading event's type (example - "בוחן בכתב")

    """
    event_id: int
    grade: int
    grade_range: str
    timestamp: datetime.datetime
    teacher_name: str
    group_id: str
    group_name: str
    subject: str
    event_date: datetime.date
    id: int
    grading_period: int
    grading_event: str
    type_id: int
    type: str

    @staticmethod
    def from_dict(grade_dict: dict) -> Grade:
        """
        Parses a grade from the given dictionary

        :param dict grade_dict: The dictionary
        """
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

    @staticmethod
    def from_params(**kwargs) -> Grade:
        """
        Parses a grade from the given parameters
        """
        pass
