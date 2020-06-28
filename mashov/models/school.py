from __future__ import annotations
from typing import List, NamedTuple


class School(NamedTuple):
    """
    A :class:`~typing.NamedTuple` representing a school

    .. py:attribute:: semel

        :class:`~int` - The school's ID number

    .. py:attribute:: name

        :class:`~str` - The school's name

    .. py:attribute:: years

        :class:`~typing.List` [:class:`~int`] - The school's available years

    """
    semel: int
    name: str
    years: List[int]

    @staticmethod
    def from_params(semel: int, name: str, years: List[int]) -> School:
        """
        Parses a school from the given parameters

        :param semel: The school's ID number
        :param name: The school's name
        :param years: The school's available years
        """
        return School(semel, name, years)
