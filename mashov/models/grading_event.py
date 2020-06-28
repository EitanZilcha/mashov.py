from typing import NamedTuple
from datetime import date


# - GradingEvent
#   - gradingEvent (title)
#   - gradingEventId (id)
#   - eventDate (date)
#   - gradeType (type)
#   - gradeTypeId (type_id)


class GradingEvent(NamedTuple):
    """
    A :class:`~NamedTuple` representing a grading event

    .. py:attribute:: id

        :class:`~int` - The grading event's ID

    .. py:attribute:: title

        :class:`~str` - The grading event's title

    .. py:attribute:: date

        :class:`~datetime.date` - The grading event's date

    .. py:attribute:: type

        :class:`~str` - The grading event's type

    .. py:attribute:: type_id

        :class:`~int` - The grading event's type's ID
    """

    id: int
    title: str
    date: date
    type: str
    type_id: int
