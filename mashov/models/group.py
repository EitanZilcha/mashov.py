from typing import NamedTuple


class PartialGroup(NamedTuple):
    """
    A :class:`~NamedTuple` partially representing a group, originating from a grade.
    This :class:`~NamedTuple` is missing:
    - The full teachers list
    - The teacher(s)'s GUID
    - The inactive teachers list

    .. py:attribute:: id

        :class:`~int` - The group's ID

    .. py:attribute:: name

        :class:`~str` - The group's name

    .. py:attribute:: level

        :class:`~str` - No idea, this was empty in everything I've seen.
        Some grades don't even list it.

    .. py:attribute:: subject

        :class:`~str` - The group's subject

    .. py:attribute:: teacher

        :class:`~str` - The group teacher's name
    """
    id: int
    name: str
    level: str
    subject: str
    teacher: str
